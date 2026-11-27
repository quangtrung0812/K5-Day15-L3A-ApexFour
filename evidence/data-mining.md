# Đào data — cách đếm và kết quả

> Điền ở guide bước 1.2. Ôn lại: ngày 2, ngày 6 · lab ngày 2, lab ngày 6.
> Script đếm tái lập 100% đặt tại `evidence/count_reviews.py` (đọc bảng ẩn danh `evidence/reviews_raw.csv`, chạy `python evidence/count_reviews.py` ra đúng bảng số bên dưới).
> Repo chỉ chứa bản ẩn danh (bỏ tên người viết, trích tối đa 2 câu/review) và số đã tổng hợp.

## 1. Cách đếm — viết TRƯỚC khi chạy

- **Data dùng:** Review công khai tiếng Việt trên **Google Play — Ứng dụng VinWonders** (`https://play.google.com/store/apps/details?id=com.vinwonders.app&hl=vi&gl=VN`), khoảng ngày đăng review: `2023-07-02` → `2026-11-20`, ngày xem & thu thập: `2026-11-27`. *(Bản CP2 dùng lô mẫu thật đầu tiên từ Google Play do Bình & Hoàng gộp vào `evidence/reviews_raw.csv`; nhóm có thể mở rộng thêm review Google Maps của Sun World Bà Nà Hills / VinWonders trước CP3 nếu cần).*
- **Đếm gì:** Số review phản ánh vấn đề liên quan đến lập lịch trình / bản đồ di chuyển / giờ mở cửa & giờ show / giới hạn độ tuổi & chiều cao trẻ em / thời tiết mưa / chi phí & voucher ăn uống phát sinh.
- **Tập lấy mẫu & lọc:** Lấy **100 review mới nhất mọi mức sao (1–5 sao)** trên Google Play (không lọc riêng 1–3 sao để tránh thiên lệch chủ quan) → lọc giữ các review tiếng Việt có tổng độ dài bài gốc (tiêu đề + nội dung) **≥10 từ** để đảm bảo có nội dung phân tích → thu được **`N = 39` review** hợp lệ *(khi cắt trích dẫn tối đa 2 câu vào cột `quote_max_2_sentences`, một số câu ngắn còn 6–9 từ nhưng bài gốc đủ ≥10 từ)*.
- **Mẫu số là gì:** **`N = 39`** = tổng số review tiếng Việt ≥10 từ đã đọc và gắn nhãn theo quy tắc chọn mẫu trên (tính cả review khen chung và lỗi kỹ thuật không liên quan đến lịch trình `L0_KHAC`).
- **6 nhãn đã định nghĩa trước khi đếm** (một review có thể gắn ≥1 nhãn `L1`–`L5`; khi tính tổng số review gặp pain chỉ đếm **số review duy nhất**, không cộng trùng):
  - `L1_TRE_SHOW_GIO_MO_CUA`: Lỡ giờ biểu diễn cố định, thiếu thông báo giờ cụ thể, không hiển thị thông tin show / giờ mở cửa / bảo trì.
  - `L2_DI_CHUYEN_RONG_MET`: Khu rộng, bản đồ khó hiểu/định vị sai/tải chậm, thiếu chỉ đường trạm di chuyển, hoặc người dùng mong muốn tối ưu danh sách trò chơi – thời gian chơi – đường đi.
  - `L3_TRE_NHO_DO_TUOI`: Thiếu thông tin giới hạn độ tuổi / chiều cao trẻ em (vd dưới 1m4) để chủ động sắp xếp thời gian di chuyển và chọn khu chơi phù hợp.
  - `L4_THOI_TIET_MUA`: Mưa / thời tiết xấu làm dừng trò ngoài trời, huỷ show, lúng túng đổi điểm trong nhà.
  - `L5_GIA_PHAT_SINH`: Phát sinh chi phí ăn uống / voucher / vé lẻ không rõ ràng so với dự tính ban đầu.
  - `L0_KHAC`: Vấn đề khác (lỗi đăng nhập/OTP, app lag, xếp hàng nắng nóng, khen chung…) không thuộc bài toán xếp lịch.
- **Script đếm:** `evidence/count_reviews.py` đọc `evidence/reviews_raw.csv` (chạy: `python evidence/count_reviews.py`).

## 2. Đọc trước, đếm sau

Đã đọc toàn bộ **39 dòng đầu (`R01`–`R39`)** và kiểm tra các cột (`id, source_name, source_url, viewed_date, review_date, stars, quote_max_2_sentences, labels`). Phân bố sao trong mẫu: `1*: 26 · 2*: 3 · 3*: 6 · 4*: 1 · 5*: 3`.

Các *kiểu* hành vi / phàn nàn nổi bật thấy được trước khi đếm:
- **Bản đồ, định vị và nhu cầu tối ưu lộ trình chơi:** Nhiều khách phàn nàn bản đồ trong app tải chậm, định vị sai, tên địa điểm khó hiểu hoặc khác địa hình thực tế; có khách đề xuất thẳng tính năng chọn trò chơi rồi tự tối ưu thời gian chơi và đường đi (`R02`, `R07`, `R09`, `R24`, `R33`, `R36`, `R39`).
- **Thiếu thông tin ràng buộc cho trẻ nhỏ để tự xếp lịch:** Khách yêu cầu bổ sung mô tả trò nào không dành cho trẻ em / người dưới 1m4 để chủ động sắp xếp thời gian di chuyển và chọn khu phù hợp (`R32`).
- **Thiếu thông tin giờ show, trạm di chuyển và voucher ăn uống:** Khách nâng hạng vé xem Tata Show nhưng không hiển thị thông tin, không rõ trạm tuk-tuk, hoặc không rõ voucher ăn uống dùng ở đâu / bị từ chối gây phát sinh chi phí (`R03`, `R18`, `R27`).
- **Nhóm lỗi kỹ thuật app & đông đúc xếp hàng (`L0_KHAC`):** Phần lớn review 1 sao trên Google Play phản ánh lỗi đăng nhập/OTP/sập app khi săn sale hoặc sảnh chờ nắng nóng (`R01`, `R05`, `R06`, `R13`, `R19`…).

## 3. Kết quả

Chạy `python evidence/count_reviews.py` trên `evidence/reviews_raw.csv` (`N = 39`):

| Đếm gì | x / N | % | Ghi chú |
|---|---:|---:|---|
| **Tổng review gặp ≥1 vấn đề xếp lịch (`L1`–`L5`, không đếm trùng)** | **11 / 39** | **28.2%** | Mã: `R02, R03, R07, R09, R18, R24, R27, R32, R33, R36, R39` |
| `L2_DI_CHUYEN_RONG_MET` (Bản đồ / đường đi / tối ưu lịch) | 9 / 39 | 23.1% | Nhóm pain lớn nhất trong mẫu |
| `L1_TRE_SHOW_GIO_MO_CUA` (Giờ show / thông báo giờ cụ thể) | 2 / 39 | 5.1% | `R03, R18` |
| `L5_GIA_PHAT_SINH` (Chi phí ăn uống / voucher không rõ) | 2 / 39 | 5.1% | `R03, R27` |
| `L3_TRE_NHO_DO_TUOI` (Giới hạn độ tuổi / chiều cao <1m4) | 1 / 39 | 2.6% | `R32` (gắn cùng `L2`) |
| `L4_THOI_TIET_MUA` (Mưa / thời tiết làm hỏng kế hoạch) | 0 / 39 | 0.0% | Chưa xuất hiện trên nguồn review app; cần kiểm ở phỏng vấn & Google Maps |
| `L0_KHAC` (Lỗi đăng nhập, xếp hàng, khen chung) | 28 / 39 | 71.8% | Không thuộc bài toán xếp lịch |

*(Lưu ý: `R03` gắn đồng thời 3 nhãn `L1;L2;L5` và `R32` gắn 2 nhãn `L3;L2`, nên tổng lượt nhãn là 14 nhưng số review duy nhất thuộc `L1`–`L5` là **11/39 = 28.2%**).*

## 4. ≥5 ví dụ cụ thể (mã dòng đã ẩn danh, trích ≤2 câu nguyên văn)

1. **`R02`** *(4★ · 2026-09-05 · `L2`)*: *"liệt kê tối ưu trò chơi, thời gian chơi, đường đi và thêm stick để người chơi lựa chọn trò xong app tối ưu (nếu được nên khuyến nghị nếu khách quá đông) là rất hay"*
2. **`R03`** *(2★ · 2026-09-04 · `L1;L2;L5`)*: *"thông tin hạng vé vào cửa dc tặng vouchers ăn nhưng vào app k hiển thị vouchers ăn nên bố k biết vouchers sử dụng cho ăn uống ở đâu. k có thông tin các trạm tuktuk di chuyển trg vinwonders Nha Trang, đổi lên Premium xem show Tata miễn phí mà đổi xog cũg méo hiện trg app"*
3. **`R18`** *(3★ · 2025-11-08 · `L1`)*: *"đơn vị tổ chức không chuyên nghiệp, hành merchandise nhập về để khách đứng đợi k có thông báo giờ cụ thể"*
4. **`R27`** *(1★ · 2023-12-30 · `L5`)*: *"dụ dỗ tải app tặng voucher 200k sài đi thuyền grand world ăn uống. CUỐI CÙNG KO SÀI ĐƯỢC CÁI GÌ HẾT VOUCHER ĐI ĐÂU CŨNG BỊ TỪ CHỐI"*
5. **`R32`** *(3★ · 2023-07-24 · `L3;L2`)*: *"Cần bổ sung thêm mô tả cho các trò chơi. Trò nào không dành cho trẻ em, người dưới 1m4... để chủ động sắp xếp thời gian di chuyển và chọn khu vui chơi phù hợp"*
6. **`R33`** *(2★ · 2023-07-13 · `L2`)*: *"xem map kh ổn chút nao, định vị chậm, dùng 4g cũng kh load được, nchung quá nhìu lỗi, rất tệ nka"*
7. **`R39`** *(1★ · 2023-07-02 · `L2`)*: *"Đường đi hoàn toàn khác địa hình. Nhìn bản đồ leo rào không."*

## 5. Giới hạn của data

- **Thiên lệch nguồn review app:** Mẫu đầu tiên lấy từ Google Play của ứng dụng VinWonders nên 71.8% review (`L0_KHAC`) phản ánh lỗi kỹ thuật app (đăng nhập, OTP, quảng cáo) và nghiêng về người dùng đang bực (26/39 là 1 sao). Tỷ lệ `28.2%` không đồng nghĩa đúng 28.2% toàn bộ khách đi khu vui chơi gặp lỗi này.
- **Thiếu dữ liệu về thời tiết (`L4 = 0/39`) và thiếu ngữ cảnh "vì sao / mất bao nhiêu phút":** Review ngắn trên app cho biết khách gặp khó về bản đồ, độ tuổi trẻ em, giờ show và chi phí, nhưng chưa cho biết phụ huynh mất bao nhiêu phút tự chuẩn bị trước chuyến đi và xử lý ra sao khi gặp mưa đột xuất.
- **→ Kiểm lại bằng:** Phỏng vấn trực tiếp **≥3 người dùng ngoài nhóm (`P1`–`P3`)** từng lập lịch đi khu vui chơi cùng gia đình/nhóm bạn (đã lên lịch hẹn ở cuối `evidence/summary.md`, hoàn thành trước CP3 10:00 Thứ Bảy 28/11).
