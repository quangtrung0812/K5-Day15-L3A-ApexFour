# Dàn slide → lấy số từ file nào

> Làm ở guide bước 5.1. Luật: **không có bằng chứng thì không có slide** — mỗi trang ≥1 con số / trích dẫn có nguồn / kết quả đo.
> Xuất PDF thành `demo-slides.pdf` ở thư mục gốc repo, nộp tại CP4 14:30 Thứ Bảy 28/11. Định dạng nào cũng được (PDF, PPTX, HTML…); hoặc nộp link slide (Drive, Canva, Google Slides…) ở form CP4, để ai có link cũng xem được.

| # | Trang | Có gì | Số lấy từ | Xong |
|---|---|---|---|---|
| 1 | Người dùng & pain | Ai · việc gì · chỗ đau + số và trích dẫn | `evidence/summary.md` | ☐ |
| 2 | Vì sao chọn bài này | Bảng impact rút gọn + hướng bị loại | `spec.md` §2 | ☐ |
| 3 | Giải pháp | Lát cắt một câu · sơ đồ · AI tự làm đến đâu, vì sao | `spec.md` §4 | ☐ |
| 4 | Demo live | Hưng chạy 1 lịch thường, rồi nhập báo mưa từ 14:00 để xếp lại phần buổi chiều. Chiếu bảng giờ, tổng tiền và hoạt động được đổi. | `eval/benchmark.csv`, ca H05 trong `spec.md` | ☐ |
| 5 | **Đánh giá thế nào** | Dataset · bộ câu thử · metric · lượt 1 → lượt 2 so với chuẩn "đạt" (kèm run ID) · lỗi chính | `eval/README.md`, `eval/report.md` | ☐ |
| 6 | **Chi phí khi dùng thật** | Chi phí / task thành công · 3 kịch bản · so với impact | `cost/cost-estimate.md` | ☐ |
| 7 | Kết luận | Go / iterate / stop — dẫn số ở trang 1, 5, 6 | — | ☐ |
| 8 | Nếu có thêm 1 tuần | 2–3 việc, trỏ về lỗi còn lại / phản hồi người dùng | `eval/report.md` mục 4 · `validation/log.md` | ☐ |

### Kịch bản demo của Hưng

1. Nhập ngày 28/11/2026, 2 người lớn, 1 trẻ 6 tuổi, giờ 09:00–17:00 và ngân sách 3 triệu đồng. Chỉ trên màn hình một suất show và tổng tiền do công cụ tính.
2. Báo mưa đột xuất từ 14:00 cho ngày đang xem rồi yêu cầu xếp lại buổi chiều. So sánh hoạt động ngoài trời đã đổi với hoạt động trong nhà mới, thời gian đi bộ và tổng tiền.
3. Chuyển sang slide chi phí. Lấy chi phí mỗi tác vụ thành công và ba kịch bản tháng từ kết quả mô phỏng đã đo. Ghi rõ quy mô nào là giả định.

Quay dự phòng cả hai lượt nhập sau khi model thật và dữ liệu đã ghép. Dùng cùng các đầu vào khi quay và khi demo.

**Trước khi lên:** tải repo về một máy khác (hoặc thư mục mới), chạy theo mục "Chạy trong 3 phút" của `README.md` · `.env` có trên máy demo, đã gọi thử 1 câu trong vòng 1 giờ trước giờ demo · video dự phòng mở được bằng cửa sổ ẩn danh · biết bản chạy thử sẽ làm gì với **1 câu thử lạ** của giám khảo.

Ai nói trang nào (mỗi người ≥1 phần):

| Trang | Người nói |
|---|---|
| | |
