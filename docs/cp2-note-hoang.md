# Take note CP2 — Phần việc Lê Văn Hoàng (`2A202603357`)

- **Nhánh:** `LeVanHoang-2A202603357`
- **Cập nhật lúc:** 27/11/2026 18:05
- **Mục tiêu:** Zero merge conflict với `main`, `feat/cp2-binh-data-eval` và nhánh của Trung/Hưng. Các đoạn dành cho `canvas.md` và `spec.md` §1–§2 được chuẩn bị sẵn bên dưới để Trung ghép trực tiếp vào `main`.

---

## 1. Các file đã hoàn thành trên nhánh `LeVanHoang-2A202603357`

1. `evidence/reviews_raw.csv`: Bảng tổng hợp chính thức **39 review công khai tiếng Việt thật** (gộp lô mẫu Google Play VinWonders `com.vinwonders.app` do Bình & Hoàng kiểm duyệt; đã ẩn danh hoàn toàn, trích ≤2 câu/review, đủ link + ngày xem `2026-11-27`).
2. `evidence/count_reviews.py`: Script đếm tái lập 100% (`python evidence/count_reviews.py`), kiểm tra schema, phân bố sao, đếm **số review duy nhất** gặp `L1`–`L5` (không cộng trùng) và xuất bảng Markdown.
3. `evidence/data-mining.md`: Điền đầy đủ Mục 1–5 (cách đếm, đọc trước đếm sau, bảng kết quả `x/N (%)`, 7 trích dẫn nguyên văn `R02, R03, R18, R27, R32, R33, R39`, giới hạn data).
4. `evidence/summary.md`: Tổng hợp số liệu CP2 (`11/39 = 28.2%`), 6 trích dẫn nguyên văn, đánh giá giả thuyết và **bảng Lịch hẹn 3 cuộc phỏng vấn** (`P1`, `P2`, `P3`) cho CP3.
5. `evidence/interviews/TEMPLATE.md`: Bộ 6 câu hỏi phỏng vấn Mom Test chuẩn cho Track C · C1 (sẵn sàng chép sang `P1.md`–`P3.md`).

---

## 2. Bàn giao cho Trung — Dán vào `canvas.md` (dòng 4) & `spec.md` §1

> **Dòng 4 `canvas.md` (CP2):**
> **Số đầu tiên (`evidence/data-mining.md`):** **11/39 (28.2%)** review tiếng Việt (≥10 từ, mọi mức sao) trên Google Play VinWonders nêu vấn đề thuộc nhóm xếp lịch trình — dẫn đầu là bản đồ/di chuyển/tối ưu lộ trình (**9/39 = 23.1%**), giờ show/thông báo giờ (**2/39 = 5.1%**), chi phí/voucher (**2/39 = 5.1%**), giới hạn độ tuổi/chiều cao trẻ em (**1/39 = 2.6%**). **Trích dẫn thật (`R32`):** *"Cần bổ sung thêm mô tả cho các trò chơi. Trò nào không dành cho trẻ em, người dưới 1m4... để chủ động sắp xếp thời gian di chuyển và chọn khu vui chơi phù hợp."* **Đang làm tiếp:** đã lên lịch hẹn phỏng vấn 3 người dùng ngoài nhóm (`P1`–`P3` trong `evidence/summary.md`) để kiểm chéo trước CP3.

---

## 3. Bàn giao cho Trung — Nháp `spec.md` §2 (Impact & quyết định chọn)

| Hướng (Track C) | Bao nhiêu người gặp | Bao nhiêu lần / tháng | Mỗi lần tốn gì | Impact / tháng | Làm kịp không | Chọn? |
|---|---|---|---|---|---|---|
| **C1 · Lịch trình 1 ngày ở khu vui chơi thoả ràng buộc** *(gia đình có trẻ nhỏ)* | ~30.000 gia đình/nhóm khách/tháng tại 1 khu vui chơi lớn *(tự ước tính từ quy mô >1 triệu lượt/năm)* × **28.2%** gặp vướng lịch/bản đồ (`evidence/data-mining.md`) ≈ **8.460 gia đình** | 1 lần / chuyến đi *(tự ước tính)* | ~60 phút tra cứu trước chuyến + dò bản đồ/đổi lịch tại chỗ *(tự ước tính, kiểm lại ở phỏng vấn P1–P3)*; nguy cơ lỡ show chính & đi vòng vèo mệt trẻ nhỏ | **~8.460 giờ / tháng** (~507.600 phút / tháng) | **Có** (chỉ đọc dữ liệu, chặn lỗi bằng code `kiem_lich_trinh`, demo rõ trong 2 phút) | **CHỌN** |
| **C2 · Đề xuất đổi / nâng hạng phòng cho lễ tân khách sạn** | ~50 lễ tân tại 1 chuỗi khách sạn vừa *(tự ước tính)* | ~60 ca xin đổi phòng / lễ tân / tháng *(tự ước tính)* | ~10 phút tra phòng trống, chính sách & tính phí chênh *(tự ước tính)* | ~500 giờ / tháng | Khó lấy bằng chứng thật trong 2 ngày vì phải hẹn lễ tân khách sạn ngoài khoá | **Loại** |
| **C3 · Hỗ trợ hành khách khi chuyến bay bị huỷ** | ~5.000 hành khách bị huỷ chuyến / tháng *(tự ước tính)* | 1 lần / sự cố *(tự ước tính)* | ~45 phút tự bấm đổi/hoàn vé, rủi ro mất lần đổi miễn phí hoặc gửi hoàn không huỷ được | ~3.750 giờ / tháng | Rủi ro hành động không đảo được rất cao; ít gặp người vừa bị huỷ chuyến trong lớp để phỏng vấn | **Loại** |

- **Impact / tháng của hướng chọn (C1)** = `8.460` gia đình gặp vướng *(30.000 lượt gia đình/tháng tự ước tính × 28.2% tỷ lệ gặp pain từ `evidence/data-mining.md`)* × `1` lần/tháng *(tự ước tính)* × `60` phút/lần *(tự ước tính — sẽ cập nhật từ phỏng vấn P1–P3 trước CP3)* = **507.600 phút/tháng (~8.460 giờ/tháng)** ở quy mô 1 khu vui chơi lớn.
- **Hướng ĐÃ LOẠI + vì sao:**
  - **C2 (Lễ tân đổi phòng):** Không có nguồn người dùng là lễ tân khách sạn để phỏng vấn trực tiếp trong 2 ngày (rủi ro bẫy Track C: *"C2 chỉ có review của khách, trong khi người dùng là lễ tân"*).
  - **C3 (Chuyến bay bị huỷ):** Tỷ lệ bạn học/người thân vừa bị huỷ chuyến trong 1 tháng qua thấp nên khó gom đủ bằng chứng phỏng vấn; đồng thời hành động đổi/hoàn vé khó đảo đòi hỏi quy trình xác nhận phức tạp hơn lát cắt 10 giờ.
- **Số lần dùng / tháng của 3 kiểu người dùng (dùng cho `cost/personas.yaml` ở §8):**
  1. **Khách đi chơi lần đầu — xếp 1 lần chốt luôn (`xep_mot_lan`):** ~1 phiên / tháng *(tự ước tính)*, 1–2 lượt gọi model.
  2. **Phụ huynh kỹ tính — sửa lịch nhiều lần trước ngày đi (`sua_nhieu_lan`):** ~3 phiên / tháng *(tự ước tính)*, mỗi phiên chỉnh ngân sách/giờ đi 2–3 vòng tự kiểm.
  3. **Gia đình đi vào ngày mưa / show huỷ — xếp lại giữa ngày (`ngay_mua_xep_lai`):** ~2 phiên / tháng vào mùa mưa *(tự ước tính)*, nhiều vòng gọi `kiem_lich_trinh` để chuyển điểm trong nhà.

---

## 4. Bàn giao cho Bình — 5 tình huống thật từ review (`data_that:`) & lịch chấm chéo 18:55

5 case cốt lõi đã có trong `evidence/reviews_raw.csv` (khớp với 6 câu `data_that:` Bình đã đưa vào `eval/benchmark.csv`):
- `R02`: Người dùng muốn chọn danh sách trò chơi yêu thích rồi AI tự tối ưu thứ tự, thời gian chơi và đường đi.
- `R32`: Gia đình có trẻ nhỏ (<1m4 / 5 tuổi) cần lọc trò không hợp tuổi để chủ động sắp xếp thời gian di chuyển.
- `R03`: Cần biết giờ show cố định (như Tata Show), cách di chuyển giữa phân khu và điểm ăn uống phù hợp voucher/ngân sách.
- `R18`: Cần thông báo giờ cụ thể, tránh đến nơi không có lịch hoặc chờ vô ích.
- `R27`: Cần minh bạch chi phí ăn uống / phụ thu trong tổng ngân sách để không bị phát sinh ngoài dự tính.

**Lịch phối hợp tiếp theo của Hoàng:**
- [ ] **18:55:** Chấm thử độc lập 5 output mẫu cùng **Bình** theo `eval/metric_spec.yaml` (mục tiêu khớp ≥4/5 để Bình điền vào `eval/README.md` mục 3).
- [ ] **20:00 tối 27/11 → 09:00 sáng 28/11:** Phỏng vấn trực tiếp `P1`, `P2`, `P3`, cập nhật `evidence/interviews/P1.md`–`P3.md`, `evidence/summary.md` và cập nhật số phút thật vào `spec.md` §2 trước **CP3 (10:00 Thứ Bảy 28/11)**.
