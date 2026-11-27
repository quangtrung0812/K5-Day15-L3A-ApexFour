# Chi phí khi dùng thật

> Điền ở guide bước 4.2, nộp ở CP4 14:30 Thứ Bảy 28/11. Ôn lại: ngày 13, ngày 1, ngày 14 · lab ngày 13, lab ngày 14. Chấm ở rubric R6.
> Số **không điền tay**: điền `cost/personas.yaml` → `python run.py simulate` → chép bảng trong `cost/simulate-N-summary.md` vào đây.
> Lúc build dùng gói miễn phí vẫn tính theo **giá gói trả phí** — đây là chi phí cho lúc đưa vào dùng thật.

## 1. Đầu vào

- **Ba kiểu sử dụng** (tự ước tính) gồm lập lịch một lần (65%, 1 lượt hỏi/phiên), sửa lịch nhiều lần trước chuyến đi (25%, 3 lượt/phiên) và xếp lại trong ngày mưa (10%, 4 lượt/phiên). Mỗi kiểu dùng 1 phiên/tháng. Khung lấy ngẫu nhiên các câu có đủ thông tin chuyến đi và gọi agent riêng cho từng lượt.
- **Quy mô thử nghiệm tại một khu vui chơi** là 50, 200 hoặc 500 gia đình hoạt động mỗi tháng (tự ước tính).
- **Giá Standard trả phí** đối chiếu Google AI Studio ngày 27/11/2026 và bảng BTC ngày 25/11/2026, tính bằng USD/1 triệu token văn bản. Gemini 3.1 Flash-Lite có giá vào 0,25 và ra 1,50. Gemini 4 Hydrogen có giá vào 1,50 và ra 7,50. [Giá Flash-Lite](https://aistudio.google.com/docs/pricing#gemini-3.1-flash-lite) · [Giá Hydrogen](https://aistudio.google.com/docs/pricing#gemini-4-hydrogen)
- **Đo chi phí** theo số token của lượt mô phỏng bằng model thật. Khi tính chi phí mỗi tác vụ thành công, dùng tỉ lệ đạt từ lượt eval đã chấm của cùng model.

## 2. Kết quả mô phỏng

CP3 đã kiểm cấu hình với 10 phiên ở chế độ giả, seed 42, cả 10 phiên chạy hết và 0 lỗi thực thi. Khung lưu lượt này vào `cost/simulate-mock.csv`, số token bằng 0. Bảng chi phí lấy từ lượt chạy model thật.

Lượt mô phỏng: `cost/simulate-__.csv` · run ID __ · __ phiên · seed __

*(dán bảng từ `cost/simulate-N-summary.md`)*

| Model | Chi phí / phiên | Chi phí / task thành công | / tháng — thấp | / tháng — cơ sở | / tháng — cao | / người / tháng (cơ sở) |
|---|---|---|---|---|---|---|
| | | | | | | |
| | | | | | | |

Chi phí / task thành công = chi phí trung bình mỗi phiên ÷ tỉ lệ đạt — **không coi như đạt 100%**.

## 3. So với impact

- Impact / người / tháng (`spec.md` §2): __
- Chi phí / người / tháng (cơ sở, model __): __
- **Kết luận một dòng — đáng làm không:** __

## 4. *(Muốn sâu hơn, không bắt buộc)*

- Bảng độ nhạy: model rẻ hơn · cache · cắt ngữ cảnh · giới hạn bước — mỗi cần gạt đổi chi phí bao nhiêu
- Chi phí ngoài model: hosting, lưu trữ, giờ công người duyệt
- Quy mô nào thì bài toán còn đáng làm
