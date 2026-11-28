# Reflection — Dương Thanh Bình

> Vai trò: Thành viên · Mã học viên: `2A202603531` · Nhóm ApexFour · Lớp L3A · Track C (C1)

1. **Vai trò + phần mình làm (trỏ tới file / commit):**
   Tôi phụ trách xây dựng dữ liệu nền, bộ câu thử benchmark, tiêu chí đánh giá và hạ tầng chạy đánh giá cho nhóm.
   Ở CP2 (`7daa207`), tôi thu thập 39 review tiếng Việt thật (≥10 từ) của app VinWonders trên Google Play kèm script đếm (`evidence/reviews_vinwonders_binh.csv`, `evidence/count_reviews_binh.py`), sinh dữ liệu khu vui chơi giả lập có seed cố định `seed=42` (`data/generate_park_data.py`, `data/park_data.json`, `data/DATA_CARD.md`), chốt 4 metric (`eval/metric_spec.yaml`), 15 câu thử đầu tiên (`eval/benchmark.csv`) và hồ sơ đánh giá (`eval/README.md`).
   Sang CP3 (`871bcd6`, `29ba922`, `1089463`, `9a8771b`, `1f25225`), tôi mở rộng benchmark lên 25 câu (`B16`–`B25`, nguồn dữ liệu thật `10/25 = 40%`, giữ nguyên `B01`–`B15` và chuẩn "đạt" §7), chấm chéo độc lập 5 output mẫu với Lê Văn Hoàng (khớp 5/5), viết công cụ kiểm tự động 2 metric bằng code (`eval/grade_helper.py`), nối gọi model thật (`codebase/ai.py`) và chạy + chấm Lượt 1 (`eval/run-1.csv`, `9/25 = 36%`).
   Ở CP4 (`1dcbe3e`), tôi tích hợp bộ xếp lịch bằng Python (`codebase/route.py`), chạy đánh giá `run-2` đến `run-4`, mô phỏng chi phí 50 phiên (`cost/simulate-1.csv`), dựng demo HTML (`demo/server.py`, `demo.html`), slide (`demo-slides.pdf`) và video dự phòng (`demo-backup.mp4`).

2. **AI hỗ trợ mình thế nào (việc gì, công cụ gì, chỗ nào phải sửa lại output AI):**
   Tôi dùng coding agent (Antigravity / Gemini) và Codex để dựng nhanh script sinh dữ liệu `data/generate_park_data.py`, bộ kiểm tự động `eval/grade_helper.py`, bộ xếp tuyến `codebase/route.py` và khung tài liệu `data/DATA_CARD.md`, `eval/README.md`.
   Các chỗ phải tự kiểm và sửa lại output AI gồm: (a) khi mở rộng `B16`–`B25`, tôi phải chạy lại `kiem_lich_trinh` để kiểm tay toàn bộ giá vé cổng, phụ thu và thời gian di chuyển thay vì tin vào đáp án nhẩm của AI; (b) trong `codebase/ai.py`, AI tự thêm tham số `temperature` vào lệnh gọi OpenAI gây lỗi tương thích với dòng model reasoning mới nên tôi phải gỡ bỏ (`343dbbc`); (c) `eval/grade_helper.py` do AI hỗ trợ viết chỉ kiểm được ràng buộc cứng (đánh dấu qua `16/25` ở Lượt 2 và `25/25` ở Lượt 3–4), không bắt được lỗi thuyết minh sai giới hạn tuổi hoặc bịa giờ điểm ngoài danh mục, nên nhóm vẫn phải rà soát tay từng câu theo `pass_criterion`.

3. **Một câu thử trượt của nhóm và mình học được gì từ nó:**
   Câu `B20` do tôi thêm ở CP3 (yêu cầu xếp lịch ngày 28/11/2026 kèm hai điểm không tồn tại trong `data/park_data.json` là *"Show Cá Heo"* và *"Vòng quay Mặt Trời"*) đã trượt xuyên suốt từ Lượt 1 đến Lượt 3 (`eval/run-1.csv` → `eval/run-3.csv`).
   Đáng chú ý nhất là ở Lượt 2 (`eval/run-2.csv`): bộ kiểm tự động `grade_helper.py` xác nhận lịch thay thế đạt 0 vi phạm ràng buộc cứng, nhưng khi đọc kỹ phần văn bản thì model vẫn tự bịa giờ `18:30` cho điểm ngoài danh mục, và sang Lượt 3 vẫn thiếu câu xác nhận rõ hai điểm đó không có trong dữ liệu trước khi được khắc phục ở Lượt 4 (`eval/run-4.csv`).
   Bài học lớn nhất tôi rút ra là: chấm tự động bằng code chỉ đảm bảo điều kiện cần (lịch không sai giờ, tuổi, tiền), còn để đánh giá đúng lỗi bịa nguồn sự thật thì bộ câu thử phải có `pass_criterion` kiểm được cả phần thuyết minh văn bản và luôn cần bước rà soát đối chiếu dữ liệu gốc trước khi kết luận "đạt".
