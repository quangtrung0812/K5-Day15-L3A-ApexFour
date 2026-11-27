# Chi phí khi dùng thật

> Điền ở guide bước 4.2, nộp ở CP4 14:30 Thứ Bảy 28/11. Ôn lại: ngày 13, ngày 1, ngày 14 · lab ngày 13, lab ngày 14. Chấm ở rubric R6.
> Số **không điền tay**: điền `cost/personas.yaml` → `python run.py simulate` → chép bảng trong `cost/simulate-N-summary.md` vào đây.
> Lúc build dùng gói miễn phí vẫn tính theo **giá gói trả phí** — đây là chi phí cho lúc đưa vào dùng thật.

## 1. Đầu vào

- **Ba kiểu sử dụng** (tự ước tính) gồm lập lịch một lần (65%, 1 lượt hỏi/phiên), sửa lịch nhiều lần trước chuyến đi (25%, 3 lượt/phiên) và xếp lại trong ngày mưa (10%, 4 lượt/phiên). Mỗi kiểu dùng 1 phiên/tháng. Khung lấy ngẫu nhiên các câu có đủ thông tin chuyến đi và gọi agent riêng cho từng lượt.
- **Quy mô thử nghiệm tại một khu vui chơi** là 50, 200 hoặc 500 gia đình hoạt động mỗi tháng (tự ước tính).
- **Giá Standard trả phí** đối chiếu Google AI Studio ngày 27/11/2026 và bảng BTC ngày 25/11/2026, tính bằng USD/1 triệu token văn bản. Gemini 3.1 Flash-Lite có giá vào 0,25 và ra 1,50. Gemini 4 Hydrogen có giá vào 1,50 và ra 7,50. [Giá Flash-Lite](https://aistudio.google.com/docs/pricing#gemini-3.1-flash-lite) · [Giá Hydrogen](https://aistudio.google.com/docs/pricing#gemini-4-hydrogen)
- **Đo chi phí** theo số token của lượt mô phỏng bằng model thật. Khi tính chi phí mỗi tác vụ thành công, dùng tỉ lệ đạt từ lượt eval đã chấm của cùng model.

- Model đo thực tế là gpt-4o-mini, đơn giá 0,15 USD đầu vào và 0,60 USD đầu ra trên một triệu token. [Bảng giá OpenAI](https://developers.openai.com/api/docs/models/gpt-4o-mini)

## 2. Kết quả mô phỏng

Lượt `simulate-1@20261127-235010`, 50 phiên, seed 42. Dữ liệu từng phiên ở [simulate-1.csv](simulate-1.csv), trace ở `traces/simulate-1.jsonl`. Số liệu dưới đây dùng tỉ lệ đạt đã xác nhận 10/25 (40%) của lượt 2 (`run-2@20261127-234939`, cùng cấu hình lúc chạy mô phỏng). Hai dòng Gemini là kịch bản đổi đơn giá trên cùng lượng token `gpt-4o-mini` đã đo.

| Persona | Số phiên mô phỏng | Lượt hỏi / phiên | Token vào / phiên | Token ra / phiên | Gọi model / phiên | Gọi công cụ / phiên |
|---|---:|---:|---:|---:|---:|---:|
| lap_lich_truoc_chuyen_di | 36 | 1 | 9007 | 809 | 2.0 | 14.8 |
| sua_lich_truoc_khi_di | 13 | 3 | 25535 | 1946 | 5.7 | 43.3 |
| xep_lai_trong_ngay_mua | 1 | 4 | 26871 | 2273 | 6.0 | 50.0 |

Tỉ lệ đạt dùng để tính: 10/25 (40%) — lượt run-2@20261127-234939

- Tự chọn: lượt run-N mới nhất đã chấm xong, chạy bằng đúng model đang đo (run-2.csv). Muốn dùng lượt khác (vd lượt 2): thêm `--rate-from eval/run-2.csv`.

| Model (giá) | Chi phí / phiên | Chi phí / task thành công | Chi phí / câu hỏi đạt | Chi phí / tháng — thấp (50 người) | Chi phí / tháng — cơ sở (200 người) | Chi phí / tháng — cao (500 người) | Chi phí / người / tháng (cơ sở) |
|---|---:|---:|---:|---:|---:|---:|---:|
| gpt-4o-mini (vào 0.15 · ra 0.6 $/1M) | $0.0027 | $0.0068 | $0.0043 | $0.1491 | $0.5965 | $1.49 | $0.0030 |
| gemini-3.1-flash-lite (vào 0.25 · ra 1.5 $/1M) | $0.0051 | $0.0128 | $0.0081 | $0.2795 | $1.12 | $2.80 | $0.0056 |
| gemini-4-hydrogen (vào 1.5 · ra 7.5 $/1M) | $0.0290 | $0.0725 | $0.0459 | $1.58 | $6.34 | $15.84 | $0.0317 |

- Chi phí / task thành công = chi phí / phiên ÷ tỉ lệ đạt. Chi phí / câu hỏi đạt = chi phí / phiên ÷ số lượt hỏi trung bình mỗi phiên (1.6) ÷ tỉ lệ đạt — tỉ lệ đạt đo theo từng câu thử.
- Token đo trên model: gpt-4o-mini. Giá tính theo từng model trong bảng — model khác bộ tách token thì số token thật có thể lệch; ghi rõ "đo trên model X, tính giá model Y" trong cost/cost-estimate.md.
- Phiên lỗi (không tính vào trung bình): 0/50.

## 3. Giá trị cho gia đình

Ở kịch bản cơ sở, chi phí model là $0.0030 mỗi gia đình mỗi tháng. Hai phụ huynh báo mất 40–55 phút tự chuẩn bị và xoay xở. Mốc 45 phút là thời gian hiện tại, số phút sản phẩm giúp tiết kiệm vẫn cần đo. Tiếp tục thử nghiệm hẹp để xem gia đình có chốt được lịch nhanh hơn, nhất là khi phải đổi lịch giữa ngày.
