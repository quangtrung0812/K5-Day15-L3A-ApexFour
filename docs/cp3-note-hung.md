# Bàn giao CP3 — Nguyễn Quốc Hưng

Nhánh `feat/cp3-hung-tools-cost` tạo từ `origin/main` tại `f90948a`.

## Công cụ và kiểm thử

- `tra_lich_show` và `kiem_lich_trinh` dùng chung quy tắc hủy show theo dự báo, giờ người dùng báo mưa hoặc mã suất báo hủy. Một hoạt động ngoài trời kết thúc đúng lúc bắt đầu mưa vẫn hợp lệ về thời tiết. Lịch tra ở lần sau tiếp tục đọc dữ liệu gốc.
- Bộ kiểm lấy giá vé, phụ thu và trạng thái bảo trì từ `data/park_data.json`. Bài thử B15 kiểm việc từ chối trước khi gọi model. Bài thử ở lớp công cụ kiểm cả trường hợp bản nháp tự gửi giá và trạng thái khác dữ liệu.
- `python -m unittest discover -s tests -v` qua 14/14 bài, gồm ca nhận bản nháp có show ngoài trời bị hủy do mưa rồi chuyển sang show trong nhà.
- Agent hiện đã truyền giờ mưa qua `thoi_tiet["mua_tu"]`. Khi ghép xử lý tin nhắn báo hủy show vào agent, dùng mã show trong danh mục và truyền cùng `show_da_huy` vào `tra_lich_show` và `kiem_lich_trinh`. `tra_lich_show` cũng nhận `mua_tu` để model thấy ngay cờ `huy` khi nhận danh mục.

## Chi phí

- `cost/personas.yaml` có ba kiểu dùng (65% / 25% / 10%), với 1 / 3 / 4 lượt hỏi mỗi phiên và 1 phiên mỗi tháng (tự ước tính). Bảng giá Standard của Gemini 3.1 Flash-Lite và Gemini 4 Hydrogen được đối chiếu ngày 27/11/2026.
- `python run.py simulate --try` ở chế độ giả chạy đủ 10 phiên, 16 lượt hỏi, 0 lỗi thực thi. Khung ghi `cost/simulate-mock.csv` và trả mã 1 do token bằng 0. Với seed 42, lượt này chọn 7 phiên lập lịch và 3 phiên sửa lịch trước khi đi. Đã chạy riêng cả 4 đầu vào của kiểu ngày mưa và nhận lịch qua bộ kiểm cho cả 4.
- Sau khi ghép model thật, chạy lại `python run.py simulate --try` để đo token trên 10 phiên. Lượt eval của cùng model cần được chấm trước khi tính chi phí mỗi tác vụ thành công.

Kiểm tra với benchmark 25 câu trên nhánh của Bình cho kết quả 0 cảnh báo và 10/25 câu từ dữ liệu thật.
