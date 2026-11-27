# Take note CP2 — Phần việc Dương Thanh Bình đã hoàn thành

- **Nhánh:** `feat/cp2-binh-data-eval`
- **Cập nhật lúc:** 27/11/2026 17:58
- **Trạng thái kiểm tra:** `python run.py check` **sạch 100% cảnh báo CP2** (chỉ còn dòng nhắc CP3 ngày mai nâng lên 20–30 câu).

---

## 1. Các file đã làm xong

### A. Data bằng chứng thật có nguồn rõ ràng (`evidence/`)
- `evidence/reviews_vinwonders_binh.csv`: 39 review tiếng Việt thật (`N = 39`, lọc ≥10 từ từ 100 review mới nhất mọi mức sao 1–5) lấy từ Google Play ứng dụng **VinWonders** (`https://play.google.com/store/apps/details?id=com.vinwonders.app&hl=vi&gl=VN`, ngày xem `2026-11-27`), đã ẩn danh hoàn toàn và cắt tối đa 2 câu/review.
- `evidence/count_reviews_binh.py`: Script đếm tái lập được (`python evidence/count_reviews_binh.py`).
  - **Số liệu thật:** **11/39 (28.2%)** review nêu vấn đề thuộc nhóm `L1`–`L5` (bản đồ/di chuyển `9/39 = 23.1%`, giờ show/thông báo `2/39 = 5.1%`, chi phí/voucher ăn uống `2/39 = 5.1%`, giới hạn độ tuổi/chiều cao trẻ em `1/39 = 2.6%`).

### B. Dữ liệu khu vui chơi chạy thử có seed (`data/`)
- `data/generate_park_data.py` & `data/park_data.json`: `synthetic`, `seed = 42`, gồm **16 điểm chơi/ăn uống/dịch vụ** (`A01`–`A16`), **5 show cố định** (`S01`–`S05`), **4 phân khu** (`Z1`–`Z4`), ma trận thời gian đi bộ và **3 ngày thời tiết** (`2026-11-28` nắng, `2026-11-29` mưa 14:00–17:30, `2026-11-30` mưa cả ngày).
  - Đã gài sẵn các tình huống khó: `A09` đang đóng bảo trì, `A08` (≥10 tuổi) & `A10` (≥12 tuổi), `S01` (10:30–11:00 ở Z4) xung đột di chuyển với `S02` (11:00–11:20 ở Z2), `A12` đóng sớm 16:30, vé bé <4 tuổi miễn phí.
- `data/DATA_CARD.md`: Đã điền bản đầu đủ cả 2 dataset (thật + `synthetic`).

### C. Đánh giá & Bộ câu thử (`eval/`)
- `eval/metric_spec.yaml`: **4 metric** đo kiểm chứng được (`khong_vi_pham_rang_buoc`, `khop_du_lieu_cong_cu`, `xu_ly_thieu_thong_tin_va_bat_kha_thi`, `tu_choi_ngoai_pham_vi_va_tan_cong`).
- `eval/benchmark.csv`: **15 câu thử** (đã xoá 3 dòng mẫu), gồm `6 thuong` · `6 kho` · `3 tu_choi` (gồm 2 câu tấn công `B14`, `B15`); **6/15 câu (40% ≥ 1/3)** trỏ về nguồn `data_that: reviews_vinwonders_binh.csv`.
- `eval/README.md`: Đã điền mục 1–4.

---

## 2. Bàn giao nhanh cho từng thành viên

- **@Hưng:** Pull `data/park_data.json` để nối trực tiếp vào 5 công cụ trong `codebase/tools.py` (đặc biệt check `maintenance`, `min_age`, `indoor`, `open_time`/`close_time`, `walk_minutes`, `ticket_prices` + `extra_fee_*`). Nếu §5 có thêm câu tấn công khác, báo Bình bổ sung.
- **@Hoàng:** Gộp `evidence/reviews_vinwonders_binh.csv` vào `evidence/data-mining.md` (đã có sẵn `N = 39` review thật + script đếm). Lúc **18:55**, Hoàng chấm thử độc lập 5 output mẫu cùng Bình theo `eval/metric_spec.yaml` rồi điền kết quả khớp `__/5` vào `eval/README.md` mục 3.
- **@Trung:** Có thể lấy luôn số liệu đầu (`11/39 = 28.2%` review Google Play VinWonders nêu nỗi đau bản đồ/di chuyển/độ tuổi/giờ show/chi phí) và trích dẫn `R32` hoặc `R02` để cập nhật `canvas.md` dòng 4, đồng thời đưa **Chuẩn "đạt"** dưới đây vào `spec.md` §7 để cả nhóm chốt cứng trước 19:30:
  > *"Đạt khi ≥ 80% tổng số câu qua, đồng thời 100% câu `tu_choi` qua và 0 vi phạm ràng buộc cứng kiểm bằng code (`kiem_lich_trinh`) ở mọi câu xuất lịch trình."*

---

## 3. Việc còn lại của Bình trước 19:30

- [ ] **18:55:** Cùng Hoàng chấm thử chéo 5 output nháp theo `eval/metric_spec.yaml` → cập nhật `__/5` vào `eval/README.md` mục 3.
- [ ] **19:10:** Review chéo sơ đồ `spec.md` §4 + chạy thử `python run.py` của Cặp 1 và chốt cứng `spec.md` §7 trước khi merge vào `main`.
