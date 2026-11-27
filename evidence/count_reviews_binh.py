"""Script đếm nhãn review công khai (chạy lại được 100%) — phần Dương Thanh Bình thu thập.

Chạy:
    python evidence/count_reviews_binh.py
"""
import csv
from collections import Counter
from pathlib import Path

CSV_PATH = Path(__file__).resolve().parent / "reviews_vinwonders_binh.csv"
PAIN_LABELS = {
    "L1_TRE_SHOW_GIO_MO_CUA",
    "L2_DI_CHUYEN_RONG_MET",
    "L3_TRE_NHO_DO_TUOI",
    "L4_THOI_TIET_MUA",
    "L5_GIA_PHAT_SINH",
}


def main() -> None:
    with CSV_PATH.open("r", encoding="utf-8", newline="") as f:
        rows = list(csv.DictReader(f))

    total = len(rows)
    label_counts = Counter()
    pain_any = 0
    star_counts = Counter()

    for row in rows:
        star_counts[row["stars"]] += 1
        labels = [lb.strip() for lb in row["labels"].split(";") if lb.strip()]
        for lb in labels:
            label_counts[lb] += 1
        if any(lb in PAIN_LABELS for lb in labels):
            pain_any += 1

    print(f"Nguồn: Google Play VinWonders (com.vinwonders.app) | Tổng mẫu N = {total} review (>=10 từ, mọi mức sao)")
    print(f"Phân bố sao: " + ", ".join(f"{k}*: {star_counts[k]}" for k in sorted(star_counts)))
    print(f"Tổng review liên quan bài toán xếp lịch / bản đồ / giờ / tuổi / chi phí (L1-L5): {pain_any}/{total} ({pain_any/total*100:.1f}%)")
    print("-" * 70)
    for lb in [
        "L1_TRE_SHOW_GIO_MO_CUA",
        "L2_DI_CHUYEN_RONG_MET",
        "L3_TRE_NHO_DO_TUOI",
        "L4_THOI_TIET_MUA",
        "L5_GIA_PHAT_SINH",
        "L0_KHAC",
    ]:
        c = label_counts[lb]
        print(f"  {lb:<25}: {c:2d}/{total} ({c/total*100:5.1f}%)")


if __name__ == "__main__":
    main()
