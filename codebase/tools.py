"""Công cụ chỉ đọc dữ liệu mô phỏng trong data/park_data.json của nhóm.

Giờ địa phương HH:MM, giá nguyên VND. Các khoảng thời gian gồm đầu mút
bắt đầu và không gồm đầu mút kết thúc. Lịch show lặp trên các ngày có dữ
liệu mô phỏng. Theo data card, trẻ dưới 4 tuổi dùng vé cổng toddler.
"""

from datetime import date
import json
from pathlib import Path
import re

from tracing import tool


PARK_DATA = Path(__file__).resolve().parents[1] / "data" / "park_data.json"
TODDLER_AGE_LIMIT = 4


def _park():
    return json.loads(PARK_DATA.read_text(encoding="utf-8-sig"))


def _date(value):
    if not isinstance(value, str) or not re.fullmatch(r"[0-9]{4}-[0-9]{2}-[0-9]{2}", value):
        raise ValueError("Ngày đi phải có định dạng YYYY-MM-DD.")
    return date.fromisoformat(value).isoformat()


def _minute(value):
    if value == "24:00":
        return 24 * 60
    if not isinstance(value, str) or not re.fullmatch(r"(?:[01][0-9]|2[0-3]):[0-5][0-9]", value):
        raise ValueError("Giờ phải có định dạng HH:MM.")
    hour, minute = map(int, value.split(":"))
    return hour * 60 + minute


def _span(start, end):
    start, end = _minute(start), _minute(end)
    if start >= end:
        raise ValueError("Giờ kết thúc phải sau giờ bắt đầu trong cùng ngày.")
    return start, end


def _whole_number(value):
    if type(value) is not int or value < 0:
        raise ValueError("Số lượng, tuổi, giá và thời gian đi bộ phải là số nguyên không âm.")
    return value


def _age_allowed(point, ages):
    minimum = _whole_number(point["min_age"])
    return all(age >= minimum for age in ages)


def _walk_minutes(park, origin, destination):
    if origin["id"] == destination["id"]:
        return 0
    return _whole_number(park["walk_minutes"][origin["zone"]][destination["zone"]])


def _ticket_total(prices, adults, ages):
    ticket = adults * _whole_number(prices["gate_adult_vnd"])
    child_price = _whole_number(prices["gate_child_vnd"])
    toddler_price = _whole_number(prices["gate_toddler_vnd"])
    return ticket + sum(toddler_price if age < TODDLER_AGE_LIMIT else child_price for age in ages)


def _rain_window(weather):
    if weather is None:
        return None
    start, end = weather["rain_from"], weather["rain_to"]
    return (1440, 1440) if start is None and end is None else _span(start, end)


def _weather_issue(rain_window, start, end, reported_rain):
    if end > reported_rain:
        return "MUA_NGOAI_TROI"
    if rain_window is None:
        return "THIEU_THOI_TIET"
    rain_start, rain_end = rain_window
    if rain_start < end and rain_end > start:
        return "MUA_NGOAI_TROI"
    return None


def _cancellations(reports):
    if not isinstance(reports, (list, tuple)):
        raise ValueError("Danh sách show hủy phải chứa các ID hoặc các suất.")
    cancellations = set()
    for report in reports:
        if isinstance(report, str) and report.strip():
            cancellations.add((report, None))
        elif isinstance(report, dict) and isinstance(report.get("diem_id"), str):
            cancellations.add((report["diem_id"], _minute(report["bat_dau"])))
        else:
            raise ValueError("Mỗi show hủy cần mã show hoặc mã show và giờ bắt đầu.")
    return cancellations


def _show_cancelled(show, rain, start, end, reported_rain, cancellations):
    show_id = show["id"]
    return (
        (show_id, None) in cancellations
        or (show_id, start) in cancellations
        or (
            show["cancelled_on_rain"]
            and _weather_issue(rain, start, end, reported_rain) == "MUA_NGOAI_TROI"
        )
    )


@tool
def tra_diem_choi(khu=None, do_tuoi_tre_em=None, trong_nha_only=False, *, bao_gom_bao_tri=False):
    """Tra điểm chơi. Input là mã khu, tuổi hoặc danh sách tuổi và lọc trong nhà.
    Mặc định ẩn điểm bảo trì. Bật bao_gom_bao_tri để tra cả trạng thái đóng.
    Output là danh sách điểm phù hợp có giờ, giá và giới hạn. Chỉ đọc dữ liệu.
    """
    ages = [] if do_tuoi_tre_em is None else do_tuoi_tre_em
    if not isinstance(ages, (list, tuple)):
        ages = [ages]
    ages = [_whole_number(age) for age in ages]
    return [
        point for point in _park()["attractions"]
        if (not khu or point["zone"] == khu)
        and (bao_gom_bao_tri or point["maintenance"] is False)
        and (not trong_nha_only or point["indoor"] is True)
        and _age_allowed(point, ages)
    ]


@tool
def tra_lich_show(ngay, *, mua_tu=None, show_da_huy=()):
    """Tra lịch show theo ngày ISO, giờ bắt đầu mưa và các suất báo hủy nếu có.
    Output là các suất trong ngày có cờ huy theo dự báo và báo cáo mới.
    show_da_huy nhận mã show hoặc {diem_id, bat_dau} của một suất. Chỉ đọc dữ liệu.
    """
    day = _date(ngay)
    reported_rain = 1440 if mua_tu is None else _minute(mua_tu)
    cancellations = _cancellations(show_da_huy)
    park = _park()
    rain = _rain_window(park["weather_by_date"].get(day))
    if rain is None:
        return []
    shows = []
    for show in park["shows"]:
        start, end = _span(show["start_time"], show["end_time"])
        cancelled = _show_cancelled(show, rain, start, end, reported_rain, cancellations)
        shows.append({**show, "ngay": day, "huy": cancelled})
    return shows


@tool
def tra_thoi_tiet(ngay):
    """Tra thời tiết. Input là ngày ISO. Output có ngay, co_du_lieu và dự
    báo mô phỏng (summary, rain_from, rain_to, outdoor_ok) nếu có. Chỉ đọc dữ liệu.
    """
    day = _date(ngay)
    weather = _park()["weather_by_date"].get(day)
    return {**(weather or {}), "ngay": day, "co_du_lieu": weather is not None}


@tool
def uoc_thoi_gian_di(diem_a, diem_b):
    """Tra thời gian đi bộ. Input là hai ID điểm chơi. Output là số phút theo
    chiều đi, hoặc None nếu thiếu tuyến/điểm. Chỉ đọc dữ liệu.
    """
    park = _park()
    points = {point["id"]: point for point in park["attractions"] + park["shows"]}
    try:
        return _walk_minutes(park, points[diem_a], points[diem_b])
    except KeyError:
        return None


@tool
def kiem_lich_trinh(
    lich_trinh, so_nguoi_lon, so_tre_em, tuoi_tre_em, ngan_sach, thoi_tiet,
    *, khung_gio=None, show_da_huy=(), chieu_cao_tre_em=None,
):
    """Kiểm lịch một ngày. Input gồm các mục {diem_id, bat_dau, ket_thuc},
    số khách, tuổi từng trẻ, ngân sách VND và kết quả tra_thoi_tiet. Có thể
    thêm thoi_tiet["mua_tu"] theo báo cáo người dùng, khung_gio của chuyến đi
    {bat_dau, ket_thuc}, các show báo hủy (ID cả show hoặc {diem_id, bat_dau}
    của một suất) và chiều cao từng trẻ.
    Output có hop_le, loi (mã lỗi và vị trí nếu có), tong_tien và chi_tiet
    giá theo từng mục. Giá, bảo trì và dự báo lấy từ dữ liệu khu vui chơi.
    Chỉ đọc dữ liệu.
    """
    result = {"hop_le": False, "loi": [], "tong_tien": None, "chi_tiet": []}
    errors = result["loi"]
    try:
        _whole_number(so_nguoi_lon)
        _whole_number(so_tre_em)
        _whole_number(ngan_sach)
        if so_nguoi_lon < 1:
            raise ValueError("Cần ít nhất một người lớn.")
        if not isinstance(tuoi_tre_em, (list, tuple)) or len(tuoi_tre_em) != so_tre_em:
            raise ValueError("Cần tuổi của từng trẻ.")
        ages = [_whole_number(age) for age in tuoi_tre_em]
        if chieu_cao_tre_em is not None:
            if not isinstance(chieu_cao_tre_em, (list, tuple)) or len(chieu_cao_tre_em) != so_tre_em:
                raise ValueError("Cần chiều cao của từng trẻ.")
            chieu_cao_tre_em = [_whole_number(height) for height in chieu_cao_tre_em]
        day = _date(thoi_tiet["ngay"])
        mua_tu = thoi_tiet.get("mua_tu")
        reported_rain = 1440 if mua_tu is None else _minute(mua_tu)
        bounds = (0, 1440)
        if khung_gio is not None:
            bounds = _span(khung_gio["bat_dau"], khung_gio["ket_thuc"])
        cancellations = _cancellations(show_da_huy)
        if not isinstance(lich_trinh, (list, tuple)):
            raise ValueError("Lịch phải là danh sách các hoạt động.")
    except (KeyError, TypeError, ValueError) as exc:
        errors.append({"ma": "DAU_VAO_KHONG_HOP_LE", "ly_do": str(exc)})
        return result

    try:
        park = _park()
        all_points = park["attractions"] + park["shows"]
        points = {point["id"]: point for point in all_points}
        if len(points) != len(all_points):
            raise ValueError("ID điểm chơi bị trùng.")
        ticket = _ticket_total(park["ticket_prices"], so_nguoi_lon, ages)
        rain = _rain_window(park["weather_by_date"].get(day))
        park_open, park_close = _span(park["park_hours"]["open"], park["park_hours"]["close"])
        show_ids = {show["id"] for show in park["shows"]}
        scheduled = []
        for index, item in enumerate(lich_trinh):
            try:
                point_id = item["diem_id"]
                point = points[point_id]
                start, end = _span(item["bat_dau"], item["ket_thuc"])
            except (KeyError, TypeError, ValueError):
                errors.append({"ma": "MUC_LICH_KHONG_HOP_LE", "vi_tri": index})
                continue
            scheduled.append((start, end, index, point))

            def mark(code):
                errors.append({"ma": code, "vi_tri": index, "diem_id": point_id})

            if start < bounds[0] or end > bounds[1]:
                mark("NGOAI_GIO_CHUYEN_DI")
            opens, closes = park_open, park_close
            if point_id in show_ids:
                slot = _span(point["start_time"], point["end_time"])
                if rain is None or (start, end) != slot or _show_cancelled(
                    point, rain, start, end, reported_rain, cancellations
                ):
                    mark("SUAT_SHOW_KHONG_CO_HOAC_DA_HUY")
            else:
                point_open, point_close = _span(point["open_time"], point["close_time"])
                opens, closes = max(opens, point_open), min(closes, point_close)
                if point["maintenance"] is not False:
                    mark("BAO_TRI")
                if end - start < _whole_number(point["duration_min"]):
                    mark("KHONG_DU_THOI_LUONG")
            if start < opens or end > closes:
                mark("NGOAI_GIO_MO_CUA")
            if not _age_allowed(point, ages):
                mark("GIOI_HAN_TUOI")
            minimum_height = _whole_number(point.get("min_height_cm", 0))
            if ages and minimum_height:
                if chieu_cao_tre_em is None:
                    mark("THIEU_CHIEU_CAO")
                elif any(height < minimum_height for height in chieu_cao_tre_em):
                    mark("GIOI_HAN_CHIEU_CAO")
            if point["indoor"] is not True:
                weather_issue = _weather_issue(rain, start, end, reported_rain)
                if weather_issue:
                    mark(weather_issue)
            price = (so_nguoi_lon * _whole_number(point["extra_fee_adult_vnd"])
                     + so_tre_em * _whole_number(point["extra_fee_child_vnd"]))
            result["chi_tiet"].append({"diem_id": point_id, "vi_tri": index, "tien": price})

        scheduled.sort()
        previous = None
        for start, end, index, point in scheduled:
            if previous is not None:
                last_end, last_index, last_point = previous
                info = {"vi_tri": index, "vi_tri_truoc": last_index}
                if start < last_end:
                    errors.append({"ma": "TRUNG_GIO", **info})
                    if end <= last_end:
                        continue
                else:
                    try:
                        walk = _walk_minutes(park, last_point, point)
                    except KeyError:
                        errors.append({"ma": "THIEU_DU_LIEU_DI_BO", **info})
                    else:
                        if start - last_end < walk:
                            errors.append({"ma": "KHONG_DU_GIO_DI_BO", "can_phut": walk, **info})
            previous = (end, index, point)
    except (OSError, KeyError, TypeError, ValueError) as exc:
        errors.append({"ma": "DU_LIEU_KHU_KHONG_HOP_LE", "ly_do": str(exc)})
        result["chi_tiet"].clear()
        return result

    result["tien_ve_cong"] = ticket
    if not lich_trinh:
        errors.append({"ma": "LICH_TRONG"})
    if len(scheduled) == len(lich_trinh):
        result["tong_tien"] = ticket + sum(item["tien"] for item in result["chi_tiet"])
        if result["tong_tien"] > ngan_sach:
            errors.append({"ma": "VUOT_NGAN_SACH", "vuot_tien": result["tong_tien"] - ngan_sach})
    result["hop_le"] = not errors
    return result


@tool
def search_example(query: str) -> list:
    """Công cụ tạm để agent mẫu chạy tới khi chuyển sang 5 công cụ của nhóm."""
    return [{"code": "VD-1", "text": "(ví dụ) đoạn dữ liệu giả — thay bằng dữ liệu thật của bài toán"}]
