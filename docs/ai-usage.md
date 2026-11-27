# Khai báo dùng AI

README của nhóm có mục "Dùng AI vào việc gì" (2–3 dòng, bắt buộc). Ghi chi tiết vào bảng dưới đây.

> Luật của đề: dùng AI để làm bài thoải mái, nhưng **ai không giải thích được phần có tên mình thì phần đó nhận 0 điểm**. Khai thiếu không bị trừ; giấu mới bị.

| Việc | Công cụ AI | AI làm gì | Người kiểm/sửa gì | Ai phụ trách |
|---|---|---|---|---|
| Code bản chạy thử | Codex | Viết 5 công cụ đọc dữ liệu SunWonder Mẫu và bộ kiểm thử ràng buộc | Kết quả `python -m unittest discover -s tests -v` kiểm tuổi, giờ, mưa, đi bộ, show, bảo trì và giá | Nguyễn Quốc Hưng |
| Prompt / thiết kế lời gọi mô hình | | | | |
| Đào data (viết script đếm, gợi ý nhãn) | | | Kiểm tay __ dòng, khớp __ | |
| Rà câu hỏi phỏng vấn / khảo sát | | Chỉ rà câu dẫn dắt | | |
| Viết câu thử (benchmark) | Codex | Soạn các ca tự viết H01–H08 trong `spec.md` §5 | Đối chiếu mã, giờ và giá với `data/park_data.json` khi ghép ca vào benchmark | Nguyễn Quốc Hưng |
| Sinh data `synthetic` (nếu có) | | | Seed __ · kiểm tay __ dòng | |
| Chấm cột `pass` bằng LLM (nếu có) | | | Kiểm tra thủ công __ câu thử, khớp __/__ | |
| Slide, văn bản | Codex | Soạn kịch bản demo và cấu hình mô phỏng chi phí của Hưng | Lấy kết quả trình bày từ lượt chạy có model thật và benchmark đã chấm | Nguyễn Quốc Hưng |

**Không dùng AI để:** tạo người được phỏng vấn, trích dẫn, câu trả lời khảo sát; sửa kết quả các lượt đã chạy (`eval/run-*.csv`, `cost/simulate-*.csv`, `traces/`).
