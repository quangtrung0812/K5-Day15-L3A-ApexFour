# Tổng hợp bằng chứng pain

> Điền ở guide bước 1.2, xong trước **CP3 10:00 Thứ Bảy 28/11**. Phụ trách: Lê Văn Hoàng (bổ sung phỏng vấn P1–P5 ngày 27/11). Chấm ở rubric R1.
> Ba nguồn ngang nhau — tối thiểu **≥1 nguồn đạt ngưỡng**. Nhóm đã hoàn thiện **2 nguồn đạt ngưỡng kiểm chéo nhau**: Đào data công khai + Phỏng vấn 5 người ngoài nhóm (`P1`–`P5`).

## 1. Nguồn đã dùng

| Nguồn | Đạt ngưỡng? | File |
|---|---|---|
| Đào data (x/N, %, cách đếm chạy lại được, ≥5 ví dụ) | ☑ **Đạt ngưỡng** (`11/39 = 28.2%` ở VinWonders + đối chiếu `3/10 = 30.0%` ở Sun World Hạ Long; 7 ví dụ nguyên văn) | `evidence/data-mining.md` · `evidence/reviews_raw.csv` · `evidence/count_reviews.py` · `evidence/hung-ha-long.md` |
| Phỏng vấn (≥3 người ngoài nhóm, đúng người dùng) | ☑ **Đạt ngưỡng** (5 người ngoài nhóm `P1`–`P5`, tách rõ theo 2 vai: 3 gia đình có trẻ nhỏ + 2 nhóm không có trẻ nhỏ) | `evidence/interviews/P1.md` … `P5.md` |
| Khảo sát (≥20 người ngoài nhóm, đúng người dùng) | — *(không chọn ở `hypothesis.md`)* | — |

## 2. Số chính

- **Đào data — Nguồn chính (`evidence/data-mining.md`, Google Play — VinWonders, `N = 39` review tiếng Việt ≥10 từ ở bài gốc, mọi mức sao):**
  - **11/39 (28.2%)** review nêu ít nhất 1 vấn đề thuộc nhóm bài toán xếp lịch trình (`L1`–`L5`):
    - Bản đồ / chỉ đường / tối ưu thứ tự chơi (`L2`): **9/39 (23.1%)**
    - Giờ show / thông báo giờ cụ thể (`L1`): **2/39 (5.1%)**
    - Chi phí ăn uống / voucher phát sinh (`L5`): **2/39 (5.1%)**
    - Giới hạn độ tuổi / chiều cao trẻ em <1m4 (`L3`): **1/39 (2.6%)**
    - Thời tiết mưa (`L4`): **0/39 (0.0%)**
- **Đào data — Mẫu đối chiếu bổ sung (`evidence/hung-ha-long.md`, Tripadvisor — Sun World Hạ Long, `N = 10` review tiếng Việt ≥10 từ):**
  - **3/10 (30.0%)** review mô tả khu vực / trò chơi đóng cửa hoặc đang bảo trì bất ngờ khi khách đi 2 công viên trong ngày (`L1_TRE_SHOW_GIO_MO_CUA`: `HL01, HL02, HL04`). *(Gộp cả hai nguồn công khai: **14/49 = 28.6%**).*
- **Phỏng vấn *(đếm tách theo từng vai, n nhỏ không ghi %)*:**
  - **Vai chính — Gia đình có trẻ nhỏ (4–10 tuổi, n = 3: `P1`, `P3`, `P4`):** **2/3 người** gặp pain (`P1` vướng chiều cao bé + vượt 250k; `P3` gặp trò đóng cửa + vượt 150k; `P4` không vỡ lịch do đã quen Suối Tiên). Số lần đi/năm: `P1: 1`, `P3: 1`, `P4: 3`. Tổng thời gian chuẩn bị + xoay xở của 2 gia đình gặp pain: **40–55 phút** (trung bình **47,5 phút**).
  - **Vai phụ — Nhóm bạn / Gia đình không có trẻ nhỏ (n = 2: `P2`, `P5`):** **2/2 người** gặp sự cố đổi lịch/lỡ show (`P2` gặp mưa phải chuyển khu trong nhà, nhưng bực nhất vẫn là chờ cáp treo; `P5` lỡ giờ show vì đi bộ giữa 2 phân khu lâu hơn dự tính + vượt 200k). Số lần đi/năm: `P2: 2`, `P5: 2`. Tổng thời gian chuẩn bị + xoay xở: **25–50 phút**.

| Mã | Vai | Gặp pain? | Số lần đi / 1 năm qua | Chuẩn bị + xoay xở | Đang xoay xở bằng |
|---|---|---|---|---|---|
| P1 | Phụ huynh có con 6 tuổi (VinWonders Nha Trang) | **Có** (bé không đủ chiều cao + lố 250k ăn uống) | 1 lần | 35p + 20p = **55 phút** | Chụp ảnh lịch show gửi nhóm chat, hỏi nhân viên đổi khu |
| P3 | Người thân dẫn cháu 9 tuổi (Sun World Hạ Long) | **Có** (trò mong chơi tạm đóng + lố 150k) | 1 lần | 25p + 15p = **40 phút** | Xem video review + lướt bản đồ, tới nơi hỏi nhân viên đi vòng |
| P4 | Phụ huynh có 2 con 5 & 8 tuổi (Suối Tiên) | **Không** (quen đường, bé mệt sớm nên về sớm) | 3 lần | 5p + 0p = **5 phút** | Chọn trò quen, thấy hàng dài thì sang trò kế bên |
| P2 | Nhóm 4 bạn, không trẻ nhỏ (Bà Nà Hills) | **Một phần** (mưa đổi vào trong nhà; bực nhất chờ cáp treo) | 2 lần | 15p + 10p = **25 phút** | Xem giờ mở cửa, gặp mưa tự mở bản đồ thống nhất |
| P5 | Gia đình không trẻ nhỏ (VinWonders Phú Quốc) | **Có** (lỡ giờ show vì đi bộ xa + lố 200k ăn tối) | 2 lần | 40p + 10p = **50 phút** | Ghi giờ show vào điện thoại, lỡ show hỏi nhân viên đổi sang thủy cung |

## 3. ≥5 trích dẫn hoặc ví dụ nguyên văn (có nguồn, bỏ tên)

1. *"liệt kê tối ưu trò chơi, thời gian chơi, đường đi và thêm stick để người chơi lựa chọn trò xong app tối ưu (nếu được nên khuyến nghị nếu khách quá đông) là rất hay"* — `reviews_raw.csv` dòng `R02` (Google Play VinWonders, 4★, 2026-09-05)
2. *"Cần bổ sung thêm mô tả cho các trò chơi. Trò nào không dành cho trẻ em, người dưới 1m4... để chủ động sắp xếp thời gian di chuyển và chọn khu vui chơi phù hợp"* — `reviews_raw.csv` dòng `R32` (Google Play VinWonders, 3★, 2023-07-24)
3. *"thông tin hạng vé vào cửa dc tặng vouchers ăn nhưng vào app k hiển thị vouchers ăn nên bố k biết vouchers sử dụng cho ăn uống ở đâu. k có thông tin các trạm tuktuk di chuyển trg vinwonders Nha Trang, đổi lên Premium xem show Tata miễn phí mà đổi xog cũg méo hiện trg app"* — `reviews_raw.csv` dòng `R03` (Google Play VinWonders, 2★, 2026-09-04)
4. *"Tới nơi mới biết bé chưa đủ chiều cao chơi trò đã chọn. Bé hụt hẫng là cái mình nhớ nhất."* — `evidence/interviews/P1.md` (Phụ huynh có con 6 tuổi)
5. *"Đi tới trò cháu mong chơi thì thấy bảng báo tạm đóng. Bực nhất là đi bộ tới tận nơi mới biết."* — `evidence/interviews/P3.md` (Người thân dẫn cháu 9 tuổi)
6. *"Đến chỗ xem show thì đã qua giờ vì đi từ phân khu bên kia lâu hơn mình tưởng. Tiếc nhất là đã canh giờ mà vẫn lỡ."* — `evidence/interviews/P5.md` (Gia đình đi VinWonders Phú Quốc)
7. *"Mưa đúng lúc định đi chụp ảnh ngoài trời. Cả nhóm xem bản đồ rồi chuyển vào khu trong nhà, mất khoảng 10 phút để thống nhất. Khó chịu nhất hôm đó vẫn là chờ cáp treo."* — `evidence/interviews/P2.md` (Nhóm bạn đi Bà Nà Hills)

## 4. Các nguồn có khớp nhau không

- **Khớp mạnh giữa Đào data và Phỏng vấn:**
  - Nỗi đau **giới hạn chiều cao trẻ em** (`R32` trong data) được `P1` xác nhận trực tiếp (*"tới nơi mới biết bé chưa đủ chiều cao... bé hụt hẫng"*).
  - Nỗi đau **trò chơi tạm đóng bất ngờ** (`3/10 = 30.0%` trong `hung-ha-long.md`) được `P3` xác nhận đúng tại Sun World Hạ Long (*"đi bộ tới tận nơi mới biết"*).
  - Nỗi đau **ước lượng sai thời gian đi bộ giữa phân khu gây lỡ show** (`9/39 = 23.1%` bản đồ/di chuyển ở `data-mining.md`) được `P5` xác nhận (*"đã canh giờ mà vẫn lỡ"*), còn **phát sinh ăn uống 150k–250k** xuất hiện ở 3/5 người (`P1`, `P3`, `P5`).
- **Điểm bổ sung & điểm lệch (giải thích rõ):**
  - **Mưa đột xuất (`L4`):** bằng `0/39` trên review kho ứng dụng, nhưng xuất hiện ở `P2` (mất 10 phút đổi vào khu trong nhà) → chứng tỏ review app thiên về lỗi kỹ thuật, còn phỏng vấn bắt được tình huống thực địa.
  - **Giới hạn phạm vi pain (`P2`, `P4`):** `P4` đi Suối Tiên 3 lần/năm đã quen đường nên không bị vỡ lịch; `P2` không có trẻ nhỏ vẫn thấy chờ cáp treo là khó chịu nhất → xác nhận giải pháp **hữu ích nhất cho gia đình lần đầu / ít đi (1–2 lần/năm) tới khu vui chơi quy mô lớn** (VinWonders, Sun World), đúng với lát cắt đã chọn.

## 5. Kết luận

Giả thuyết ở `evidence/hypothesis.md`: **ĐÚNG** ở cả hai nguồn kiểm chéo — Đào data đạt **11/39 (28.2%)** ở VinWonders và **3/10 (30.0%)** ở Sun World Hạ Long (vượt ngưỡng 15–20%), Phỏng vấn đạt **2/3 gia đình có trẻ nhỏ** gặp pain trực tiếp (và **2/2** nhóm không trẻ nhỏ gặp lỡ show/mưa).
- **Điều đã tinh chỉnh từ phỏng vấn:** Thời gian chuẩn bị + xoay xở thực tế của gia đình có trẻ nhỏ gặp pain là **40–55 phút (trung bình ~47,5 phút)**, thấp hơn mức tự ước tính 60 phút ban đầu → cập nhật về **45 phút** trong công thức Impact ở `spec.md` §2.
- **Điều vẫn chưa biết:** Mức độ sẵn sàng dùng công cụ lập lịch trên điện thoại ngay trong lúc đang đi bộ cùng trẻ nhỏ (sẽ kiểm thêm nếu làm phần bonus người dùng thử ở CP4).
