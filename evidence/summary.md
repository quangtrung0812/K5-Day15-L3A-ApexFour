# Tổng hợp bằng chứng pain

> Điền ở guide bước 1.2, xong trước **CP3 10:00 Thứ Bảy 28/11**. Chấm ở rubric R1.
> Ba nguồn ngang nhau — tối thiểu **≥1 nguồn đạt ngưỡng**. Nhóm dùng **Đào data (review công khai)** làm nguồn chính và **Phỏng vấn ≥3 người ngoài nhóm** để kiểm lại.

## 1. Nguồn đã dùng

| Nguồn | Đạt ngưỡng? | File |
|---|---|---|
| Đào data (x/N, %, cách đếm chạy lại được, ≥5 ví dụ) | ☑ *(đạt bản đầu CP2: `N = 39`, `11/39 = 28.2%`, 7 ví dụ)* | `evidence/data-mining.md` · `evidence/reviews_raw.csv` · `evidence/count_reviews.py` |
| Phỏng vấn (≥3 người ngoài nhóm, đúng người dùng) | ☐ *(đang thực hiện tối 27/11 – sáng 28/11, xem Lịch hẹn bên dưới)* | `evidence/interviews/P1.md`… *(sẽ cập nhật trước CP3)* |
| Khảo sát (≥20 người ngoài nhóm, đúng người dùng) | — *(không chọn ở `hypothesis.md`)* | — |

## 2. Số chính

- **Đào data (Google Play — VinWonders, `N = 39` review tiếng Việt ≥10 từ, mọi mức sao):**
  - **11/39 (28.2%)** review nêu ít nhất 1 vấn đề thuộc nhóm bài toán xếp lịch trình (`L1`–`L5`):
    - Bản đồ / chỉ đường / tối ưu thứ tự chơi (`L2`): **9/39 (23.1%)**
    - Giờ show / thông báo giờ cụ thể (`L1`): **2/39 (5.1%)**
    - Chi phí ăn uống / voucher phát sinh (`L5`): **2/39 (5.1%)**
    - Giới hạn độ tuổi / chiều cao trẻ em <1m4 (`L3`): **1/39 (2.6%)**
    - Thời tiết mưa (`L4`): **0/39 (0.0%)** — sẽ kiểm thêm qua phỏng vấn & bổ sung review điểm ngoài trời.
- **Phỏng vấn:** `0/3` người hoàn thành tại mốc CP2 *(đã chốt lịch hẹn 3 người ngoài nhóm bên dưới; sẽ cập nhật số lần / tháng và thời gian chuẩn bị thực tế trước CP3 10:00 Thứ Bảy 28/11)*.

| | Vai | Gặp pain? | Số lần / 1 năm qua | Lần gần nhất mất | Đang xoay xở bằng |
|---|---|---|---|---|---|
| P1 | *(chờ phỏng vấn 27/11 20:00)* | | | | |
| P2 | *(chờ phỏng vấn 27/11 21:00)* | | | | |
| P3 | *(chờ phỏng vấn 28/11 08:30)* | | | | |

## 3. ≥5 trích dẫn hoặc ví dụ nguyên văn (có nguồn, bỏ tên)

1. *"liệt kê tối ưu trò chơi, thời gian chơi, đường đi và thêm stick để người chơi lựa chọn trò xong app tối ưu (nếu được nên khuyến nghị nếu khách quá đông) là rất hay"* — `reviews_raw.csv` dòng `R02` (Google Play VinWonders, 4★, 2026-09-05)
2. *"Cần bổ sung thêm mô tả cho các trò chơi. Trò nào không dành cho trẻ em, người dưới 1m4... để chủ động sắp xếp thời gian di chuyển và chọn khu vui chơi phù hợp"* — `reviews_raw.csv` dòng `R32` (Google Play VinWonders, 3★, 2023-07-24)
3. *"thông tin hạng vé vào cửa dc tặng vouchers ăn nhưng vào app k hiển thị vouchers ăn nên bố k biết vouchers sử dụng cho ăn uống ở đâu. k có thông tin các trạm tuktuk di chuyển trg vinwonders Nha Trang, đổi lên Premium xem show Tata miễn phí mà đổi xog cũg méo hiện trg app"* — `reviews_raw.csv` dòng `R03` (Google Play VinWonders, 2★, 2026-09-04)
4. *"đơn vị tổ chức không chuyên nghiệp, hành merchandise nhập về để khách đứng đợi k có thông báo giờ cụ thể"* — `reviews_raw.csv` dòng `R18` (Google Play VinWonders, 3★, 2025-11-08)
5. *"dụ dỗ tải app tặng voucher 200k sài đi thuyền grand world ăn uống. CUỐI CÙNG KO SÀI ĐƯỢC CÁI GÌ HẾT VOUCHER ĐI ĐÂU CŨNG BỊ TỪ CHỐI"* — `reviews_raw.csv` dòng `R27` (Google Play VinWonders, 1★, 2023-12-30)
6. *"Đường đi hoàn toàn khác địa hình. Nhìn bản đồ leo rào không."* — `reviews_raw.csv` dòng `R39` (Google Play VinWonders, 1★, 2023-07-02)

## 4. Các nguồn có khớp nhau không

*(Cập nhật đầy đủ sau khi xong phỏng vấn `P1`–`P3` trước CP3).*
- **Bản đầu CP2:** Nguồn đào data cho thấy rõ nỗi đau về bản đồ/di chuyển (`23.1%`), thiếu thông tin giới hạn chiều cao trẻ em để xếp khu (`R32`), giờ show & voucher ăn uống (`R03`, `R27`), nhưng chưa có số liệu về thời gian chuẩn bị trước chuyến đi và cách xử lý khi gặp mưa (`L4 = 0/39`). Nhóm dùng 3 cuộc phỏng vấn trực tiếp để kiểm chứng lại 2 điểm còn thiếu này.

## 5. Kết luận

Giả thuyết ở `evidence/hypothesis.md`: **Bước đầu ĐÚNG ở vế Đào data (chờ kiểm chéo bằng phỏng vấn trước CP3)** — vì tỷ lệ review gặp vấn đề liên quan xếp lịch / di chuyển / giờ / tuổi / chi phí đạt **11/39 (28.2%)**, vượt ngưỡng đặt trước (`≥15–20%`).
- **Điều vẫn chưa biết (cần làm rõ ở phỏng vấn `P1`–`P3`):** (1) Phụ huynh mất chính xác bao nhiêu phút chuẩn bị lịch trình trước chuyến đi? (2) Khi gặp mưa đột xuất hoặc trẻ mệt giữa ngày, họ xoay xở thực tế ra sao? (3) Tần suất đi khu vui chơi / năm của các nhóm khách (để tinh chỉnh persona chi phí ở `cost/personas.yaml`).

## Lịch hẹn (dùng cho CP2 — chỉ ghi vai và giờ, không tên)

| Vai | Giờ hẹn | Đã xong? |
|---|---|---|
| Học viên L3A ngoài nhóm (từng đi VinWonders cùng gia đình/nhóm bạn) — `P1` | 20:00 Thứ Sáu 27/11 | Chưa |
| Học viên L3A ngoài nhóm (từng đi Sun World Bà Nà Hills / Hạ Long trong 6 tháng qua) — `P2` | 21:00 Thứ Sáu 27/11 | Chưa |
| Phụ huynh có con nhỏ 4–10 tuổi (người thân/đồng nghiệp ngoài nhóm) — `P3` | 08:30 Thứ Bảy 28/11 | Chưa |
