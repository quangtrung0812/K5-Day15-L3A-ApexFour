# Tổng hợp bằng chứng pain

> Điền ở guide bước 1.2, xong trước **CP3 10:00 Thứ Bảy 28/11**. Phụ trách: Lê Văn Hoàng. Chấm ở rubric R1.
> Ba nguồn ngang nhau — tối thiểu **≥1 nguồn đạt ngưỡng**. Nhóm dùng **Đào data (review công khai)** làm nguồn chính và **Phỏng vấn ≥3 người ngoài nhóm** để kiểm lại.

## 1. Nguồn đã dùng

| Nguồn | Đạt ngưỡng? | File |
|---|---|---|
| Đào data (x/N, %, cách đếm chạy lại được, ≥5 ví dụ) | ☑ **Đạt ngưỡng** (`11/39 = 28.2%` ở VinWonders + tham chiếu `3/10 = 30.0%` ở Sun World Hạ Long; ≥7 ví dụ nguyên văn) | `evidence/data-mining.md` · `evidence/reviews_raw.csv` · `evidence/count_reviews.py` · `evidence/hung-ha-long.md` |
| Phỏng vấn (≥3 người ngoài nhóm, đúng người dùng) | ☐ *(đã dựng khung `P1.md`–`P3.md`, đang hoàn tất ghi chép phỏng vấn trước 08:15 Thứ Bảy 28/11)* | `evidence/interviews/P1.md`, `P2.md`, `P3.md` |
| Khảo sát (≥20 người ngoài nhóm, đúng người dùng) | — *(không chọn ở `hypothesis.md`)* | — |

## 2. Số chính

- **Đào data — Nguồn chính (`evidence/data-mining.md`, Google Play — VinWonders, `N = 39` review tiếng Việt ≥10 từ ở bài gốc, mọi mức sao):**
  - **11/39 (28.2%)** review nêu ít nhất 1 vấn đề thuộc nhóm bài toán xếp lịch trình (`L1`–`L5`):
    - Bản đồ / chỉ đường / tối ưu thứ tự chơi (`L2`): **9/39 (23.1%)**
    - Giờ show / thông báo giờ cụ thể (`L1`): **2/39 (5.1%)**
    - Chi phí ăn uống / voucher phát sinh (`L5`): **2/39 (5.1%)**
    - Giới hạn độ tuổi / chiều cao trẻ em <1m4 (`L3`): **1/39 (2.6%)**
    - Thời tiết mưa (`L4`): **0/39 (0.0%)**
- **Đào data — Mẫu đối chiếu bổ sung (`evidence/hung-ha-long.md`, Tripadvisor — Sun World Hạ Long, `N = 10` review tiếng Việt ≥10 từ):**
  - **3/10 (30.0%)** review mô tả khu vực / trò chơi đóng cửa hoặc đang bảo trì bất ngờ khi khách đi 2 công viên trong ngày (`L1_TRE_SHOW_GIO_MO_CUA`: `HL01, HL02, HL04`). *(Nếu tính gộp cả hai nguồn công khai: **14/49 = 28.6%** review gặp pain `L1`–`L5`).*
- **Phỏng vấn *(n nhỏ không ghi %)*:** `__/3` người gặp *(cập nhật ngay khi điền xong `P1.md`–`P3.md` trước 08:15 28/11)* · số lần đi / năm: P1 `___`, P2 `___`, P3 `___` · mỗi lần chuẩn bị + xoay xở mất `___–___` phút.

| | Vai | Gặp pain? | Số lần đi / 1 năm qua | Lần gần nhất mất | Đang xoay xở bằng |
|---|---|---|---|---|---|
| P1 | *(điền từ `P1.md`)* | *(chờ điền)* | *(chờ điền)* | *(chờ điền)* | *(chờ điền)* |
| P2 | *(điền từ `P2.md`)* | *(chờ điền)* | *(chờ điền)* | *(chờ điền)* | *(chờ điền)* |
| P3 | *(điền từ `P3.md`)* | *(chờ điền)* | *(chờ điền)* | *(chờ điền)* | *(chờ điền)* |

## 3. ≥5 trích dẫn hoặc ví dụ nguyên văn (có nguồn, bỏ tên)

1. *"liệt kê tối ưu trò chơi, thời gian chơi, đường đi và thêm stick để người chơi lựa chọn trò xong app tối ưu (nếu được nên khuyến nghị nếu khách quá đông) là rất hay"* — `reviews_raw.csv` dòng `R02` (Google Play VinWonders, 4★, 2026-09-05)
2. *"Cần bổ sung thêm mô tả cho các trò chơi. Trò nào không dành cho trẻ em, người dưới 1m4... để chủ động sắp xếp thời gian di chuyển và chọn khu vui chơi phù hợp"* — `reviews_raw.csv` dòng `R32` (Google Play VinWonders, 3★, 2023-07-24)
3. *"thông tin hạng vé vào cửa dc tặng vouchers ăn nhưng vào app k hiển thị vouchers ăn nên bố k biết vouchers sử dụng cho ăn uống ở đâu. k có thông tin các trạm tuktuk di chuyển trg vinwonders Nha Trang, đổi lên Premium xem show Tata miễn phí mà đổi xog cũg méo hiện trg app"* — `reviews_raw.csv` dòng `R03` (Google Play VinWonders, 2★, 2026-09-04)
4. *"đơn vị tổ chức không chuyên nghiệp, hành merchandise nhập về để khách đứng đợi k có thông báo giờ cụ thể"* — `reviews_raw.csv` dòng `R18` (Google Play VinWonders, 3★, 2025-11-08)
5. *"dụ dỗ tải app tặng voucher 200k sài đi thuyền grand world ăn uống. CUỐI CÙNG KO SÀI ĐƯỢC CÁI GÌ HẾT VOUCHER ĐI ĐÂU CŨNG BỊ TỪ CHỐI"* — `reviews_raw.csv` dòng `R27` (Google Play VinWonders, 1★, 2023-12-30)
6. *"Đường đi hoàn toàn khác địa hình. Nhìn bản đồ leo rào không."* — `reviews_raw.csv` dòng `R39` (Google Play VinWonders, 1★, 2023-07-02)
7. Trích từ `HL01` & `HL04` (`evidence/hung-ha-long.md`, Tripadvisor Sun World Hạ Long): *"Công viên nước đang đóng"* (khách chuyển sang công viên Rồng nhưng nhiều trò mạo hiểm bảo trì) và *"cái khu ống trượt hình phễu màu đỏ k mở"*.
8. *(Bổ sung thêm 2–3 trích dẫn nguyên văn từ `P1`–`P3` sau khi hoàn tất phỏng vấn).*

## 4. Các nguồn có khớp nhau không

- **Giữa 2 nguồn review công khai (Google Play VinWonders vs Tripadvisor Sun World Hạ Long):** Tỷ lệ gặp vấn đề liên quan bài toán xếp lịch rất nhất quán (**28.2%** so với **30.0%**), đồng thời bổ khuyết cho nhau: Google Play làm nổi bật nỗi đau bản đồ/di chuyển (`23.1%`), thiếu thông tin chiều cao trẻ em <1m4 (`R32`) và chi phí/voucher (`5.1%`), còn Tripadvisor làm nổi bật tình huống khu/trò chơi đóng bảo trì bất ngờ khi di chuyển giữa các phân khu (`30.0%`).
- **Đối chiếu Đào data với Phỏng vấn `P1`–`P3`:** *(Cập nhật ngay sau khi điền xong `P1.md`–`P3.md` trước 08:15 28/11 — trọng tâm đối chiếu: (1) số phút chuẩn bị thực tế so với ước tính 60 phút, (2) tình huống mưa đột xuất `L4` vốn bằng `0/39` trên kho ứng dụng, và (3) liệu người dùng bực vì xếp hàng đông hơn hay vì vỡ lịch trình).*

## 5. Kết luận

Giả thuyết ở `evidence/hypothesis.md`: **ĐÚNG ở vế Đào data (`28.2% > ngưỡng 15–20%`), đang chốt vế kiểm chéo từ Phỏng vấn `P1`–`P3` trước CP3.**
- **Điều đã chứng minh rõ bằng dữ liệu thật:** Nhu cầu tối ưu thứ tự trò chơi – thời gian – đường đi (`R02`), lọc giới hạn độ tuổi/chiều cao trẻ em (`R32`), cảnh báo điểm đóng bảo trì (`HL01`, `HL04`) và minh bạch chi phí ăn uống/phụ thu (`R03`, `R27`) đều là nỗi đau có thật của khách đi khu vui chơi.
- **Điều đang chốt nốt qua `P1`–`P3`:** Thời gian chuẩn bị trung bình (phút/chuyến) để cập nhật vào bảng Impact `spec.md` §2.

## Lịch hẹn phỏng vấn (ẩn danh — chỉ ghi vai và giờ, không tên)

| Vai | Giờ hẹn | Đã xong? |
|---|---|---|
| Học viên L3A ngoài nhóm (từng đi VinWonders cùng gia đình/nhóm bạn) — `P1` | Tối 27/11 – Sáng 28/11 | Đang hoàn tất ghi chép (`P1.md`) |
| Học viên L3A ngoài nhóm (từng đi Sun World Bà Nà Hills / Hạ Long) — `P2` | Tối 27/11 – Sáng 28/11 | Đang hoàn tất ghi chép (`P2.md`) |
| Phụ huynh có con nhỏ 4–10 tuổi (ngoài nhóm) — `P3` | Trước 08:15 sáng 28/11 | Đang hoàn tất ghi chép (`P3.md`) |
