"""Script đếm nhãn review công khai — Nhóm ApexFour (Track C · C1).

Chạy lại từ thư mục gốc repo:
    python evidence/count_reviews.py

Đọc file ẩn danh `evidence/reviews_raw.csv` (không chứa tên người viết, mỗi trích dẫn <= 2 câu),
kiểm tra schema và in bảng đếm x/N (%) tái lập 100%.
"""
import csv
import sys
from collections import Counter
from pathlib import Path

for _stream in (sys.stdout, sys.stderr):
    try:
        _stream.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass

CSV_PATH = Path(__file__).resolve().parent / "reviews_raw.csv"

LABEL_META = [
    ("L1_TRE_SHOW_GIO_MO_CUA", "Trễ show / giờ mở cửa / bảo trì / thiếu thông báo giờ"),
    ("L2_DI_CHUYEN_RONG_MET", "Bản đồ / chỉ đường / di chuyển rộng / tối ưu thứ tự chơi"),
    ("L3_TRE_NHO_DO_TUOI", "Giới hạn độ tuổi / chiều cao trẻ em (<1m4)"),
    ("L4_THOI_TIET_MUA", "Mưa / thời tiết làm hỏng kế hoạch ngoài trời"),
    ("L5_GIA_PHAT_SINH", "Chi phí phát sinh / voucher ăn uống / vé lẻ"),
    ("L0_KHAC", "Khác (lỗi kỹ thuật đăng nhập, xếp hàng, khen chung)"),
]
PAIN_LABELS = {code for code, _ in LABEL_META if code != "L0_KHAC"}
VALID_LABELS = {code for code, _ in LABEL_META}
REQUIRED_COLS = {
    "id",
    "source_name",
    "source_url",
    "viewed_date",
    "review_date",
    "stars",
    "quote_max_2_sentences",
    "labels",
}


def main() -> int:
    if not CSV_PATH.exists():
        print(f"Không tìm thấy {CSV_PATH}", file=sys.stderr)
        return 1

    with CSV_PATH.open("r", encoding="utf-8-sig", newline="") as f:
        reader = csv.DictReader(f)
        cols = set(reader.fieldnames or [])
        missing = REQUIRED_COLS - cols
        if missing:
            print(f"Thiếu cột trong CSV: {sorted(missing)}", file=sys.stderr)
            return 1
        rows = list(reader)

    total = len(rows)
    if total == 0:
        print("File CSV chưa có dòng review nào.", file=sys.stderr)
        return 1

    label_counts = Counter()
    star_counts = Counter()
    source_counts = Counter()
    dates = []
    pain_unique_ids = []

    for row in rows:
        rid = row["id"].strip()
        star_counts[row["stars"].strip()] += 1
        source_counts[row["source_name"].strip()] += 1
        if row["review_date"].strip():
            dates.append(row["review_date"].strip())

        labels = [lb.strip() for lb in row["labels"].split(";") if lb.strip()]
        unknown = [lb for lb in labels if lb not in VALID_LABELS]
        if unknown:
            print(f"Cảnh báo: {rid} có nhãn lạ {unknown}", file=sys.stderr)
        for lb in labels:
            label_counts[lb] += 1
        if any(lb in PAIN_LABELS for lb in labels):
            pain_unique_ids.append(rid)

    pain_any = len(pain_unique_ids)
    date_range = f"{min(dates)} -> {max(dates)}" if dates else "không rõ"

    print("=" * 78)
    print(f"TỔNG HỢP ĐÀO DATA REVIEW CÔNG KHAI — ApexFour (Track C · C1)")
    print("=" * 78)
    print(f"File dữ liệu : {CSV_PATH.name}")
    print(f"Tổng mẫu (N) : {total} review (>= 10 từ, mọi mức sao 1-5)")
    print(f"Khoảng ngày  : {date_range}")
    print("Nguồn        : " + ", ".join(f"{k} ({v})" for k, v in source_counts.items()))
    print("Phân bố sao  : " + ", ".join(f"{k}*: {star_counts[k]}" for k in sorted(star_counts)))
    print("-" * 78)
    print(
        f"TỔNG REVIEW GẶP >=1 PAIN XẾP LỊCH (L1-L5, không đếm trùng): "
        f"{pain_any}/{total} ({pain_any / total * 100:.1f}%)"
    )
    print(f"Mã các review gặp pain: {', '.join(pain_unique_ids)}")
    print("-" * 78)
    print("| Nhãn | Mô tả | x / N | % |")
    print("|---|---|---:|---:|")
    for code, desc in LABEL_META:
        c = label_counts[code]
        print(f"| `{code}` | {desc} | {c}/{total} | {c / total * 100:.1f}% |")
    print("-" * 78)
    print("Lưu ý: Một review có thể gắn nhiều nhãn L1-L5 nên tổng lượt nhãn có thể > số review duy nhất.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
