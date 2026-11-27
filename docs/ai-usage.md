# Khai báo dùng AI

README của nhóm có mục "Dùng AI vào việc gì" (2–3 dòng, bắt buộc). Ghi chi tiết vào bảng dưới đây.

> Luật của đề: dùng AI để làm bài thoải mái, nhưng **ai không giải thích được phần có tên mình thì phần đó nhận 0 điểm**. Khai thiếu không bị trừ; giấu mới bị.

| Việc | Công cụ AI | AI làm gì | Người kiểm/sửa gì | Ai phụ trách |
|---|---|---|---|---|
| Code bản chạy thử | Coding agent (Antigravity / Gemini) | Dựng khung workflow `codebase/agent.py`, mẫu hợp đồng 5 hàm công cụ trong `docs/interface-contract.md` | Rà từng nhánh guardrail, vòng lặp `MAX_STEPS=3`, chạy thử `python run.py` và ghép với `tools.py` | Nguyễn Quang Trung, Nguyễn Quốc Hưng |
| Prompt / thiết kế lời gọi mô hình | Coding agent (Antigravity / Gemini) | Gợi ý `SYSTEM` prompt định dạng JSON và quy tắc không bịa nguồn | Đối chiếu với 4 lớp chỗ khó trong `spec.md` §5, chỉnh điều kiện từ chối | Nguyễn Quang Trung |
| Đào data (viết script đếm, gợi ý nhãn) | Coding agent / ChatGPT | Hỗ trợ viết khung quy tắc chọn mẫu, bộ nhãn `L1`–`L5` và script đếm review | Tự thu review thật trên Google Maps/Tripadvisor, kiểm tay gắn nhãn (cập nhật số dòng sau khi chạy) | Lê Văn Hoàng |
| Rà câu hỏi phỏng vấn / khảo sát | Chỉ rà câu dẫn dắt | Gợi ý sửa các câu hỏi dễ dẫn dắt theo Mom Test | Tự phỏng vấn người dùng thật ngoài nhóm, ghi chép nguyên văn | Cả nhóm (Hoàng tổng hợp) |
| Viết câu thử (benchmark) | Coding agent | Gợi ý biến thể câu chữ theo lưới input do nhóm thiết kế | Mỗi câu thử gắn `source` thật (`data_that`/`nguoi_dung`/`tu_viet`), tự kiểm `pass_criterion` | Dương Thanh Bình, Nguyễn Quốc Hưng |
| Sinh data `synthetic` (nếu có) | Coding agent / Script Python | Hỗ trợ sinh `data/park_data.json` có seed cố định (`seed=42`) | Kiểm tay toàn bộ điểm chơi, giờ mở cửa, lịch show, giá vé và bẫy bảo trì/mưa/tuổi | Dương Thanh Bình |
| Chấm cột `pass` bằng LLM (nếu có) | *(Cập nhật ở CP3/CP4 nếu dùng)* | — | Ưu tiên chấm bằng code (`kiem_lich_trinh`) + người chấm kiểm chéo ≥4/5 | Dương Thanh Bình, Lê Văn Hoàng |
| Slide, văn bản | Coding agent | Hỗ trợ cấu trúc `spec.md`, `canvas.md`, `README.md`, `docs/cp2-plan.md` | Toàn bộ thành viên đọc duyệt từng mục, khớp với số liệu thật | Nguyễn Quang Trung và cả nhóm |
| Code bản chạy thử | Codex | Viết 5 công cụ đọc dữ liệu SunWonder Mẫu và bộ kiểm thử ràng buộc | Kết quả `python -m unittest discover -s tests -v` kiểm tuổi, giờ, mưa, đi bộ, show, bảo trì và giá | Nguyễn Quốc Hưng |
| Viết câu thử (benchmark) | Codex | Soạn các ca tự viết H01–H08 trong `spec.md` §5 | Đối chiếu mã, giờ và giá với `data/park_data.json` khi ghép ca vào benchmark | Nguyễn Quốc Hưng |
| Slide, văn bản | Codex | Soạn kịch bản demo và cấu hình mô phỏng chi phí của Hưng | Lấy kết quả trình bày từ lượt chạy có model thật và benchmark đã chấm | Nguyễn Quốc Hưng |

**Không dùng AI để:** tạo người được phỏng vấn, trích dẫn, câu trả lời khảo sát; sửa kết quả các lượt đã chạy (`eval/run-*.csv`, `cost/simulate-*.csv`, `traces/`).
