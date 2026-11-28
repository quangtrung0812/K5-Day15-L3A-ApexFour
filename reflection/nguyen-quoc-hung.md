# Reflection — Nguyễn Quốc Hưng

> Thành viên nhóm ApexFour · Lớp L3A · Track C

1. **Vai trò và phần tôi làm**
   Ở CP2, tôi tổng hợp 10 review Sun World Hạ Long, xây dựng các công cụ tra dữ liệu và kiểm lịch, rồi soạn kịch bản demo (`f09091b`).
   Sang CP3, tôi đồng bộ cách xử lý mưa và show hủy giữa công cụ tra lịch với bộ kiểm. Tôi bổ sung bài thử để chắc rằng bản nháp dùng đúng giá vé và trạng thái bảo trì từ dữ liệu khu vui chơi.
   Tôi cũng cấu hình mô phỏng chi phí cho ba kiểu sử dụng, từ lập lịch một lần đến đổi lịch trong ngày mưa (`333d4d3`).
   [Review Hạ Long](../evidence/hung-ha-long.md) · [Công cụ kiểm lịch](../codebase/tools.py) · [Bàn giao CP3](../docs/cp3-note-hung.md)

2. **Cách tôi dùng AI và kiểm lại kết quả**
   Tôi dùng Codex để hỗ trợ viết code Python, soạn ca kiểm thử và chuẩn bị đầu vào cho mô phỏng chi phí.
   Chỗ cần sửa là công cụ tra lịch đã đánh dấu show bị hủy do mưa, còn bộ kiểm chỉ báo lỗi hoạt động ngoài trời. Tôi dùng chung quy tắc hủy show và thêm bài thử đưa lịch về cho agent sửa, rồi kiểm lịch thay thế trong nhà.
   Trước khi bàn giao, bộ kiểm thử qua 14/14 bài. Với seed 42, lượt chạy thử 10 phiên chỉ chọn hai kiểu sử dụng, nên tôi chạy riêng cả bốn đầu vào của kiểu ngày mưa.
   [Bài kiểm thử công cụ](../tests/test_park_tools.py) · [Bài kiểm thử agent](../tests/test_agent_tools.py) · [Cấu hình mô phỏng](../cost/personas.yaml)

3. **Ca B17 và bài học tôi rút ra**
   B17 lấy tình huống từ review Hạ Long tôi tổng hợp. Gia đình báo hồ bơi A13 vừa đóng và cần xếp lại lịch từ 13:00 đến 17:00 với ngân sách 3 triệu đồng.
   Lượt 1 báo bất khả thi và chỉ liệt kê vài điểm gợi ý. Đến lượt 3, nhóm có lịch thay thế bỏ A13, kết thúc lúc 16:30 và vừa đúng ngân sách.
   Tôi rút ra rằng bài thử đổi lịch phải kiểm cả việc loại điểm đã đóng lẫn việc đưa ra phương án thay thế có giờ cụ thể. Phương án đó vẫn cần qua bộ kiểm thời gian đi bộ và tổng chi phí.
   [Kết quả lượt 1](../eval/run-1.csv) · [Kết quả lượt 3](../eval/run-3.csv)
