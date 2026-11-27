# Dàn slide → lấy số từ file nào

> Làm ở guide bước 5.1. Luật: **không có bằng chứng thì không có slide** — mỗi trang ≥1 con số / trích dẫn có nguồn / kết quả đo.
> Xuất PDF thành `demo-slides.pdf` ở thư mục gốc repo, nộp tại CP4 14:30 Thứ Bảy 28/11. Định dạng nào cũng được (PDF, PPTX, HTML…); hoặc nộp link slide (Drive, Canva, Google Slides…) ở form CP4, để ai có link cũng xem được.

| # | Trang | Có gì | Số lấy từ | Xong |
|---|---|---|---|---|
| 1 | Người dùng & pain | Ai · việc gì · chỗ đau + số và trích dẫn | `evidence/summary.md` | ✓ |
| 2 | Vì sao chọn bài này | Bảng impact rút gọn + hướng bị loại | `spec.md` §2 | ✓ |
| 3 | Giải pháp | Lát cắt một câu · sơ đồ · AI tự làm đến đâu, vì sao | `spec.md` §4 | ✓ |
| 4 | Demo live | Hưng chạy 1 lịch thường, rồi nhập báo mưa từ 14:00 để xếp lại phần buổi chiều. Chiếu bảng giờ, tổng tiền và hoạt động được đổi. | `eval/benchmark.csv`, ca H05 trong `spec.md` | ✓ |
| 5 | **Đánh giá thế nào** | Dataset · bộ câu thử · metric · lượt 1 → lượt 2 so với chuẩn "đạt" (kèm run ID) · lỗi chính | `eval/README.md`, `eval/report.md` | ✓ |
| 6 | **Chi phí khi dùng thật** | Chi phí / task thành công · 3 kịch bản · so với impact | `cost/cost-estimate.md` | ✓ |
| 7 | Kết luận | Go / iterate / stop — dẫn số ở trang 1, 5, 6 | — | ✓ |
| 8 | Nếu có thêm 1 tuần | 2–3 việc, trỏ về lỗi còn lại / phản hồi người dùng | `eval/report.md` mục 4 · `validation/log.md` | ✓ |

### Kịch bản demo của Hưng

1. Nhập ngày 28/11/2026, 2 người lớn, 1 bé 6 tuổi, 09:00–17:00, ngân sách 3 triệu, muốn đi thủy cung và xem show. Trong bản ghi, A05 bắt đầu lúc 09:00, S02 lúc 11:00. Tổng 3.000.000đ.
2. Nhập lại thông tin gia đình và ngân sách cùng khung 14:00–17:00, báo mưa từ 14:00. Bản chạy nhận mỗi yêu cầu độc lập. Trong video, model báo không xếp được lịch. Khi demo, đọc kết quả hiện tại và chỉ ra nếu lịch còn thiếu.
3. Mở trang 6 để đối chiếu chi phí với kết quả eval. Nếu mất mạng, phát [video dự phòng](../demo-backup.mp4). Video có phần phát lại hai yêu cầu và một lượt chạy qua giao diện dòng lệnh.

**Trước khi lên:** tải repo về một máy khác (hoặc thư mục mới), chạy theo mục "Chạy trong 3 phút" của `README.md` · `.env` có trên máy demo, đã gọi thử 1 câu trong vòng 1 giờ trước giờ demo · video dự phòng mở được bằng cửa sổ ẩn danh · biết bản chạy thử sẽ làm gì với **1 câu thử lạ** của giám khảo.

Phân công thuyết trình đề xuất

| Trang | Người nói |
|---|---|
| 1–2 | Lê Văn Hoàng |
| 3, 7–8 | Nguyễn Quang Trung |
| 4, 6 | Nguyễn Quốc Hưng |
| 5 | Dương Thanh Bình |
