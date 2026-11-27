# Take note CP2 — Phần việc Lê Văn Hoàng (`2A202603357`)

- **Nhánh:** `LeVanHoang-2A202603357` (đã merge vào `main`)
- **Cập nhật lúc:** 27/11/2026 18:20
- **Kiểm tra:** `python evidence/count_reviews.py` và `python run.py check` (phần `TEAMS.md` đạt chuẩn 100%, 0 lỗi format).

---

## 1. Các file đã hoàn thành & tích hợp sẵn vào `main`

1. **`evidence/reviews_raw.csv`**: Bảng tổng hợp chính thức **39 review tiếng Việt công khai thật** từ Google Play VinWonders (`com.vinwonders.app`, ẩn danh 100%, trích ≤2 câu/review, đủ link & ngày xem `2026-11-27`).
2. **`evidence/count_reviews.py`**: Script đếm tái lập 100% (`python evidence/count_reviews.py`), tự kiểm tra schema, chống lộ cột PII, chống trùng ID, đếm **số review duy nhất** gặp `L1`–`L5` (**11/39 = 28.2%**) và xuất bảng Markdown.
3. **`evidence/data-mining.md`**: Điền đầy đủ Mục 1–5 chuẩn Rubric R1 (cách đếm, đọc trước đếm sau, bảng kết quả `x/N (%)`, 7 trích dẫn nguyên văn `R02, R03, R18, R27, R32, R33, R39`, giới hạn data).
4. **`evidence/summary.md`**: Tổng hợp số liệu CP2 (`11/39 = 28.2%`), 6 trích dẫn nguyên văn, đánh giá giả thuyết sơ bộ và **bảng Lịch hẹn 3 cuộc phỏng vấn** (`P1`–`P3`) cho CP3. *(Đã xoá `evidence/survey/TEMPLATE.md` theo đúng hướng dẫn vì nhóm không dùng khảo sát).*
5. **`evidence/interviews/TEMPLATE.md`**: Bộ 6 câu hỏi phỏng vấn Mom Test chuẩn cho Track C · C1 (sẵn sàng chép sang `P1.md`–`P3.md`).
6. **`spec.md` §1 (dòng Bằng chứng) & §2 (Bảng Impact 3 hướng C1/C2/C3)**: Đã điền trực tiếp chuẩn Rubric R2 & R6 (mô tả 3 hướng **0 chữ AI**, số liệu trỏ về `evidence/data-mining.md`, công thức Impact theo cả toàn khu `8.460 giờ/tháng` lẫn từng gia đình `60 phút/gia đình/tháng` để khớp với §8, giữ lại 2 hướng loại kèm lý do, và 3 persona chi phí).
7. **`canvas.md` dòng 4**: Đã cập nhật số đầu tiên (`11/39 = 28.2%`) + trích dẫn thật (`R32`) + tiến độ hẹn phỏng vấn `P1`–`P3`.
8. **`TEAMS.md`**: Đã sửa lại `Link repo` đúng tên chính thức `https://github.com/quangtrung0812/K5-Day15-L3A-ApexFour` và cập nhật dòng phần việc của Lê Văn Hoàng khớp Track C.

---

## 2. Phối hợp tiếp theo với nhóm

- **@Trung & @Hưng:** Khi merge nhánh kiến trúc/code vào `main`, giữ nguyên `spec.md` §1–§2 và `canvas.md` dòng 4 đã điền sẵn.
- **@Bình (18:55):** Hoàng cùng Bình chấm độc lập 5 output mẫu theo `eval/metric_spec.yaml` để ghi độ khớp `__/5` vào `eval/README.md` mục 3.
- **@Hoàng (tối 27/11 – trước 09:00 sáng 28/11):** Thực hiện 3 cuộc phỏng vấn `P1`–`P3` theo `evidence/interviews/TEMPLATE.md`, cập nhật `evidence/summary.md` và tinh chỉnh con số phút chuẩn bị thực tế ở `spec.md` §2 trước **CP3 (10:00 Thứ Bảy 28/11)**.
