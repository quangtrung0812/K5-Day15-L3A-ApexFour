"""Xếp điểm do model chọn vào các khoảng trống, giữ nguyên suất show."""
import re
from functools import lru_cache

from tools import uoc_thoi_gian_di


def minutes(t):
    hour, minute = map(int, t.split(":"))
    return hour * 60 + minute


def hhmm(t):
    return f"{t // 60:02}:{t % 60:02}"


def arrange(intent, catalog, req, weather, gate, text):
    start, end = map(minutes, (req["gio_bat_dau"], req["gio_ket_thuc"]))
    rain = []
    if weather.get("rain_from") and weather.get("rain_to"):
        rain.append((minutes(weather["rain_from"]), minutes(weather["rain_to"])))
    if req["mua_tu"]:
        rain.append((minutes(req["mua_tu"]), 1440))
    walk = lru_cache(maxsize=None)(uoc_thoi_gian_di)
    group_age = min(req["tuoi_tre_em"], default=100)
    def strings(key):
        values = intent.get(key, [])
        return [v for v in values if isinstance(v, str)] if isinstance(values, list) else []

    required = list(dict.fromkeys(strings("uu_tien")))
    preferred = list(dict.fromkeys(required + strings("thay_the")))
    zones = {z for z in strings("zones") if re.search(r"\b" + re.escape(z) + r"\b", text, re.I)}
    excluded = set(strings("tranh"))
    notes = [f"{name} không có trong dữ liệu khu vui chơi." for name in strings("thieu_du_lieu")
             if name and name.casefold() in text.casefold()]
    # Nhận diện tên riêng sau động từ yêu cầu, kể cả khi model ghép nhầm sang một mã gần giống.
    proper = r"[A-ZÀÁẢÃẠĂẰẮẲẴẶÂẦẤẨẪẬĐÈÉẺẼẸÊỀẾỂỄỆÌÍỈĨỊÒÓỎÕỌÔỒỐỔỖỘƠỜỚỞỠỢÙÚỦŨỤƯỪỨỬỮỰỲÝỶỸỴ][^\W\d_]*"
    named = rf"(?:[Ss]how |[Vv]òng quay )?{proper}(?: {proper})+"
    for match in re.finditer(r"(?i:\b(?:xem|chơi|thăm|ghé))\s+(" + named + r")", text):
        name = match[1]
        if not any(name.casefold() in p["name"].casefold() for p in catalog.values()):
            message = f"{name} không có trong dữ liệu khu vui chơi."
            if message not in notes:
                notes.append(message)
    for pid in required:
        first = catalog.get(pid, {})
        if "start_time" not in first or first.get("huy"):
            continue
        for other in required:
            second = catalog.get(other, {})
            if other == pid or "start_time" not in second or second.get("huy"):
                continue
            if (first["start_time"], pid) >= (second["start_time"], other):
                continue
            transit = walk(pid, other)
            if transit is not None and minutes(first["end_time"]) + transit > minutes(second["start_time"]):
                notes.append(f"{first['name']} kết thúc {first['end_time']}, cần {transit} phút đi bộ "
                             f"đến {second['name']} bắt đầu {second['start_time']}. Chỉ xếp được một suất.")
    route = []
    remaining = req["ngan_sach"] - gate
    required_fees = {}
    # Chèn vào khoảng giữa hai điểm. Mỗi phương án phải đủ phút đi bộ ở cả hai đầu.
    for pid in preferred:
        if pid not in catalog:
            continue
        p = catalog[pid]
        name = p["name"]
        fee = req["so_nguoi_lon"] * p["extra_fee_adult_vnd"] + req["so_tre_em"] * p["extra_fee_child_vnd"]
        if pid in required:
            required_fees[name] = fee
        reason = ""
        if pid in req["diem_bao_dong"] or p.get("maintenance"):
            reason = "đang tạm đóng hoặc bảo trì"
        elif p.get("huy"):
            reason = "suất diễn đã hủy"
        elif p["min_age"] > group_age:
            reason = f"yêu cầu từ {p['min_age']} tuổi, bé nhỏ nhất {group_age} tuổi"
        elif p.get("min_height_cm") and req["so_tre_em"]:
            reason = f"cần xác nhận chiều cao tối thiểu {p['min_height_cm']} cm"
        elif pid in excluded or (zones and p["zone"] not in zones):
            reason = "ngoài lựa chọn của gia đình"
        elif fee > remaining:
            reason = f"phụ thu {fee:,}đ vượt phần ngân sách còn lại".replace(",", ".")
        options = []
        if not reason:
            for i in range(len(route) + 1):
                left = route[i-1] if i else None
                right = route[i] if i < len(route) else None
                before = walk(left[2], pid) if left else 0
                after = walk(pid, right[2]) if right else 0
                if before is None or after is None:
                    continue
                earliest = left[1] + before if left else start
                latest = right[0] - after if right else end
                if "start_time" in p:
                    t, u = minutes(p["start_time"]), minutes(p["end_time"])
                else:
                    t = max(earliest, minutes(p["open_time"]))
                    if "ăn tối" in text.lower() and "nhà hàng" in p["name"].lower():
                        t = max(t, 17 * 60)
                    duration = p["duration_min"]
                    if not p["indoor"]:
                        for a,b in sorted(rain):
                            if t < b and t + duration > a:
                                t = b
                    u = t + duration
                    latest = min(latest, minutes(p["close_time"]))
                wet = not p["indoor"] and any(t < b and u > a for a,b in rain)
                if earliest <= t and u <= latest and not wet:
                    options.append((before + after, t, u, i))
            if options:
                _, t, u, i = min(options)
                route.insert(i, (t, u, pid))
                remaining -= fee
            else:
                reason = "không đủ khung giờ và thời gian đi bộ giữa các điểm, hoặc vướng mưa"
        if reason and pid in required:
            notes.append(f"{name} ({pid}): {reason}.")
    if sum(required_fees.values()) > req["ngan_sach"] - gate:
        detail = ", ".join(f"{n} {v:,}đ".replace(",", ".") for n,v in required_fees.items() if v)
        total = f"{gate + sum(required_fees.values()):,}đ".replace(",", ".")
        notes.append(f"Phụ thu cả gia đình: {detail}. Để chọn đủ các mục này, cần ngân sách ít nhất {total}.")
    for pid in req["diem_bao_dong"]:
        if pid not in required:
            notes.append(f"Đã đổi tuyến vì {catalog[pid]['name']} đang tạm đóng.")
    if req["mua_tu"]:
        notes.append("Ưu tiên hoạt động trong nhà kể từ khi gia đình báo mưa lúc " + req["mua_tu"] + ".")
    elif weather.get("rain_from"):
        notes.append(f"Tránh điểm ngoài trời trong mưa từ {weather['rain_from']} đến {weather['rain_to']}.")
    plan = []
    for i,(t,u,pid) in enumerate(route):
        p = catalog[pid]
        why = "Điểm mở đầu" if i == 0 else f"Đi bộ {walk(route[i-1][2], pid)} phút từ điểm trước"
        why += ", trong nhà" if p["indoor"] else ", ngoài trời trong khung không mưa"
        plan.append(dict(diem_id=pid, bat_dau=hhmm(t), ket_thuc=hhmm(u), ly_do=why + "."))
    return plan, " ".join(notes)
