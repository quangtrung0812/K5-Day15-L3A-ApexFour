"""Sinh dữ liệu khu vui chơi giải trí giả lập có seed (synthetic) cho bản chạy thử Track C1.

Chạy:
    python data/generate_park_data.py

Đầu ra:
    data/park_data.json (seed cố định = 42, có thể tái tạo 100%).
Lưu ý:
    Đây là dữ liệu giả lập ("SunWonder Mẫu" — tên dựng) dùng cho công cụ trong codebase/tools.py
    và kiểm chứng bộ câu thử eval/benchmark.csv. KHÔNG phải bằng chứng pain.
"""
import json
import random
from pathlib import Path

SEED = 42


def build_park_data(seed: int = SEED) -> dict:
    rng = random.Random(seed)

    # Tham khảo khung giá & cấu trúc phân khu phổ biến của khu vui chơi lớn tại VN (nhưng là dữ liệu dựng)
    ticket_prices = {
        "gate_adult_vnd": 880_000,      # >= 140cm hoặc người lớn
        "gate_child_vnd": 660_000,      # trẻ em 4-10 tuổi (100-140cm)
        "gate_toddler_vnd": 0,          # dưới 4 tuổi (<100cm) miễn phí
    }

    zones = [
        {"id": "Z1", "name": "Quảng trường Cổ Tích", "theme": "gia_dinh"},
        {"id": "Z2", "name": "Cung điện Hải Vương", "theme": "trong_nha_thuy_cung"},
        {"id": "Z3", "name": "Đồi Thử Thách", "theme": "cam_giac_manh"},
        {"id": "Z4", "name": "Vịnh Nhiệt Đới", "theme": "cong_vien_nuoc_vuon_thu"},
    ]

    # Ma trận thời gian đi bộ giữa các phân khu (phút), cùng khu = 5 phút
    walk_minutes = {
        "Z1": {"Z1": 5, "Z2": 10, "Z3": 18, "Z4": 15},
        "Z2": {"Z1": 10, "Z2": 5, "Z3": 20, "Z4": 12},
        "Z3": {"Z1": 18, "Z2": 20, "Z3": 5, "Z4": 16},
        "Z4": {"Z1": 15, "Z2": 12, "Z3": 16, "Z4": 5},
    }

    # 16 điểm chơi / ăn uống / nghỉ ngơi (cố tình gài bẫy: bảo trì, giới hạn tuổi, ngoài trời, phụ thu)
    attractions = [
        {
            "id": "A01",
            "name": "Lâu đài Kẹo Ngọt",
            "zone": "Z1",
            "category": "tro_choi_gia_dinh",
            "open_time": "09:00",
            "close_time": "19:00",
            "duration_min": 40,
            "min_age": 3,
            "indoor": True,
            "maintenance": False,
            "extra_fee_adult_vnd": 0,
            "extra_fee_child_vnd": 0,
            "tags": ["tre_em", "trong_nha", "nhe_nhang"],
            "note": "Khu vui chơi trong nhà có điều hoà, hợp tránh nắng/trú mưa.",
        },
        {
            "id": "A02",
            "name": "Vòng quay Ngựa Gỗ Cổ Tích",
            "zone": "Z1",
            "category": "tro_choi_gia_dinh",
            "open_time": "09:00",
            "close_time": "18:30",
            "duration_min": 30,
            "min_age": 3,
            "indoor": False,
            "maintenance": False,
            "extra_fee_adult_vnd": 0,
            "extra_fee_child_vnd": 0,
            "tags": ["tre_em", "ngoai_troi", "nhe_nhang"],
            "note": "Tạm dừng nếu trời mưa lớn.",
        },
        {
            "id": "A03",
            "name": "Rạp phim 4D Phép Thuật",
            "zone": "Z1",
            "category": "giai_tri_trong_nha",
            "open_time": "09:30",
            "close_time": "19:30",
            "duration_min": 35,
            "min_age": 4,
            "indoor": True,
            "maintenance": False,
            "extra_fee_adult_vnd": 0,
            "extra_fee_child_vnd": 0,
            "tags": ["tre_em", "trong_nha", "nghi_ngoi"],
            "note": "Chiếu liên tục mỗi 30 phút, trong nhà có máy lạnh.",
        },
        {
            "id": "A04",
            "name": "Nhà hàng Làng Cổ Tích (Combo gia đình)",
            "zone": "Z1",
            "category": "an_uong",
            "open_time": "10:30",
            "close_time": "20:00",
            "duration_min": 50,
            "min_age": 0,
            "indoor": True,
            "maintenance": False,
            "extra_fee_adult_vnd": 220_000,
            "extra_fee_child_vnd": 140_000,
            "tags": ["an_trua", "an_toi", "trong_nha"],
            "note": "Set cơm gia đình, có ghế trẻ em.",
        },
        {
            "id": "A05",
            "name": "Thủy cung Cung điện Hải Vương",
            "zone": "Z2",
            "category": "tham_quan",
            "open_time": "09:00",
            "close_time": "18:00",
            "duration_min": 60,
            "min_age": 0,
            "indoor": True,
            "maintenance": False,
            "extra_fee_adult_vnd": 0,
            "extra_fee_child_vnd": 0,
            "tags": ["tre_em", "trong_nha", "kham_pha"],
            "note": "Đường hầm kính ngắm cá mập, rùa biển; điểm trú mưa/tránh nắng lý tưởng.",
        },
        {
            "id": "A06",
            "name": "Khu Game Thùng & Thực Tế Ảo",
            "zone": "Z2",
            "category": "giai_tri_trong_nha",
            "open_time": "09:30",
            "close_time": "20:00",
            "duration_min": 45,
            "min_age": 5,
            "indoor": True,
            "maintenance": False,
            "extra_fee_adult_vnd": 80_000,
            "extra_fee_child_vnd": 80_000,
            "tags": ["tre_em", "trong_nha", "game"],
            "note": "Phụ thu gói xu game VR riêng ngoài vé cổng.",
        },
        {
            "id": "A07",
            "name": "Quầy Ăn Nhanh Hải Đăng",
            "zone": "Z2",
            "category": "an_uong",
            "open_time": "10:00",
            "close_time": "19:30",
            "duration_min": 40,
            "min_age": 0,
            "indoor": True,
            "maintenance": False,
            "extra_fee_adult_vnd": 130_000,
            "extra_fee_child_vnd": 90_000,
            "tags": ["an_trua", "tiet_kiem", "trong_nha"],
            "note": "Gà rán, mì Ý, combo tiết kiệm trong khu máy lạnh.",
        },
        {
            "id": "A08",
            "name": "Tàu lượn Siêu Tốc Rồng Lửa",
            "zone": "Z3",
            "category": "cam_giac_manh",
            "open_time": "09:30",
            "close_time": "17:30",
            "duration_min": 45,
            "min_age": 10,
            "indoor": False,
            "maintenance": False,
            "extra_fee_adult_vnd": 0,
            "extra_fee_child_vnd": 0,
            "tags": ["cam_giac_manh", "ngoai_troi"],
            "note": "Yêu cầu từ 10 tuổi trở lên (cao >= 130cm); không dành cho trẻ nhỏ.",
        },
        {
            "id": "A09",
            "name": "Đường trượt Núi Alpine Mẫu",
            "zone": "Z3",
            "category": "cam_giac_manh",
            "open_time": "09:00",
            "close_time": "17:00",
            "duration_min": 45,
            "min_age": 6,
            "indoor": False,
            "maintenance": True,  # BẪY: đang bảo trì, không được xếp vào lịch
            "extra_fee_adult_vnd": 0,
            "extra_fee_child_vnd": 0,
            "tags": ["cam_giac_manh", "ngoai_troi"],
            "note": "ĐANG TẠM ĐÓNG BẢO TRÌ trong ngày hôm nay.",
        },
        {
            "id": "A10",
            "name": "Tháp Rơi Tự Do 35m",
            "zone": "Z3",
            "category": "cam_giac_manh",
            "open_time": "10:00",
            "close_time": "17:30",
            "duration_min": 35,
            "min_age": 12,
            "indoor": False,
            "maintenance": False,
            "extra_fee_adult_vnd": 0,
            "extra_fee_child_vnd": 0,
            "tags": ["cam_giac_manh", "ngoai_troi"],
            "note": "Chỉ dành cho khách từ 12 tuổi trở lên.",
        },
        {
            "id": "A11",
            "name": "Bánh Xe Bầu Trời (Vòng quay ngắm cảnh)",
            "zone": "Z3",
            "category": "tham_quan",
            "open_time": "10:00",
            "close_time": "19:30",
            "duration_min": 35,
            "min_age": 3,
            "indoor": True,
            "maintenance": False,
            "extra_fee_adult_vnd": 0,
            "extra_fee_child_vnd": 0,
            "tags": ["tre_em", "ngam_canh", "trong_nha"],
            "note": "Cabin kín có điều hoà, ngắm toàn cảnh vịnh (dừng nếu giông sét).",
        },
        {
            "id": "A12",
            "name": "Vườn Thú Bán Hoang Dã Nhỏ",
            "zone": "Z4",
            "category": "tham_quan",
            "open_time": "09:00",
            "close_time": "16:30",
            "duration_min": 55,
            "min_age": 0,
            "indoor": False,
            "maintenance": False,
            "extra_fee_adult_vnd": 0,
            "extra_fee_child_vnd": 0,
            "tags": ["tre_em", "ngoai_troi", "dong_vat"],
            "note": "Đóng cửa sớm lúc 16:30; nên đi buổi sáng hoặc đầu giờ chiều trời tạnh.",
        },
        {
            "id": "A13",
            "name": "Hồ Bơi Trẻ Em & Vịnh Phao Nổi",
            "zone": "Z4",
            "category": "cong_vien_nuoc",
            "open_time": "09:30",
            "close_time": "17:00",
            "duration_min": 60,
            "min_age": 4,
            "indoor": False,
            "maintenance": False,
            "extra_fee_adult_vnd": 0,
            "extra_fee_child_vnd": 0,
            "tags": ["tre_em", "ngoai_troi", "nuoc"],
            "note": "Đóng cửa lúc 17:00 và tạm dừng ngay khi trời mưa.",
        },
        {
            "id": "A14",
            "name": "Dịch vụ Xe Điện Nội Khu (Vé ngày)",
            "zone": "Z1",
            "category": "dich_vu",
            "open_time": "08:30",
            "close_time": "20:30",
            "duration_min": 15,
            "min_age": 0,
            "indoor": True,
            "maintenance": False,
            "extra_fee_adult_vnd": 100_000,
            "extra_fee_child_vnd": 70_000,
            "tags": ["di_chuyen", "gia_dinh"],
            "note": "Tùy chọn phụ thu cho gia đình có trẻ nhỏ không muốn đi bộ nhiều.",
        },
        {
            "id": "A15",
            "name": "Buffet Trưa Đại Dương",
            "zone": "Z4",
            "category": "an_uong",
            "open_time": "11:00",
            "close_time": "14:00",
            "duration_min": 60,
            "min_age": 0,
            "indoor": True,
            "maintenance": False,
            "extra_fee_adult_vnd": 350_000,
            "extra_fee_child_vnd": 200_000,
            "tags": ["an_trua", "cao_cap", "trong_nha"],
            "note": "Chỉ phục vụ 11:00–14:00, phụ thu cao.",
        },
        {
            "id": "A16",
            "name": "Nhà Banh & Góc Nghỉ Trưa Gia Đình",
            "zone": "Z2",
            "category": "giai_tri_trong_nha",
            "open_time": "09:00",
            "close_time": "19:00",
            "duration_min": 45,
            "min_age": 2,
            "indoor": True,
            "maintenance": False,
            "extra_fee_adult_vnd": 0,
            "extra_fee_child_vnd": 0,
            "tags": ["tre_em", "trong_nha", "nghi_ngoi"],
            "note": "Miễn phí trong vé cổng, có ghế nghỉ cho phụ huynh.",
        },
    ]

    # 5 show diễn có khung giờ cố định (bao gồm 1 show ngoài trời bị huỷ khi mưa)
    shows = [
        {
            "id": "S01",
            "name": "Biểu diễn Chim Thông Minh",
            "zone": "Z4",
            "start_time": "10:30",
            "end_time": "11:00",
            "indoor": False,
            "min_age": 0,
            "cancelled_on_rain": True,
            "extra_fee_adult_vnd": 0,
            "extra_fee_child_vnd": 0,
            "note": "Sân khấu ngoài trời tại Vườn thú, huỷ nếu trời mưa.",
        },
        {
            "id": "S02",
            "name": "Biểu diễn Nàng Tiên Cá",
            "zone": "Z2",
            "start_time": "11:00",
            "end_time": "11:20",
            "indoor": True,
            "min_age": 0,
            "cancelled_on_rain": False,
            "extra_fee_adult_vnd": 0,
            "extra_fee_child_vnd": 0,
            "note": "Trong nhà tại Thủy cung; trùng giờ với phần cuối S01 nên không thể xem cả hai cùng lúc.",
        },
        {
            "id": "S03",
            "name": "Cho Cá Mập Ăn",
            "zone": "Z2",
            "start_time": "15:00",
            "end_time": "15:20",
            "indoor": True,
            "min_age": 0,
            "cancelled_on_rain": False,
            "extra_fee_adult_vnd": 0,
            "extra_fee_child_vnd": 0,
            "note": "Trong nhà tại Thủy cung, vẫn diễn bình thường khi trời mưa.",
        },
        {
            "id": "S04",
            "name": "Diễu hành Carnival Đường Phố",
            "zone": "Z1",
            "start_time": "16:15",
            "end_time": "16:45",
            "indoor": False,
            "min_age": 0,
            "cancelled_on_rain": True,
            "extra_fee_adult_vnd": 0,
            "extra_fee_child_vnd": 0,
            "note": "Diễu hành ngoài trời, huỷ nếu trời mưa.",
        },
        {
            "id": "S05",
            "name": "Show Thực Cảnh Ánh Sáng Đêm",
            "zone": "Z1",
            "start_time": "19:30",
            "end_time": "20:15",
            "indoor": False,
            "min_age": 0,
            "cancelled_on_rain": True,
            "extra_fee_adult_vnd": 0,
            "extra_fee_child_vnd": 0,
            "note": "Show chính buổi tối tại Quảng trường Cổ Tích (huỷ nếu mưa lớn).",
        },
    ]

    # 3 kịch bản thời tiết theo ngày mẫu để công cụ tra_thoi_tiet(ngay) trả về nhất quán
    weather_by_date = {
        "2026-11-28": {
            "summary": "Nắng nhẹ cả ngày, không mưa",
            "rain_from": None,
            "rain_to": None,
            "outdoor_ok": True,
        },
        "2026-11-29": {
            "summary": "Sáng nắng, mưa rào từ 14:00 đến 17:30",
            "rain_from": "14:00",
            "rain_to": "17:30",
            "outdoor_ok": False,
        },
        "2026-11-30": {
            "summary": "Mưa lớn cả ngày từ 09:00 đến 20:30",
            "rain_from": "09:00",
            "rain_to": "20:30",
            "outdoor_ok": False,
        },
    }

    # Sinh thêm thời gian xếp hàng ước lượng ổn định theo seed
    for item in attractions:
        if item["category"] == "an_uong" or item["category"] == "dich_vu":
            item["est_wait_min"] = rng.choice([5, 10])
        elif item["category"] == "cam_giac_manh":
            item["est_wait_min"] = rng.choice([20, 25, 30])
        else:
            item["est_wait_min"] = rng.choice([10, 15])

    return {
        "park_name": "Khu vui chơi SunWonder Mẫu",
        "dataset_label": "synthetic",
        "seed": seed,
        "generated_date": "2026-11-27",
        "park_hours": {"open": "08:30", "close": "20:30"},
        "ticket_prices": ticket_prices,
        "zones": zones,
        "walk_minutes": walk_minutes,
        "attractions": attractions,
        "shows": shows,
        "weather_by_date": weather_by_date,
    }


def main() -> None:
    out_path = Path(__file__).resolve().parent / "park_data.json"
    data = build_park_data(SEED)
    out_path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"Đã sinh {out_path} (seed={SEED}): {len(data['attractions'])} điểm, {len(data['shows'])} show, {len(data['weather_by_date'])} ngày thời tiết.")


if __name__ == "__main__":
    main()
