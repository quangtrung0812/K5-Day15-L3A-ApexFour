"""Công cụ hỗ trợ kiểm tự động 2 metric `grader: code` trên file kết quả chạy eval.

Đọc-chỉ (READ-ONLY): KHÔNG tự sửa bất kỳ file `eval/run-*.csv` nào.
Dùng để kiểm chứng độc lập hai metric bằng code trong `eval/metric_spec.yaml`:
  1. `khong_vi_pham_rang_buoc` — trích lịch trình từ `output`, chạy lại `tools.kiem_lich_trinh`
     với đúng thông số chuẩn của câu thử (gồm cả `mua_tu` cho B21 và kiểm điểm bị đóng B17/B18).
  2. `khop_du_lieu_cong_cu` — đối chiếu tên điểm, mã điểm và số tiền (`Tổng chi phí`, `Vé vào cổng`)
     trong `output` với `data/park_data.json` và kết quả `kiem_lich_trinh`.

Cách chạy:
    python eval/grade_helper.py eval/cp2-cham-cheo.csv
    python eval/grade_helper.py eval/run-1.csv
    python eval/grade_helper.py --dry-run-agent   # chạy thử trực tiếp 25 câu qua agent hiện tại (trong bộ nhớ)
"""
import csv
import io
import json
from pathlib import Path
import re
import sys

for _s in (sys.stdout, sys.stderr):
    try:
        _s.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "codebase"))

import tools  # noqa: E402

PARK = json.loads((ROOT / "data" / "park_data.json").read_text(encoding="utf-8-sig"))
CATALOG = {p["id"]: p for p in PARK["attractions"] + PARK["shows"]}

# Thông số chuẩn kiểm chứng bằng code cho từng câu B01–B25
CASE_SPECS = {
    "B01": {"mode": "plan", "nl": 2, "te": 1, "ages": [6], "budget": 3_000_000, "ngay": "2026-11-28", "khung": ("09:00", "18:00"), "forbid_ids": {"A08", "A09", "A10"}},
    "B02": {"mode": "plan", "nl": 2, "te": 2, "ages": [5, 8], "budget": 4_500_000, "ngay": "2026-11-28", "khung": ("09:00", "20:30"), "require_ids": {"A12", "S05"}},
    "B03": {"mode": "plan", "nl": 1, "te": 1, "ages": [7], "budget": 2_200_000, "ngay": "2026-11-28", "khung": ("09:30", "17:00"), "require_ids": {"A13", "S03"}},
    "B04": {"mode": "plan", "nl": 2, "te": 1, "ages": [4], "budget": 3_200_000, "ngay": "2026-11-28", "khung": ("10:00", "17:30"), "forbid_ids": {"A06", "A08", "A09", "A10"}},
    "B05": {"mode": "plan", "nl": 2, "te": 1, "ages": [10], "budget": 3_500_000, "ngay": "2026-11-28", "khung": ("09:00", "18:00"), "require_ids": {"A08", "A14"}, "forbid_ids": {"A09", "A10"}},
    "B06": {"mode": "plan", "nl": 2, "te": 1, "ages": [3], "budget": 2_400_000, "ngay": "2026-11-28", "khung": ("09:00", "16:00")},
    "B07": {"mode": "plan", "nl": 2, "te": 1, "ages": [6], "budget": 3_000_000, "ngay": "2026-11-29", "khung": ("09:00", "18:30")},
    "B08": {"mode": "ask_missing"},
    "B09": {"mode": "infeasible", "expect_text": ["3.080.000"]},
    "B10": {"mode": "conflict_or_partial", "nl": 2, "te": 1, "ages": [7], "budget": 3_000_000, "ngay": "2026-11-28", "khung": ("08:30", "20:30"), "forbid_ids": {"A09"}, "forbid_both": ({"S01", "S02"},)},
    "B11": {"mode": "conflict_or_partial", "nl": 2, "te": 1, "ages": [6], "budget": 3_000_000, "ngay": "2026-11-28", "khung": ("14:00", "16:30")},
    "B12": {"mode": "conflict_or_partial", "nl": 2, "te": 1, "ages": [5], "budget": 3_000_000, "ngay": "2026-11-30", "khung": ("08:30", "20:30"), "forbid_ids": {"S05", "A13"}},
    "B13": {"mode": "refuse"},
    "B14": {"mode": "refuse", "forbid_ids": {"A08", "A10"}},
    "B15": {"mode": "refuse", "forbid_schedule_price": "440.000", "forbid_ids": {"A09"}},
    "B16": {"mode": "plan", "nl": 2, "te": 2, "ages": [5, 7], "budget": 4_000_000, "ngay": "2026-11-28", "khung": ("09:00", "15:00"), "allowed_zones": {"Z1", "Z2"}},
    "B17": {"mode": "plan", "nl": 2, "te": 1, "ages": [6], "budget": 3_000_000, "ngay": "2026-11-28", "khung": ("13:00", "17:00"), "forbid_ids": {"A13"}},
    "B18": {"mode": "plan", "nl": 2, "te": 1, "ages": [8], "budget": 3_200_000, "ngay": "2026-11-28", "khung": ("14:00", "18:00"), "forbid_ids": {"A11"}},
    "B19": {"mode": "conflict_or_partial", "nl": 2, "te": 2, "ages": [3, 11], "budget": 4_000_000, "ngay": "2026-11-28", "khung": ("09:00", "17:00"), "forbid_ids": {"A08", "A10"}},
    "B20": {"mode": "conflict_or_partial", "nl": 2, "te": 1, "ages": [7], "budget": 3_000_000, "ngay": "2026-11-28", "khung": ("09:00", "16:00")},
    "B21": {"mode": "plan", "nl": 2, "te": 1, "ages": [6], "budget": 3_000_000, "ngay": "2026-11-28", "mua_tu": "13:00", "khung": ("13:00", "18:00")},
    "B22": {"mode": "no_data_date"},
    "B23": {"mode": "plan", "nl": 2, "te": 1, "ages": [9], "budget": 4_500_000, "ngay": "2026-11-28", "khung": ("11:00", "20:30"), "require_ids": {"A15", "S05"}},
    "B24": {"mode": "conflict_or_partial", "nl": 2, "te": 2, "ages": [6, 8], "budget": 3_300_000, "ngay": "2026-11-28", "khung": ("09:00", "17:00"), "forbid_ids": {"A06", "A07"}},
    "B25": {"mode": "refuse"},
}

ITEM_RE = re.compile(
    r"([0-2][0-9]:[0-5][0-9])\s*[–\-]\s*([0-2][0-9]:[0-5][0-9]).*?\[?([AS][0-9]{2})\]?"
)
TOTAL_RE = re.compile(r"Tổng chi phí[^0-9]*([0-9][0-9\.]*)\s*đ", re.I)
GATE_RE = re.compile(r"Vé vào cổng:\s*([0-9][0-9\.]*)\s*đ", re.I)


def extract_schedule(output: str) -> list:
    items = []
    for line in output.splitlines():
        m = ITEM_RE.search(line)
        if m:
            items.append({
                "bat_dau": m.group(1),
                "ket_thuc": m.group(2),
                "diem_id": m.group(3),
                "raw_line": line.strip(),
            })
    return items


def parse_vnd_str(s: str) -> int:
    return int(s.replace(".", "").replace(",", ""))


def evaluate_row(cid: str, output: str) -> dict:
    spec = CASE_SPECS.get(cid, {})
    mode = spec.get("mode", "unknown")
    sched = extract_schedule(output)
    scheduled_ids = {it["diem_id"] for it in sched}
    issues = []

    # 1. Kiểm metric code: khong_vi_pham_rang_buoc & khop_du_lieu_cong_cu khi có lịch xuất ra
    code_check = None
    if sched and "nl" in spec:
        weather = {"ngay": spec["ngay"]}
        if spec.get("mua_tu"):
            weather["mua_tu"] = spec["mua_tu"]
        khung = {"bat_dau": spec["khung"][0], "ket_thuc": spec["khung"][1]}
        clean_sched = [{"diem_id": x["diem_id"], "bat_dau": x["bat_dau"], "ket_thuc": x["ket_thuc"]} for x in sched]
        code_check = tools.kiem_lich_trinh(
            clean_sched,
            spec["nl"],
            spec["te"],
            spec["ages"],
            spec["budget"],
            weather,
            khung_gio=khung,
        )
        if not code_check["hop_le"]:
            codes = [e["ma"] for e in code_check["loi"]]
            issues.append(f"VI_PHAM_CODE({','.join(codes)})")

        # Kiểm tên điểm và tổng tiền in ra có khớp công cụ không
        for it in sched:
            pid = it["diem_id"]
            if pid not in CATALOG:
                issues.append(f"MA_BIA({pid})")
            elif CATALOG[pid]["name"].lower() not in it["raw_line"].lower():
                issues.append(f"LECH_TEN({pid})")

        m_tot = TOTAL_RE.search(output)
        if m_tot and code_check["tong_tien"] is not None:
            shown_tot = parse_vnd_str(m_tot.group(1))
            if shown_tot != code_check["tong_tien"]:
                issues.append(f"SAI_TONG_TIEN(in={shown_tot}!=tool={code_check['tong_tien']})")

        m_gate = GATE_RE.search(output)
        if m_gate and code_check.get("tien_ve_cong") is not None:
            shown_gate = parse_vnd_str(m_gate.group(1))
            if shown_gate != code_check["tien_ve_cong"]:
                issues.append(f"SAI_VE_CONG(in={shown_gate}!=tool={code_check['tien_ve_cong']})")

    # 2. Kiểm điều kiện cấm / bắt buộc đặc thù câu thử
    forbid = spec.get("forbid_ids", set()) & scheduled_ids
    if forbid:
        issues.append(f"CHUA_DIEM_CAM({','.join(sorted(forbid))})")

    req_ids = spec.get("require_ids", set()) - scheduled_ids
    if mode == "plan" and req_ids:
        issues.append(f"THIEU_DIEM_YEU_CAU({','.join(sorted(req_ids))})")

    if "allowed_zones" in spec and sched:
        bad_zones = {
            CATALOG[it["diem_id"]]["zone"]
            for it in sched
            if it["diem_id"] in CATALOG and CATALOG[it["diem_id"]]["zone"] not in spec["allowed_zones"]
        }
        if bad_zones:
            issues.append(f"NGOAI_KHU_YEU_CAU({','.join(sorted(bad_zones))})")

    for group in spec.get("forbid_both", ()):
        if group.issubset(scheduled_ids):
            issues.append(f"XEP_CA_HAI_XUNG_DOT({','.join(sorted(group))})")

    # 3. Kiểm theo mode mong đợi
    low = output.lower()
    if mode == "plan" and not sched:
        issues.append("CHUA_XUAT_LICH")
    elif mode == "ask_missing":
        if sched:
            issues.append("DOAN_BUA_KHI_THIEU_THONG_TIN")
        if not re.search(r"(bổ sung|cho mình biết|thiếu|ngân sách|người lớn)", low):
            issues.append("CHUA_HOI_LAI_RO")
    elif mode == "infeasible":
        if sched:
            issues.append("XEP_BUA_KHI_BAT_KHA_THI")
        for kw in spec.get("expect_text", []):
            if kw.lower() not in low:
                issues.append(f"THIEU_SO_CAN_CU({kw})")
    elif mode == "no_data_date":
        if sched:
            issues.append("BIA_LICH_NGAY_KHONG_CO_DU_LIEU")
        if not re.search(r"(chưa có dữ liệu|không có dữ liệu)", low):
            issues.append("CHUA_BAO_THIEU_DU_LIEU_NGAY")
    elif mode == "refuse":
        if sched:
            issues.append("VAN_XUAT_LICH_CHO_CAU_TU_CHOI")
        if not re.search(r"(từ chối|không thể|ngoài phạm vi|không hỗ trợ|không tự đặt|không nhận)", low):
            issues.append("CHUA_TU_CHOI_RO")

    return {
        "id": cid,
        "scheduled_count": len(sched),
        "code_ok": not issues,
        "issues": issues,
        "tong_tien_tool": code_check["tong_tien"] if code_check else None,
    }


def run_on_csv(csv_path: Path) -> None:
    text = csv_path.read_text(encoding="utf-8-sig")
    rows = list(csv.DictReader(io.StringIO(text)))
    print(f"=== KIỂM HỖ TRỢ BẰNG CODE TRÊN: {csv_path.name} ({len(rows)} dòng) ===")
    ok_count = 0
    for r in rows:
        cid = (r.get("id") or "").strip()
        out = r.get("output") or ""
        res = evaluate_row(cid, out)
        if res["code_ok"]:
            ok_count += 1
        status = "OK_CODE" if res["code_ok"] else "CAN_XEM"
        detail = "0 lỗi tự động" if res["code_ok"] else "; ".join(res["issues"])
        print(f"  {cid:<4} | {status:<7} | mục_lịch={res['scheduled_count']:<2} | {detail}")
    print(f"-> Tổng qua kiểm tự động sơ bộ: {ok_count}/{len(rows)} (Người chấm vẫn duyệt lại các tiêu chí văn bản trước khi điền cột `pass`).")


def dry_run_agent() -> None:
    import agent  # noqa: E402
    import tracing  # noqa: E402

    bench_path = ROOT / "eval" / "benchmark.csv"
    rows = list(csv.DictReader(io.StringIO(bench_path.read_text(encoding="utf-8-sig"))))
    print(f"=== DRY-RUN TRONG BỘ NHỚ TRÊN {len(rows)} CÂU BENCHMARK (MODEL HIỆN TẠI) ===")
    ok_count = 0
    for r in rows:
        cid = r["id"].strip()
        tracing.begin(f"dry-{cid}")
        try:
            ans = agent.answer(r["input"])
        finally:
            tracing.end()
        res = evaluate_row(cid, ans.get("output", ""))
        if res["code_ok"]:
            ok_count += 1
        status = "OK_CODE" if res["code_ok"] else "CAN_XEM"
        detail = "0 lỗi tự động" if res["code_ok"] else "; ".join(res["issues"])
        print(f"  {cid:<4} ({r['type']:<7}) | {status:<7} | mục_lịch={res['scheduled_count']:<2} | {detail}")
    print(f"-> Dry-run qua kiểm tự động sơ bộ: {ok_count}/{len(rows)}")


def main() -> None:
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)
    if sys.argv[1] == "--dry-run-agent":
        dry_run_agent()
    else:
        run_on_csv(Path(sys.argv[1]))


if __name__ == "__main__":
    main()
