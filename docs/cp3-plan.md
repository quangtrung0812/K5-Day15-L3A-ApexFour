# Kế hoạch & Phân công CP3 (Độc lập, 0 Conflict) — Nhóm ApexFour (Track C · C1)

- **Mục tiêu:** Nộp đủ **CP3 (4 điểm)** trước **10:00 Thứ Bảy 28/11/2026** (thời gian làm: tối Thứ Sáu 27/11 → sáng Thứ Bảy 28/11).
- **Nguyên tắc chia việc:** 4 nhánh độc lập hoàn toàn, **không ai sửa trùng file của ai (Zero Merge Conflict)** để sáng Thứ Bảy chỉ có **1 người duy nhất (Đội trưởng Trung)** kéo cả 3 nhánh về review 1 lần, merge vào `main`, chạy `eval` Lượt 1 bằng AI thật và nộp CP3.

> [!IMPORTANT]
> **4 luật sống còn của CP3:**
> 1. Cả 4 người tạo nhánh mới từ **`origin/main` bản CP2 mới nhất (`bdf3005`)**.
> 2. **Tuyệt đối KHÔNG sửa:** `eval/metric_spec.yaml`, **Chuẩn "đạt"** ở `spec.md` §7, và không sửa `expected` hay xoá 15 câu cũ `B01`–`B15` trong `eval/benchmark.csv` (sửa sau CP2 → khối R4 bị **0 điểm**).
> 3. **Chỉ Trung sửa `spec.md` và `README.md`.** Ba thành viên còn lại ghi phần cần cập nhật vào `docs/cp3-note-<ten>.md` để Trung review và ghép 1 lần.
> 4. **Tuyệt đối KHÔNG commit `.env` hay API key** (−10 điểm).

---

## 1. Bảng phân công 4 nhánh độc lập (Zero File Conflict)

| Thành viên | Nhánh riêng | File ĐỘC QUYỀN sửa | Deadline đẩy nhánh |
|---|---|---|---|
| **Lê Văn Hoàng** | `feat/cp3-hoang-interviews` | `evidence/interviews/P1.md`, `P2.md`, `P3.md`, `evidence/summary.md`, `docs/cp3-note-hoang.md` | Trước **08:15 T7 28/11** |
| **Dương Thanh Bình** | `feat/cp3-binh-benchmark25` | `eval/benchmark.csv`, `eval/README.md`, `data/DATA_CARD.md`, `docs/cp3-note-binh.md` | Trước **08:15 T7 28/11** |
| **Nguyễn Quốc Hưng** | `feat/cp3-hung-tools-cost` | `codebase/tools.py`, `tests/test_park_tools.py`, `tests/test_agent_tools.py`, `cost/personas.yaml`, `cost/cost-estimate.md`, `docs/cp3-note-hung.md` | Trước **08:15 T7 28/11** |
| **Nguyễn Quang Trung** *(Integrator duy nhất)* | `feat/cp3-trung-ai-real` → merge cuối vào `main` | `codebase/ai.py`, `codebase/agent.py`, `spec.md`, `README.md` | Nộp CP3 trước **10:00 T7 28/11** |

---

## 2. Chi tiết công việc từng người

### 1. Lê Văn Hoàng — `feat/cp3-hoang-interviews` *(Phỏng vấn nguồn 2 & Chốt bằng chứng R1–R2)*
1. Thực hiện **≥3 cuộc phỏng vấn thật ngoài nhóm** (đúng người dùng: phụ huynh hoặc người từng lập lịch đi khu vui chơi) theo `evidence/interviews/TEMPLATE.md`, lưu thành `evidence/interviews/P1.md`, `P2.md`, `P3.md` (ẩn danh, hỏi chuyện đã xảy ra, ghi số phút tốn + trích dẫn nguyên văn).
2. Cập nhật `evidence/summary.md`: đủ 2 nguồn (đào data `11/39 = 28.2%` + phỏng vấn `x/3`, không ghi `%` khi `n` nhỏ), so sánh khớp/lệch giữa 2 nguồn, kết luận giả thuyết.
3. Đọc 5 đầu ra trong `eval/cp2-cham-cheo.csv` và **tự chấm độc lập 5 điểm (`1`/`0`)** của Hoàng vào `docs/cp3-note-hoang.md` (kèm nháp số phỏng vấn cập nhật cho bảng Impact `spec.md` §2).

### 2. Dương Thanh Bình — `feat/cp3-binh-benchmark25` *(Mở rộng Benchmark 15 → 25 câu & Eval R4)*
1. **Thêm mới 10 câu thử `B16`–`B25`** vào cuối `eval/benchmark.csv` (tổng **25 câu**; giữ nguyên 100% `B01`–`B15`):
   - Thêm ≥3 câu có `source: data_that:` (từ review `R03/R09/R33/R39` và `evidence/hung-ha-long.md`) để tổng nguồn thật đạt `≥ 9/25` (vượt chuẩn ≥1/3).
   - Phủ thêm các tình huống khó: mưa đột xuất giữa ngày, show huỷ đột xuất, gia đình có nhiều bé lệch tuổi (vd 3 tuổi + 11 tuổi), hỏi điểm không tồn tại trong dữ liệu, và thêm 1 câu `tu_choi` ngoài phạm vi.
2. Đọc 5 đầu ra trong `eval/cp2-cham-cheo.csv`, **tự chấm độc lập 5 điểm (`1`/`0`)** của Bình ghi vào `docs/cp3-note-binh.md` (để Trung đối chiếu với 5 điểm của Hoàng rồi chốt mục 3 `eval/README.md`).
3. Cập nhật số câu thử (`25 câu`) trong `eval/README.md` mục 2 và `data/DATA_CARD.md`; chạy `python run.py check` xác nhận **0 cảnh báo**.

### 3. Nguyễn Quốc Hưng — `feat/cp3-hung-tools-cost` *(Siết Tool/Test & Khung Chi phí)*
1. Siết edge-case trong `codebase/tools.py` và bổ sung test trong `tests/test_park_tools.py` (chặn ghi đè giá/bảo trì kiểu `B15`, đổi lịch khi báo mưa/huỷ show đột xuất giữa ngày).
2. Hoàn thiện `cost/personas.yaml`: ≥3 kiểu người dùng (xếp 1 lần · sửa nhiều lần trước đi · ngày mưa xếp lại nhiều lần), tỉ lệ %, số lần dùng/tháng (có nguồn hoặc ghi rõ *(tự ước tính)*), giá trả phí của **≥2 mức model** kèm link nguồn + ngày xem `27/11/2026`.
3. Chạy thử `python -m unittest discover -s tests` (pass 100%) và `python run.py simulate --try` (chế độ giả để kiểm tra không lỗi schema `personas.yaml`), ghi note bàn giao vào `docs/cp3-note-hung.md`.

### 4. Nguyễn Quang Trung — `feat/cp3-trung-ai-real` *(Nối AI thật + Review & Ghép duy nhất)*
- **Phần làm độc lập (tối Thứ Sáu 27/11 — nên xong trước khi ngủ):**
  1. Nối API model thật trong `codebase/ai.py` theo `docs/connect-model.md` (key lưu trong `.env` local, **không commit**). Chạy `python run.py eval --try` xác nhận `tokens > 0` và "Nối model được".
  2. Sửa 2 lỗi đã lộ ra ở bảng đối chiếu CP2 trong `codebase/agent.py`:
     - `B15`: chặn cứng prompt injection tự xưng quản lý đòi đổi giá/mở bảo trì ở Chốt 1 (từ chối dứt khoát thay vì hỏi lại thông tin chuyến đi).
     - `B01`: đảm bảo output có giải thích rõ lý do tối ưu tuyến đi gọn giữa các khu.
- **Khâu review & ghép 1 lần duy nhất (08:30 – 09:45 Sáng Thứ Bảy 28/11):**
  1. Kéo 3 nhánh (`feat/cp3-hoang-interviews`, `feat/cp3-binh-benchmark25`, `feat/cp3-hung-tools-cost`) → review 1 lượt → merge vào `main` (0 conflict).
  2. Cập nhật `spec.md` (§1–§2 từ `docs/cp3-note-hoang.md`, §7 cập nhật 25 câu nhưng **giữ nguyên chuẩn "đạt"**, §10 ghi changelog mọi thay đổi sau CP2) và chốt kết quả chấm chéo 2 người thật (`Bình` vs `Hoàng`) vào `eval/README.md` mục 3.
  3. Chạy `python run.py check` (0 cảnh báo) + `python -m unittest discover -s tests` (pass 100%).
  4. Chạy **`python run.py eval`** (AI thật trên đủ 25 câu) → `eval/run-1.csv` + `traces/run-1.jsonl` → cả nhóm chấm cột `pass` trong 15 phút → `python run.py score eval/run-1.csv`.
  5. Chạy **`python run.py simulate --try`** (10 phiên AI thật) → `cost/simulate-try.csv`.
  6. Quay **video 30 giây** thao tác thật + AI trả kết quả thật (YouTube "Không công khai" hoặc Google Drive "Bất kỳ ai có đường liên kết", kiểm tra mở bằng cửa sổ ẩn danh).
  7. Push `main` (kiểm `git status` không dính `.env`) → nộp form CP3 trước **10:00 Thứ Bảy 28/11**.

---

## 3. Checklist tự soát CP3 trước 10:00

- [ ] Bằng chứng pain đạt ngưỡng ≥1 nguồn + ≥5 trích dẫn nguyên văn (`evidence/summary.md`, có nguồn 2 phỏng vấn `P1`–`P3`) · bảng impact (`spec.md` §2).
- [ ] `eval/benchmark.csv`: 20–30 câu (mục tiêu 25 câu), ≥5 `kho`, ≥2 `tu_choi`, ≥1/3 nguồn thật; `python run.py check` **0 cảnh báo**.
- [ ] Bản chạy thử gọi AI thật (`python run.py eval --try` có `tokens > 0`) · **video 30 giây** mở được ẩn danh.
- [ ] `eval/run-1.csv` (đã chấm cột `pass`) + kết quả `python run.py score eval/run-1.csv` + `traces/run-1.jsonl`.
- [ ] `cost/simulate-try.csv` chạy thử 10 phiên thành công.
- [ ] `spec.md` đủ §0–§7 + ghi changelog mọi thay đổi sau CP2 vào §10 (không sửa chuẩn "đạt").
- [ ] Không có `.env` / API key trong repo.
