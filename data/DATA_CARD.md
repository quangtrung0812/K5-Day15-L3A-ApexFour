# Data card — dữ liệu bản chạy thử & bằng chứng (Track C · C1)

> Điền ở guide bước 2.4 (bản đầu ở CP2, cập nhật đủ ở CP3). Phụ trách: Dương Thanh Bình. Chấm ở rubric R4.
> Không commit dữ liệu cá nhân thật; mọi review công khai đều bỏ tên người viết và trích tối đa 2 câu.

## Dataset 1 · Review công khai ứng dụng VinWonders (Google Play)

| | |
|---|---|
| Dùng để làm gì | Đào bằng chứng pain (`evidence/`) · làm nguồn `data_that:` cho bộ câu thử `eval/benchmark.csv` |
| Từ đâu | Review công khai tiếng Việt trên Google Play Store của ứng dụng chính thức **VinWonders** (`https://play.google.com/store/apps/details?id=com.vinwonders.app&hl=vi&gl=VN`) |
| Xử lý những bước gì | Lấy 100 review tiếng Việt mới nhất (mọi mức sao 1–5 để tránh thiên lệch chỉ lọc 1–3 sao) → lọc giữ các review có nội dung chữ ≥10 từ (còn `N = 39` review) → ẩn danh hoàn toàn (bỏ tên người viết, thay tên cá nhân nếu có trong nội dung bằng "người quen") → rút gọn tối đa 2 câu/review → gắn nhãn `L1`–`L5`, `L0` → đếm tự động bằng script `evidence/count_reviews_binh.py` |
| Số dòng / số đoạn | 39 review (`R01`–`R39`), trải từ `2023-07-02` đến `2026-11-20` (trong đó 11/39 = 28.2% nêu trực tiếp vấn đề xếp lịch, bản đồ/di chuyển, mô tả độ tuổi/chiều cao trẻ em, giờ show hoặc chi phí/voucher ăn uống) |
| Phiên bản / ngày lấy | `2026-11-27` (lưu tại `evidence/reviews_vinwonders_binh.csv`) |
| Nhãn | **thật** |
| Giới hạn | Review trên kho ứng dụng nghiêng về người dùng gặp trục trặc kỹ thuật app (lỗi đăng nhập/lag chiếm phần lớn `L0_KHAC`) và ít nhắc trực tiếp yếu tố thời tiết mưa (`L4_THOI_TIET_MUA = 0/39`). Cần bổ sung review địa điểm Google Maps/Tripadvisor và kiểm lại bằng phỏng vấn ≥3 người dùng thật ngoài nhóm ở `evidence/interviews/` (Hoàng chủ trì). |

---

## Dataset 2 · Dữ liệu khu vui chơi mẫu (`data/park_data.json`)

| | |
|---|---|
| Dùng để làm gì | Nguồn dữ liệu nền cho 5 công cụ trong `codebase/tools.py` (`tra_diem_choi`, `tra_lich_show`, `tra_thoi_tiet`, `uoc_thoi_gian_di`, `kiem_lich_trinh`) và kiểm chứng đáp án của `eval/benchmark.csv` |
| Từ đâu | Nhóm tự dựng có seed (`synthetic`) bằng script `data/generate_park_data.py` với `SEED = 42`, đặt tên giả lập **Khu vui chơi SunWonder Mẫu** (tham khảo cấu trúc phân khu, khung giờ mở cửa 08:30–20:30 và mặt bằng giá vé phổ biến tại Việt Nam nhưng không sao chép dữ liệu thật của đơn vị nào) |
| Xử lý những bước gì | Sinh cấu trúc JSON cố định bằng `random.Random(42)` (tái tạo 100%), chia 4 phân khu (`Z1`–`Z4`), ma trận thời gian đi bộ giữa các khu (5–20 phút), bảng giá vé cổng theo độ tuổi và **cố tình gài các tình huống khó**: 1 điểm đang đóng bảo trì (`A09`), 2 trò cảm giác mạnh giới hạn tuổi ≥10 và ≥12 (`A08`, `A10`), 2 show sát/trùng giờ (`S01` 10:30–11:00 ở Z4 vs `S02` 11:00–11:20 ở Z2), 1 điểm đóng sớm 16:30 (`A12`), các điểm có phụ thu ăn uống/game/xe điện, và 3 kịch bản thời tiết (`2026-11-28` nắng, `2026-11-29` mưa 14:00–17:30, `2026-11-30` mưa cả ngày) |
| Số dòng / số đoạn | 16 điểm chơi/ăn uống/dịch vụ (`A01`–`A16`) · 5 show diễn cố định (`S01`–`S05`) · 4 phân khu (`Z1`–`Z4`) · 3 ngày thời tiết mẫu |
| Phiên bản / ngày lấy | v1.0 · `2026-11-27` |
| Nhãn | **`synthetic`** *(không phải bằng chứng pain)* |
| Giới hạn | Quy mô nhỏ hơn khu vui chơi thật (16 điểm so với 40–60 điểm), thời gian xếp hàng ước lượng cố định theo seed thay vì biến động theo thời gian thực. |

**Thông tin kiểm soát `synthetic`:** Script sinh `data/generate_park_data.py` · `seed = 42` · Người kiểm tay: Dương Thanh Bình (đã kiểm toàn bộ 16/16 điểm chơi, 5/5 show, 3/3 kịch bản thời tiết và ma trận di chuyển).
