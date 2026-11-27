# Chi phí khi dùng thật

> Điền ở guide bước 4.2, nộp ở CP4 14:30 Thứ Bảy 28/11. Ôn lại: ngày 13, ngày 1, ngày 14 · lab ngày 13, lab ngày 14. Chấm ở rubric R6.
> Số **không điền tay**: điền `cost/personas.yaml` → `python run.py simulate` → chép bảng trong `cost/simulate-N-summary.md` vào đây.
> Lúc build dùng gói miễn phí vẫn tính theo **giá gói trả phí** — đây là chi phí cho lúc đưa vào dùng thật.

## 1. Đầu vào

- **Persona** trong `cost/personas.yaml` là gia đình lập lịch trước chuyến đi, gia đình đổi lịch trong ngày và gia đình đi thường xuyên. Tỉ lệ và tần suất dùng là giả định cần đối chiếu với khảo sát của nhóm.
- **Quy mô thử nghiệm tại một khu vui chơi** là 50, 200 hoặc 500 gia đình hoạt động mỗi tháng (tự ước tính).
- **Giá chuẩn theo bảng BTC ngày 25/11/2026**, đơn vị USD/1 triệu token. Gemini 3.1 Flash-Lite có giá vào 0,25 và ra 1,50. Gemini 4 Hydrogen có giá vào 1,50 và ra 7,50. [Giá Flash-Lite](https://aistudio.google.com/docs/pricing#gemini-3.1-flash-lite) · [Giá Hydrogen](https://aistudio.google.com/docs/pricing#gemini-4-hydrogen)
- **Đo token và tỉ lệ đạt** sau khi ghép luồng chính, nối model thật và chấm bộ benchmark. Dùng lượt eval đã chấm của cùng model để tính chi phí mỗi tác vụ thành công.

## 2. Kết quả mô phỏng

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
