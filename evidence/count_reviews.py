"""Script đếm nhãn review công khai — Nhóm ApexFour (Track C · C1).

Chạy lại từ thư mục gốc repo:
    python evidence/count_reviews.py
    python evidence/count_reviews.py --csv evidence/reviews_raw.csv

Đọc bảng ẩn danh (không chứa tên người viết, mỗi dòng trích tối đa 2 câu),
kiểm tra tính toàn vẹn dữ liệu (schema, không trùng ID, không chứa cột PII, mức sao hợp lệ)
và xuất bảng đếm x/N (%) tái lập 100%.
"""
import argparse
import csv
import sys
from collections import Counter
from pathlib import Path

for _stream in (sys.stdout, sys.stderr):
    try:
        _stream.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass

DEFAULT_CSV = Path(__file__).resolve().parent / "reviews_raw.csv"

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
FORBIDDEN_PII_COLS = {"author", "user", "username", "reviewer", "name", "email", "phone"}


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Đếm nhãn review công khai đã ẩn danh (Track C · C1).")
    parser.add_argument("--csv", default=str(DEFAULT_CSV), help="Đường dẫn file CSV cần đếm")
    args = parser.parse_args(argv)

    csv_path = Path(args.csv).resolve()
    if not csv_path.exists():
        print(f"Không tìm thấy file: {csv_path}", file=sys.stderr)
        return 1

    with csv_path.open("r", encoding="utf-8-sig", newline="") as f:
        reader = csv.DictReader(f)
        cols = {(c or "").strip() for c in (reader.fieldnames or [])}
        missing = REQUIRED_COLS - cols
        if missing:
            print(f"Thiếu cột bắt buộc trong CSV: {sorted(missing)}", file=sys.stderr)
            return 1
        pii_cols = {c for c in cols if c.lower() in FORBIDDEN_PII_COLS}
        if pii_cols:
            print(f"Vi phạm ẩn danh — phát hiện cột PII cần xoá ngay: {sorted(pii_cols)}", file=sys.stderr)
            return 1
        rows = list(reader)

    total = len(rows)
    if total == 0:
        print("File CSV chưa có dòng review nào.", file=sys.stderr)
        return 1

    seen_ids: set[str] = set()
    label_counts: Counter[str] = Counter()
    star_counts: Counter[str] = Counter()
    source_counts: Counter[str] = Counter()
    dates: list[str] = []
    pain_unique_ids: list[str] = []

    for idx, row in enumerate(rows, start=1):
        rid = (row.get("id") or "").strip()
        if not rid:
            print(f"Lỗi dòng {idx}: thiếu id.", file=sys.stderr)
            return 1
        if rid in seen_ids:
            print(f"Lỗi dòng {idx}: trùng id '{rid}'.", file=sys.stderr)
            return 1
        seen_ids.add(rid)

        stars = (row.get("stars") or "").strip()
        if stars not in {"1", "2", "3", "4", "5"}:
            print(f"Cảnh báo {rid}: cột stars='{stars}' ngoài khoảng 1..5.", file=sys.stderr)
        star_counts[stars] += 1

        source_counts[(row.get("source_name") or "").strip()] += 1
        rdate = (row.get("review_date") or "").strip()
        if rdate:
            dates.append(rdate)

        quote = (row.get("quote_max_2_sentences") or "").strip()
        if not quote:
            print(f"Lỗi {rid}: quote_max_2_sentences trống.", file=sys.stderr)
            return 1

        labels = [lb.strip() for lb in (row.get("labels") or "").split(";") if lb.strip()]
        if not labels:
            print(f"Lỗi {rid}: chưa gắn nhãn ở cột labels.", file=sys.stderr)
            return 1
        unknown = [lb for lb in labels if lb not in VALID_LABELS]
        if unknown:
            print(f"Lỗi {rid}: nhãn không hợp lệ {unknown}.", file=sys.stderr)
            return 1

        for lb in labels:
            label_counts[lb] += 1
        if any(lb in PAIN_LABELS for lb in labels):
            pain_unique_ids.append(rid)

    pain_any = len(pain_unique_ids)
    date_range = f"{min(dates)} -> {max(dates)}" if dates else "không rõ"

    print("=" * 78)
    print("TỔNG HỢP ĐÀO DATA REVIEW CÔNG KHAI — ApexFour (Track C · C1)")
    print("=" * 78)
    print(f"File dữ liệu : {csv_path.name} (kiểm ẩn danh & schema: OK)")
    print(f"Tổng mẫu (N) : {total} review (bài gốc >= 10 từ, mọi mức sao 1-5)")
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
