# AI SPEC — Lịch trình 1 ngày ở khu vui chơi · Nhóm ApexFour · Lớp L3A

> Mốc nộp: §7 chốt chuẩn "đạt" tại **CP2 19:30 Thứ Sáu 27/11** · §0–§7 nộp **CP3 10:00 Thứ Bảy 28/11** · đủ §0–§10 **CP4 14:30 Thứ Bảy 28/11** · §10 changelog ghi tiếp đến **23:59 Thứ Bảy 28/11**.
> Đầu mỗi mục ghi bước guide (`02-guide.md` trong repo đề) chỉ cách điền. Mỗi mục ngắn, có số và nguồn; chi tiết để ở file được trỏ tới. Xoá dòng hướng dẫn trong ngoặc vuông khi điền xong.

Track: [ ] A · [ ] B · [x] C · [ ] D · [ ] E — bài toán: C1 · Lịch trình một ngày ở khu vui chơi thoả ràng buộc (giờ mở cửa, lịch show, độ tuổi trẻ nhỏ, thời tiết, ngân sách)
Data BTC cấp đã dùng (nếu có — không commit nguyên file): Không dùng (Track C nhóm tự thu review công khai cho `evidence/` và tự dựng dữ liệu khu vui chơi có seed cho `data/`)

## §0. Hiện tại việc này diễn ra thế nào *(guide 1.1)*
- Luồng hiện tại của việc này trên thực tế (3–5 bước):
  1. Trước ngày đi, phụ huynh/trưởng nhóm mở website hoặc app khu vui chơi (vd VinWonders, Sun World), tải ảnh bản đồ phân khu dạng tĩnh và xem bảng lịch biểu diễn trong ngày.
  2. Mở từng trang thông tin trò chơi để đọc quy định chiều cao/độ tuổi cho trẻ nhỏ và bảng giá vé cổng, vé combo ăn trưa, vé trò chơi/dịch vụ tính phí riêng.
  3. Tự ghi ra giấy/ghi chú điện thoại các điểm muốn đi, tự ước lượng thời gian đi bộ giữa các phân khu và tự cộng nhẩm tổng chi phí cho người lớn + trẻ em.
  4. Khi vào khu vui chơi gặp trời mưa, trò đóng bảo trì hoặc show đổi giờ thì phải đứng giữa đường mở lại bản đồ/lịch show để tìm điểm thay thế tại chỗ.
- Công cụ / AI đang được dùng cho việc này (nếu có) + nguồn: Website/app chính thức của khu vui chơi chủ yếu cung cấp bản đồ phân khu, danh sách điểm chơi và bảng giờ show cố định (chưa kiểm tính năng tự lập lịch cá nhân hoá theo ngân sách + ràng buộc gia đình có kiểm chứng giờ/giá tự động); người dùng tự hỏi ChatGPT/Gemini phổ thông thì hay gặp lỗi bịa giờ show, tính nhầm tổng tiền vé theo độ tuổi hoặc xếp lịch chồng giờ.

## §1. Người dùng & bằng chứng *(guide 1.1, 1.2)*
- Người dùng chính (một vai cụ thể): Phụ huynh trong gia đình có trẻ nhỏ (4–10 tuổi) lập kế hoạch đi khu vui chơi giải trí lớn trong 1 ngày.
- Việc họ cố làm xong (`động từ + đối tượng + bối cảnh`, không có chữ AI): Sắp xếp lịch trình tham quan, xem biểu diễn và ăn nghỉ khả thi cho cả gia đình có trẻ nhỏ trong một ngày tại khu vui chơi rộng lớn mà không vượt ngân sách hay trễ giờ mở cửa/giờ show.
- Hôm nay họ giải bằng gì, hỏng ở đâu, vì sao chưa bỏ: Đang tự đối chiếu bản đồ ảnh, bảng lịch show trên web/fanpage và ghi chú tay (hoặc hỏi kinh nghiệm trên hội nhóm review); cách này hỏng ở chỗ tốn nhiều thời gian tra chéo, dễ tính sót phí phụ thu/ăn uống, không kịp xoay xở khi mưa hoặc trễ 1 mắt xích làm vỡ cả dây chuyền buổi chiều — nhưng họ chưa bỏ vì chưa có công cụ nào kiểm sẵn ràng buộc giờ mở cửa, độ tuổi bé và ngân sách trên đúng dữ liệu khu vui chơi.
- Pain (KHÔNG chữ AI): Phụ huynh đưa gia đình có trẻ nhỏ đi khu vui chơi một ngày — đang tự tra bản đồ, lịch biểu diễn, giới hạn độ tuổi và giá dịch vụ ở nhiều nơi rời rạc để ghép lịch — vướng ở chỗ hàng chục điểm có giờ đóng/mở, giờ show cố định và thời gian di chuyển chồng chéo (hoặc mưa đột xuất) — hậu quả là mất hàng giờ chuẩn bị mà vẫn dễ lỡ show chính, đưa con tới trò không đủ điều kiện chơi, đi bộ vòng vèo mệt mỏi hoặc lố ngân sách.
- Bằng chứng — số chính + kết luận (chi tiết: `evidence/summary.md`): Đào **39 review tiếng Việt** (mọi mức sao, bài gốc ≥10 từ) trên Google Play ứng dụng VinWonders (`evidence/data-mining.md`): **11/39 (28.2%)** phản ánh trực tiếp vấn đề thuộc bài toán xếp lịch trình (bản đồ/di chuyển/tối ưu lộ trình `9/39 = 23.1%`, giờ show/thông báo giờ `2/39 = 5.1%`, chi phí/voucher `2/39 = 5.1%`, giới hạn độ tuổi/chiều cao trẻ em `1/39 = 2.6%`) — bước đầu vượt ngưỡng giả thuyết `≥15–20%`; đang phỏng vấn kiểm chéo 3 người dùng thật ngoài nhóm (`P1`–`P3`) trước CP3 để đo thời gian tự xếp lịch và tình huống mưa.

## §2. Impact & quyết định chọn *(guide 1.3)*

| Hướng | Bao nhiêu người gặp | Bao nhiêu lần / tháng | Mỗi lần tốn gì | Impact / tháng | Làm kịp không | Chọn? |
|---|---|---|---|---|---|---|
| **C1 · Xếp lịch trình 1 ngày ở khu vui chơi cho gia đình có trẻ nhỏ:** Phụ huynh đưa con nhỏ (4–10 tuổi) đi khu vui chơi rộng — tự tra bản đồ, lịch show, quy định tuổi và giá dịch vụ rời rạc — vướng giờ mở cửa/di chuyển chồng chéo hoặc mưa đột xuất — dễ lỡ show chính, đi bộ vòng vèo mệt trẻ hoặc vượt ngân sách | ~30.000 gia đình/nhóm khách/tháng tại 1 khu vui chơi lớn *(tự ước tính từ quy mô >1 triệu lượt khách/năm)* × **28.2%** gặp vướng lịch/bản đồ (`evidence/data-mining.md`) = **8.460 gia đình** | 1 chuyến / tháng đối với nhóm khách đi trong tháng đó *(tự ước tính)* | ~60 phút tra chéo trước chuyến + dò đường/đổi lịch tại chỗ *(tự ước tính, kiểm lại qua phỏng vấn P1–P3)*, kèm nguy cơ lỡ show chính trong vé ngày (~660k–880k/người) | **507.600 phút / tháng (~8.460 giờ / tháng)** trên 1 khu vui chơi; **60 phút / gia đình / tháng** | **Có** — dữ liệu chỉ đọc, kiểm tra ràng buộc bằng code rõ ràng, demo trọn trong 2 phút | **CHỌN** |
| **C2 · Tra cứu và tính phí đổi / nâng hạng phòng cho lễ tân khách sạn:** Lễ tân ca trực tại quầy — nhận yêu cầu đổi/nâng hạng phòng giữa kỳ nghỉ — phải dò tay bảng phòng trống, hạng thẻ và quy tắc phụ thu số đêm lẻ — khách chờ lâu ở quầy hoặc báo nhầm giá chênh phải đền | ~50 lễ tân tại 1 chuỗi khách sạn quy mô vừa *(tự ước tính)* | ~60 ca hỏi đổi phòng / lễ tân / tháng *(tự ước tính)* | ~10 phút tra phòng trống, chính sách & tính tay phí chênh mỗi ca *(tự ước tính)* | ~30.000 phút / tháng (~500 giờ / tháng) | Khó tiếp cận ≥3 lễ tân khách sạn thật trong 2 ngày để lấy bằng chứng đúng vai người dùng | **Loại** |
| **C3 · Giữ chỗ, đổi hoặc hoàn vé cho hành khách bị huỷ chuyến bay:** Hành khách (đặc biệt khi đi cùng con nhỏ) tại sân bay/trên app đặt vé — vừa nhận tin chuyến bay bị huỷ sát giờ — phải tự đọc quy định hoàn/đổi phức tạp và tìm chuyến thay thế — bấm nhầm làm mất lượt đổi miễn phí, kẹt tiền hoàn tới 90 ngày hoặc hết chỗ chuyến kế tiếp | ~5.000 hành khách gặp sự cố huỷ/đổi lịch bay / tháng trên 1 nền tảng *(tự ước tính)* | 1 lần / sự cố *(tự ước tính)* | ~45 phút tự tra cứu quy định và thao tác đổi/hoàn vé *(tự ước tính)*, rủi ro mất tiền vé nếu chọn nhầm thao tác không đảo được | ~225.000 phút / tháng (~3.750 giờ / tháng) | Ít gặp người vừa bị huỷ chuyến trong 1 tháng qua tại lớp để phỏng vấn; thao tác không đảo được phức tạp | **Loại** |

- **Impact / tháng của hướng chọn (C1):**
  - **Theo toàn khu vui chơi:** `8.460` gia đình gặp vướng/tháng *(30.000 gia đình/tháng tự ước tính × 28.2% tỷ lệ gặp pain từ `evidence/data-mining.md`)* × `1` lần/tháng *(tự ước tính)* × `60` phút/lần *(tự ước tính — cập nhật từ phỏng vấn P1–P3 trước CP3)* = **507.600 phút/tháng (~8.460 giờ/tháng)**.
  - **Theo từng người dùng (1 gia đình trong tháng có đi chơi — dùng để đối chiếu ở §8):** `1 lần × 60 phút = 60 phút/gia đình/tháng` (tương đương ~15.000đ–30.000đ giá trị thời gian chuẩn bị, chưa tính giá trị tránh lỡ show chính trong vé cổng 2,4–3,0 triệu đồng/gia đình).
- **Hướng ĐÃ LOẠI + vì sao (giữ lại):**
  - **C2 (Lễ tân đổi phòng):** Người dùng trực tiếp là lễ tân khách sạn chứ không phải khách lưu trú; trong 2 ngày nhóm không hẹn đủ ≥3 lễ tân thật (tránh bẫy Track C: chỉ lấy review khách mà người dùng là lễ tân).
  - **C3 (Chuyến bay bị huỷ):** Khó tìm đủ người dùng thật vừa bị huỷ chuyến bay trong 1 tháng gần đây ngay tại lớp để kiểm chứng sâu, đồng thời luồng giữ chỗ – đổi vé – hoàn vé có hành động không đảo được vượt quá phạm vi tối ưu nhất trong 10 giờ.
- **Số lần / tháng của từng kiểu người dùng (dùng cho persona ở `cost/personas.yaml` và §8):**
  - `xep_mot_lan` (khách đi chơi thông thường, lập lịch 1 lần trước chuyến đi): **1 phiên / tháng** *(tự ước tính)*.
  - `sua_nhieu_lan` (phụ huynh kỹ tính, đổi ngân sách/khung giờ/điểm chơi nhiều lần trước ngày đi): **3 phiên / tháng** *(tự ước tính)*.
  - `ngay_mua_xep_lai` (gia đình gặp mưa hoặc đóng trò đột xuất giữa ngày, cần xếp lại phần còn lại của ngày): **2 phiên / tháng** *(tự ước tính)*.

## §3. Giải pháp tương tự *(guide 2.1)*
- [sản phẩm / tính năng gần giống]: một điều đáng học · một điều đáng né · mình khác gì

## §4. Thiết kế *(guide 2.2, 3.2)*
- **Lát cắt MỘT CÂU** (1 người dùng · 1 việc · 1 quyết định AI · 1 kết quả):
- Không làm (≥3 điều):
- **Sơ đồ** (ảnh / Mermaid / draw.io): [chèn ở đây]
- **Hình dạng:** [ ] workflow cố định · [ ] một agent · [ ] nhiều agent — 2 dòng lý do, và vì sao **không** chọn hình dạng phức tạp hơn:
- **AI dựa vào đâu** — mỗi công cụ (khớp `codebase/tools.py`):

  | Công cụ | Input | Output | Tác động ra ngoài? |
  |---|---|---|---|
  |  |  |  |  |

- **Mức tự động:** [ ] AI gợi ý, người quyết · [ ] AI tự làm khi chắc, chuyển người khi không · [ ] AI tự làm — lý do (sai thì ai chịu gì, sửa đắt hay rẻ):
- **Chỗ chặn rủi ro** (rủi ro lớn nhất của lát cắt bị chặn ở đâu, bằng gì):
- **Chỗ người duyệt** (việc AI không được tự làm):
- **Nguyên tắc thiết kế** (≥3, bắt buộc G10):

  | Nguyên tắc | Chỗ cụ thể trên sơ đồ / trong bản chạy thử |
  |---|---|
  | G10 — thu hẹp phạm vi khi không chắc |  |
  |  |  |
  |  |  |

- Phần nào còn giả (công cụ trả dữ liệu giả, model chế độ giả…) — ghi rõ, không giả làm thật:

## §5. Chỗ khó — 4 lớp + ≥6 kịch bản + 2 tấn công *(guide 2.3)*

| Kịch bản | Lớp (1–4) | Hành vi mong muốn (nói gì, hiện gì, cho làm gì tiếp) | Câu thử |
|---|---|---|---|
|  |  |  |  |
| *(tấn công)* |  |  |  |
| *(tấn công)* |  |  |  |

(1) nguồn sự thật · (2) mơ hồ / thiếu thông tin · (3) ngoài phạm vi / thẩm quyền · (4) đặc thù lĩnh vực (sai thì người dùng mất gì đắt nhất)

## §6. Bốn đường đi của trải nghiệm
- Mọi thứ suôn sẻ: · Không chắc (lớp 2): · Không có căn cứ (lớp 1): · Người dùng sửa:
- Bị đòi ngoài phạm vi (lớp 3): · Trường hợp đặc thù lĩnh vực (lớp 4):

## §7. Đánh giá & chuẩn "đạt" *(guide 2.4, 4.1)*
- Data card: `data/DATA_CARD.md` · bộ câu thử: `eval/benchmark.csv` — __ câu (thuong __ · kho __ · tu_choi __) · metric: `eval/metric_spec.yaml` (__ metric)
- **Chuẩn "đạt"** (chốt **trước 19:30 Thứ Sáu 27/11**, giữ nguyên đến 23:59 Thứ Bảy 28/11): "Đạt khi ≥ __% câu qua, và __"
- Kết quả: lượt 1 __/__ (__%) · lượt 2 __/__ (__%) — run ID: __ / __ → chi tiết `eval/report.md`, hồ sơ `eval/README.md`

## §8. Chi phí khi dùng thật *(guide 4.2)*
- Persona + giá: `cost/personas.yaml` · lượt mô phỏng: `cost/simulate-__.csv` (__ phiên)
- Chi phí / task thành công: __ (model __) · __ (model __)
- Chi phí / tháng ở quy mô thật: thấp __ · cơ sở __ · cao __ → chi tiết `cost/cost-estimate.md`
- So với impact / người / tháng (§2): đáng làm không, vì sao:

## §9. Rủi ro & an toàn
- Dữ liệu: đã ẩn danh gì, không thu gì, không đưa gì vào model gói miễn phí:
- AI **không được** làm gì kể cả khi người dùng yêu cầu:
- Ai có thể bị hại nếu AI sai, và nhóm chặn thế nào:

## §10. Phân công & changelog
- Phân công có tên (theo chặng, chia cặp — guide "Cách chia việc"): __
- Dùng AI vào việc gì (2–3 dòng; chi tiết `docs/ai-usage.md`):
- Nhật ký thay đổi — **mọi thay đổi sau CP2 19:30 Thứ Sáu 27/11 phải có dòng ở đây**:

**CP2 → CP4** (vd thu hẹp lát cắt, hỏi thêm người dùng, lần cải tiến trước lượt 2)

| Thời điểm | Đổi gì | Vì sao (trỏ về câu thử / lỗi / bằng chứng nào) |
|---|---|---|
|  |  |  |

**Sau CP4 (đến 23:59 Thứ Bảy 28/11)** (sửa theo góp ý — không sửa chuẩn "đạt", câu thử, số bằng chứng, kết quả các lượt đã chạy)

| Thời điểm | Đổi gì | Vì sao |
|---|---|---|
|  |  |  |
