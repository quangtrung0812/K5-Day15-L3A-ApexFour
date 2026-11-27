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
- Bằng chứng — số chính + kết luận (chi tiết: `evidence/summary.md`): *(Đang thu thập ở bước 1.2 từ review công khai Google Maps/Tripadvisor và phỏng vấn người dùng ngoài nhóm — cập nhật số thật ở CP2/CP3)*

## §2. Impact & quyết định chọn *(guide 1.3)*

| Hướng | Bao nhiêu người gặp | Bao nhiêu lần / tháng | Mỗi lần tốn gì | Impact / tháng | Làm kịp không | Chọn? |
|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |

- **Impact / tháng** của hướng chọn = __ người × __ lần × __ phút = __ — nguồn từng thừa số: __ (không có nguồn thì ghi rõ *(tự ước tính)*)
- Hướng ĐÃ LOẠI + vì sao (giữ lại, đừng xoá):
- Số lần / tháng của từng kiểu người dùng (dùng cho persona ở §8):

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
