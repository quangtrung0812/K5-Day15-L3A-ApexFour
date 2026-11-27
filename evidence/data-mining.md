# Đào data — cách đếm và kết quả

> Điền ở guide bước 1.2. Ôn lại: ngày 2, ngày 6 · lab ngày 2, lab ngày 6.
> Không đào data thì xoá file này. Script / công thức đếm để trong repo (vd `evidence/count.py` hoặc ghi công thức Sheets ngay dưới), người khác chạy lại phải ra cùng số.
> Repo chỉ chứa số đã tổng hợp và vài dòng ví dụ — không chép lại nguyên file data.

## 1. Cách đếm — viết TRƯỚC khi chạy

- Data dùng: Review công khai tiếng Việt trên Google Maps / Tripadvisor / Google Play của khu vui chơi lớn (vd VinWonders Phú Quốc / Nha Trang, Sun World Bà Nà Hills — nhóm chốt link nguồn và khoảng ngày cụ thể khi lấy mẫu, ngày xem: 27/11/2026).
- Đếm gì: Số review phản ánh vấn đề liên quan đến lập lịch trình / giờ mở cửa & giờ show / trò chơi đóng bảo trì hoặc giới hạn chiều cao trẻ em / mưa làm hỏng kế hoạch / di chuyển xa chồng chéo · trên tập nào: `N` review mới nhất có nội dung chữ (≥10 từ) · lọc gì: mọi mức sao (1–5 sao) để tránh thiên lệch mẫu (hoặc nếu lọc riêng 1–3 sao để tìm nhóm phàn nàn thì ghi rõ mẫu nghiêng về phàn nàn).
- **Mẫu số là gì:** `N` = tổng số review trong mẫu đã đọc và gắn nhãn theo quy tắc chọn mẫu ở trên (tính cả các review khen chung hoặc không liên quan đến lịch trình).
- Nhãn dự kiến (mỗi review gắn ≥1 nhãn rõ định nghĩa):
  - `L1_TRE_SHOW_GIO_MO_CUA`: Lỡ giờ biểu diễn cố định, đến nơi trò chơi/khu vực đã đóng cửa hoặc bảo trì không biết trước.
  - `L2_DI_CHUYEN_RONG_MET`: Khu quá rộng, đi bộ vòng vèo giữa các phân khu không kịp chơi hết trong 1 ngày.
  - `L3_TRE_NHO_DO_TUOI`: Đưa trẻ nhỏ tới nhưng vướng giới hạn chiều cao/độ tuổi không chơi được.
  - `L4_THOI_TIET_MUA`: Mưa/thời tiết xấu làm dừng trò ngoài trời, huỷ show, lúng túng đổi điểm trong nhà.
  - `L5_GIA_PHAT_SINH`: Phát sinh chi phí ăn uống / vé lẻ ngoài dự tính ban đầu.
  - `L0_KHAC`: Vấn đề khác (đông đúc xếp hàng, thái độ phục vụ, khen chung…) không thuộc bài toán xếp lịch.
- Script / công thức: Lưu bảng gắn nhãn ẩn danh (bỏ tên người viết, trích tối đa 2 câu/review) vào CSV và đếm bằng script `evidence/count_reviews.py` (hoặc `COUNTIF` trên Sheets).

## 2. Đọc trước, đếm sau

Đã đọc __ dòng đầu và từ điển cột. Các *kiểu* hành vi thấy được (trước khi định nghĩa thứ cần đếm):
- __
- __

## 3. Kết quả

| Đếm gì | x / N | % | Ghi chú |
|---|---|---|---|
| | | | |
| | | | |

Ghi dạng "x/N (y%)". "Nhiều bạn…" không phải số.

## 4. ≥5 ví dụ cụ thể (mã dòng / mã đã ẩn danh, không đoán ai là ai)

1.
2.
3.
4.
5.

## 5. Giới hạn của data

Data cho biết người ta **làm gì**, không cho biết **vì sao**. Thiếu gì, lệch về phía nào: __
→ Kiểm lại bằng phỏng vấn / khảo sát nào: __
