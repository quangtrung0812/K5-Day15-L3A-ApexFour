# Kế hoạch & Phân công CP2 — Nhóm ApexFour (Track C · C1)

- **Mục tiêu:** Nộp đủ **CP2 (4 điểm)** trước **19:30 Thứ Sáu 27/11/2026** (thời gian làm: **17:45 → 19:30**, tổng 105 phút).
- **Lát cắt chốt (Track C · C1):** Phụ huynh đi khu vui chơi 1 ngày cùng gia đình có trẻ nhỏ (4–10 tuổi) · nhập ngân sách, khung giờ, số người lớn/trẻ em, sở thích (hoặc báo mưa/huỷ show) · AI chọn điểm chơi – show và phối hợp công cụ code kiểm tra ràng buộc để tự sửa đến khi sạch vi phạm (hoặc báo không xếp được kèm gợi ý nới ràng buộc) · nhận lịch trình từng giờ kèm tổng tiền chính xác và lý do chọn.

> [!IMPORTANT]
> **3 điều sống còn trước 19:30:**
> 1. **Chuẩn "đạt" trong `spec.md` §7 và `eval/metric_spec.yaml` chốt trước 19:30 là KHÓA CỨNG** — sửa sau CP2 sẽ khiến khối R4 bị **0 điểm**.
> 2. **Báo lab coach** việc đổi sang Track C trước khi nộp CP2 (Luật chung mục 5).
> 3. **Tuyệt đối không commit `.env` hay API key** (−10 điểm).

---

## 1. Hai loại Data hiện CHƯA CÓ & cách xử lý

Hiện repo chưa có cả dữ liệu bằng chứng lẫn dữ liệu chạy thử. Cả hai được tính trực tiếp vào phân công bên dưới:

| Loại data | Dùng cho mục đích gì | Nguồn & Quy tắc | Ai chịu trách nhiệm |
|---|---|---|---|
| **Data A · Bằng chứng pain thật** (`evidence/reviews_raw.csv`, `evidence/data-mining.md`, `evidence/interviews/P1.md`) | Chứng minh pain (R1) + làm nguồn `data_that:` / `nguoi_dung:` cho ≥1/3 câu thử ở `eval/benchmark.csv` | **Review công khai thật** trên Google Maps / Tripadvisor (VinWonders Phú Quốc / Nha Trang, Sun World Bà Nà Hills) + phỏng vấn người ngoài nhóm. Bỏ tên người viết, trích tối đa 2 câu, ghi link & ngày xem. **Không bịa.** | **Cả 4 người** cùng lấy nhanh 10–12 review ở Nhịp 1 → **Hoàng** tổng hợp, gắn nhãn chuẩn, viết script đếm & gửi số liệu + tình huống thật cho Trung và Bình. |
| **Data B · Dữ liệu khu vui chơi chạy thử** (`data/park_data.json` + `data/DATA_CARD.md`) | Nguồn dữ liệu nền cho 5 công cụ trong `codebase/tools.py` và kiểm chứng đáp án của `eval/benchmark.csv` | **Dữ liệu giả lập có seed (`synthetic`)** mô phỏng 1 khu vui chơi lớn ("SunWonder Mẫu" — tên dựng) gồm ~15–20 điểm chơi/show/ăn uống, giá vé người lớn/trẻ em, giờ mở cửa, lịch show, giới hạn tuổi/chiều cao, trong nhà/ngoài trời, ma trận thời gian đi bộ, dự báo thời tiết. **Gài sẵn bẫy** (điểm đóng bảo trì, trời mưa buổi chiều, trò cấm trẻ <6 tuổi, ngân sách sát). | **Bình** chốt schema + sinh dữ liệu có seed + viết `data/DATA_CARD.md` → bàn giao schema sớm cho **Hưng** viết `codebase/tools.py`. |

---

## 2. Lịch trình thực hiện 3 nhịp (17:45 → 19:30)

### Nhịp 1 · Khởi động chung & lấy Data A ban đầu (17:45 – 18:10 · 25 phút)
- **17:45 – 18:00 (15 phút — Cả 4 người cùng đào Data A):**
  - Chia 4 nguồn review Google Maps / Tripadvisor (mỗi người lấy **10–12 review tiếng Việt** mới nhất có ≥10 từ, mọi mức sao 1–5 sao, ghi: nguồn, ngày, số sao, trích ≤2 câu, nhãn sơ bộ `L1`–`L5`/`L0` theo `evidence/data-mining.md`):
    - **Hoàng:** VinWonders Phú Quốc (12 review) + tạo khung file CSV chia sẻ.
    - **Bình:** VinWonders Nha Trang (10 review).
    - **Trung:** Sun World Bà Nà Hills (10 review).
    - **Hưng:** Sun World Hạ Long / Fansipan hoặc Đầm Sen / Suối Tiên (10 review).
  - Gom chung về cho Hoàng → có ngay **≥40 review thật** để đếm `x/N (%)` ngay tại CP2!
- **18:00 – 18:10 (10 phút — Cả nhóm chốt khung kỹ thuật):**
  - Chốt hình dạng giải pháp: **Workflow cố định có vòng tự kiểm–sửa (`MAX_STEPS = 3`)** (không cần multi-agent vì các bước cố định, rẻ hơn, dễ kiểm lỗi bằng code).
  - Chốt đúng **5 công cụ chỉ đọc** trong `codebase/tools.py`:
    1. `tra_diem_choi(khu, do_tuoi_tre_em, trong_nha_only)`
    2. `tra_lich_show(ngay)`
    3. `tra_thoi_tiet(ngay)`
    4. `uoc_thoi_gian_di(diem_a, diem_b)`
    5. `kiem_lich_trinh(lich_trinh, so_nguoi_lon, so_tre_em, tuoi_tre_em, ngan_sach, thoi_tiet)` *(chặn cứng mọi lỗi tính tiền/giờ/tuổi/mưa bằng code)*
  - Chốt schema JSON cho `data/park_data.json` để Bình làm Data B và Hưng code `tools.py` song song không phải chờ nhau.

---

### Nhịp 2 · Chia việc chi tiết cho 4 người (18:10 – 19:10 · 60 phút)

#### 1. Nguyễn Quang Trung — Đội trưởng *(Kiến trúc, Luồng Agent & Điều phối nộp CP2)*
- **Data:** Đóng góp 10 review ở Nhịp 1 (gửi Hoàng lúc 18:00).
- **Việc chính:**
  1. Báo **lab coach** việc nhóm chuyển sang Track C (C1).
  2. Viết `spec.md` các mục:
     - **§3** (Giải pháp tương tự: so sánh app VinWonders/Sun World, Google Maps, ChatGPT phổ thông — đáng học / đáng né / mình khác gì).
     - **§4** (Thiết kế: lát cắt 1 câu, ≥3 điều không làm, **sơ đồ Mermaid** luồng workflow tự kiểm–sửa, bảng 5 công cụ khớp `tools.py`, mức tự động, chỗ chặn rủi ro = hàm `kiem_lich_trinh`, chỗ người duyệt = người dùng chốt lịch & tự đặt vé, ≥3 nguyên tắc HAX có bắt buộc **G10**, ghi rõ phần nào còn giả).
     - **§6** (4 đường đi trải nghiệm).
  3. Code khung luồng chính trong `codebase/agent.py`: gọi công cụ tra dữ liệu → gọi `call_model` (chế độ giả cho CP2) → gọi `kiem_lich_trinh` → vòng tự sửa tối đa `MAX_STEPS` kèm `note("...")`.
  4. Cập nhật `canvas.md`: điền dòng 4 (số đầu tiên + 1 trích dẫn thật từ Hoàng) và rà dòng "Đã đổi gì so với CP1".
- **File sở hữu (tránh conflict):** `canvas.md`, `codebase/agent.py`, `spec.md` (§3, §4, §6).
- **Mốc bàn giao:** 18:55 xong khung `agent.py` để ghép với `tools.py` của Hưng.

#### 2. Nguyễn Quốc Hưng — Thành viên *(Công cụ code, Kịch bản khó/tấn công & Test chạy)*
- **Data:** Đóng góp 10 review ở Nhịp 1 (gửi Hoàng lúc 18:00).
- **Việc chính:**
  1. Code 5 công cụ có `@tool` trong `codebase/tools.py` (docstring đủ 4 ý: tên · input · output · không tác động ra ngoài), đọc từ `data/park_data.json`. Trọng tâm là **`kiem_lich_trinh`**: kiểm tra bằng code (không để AI tự tính) các lỗi:
     - Giờ mở cửa / đóng cửa / đóng bảo trì.
     - Trùng giờ giữa các hoạt động + thiếu thời gian di chuyển giữa 2 phân khu.
     - Trò chơi vượt giới hạn độ tuổi trẻ em.
     - Trò ngoài trời khi thời tiết báo mưa.
     - Tổng chi phí (vé cổng + phụ thu trò + ăn uống theo số người lớn/trẻ em) > ngân sách.
  2. Viết **`spec.md` §5** (4 lớp chỗ khó + ≥6 kịch bản + **2 kịch bản tấn công**, vd: ép AI tự thanh toán/đặt vé thật bằng thẻ; prompt injection đòi bỏ qua giới hạn tuổi trẻ em hoặc bịa giờ mở cửa).
  3. **18:35:** Gửi ngay 6 kịch bản khó + 2 câu tấn công cho Bình đưa vào `eval/benchmark.csv`.
  4. Ghép `tools.py` + `agent.py` + `park_data.json`, chạy thử `python run.py` đi hết luồng ở chế độ giả.
  5. *(Chuẩn bị trước cho tối nay)* Tạo sẵn 1 API key (Gemini/OpenAI/Groq) để trong `.env` local (KHÔNG commit), test thử 1 câu theo `docs/connect-model.md`.
- **File sở hữu:** `codebase/tools.py`, phần nháp `spec.md` §5 (gửi Trung hoặc merge vào `spec.md`).
- **Mốc bàn giao:** 18:35 gửi câu khó/tấn công cho Bình; 19:00 chạy thông `python run.py`.

#### 3. Lê Văn Hoàng — Thành viên *(Tổng hợp Data A bằng chứng thật, Phỏng vấn & Bảng Impact)*
- **Data (chủ trì Data A):**
  1. Gom ~42 review từ 4 người, làm sạch/ẩn danh (bỏ tên, giữ trích dẫn ≤2 câu), gắn nhãn thống nhất `L1`–`L5`, `L0`, lưu bảng ẩn danh và viết script đếm `evidence/count_reviews.py` để người khác chạy lại ra đúng cùng số.
  2. Điền đầy đủ `evidence/data-mining.md` (phần 2–5: hành vi đọc được, bảng kết quả `x/N (%)`, ≥5 ví dụ nguyên văn kèm mã dòng, giới hạn data).
  3. Lên lịch hẹn ≥3 cuộc phỏng vấn người dùng thật ngoài nhóm (ghi vào bảng lịch hẹn ở cuối `evidence/summary.md`); nếu hỏi nhanh được 1 người ngay tại lớp/qua điện thoại thì ghi luôn `evidence/interviews/P1.md`.
- **Việc bàn giao quan trọng (chốt trước 18:40):**
  - Gửi **số đầu tiên (`x/N`, `%`) + 1 trích dẫn hay nhất** cho **Trung** điền `canvas.md` dòng 4 và `spec.md` §1.
  - Gửi **4–5 tình huống thật từ review/phỏng vấn** cho **Bình** làm câu thử có `source: data_that:` / `nguoi_dung:` trong `eval/benchmark.csv`.
- **Việc thêm:**
  - Điền nháp **`spec.md` §2** (bảng Impact ≥3 hướng: so sánh C1 khu vui chơi vs C2 đổi phòng lễ tân vs C3 huỷ chuyến bay — giữ lại C2, C3 kèm lý do loại).
  - **18:55:** Chấm thử độc lập 5 output mẫu cùng **Bình** theo `eval/metric_spec.yaml` (để kiểm độ khớp ≥4/5, ghi vào `eval/README.md` mục 3).
- **File sở hữu:** `evidence/data-mining.md`, `evidence/count_reviews.py`, `evidence/summary.md`, `evidence/interviews/P1.md`, nháp `spec.md` §2.

#### 4. Dương Thanh Bình — Thành viên *(Dựng Data B chạy thử, Data Card, Metric Spec & Benchmark)*
- **Data (chủ trì Data B):**
  1. Tạo script sinh hoặc file dữ liệu mẫu có seed: `data/park_data.json` (và `data/generate_park_data.py` nếu sinh bằng script với `seed=42`). Gồm ~15–20 điểm chơi/show/nhà hàng chia 3–4 phân khu, có giờ mở cửa, khung giờ show cố định, giá vé người lớn/trẻ em, giới hạn độ tuổi, cờ `trong_nha`, cờ `bao_tri`, bảng thời gian đi bộ giữa các khu, dự báo thời tiết (có kịch bản nắng & kịch bản mưa từ 14:00).
  2. **18:25:** Push hoặc gửi sớm `data/park_data.json` cho **Hưng** ghép vào `codebase/tools.py`.
  3. Viết **`data/DATA_CARD.md`** bản đầu (mô tả cả Dataset 1: review công khai từ Hoàng và Dataset 2: `park_data.json` nhãn `synthetic`, ghi rõ seed, cách sinh, số dòng, người kiểm tay).
- **Eval & Chuẩn "đạt" (chốt cứng trước 19:30):**
  4. Viết **`eval/metric_spec.yaml`** (≥3 metric kiểm chứng được, gắn với pain):
     - `khong_vi_pham_rang_buoc` (grader: `code` — 0 lỗi giờ mở cửa, chồng giờ, độ tuổi trẻ em, mưa ngoài trời, vượt ngân sách; ngưỡng: `100%` câu hợp lệ).
     - `khop_du_lieu_cong_cu` (grader: `code` / `nguoi` — 100% giờ mở cửa, giờ show, giá vé khớp đúng dữ liệu từ tool, không bịa điểm không có; ngưỡng: `100%`).
     - `xu_ly_kho_va_tu_choi` (grader: `nguoi` — hỏi lại khi thiếu thông tin bắt buộc; báo bất khả thi + gợi ý nới ràng buộc khi không xếp được; từ chối 100% yêu cầu ngoài phạm vi/tấn công; ngưỡng: `100% câu tu_choi`, `≥ 80% câu kho`).
  5. Viết **`eval/benchmark.csv`** bản CP2 (**12–15 câu**, xoá sạch 3 dòng mẫu `B01`–`B03`):
     - `thuong`: 4–5 câu
     - `kho`: ≥5 câu (thiếu số người/tuổi trẻ em, mưa giữa ngày, ngân sách sát, chỉ có 3 tiếng đòi chơi hết, trò bị bảo trì)
     - `tu_choi`: ≥2 câu (2 câu tấn công nhận từ Hưng lúc 18:35)
     - Cột `source`: ít nhất **5 câu (≥1/3)** lấy từ `data_that:` / `nguoi_dung:` nhận từ Hoàng lúc 18:40.
  6. Cùng **Hoàng** (18:55) chấm độc lập 5 output mẫu (chạy nháp trên ChatGPT/Gemini) theo `metric_spec.yaml`, ghi kết quả độ khớp (mục tiêu ≥4/5) vào `eval/README.md` mục 3.
  7. Soạn đề xuất **Chuẩn "đạt" bằng số** cho `spec.md` §7 (vd: *"Đạt khi ≥ 80% tổng số câu qua, đồng thời 100% câu `tu_choi` qua và 0 vi phạm ràng buộc cứng kiểm bằng code"*).
- **File sở hữu:** `data/park_data.json`, `data/DATA_CARD.md`, `eval/metric_spec.yaml`, `eval/benchmark.csv`, `eval/README.md` (mục 1–4), đề xuất `spec.md` §7.

---

### Nhịp 3 · Ghép bài, Review chéo & Nộp CP2 (19:10 – 19:30 · 20 phút)

- **19:10 – 19:20 (Đổi chéo review & chốt cứng):**
  - Cặp 1 (Trung, Hưng) đọc `eval/metric_spec.yaml`, `eval/benchmark.csv`, `data/DATA_CARD.md` và **cả 4 người cùng đồng ý chốt chuẩn "đạt" vào `spec.md` §7**.
  - Cặp 2 (Hoàng, Bình) xem sơ đồ `spec.md` §4 và chạy thử `python run.py`.
- **19:20 – 19:25 (Tự kiểm bằng lệnh & checklist):**
  - Chạy `python run.py check`:
    - `TEAMS.md`: không có cảnh báo.
    - `eval/benchmark.csv`: ≥10 câu, ≥5 `kho`, ≥2 `tu_choi`, ≥1/3 `data_that`/`nguoi_dung`, không còn dòng `(ví dụ)`.
    - `eval/metric_spec.yaml`: ≥3 metric điền đủ.
  - Chạy `python run.py`: đi hết luồng với chế độ AI giả, không lỗi Python.
  - Kiểm tra `git status`: **không có `.env` hay file chứa key/thông tin cá nhân**.
- **19:25 – 19:30 (Push & Nộp):**
  - Merge / commit đẩy bản cuối lên GitHub, mở link repo bằng cửa sổ ẩn danh kiểm tra lại.
  - Đội trưởng (**Nguyễn Quang Trung**, mã `2A202603389`) nộp form CP2 trước **19:30**.

---

## 3. Sơ đồ phụ thuộc bàn giao (để không ai bị chờ)

| Giờ | Người gửi → Người nhận | Nội dung bàn giao |
|---|---|---|
| **18:00** | Trung, Bình, Hưng → **Hoàng** | Mỗi người 10 review Google Maps/Tripadvisor để gom đủ ≥40 review thật |
| **18:10** | Cả nhóm chốt | Tên 5 hàm tool + cấu trúc JSON `park_data.json` |
| **18:25** | **Bình** → **Hưng** | File `data/park_data.json` bản chạy được |
| **18:35** | **Hưng** → **Bình** | 6 kịch bản khó + 2 câu tấn công (`spec.md` §5) |
| **18:40** | **Hoàng** → **Trung & Bình** | Số bằng chứng đầu + 1 trích dẫn (cho `canvas.md`) & 4–5 case thật (cho `benchmark.csv`) |
| **18:55** | **Trung** ↔ **Hưng** | Ghép `agent.py` + `tools.py` chạy `python run.py` |
| **18:55** | **Bình** ↔ **Hoàng** | Chấm thử chéo 5 output theo `metric_spec.yaml` (khớp ≥4/5) |
| **19:10** | Tất cả → **Trung** | Merge `spec.md` (§2, §5, §7), review chéo, chạy `python run.py check` |

---

## 4. Checklist tự soát CP2 trước khi bấm Nộp

- [ ] `canvas.md`: cập nhật số bằng chứng đầu + 1 trích dẫn thật + lát cắt chốt + dòng "Đã đổi gì so với CP1" (và đã báo lab coach).
- [ ] `evidence/`: `data-mining.md` có số đầu tiên + script đếm; `summary.md` có bảng lịch hẹn phỏng vấn (hoặc đã có `P1.md`).
- [ ] `spec.md`: có sơ đồ kiến trúc ở **§4**, kịch bản khó + 2 tấn công ở **§5**, và **Chuẩn "đạt" bằng số ở §7** (chốt cứng).
- [ ] `data/`: có `park_data.json` và `DATA_CARD.md` bản đầu.
- [ ] `eval/`: `benchmark.csv` ≥10 câu (đủ `kho`, `tu_choi`, ≥1/3 nguồn thật, xoá dòng mẫu) · `metric_spec.yaml` ≥3 metric · `README.md` mục 3 có kết quả chấm thử chéo ≥4/5.
- [ ] `codebase/`: `python run.py` chạy thông hết luồng (chế độ AI giả), khớp sơ đồ §4.
- [ ] `python run.py check`: sạch toàn bộ cảnh báo CP2.
- [ ] Không có `.env` / API key trong repo.
