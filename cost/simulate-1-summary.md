# Tóm tắt mô phỏng simulate-1@20261127-235010

Do `python run.py simulate` sinh ra — không sửa tay. Chép bảng sang `cost/cost-estimate.md`.

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
