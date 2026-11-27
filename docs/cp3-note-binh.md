# Take note CP3 — Phần việc Dương Thanh Bình

- **Nhánh:** `feat/cp3-binh-benchmark25` (tách từ `main` @ `f90948a`)
- **File đã sửa / thêm (độc quyền theo `docs/cp3-plan.md`):** `eval/benchmark.csv`, `eval/grade_helper.py`, `eval/README.md`, `data/DATA_CARD.md`, `docs/cp3-note-binh.md`
- **Không đụng:** `eval/metric_spec.yaml`, chuẩn "đạt" `spec.md` §7, `B01`–`B15` (diff `eval/benchmark.csv` chỉ có **10 dòng thêm**, 0 dòng sửa/xoá).
- **Kiểm tra:** `python run.py check` → *"Không thấy vấn đề"* (25 câu · thuong 8 · kho 13 · tu_choi 4 · data thật 10/25).

---

## 1. Mười câu mới `B16`–`B25`

| ID | Type | Tình huống | Source | Đáp án số đã kiểm bằng `kiem_lich_trinh` |
|---|---|---|---|---|
| B16 | thuong | Chỉ đi Z1/Z2 vì app định vị sai, 2 bé 5+7 | `data_that` R09, R33 | Lịch mẫu hợp lệ, tổng 3.520.000đ (vé 3.080.000 + A07 440.000) |
| B17 | kho | Hồ bơi A13 đóng khi vừa tới, xếp lại 13:00–17:00 | `data_that` HL01 | Lịch thay thế hợp lệ, 2.420.000đ |
| B18 | kho | A11 tạm dừng đột xuất, xếp lại 14:00–18:00 | `data_that` HL04 | Lịch thay thế hợp lệ (đã kiểm đủ giờ đi bộ), 2.420.000đ |
| B19 | kho | 2 bé lệch tuổi 3+11, bé lớn đòi A08 | `data_that` R32 | Vé cổng 2.420.000đ (bé 3 tuổi 0đ); A08 → `GIOI_HAN_TUOI` |
| B20 | kho | Đòi điểm không tồn tại (Show Cá Heo, Vòng quay Mặt Trời) | `tu_viet` | Không có trong `park_data.json` |
| B21 | kho | Mưa đột xuất 13:00 trong ngày dự báo nắng | `sinh_seed` | A02 sau 13:00 → `MUA_NGOAI_TROI`; lịch trong nhà hợp lệ |
| B22 | kho | Ngày 2026-12-05 không có dữ liệu | `sinh_seed` | `tra_thoi_tiet` → `co_du_lieu=False`, `tra_lich_show` → `[]` |
| B23 | thuong | Buffet A15 + ăn tối + show đêm S05 | `sinh_seed` | Lịch mẫu hợp lệ, tổng 3.900.000đ |
| B24 | kho | Đủ vé cổng nhưng thiếu tiền phụ thu A06/A07 | `sinh_seed` | A06 → 3.400.000đ `VUOT_NGAN_SACH`; A06+A07 = 3.840.000đ |
| B25 | tu_choi | Đặt khách sạn + gọi taxi (ngoài phạm vi) | `tu_viet` | — |

---

## 2. Bàn giao cho Trung (Integrator)

- Cập nhật `spec.md` §7 dòng đầu: **25 câu (8 `thuong`, 13 `kho`, 4 `tu_choi`), 4 metric** — giữ nguyên câu Chuẩn "đạt".
- Ghi changelog `spec.md` §10 (CP2 → CP4): *"27/11 tối — Thêm B16–B25 (không sửa B01–B15) để đủ 20–30 câu CP3, phủ thêm: điểm đóng đột xuất, mưa người dùng báo, hai bé lệch tuổi, điểm không tồn tại, ngày không có dữ liệu, thiếu tiền phụ thu, ngoài phạm vi."*
- Lưu ý cho agent khi chạy Lượt 1 (phát hiện từ `python eval/grade_helper.py --dry-run-agent`, Bình không tự sửa `agent.py`/`tools.py` để giữ 0 conflict):
  1. **Regex khung giờ trong `agent.py` (`B17`, `B21`):** Khi câu có dạng *"13:00 nhà mình mới tới... xếp lại từ 13:00 đến 17:00"*, parser hiện bắt 2 mốc giờ đầu tiên thành `13:00`–`13:00` → báo lỗi `Giờ kết thúc phải sau giờ bắt đầu`. Ưu tiên bắt cụm `(?:từ|tu)\s*(HH:MM)\s*(?:đến|den|tới|-|–)\s*(HH:MM)` trước sẽ hết ngay.
  2. **Chốt 1 Guardrail (`B25`):** Bổ sung từ khoá ngoài phạm vi (`đặt phòng`, `khách sạn`, `gọi taxi`, `gọi xe`, `vé máy bay`) vào Chốt 1 để từ chối thẳng thay vì rơi xuống Chốt 2 hỏi số người lớn/trẻ em.
  3. **Điểm đóng đột xuất người dùng báo (`B17` báo A13 đóng, `B18` báo A11 tạm dừng):** `kiem_lich_trinh` đã có `mua_tu` và `show_da_huy`; Hưng có thể thêm tuỳ chọn `diem_da_dong=()` hoặc prompt nhắc model loại điểm khách vừa báo đóng.
  4. **Công cụ hỗ trợ chấm nhanh Lượt 1:** Chạy `python eval/grade_helper.py eval/run-1.csv` (chỉ đọc, không sửa file) để kiểm tức thì 2 metric `grader: code` (`khong_vi_pham_rang_buoc`, `khop_du_lieu_cong_cu`) cho cả 25 câu trong 1 giây trước khi điền cột `pass`.

---

## 3. Chấm thử độc lập 5 output (Rubric R4) — Bình tự điền

> Bảng ở `eval/README.md` mục 3 hiện ghi Bình 5/5 khớp Hoàng. Bình cần **tự đọc lại** 5 output trong `eval/cp2-cham-cheo.csv` theo `pass_criterion` và xác nhận điểm của mình dưới đây (không xem cột của Hoàng trước).

| Câu | Bình chấm (`1`/`0`) | Lý do ngắn |
|---|---|---|
| B01 | `__` | |
| B07 | `__` | |
| B08 | `__` | |
| B09 | `__` | |
| B15 | `__` | |
