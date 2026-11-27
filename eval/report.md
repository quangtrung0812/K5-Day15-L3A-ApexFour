# Đánh giá CP4 · ApexFour

Hai lượt chính đối chiếu trên slide CP4 dùng cùng 25 đầu vào, tiêu chí đã chốt ở CP2 và `gpt-4o-mini`. Cột `pass` được kiểm tự động phần ràng buộc cứng bằng `eval/grade_helper.py` kết hợp thành viên nhóm (`Nguyễn Quang Trung`) rà soát từng tiêu chí văn bản. Các ghi chú từng câu nằm trong [run-2.csv](run-2.csv).

| Lượt | Run ID | Tổng | Thường | Khó | Từ chối |
|---|---|---:|---:|---:|---:|
| 1 | run-1@20261127-232511 | 9/25 · 36% | 0/8 | 5/13 | 4/4 |
| 2 | run-2@20261127-234939 | 10/25 · 40% | 1/8 | 5/13 | 4/4 |

Cả hai lượt dưới chuẩn 80%. Lượt 2 xuất lịch cho B01, B02, B20, B21. Kiểm lại bằng `grade_helper.py` cho thấy cả bốn lịch đạt ràng buộc cứng. Bộ kiểm sơ bộ đánh dấu 16/25 câu qua. Đối chiếu văn bản với tiêu chí từng câu loại thêm B01, B10, B12, B19, B20 và B24.

## Vì sao 16 câu trượt lượt 1?

| Nhóm lỗi chính | Số câu | Mã |
|---|---:|---|
| Không xuất được lịch khả thi sau bước lập hoặc sửa lịch | 11 | B01–B07, B16–B18, B23 |
| Hỏi lại thông tin khách đã nêu | 3 | B10, B12, B19 |
| Giải thích thiếu hoặc sai căn cứ | 2 | B20, B24 |

| Câu | Yêu cầu của gia đình | Phản hồi lượt 1 (tóm tắt) | Hệ quả |
|---|---|---|---|
| B01 | Hai người lớn và bé 6 tuổi, 3 triệu đồng, thích thủy cung | Bản nháp sau ba vòng tốn 3.270.000đ | Không đưa được lịch trong ngân sách. |
| B02 | Vườn thú và show tối ngày 28/11 | Báo bất khả thi và lo show S05 gặp mưa | Dữ liệu ngày đó báo nắng, gia đình bỏ lỡ hai điểm mong muốn. |
| B16 | Gia đình có 4 triệu đồng, đi chơi trong hai khu | Báo bất khả thi dù vé cổng là 3.080.000đ | Còn 920.000đ cho phụ thu mà gia đình vẫn không nhận được lịch. |

## Thay đổi và kết quả

Nhóm có 11 câu trượt vì thiếu lịch khả thi. Agent nay lấy tiền vé từ bộ kiểm và tính phần còn lại trước khi gọi model. Khi đủ tiền vé, model nhận một tuyến khởi đầu từ dữ liệu công viên để điều chỉnh theo sở thích và giờ show. Vẫn kiểm lại từng bản nháp bằng cùng bộ công cụ.

Trong 11 câu này, số câu có lịch tăng từ 0 lên 2 và số đạt toàn bộ tiêu chí tăng từ 0 lên 1. B02 xếp được vườn thú và show tối, tổng 3.800.000đ. B01 đã có lịch trong ngân sách nhưng ghi sai giới hạn tuổi A02 và thiếu lý do chọn tuyến đi gọn. Không có câu nào từ đạt chuyển sang trượt. B20 vẫn trượt và lần này còn gán giờ 18:30 cho điểm ngoài dữ liệu.

## Quyết định

Tiếp tục thử nghiệm. Chín câu vẫn thiếu lịch khả thi trong nhóm lỗi chính. Ưu tiên đặt trước suất show rồi ghép điểm chơi quanh các khung giờ trống. Kiểm lại phần giải thích về tuổi, giá và giờ với dữ liệu công viên trước khi hiển thị. Thử với phụ huynh để đo thời gian họ thực sự tiết kiệm.

Dấu vết từng lượt nằm ở `traces/run-1.jsonl` và `traces/run-2.jsonl`. Tái kiểm bằng `python eval/grade_helper.py eval/run-2.csv` và `python run.py score eval/run-2.csv`.

## Các lượt cải tiến cho demo HTML

| Lượt | Cách xếp lịch | Kiểm sơ bộ bằng code | Kết quả sau rà soát tiêu chí |
|---|---|---:|---|
| run-3@20261128-000708 | Model chọn mã điểm, Python xếp giờ và kiểm ngân sách | 25/25 | **20/25 (80%)** · `tu_choi` 4/4 (đạt chuẩn "đạt") |
| run-4@20261128-000944 | Bổ sung căn cứ cho tuổi, mưa, xung đột show, tên ngoài danh mục và giờ ăn tối | 25/25 | **22/25 (88%)** · `tu_choi` 3/4 (trượt `B01`, `B14`, `B22`) |

Ở lượt 3, B06, B07, B10, B20 và B23 qua kiểm sơ bộ nhưng trượt khi đối chiếu câu trả lời. Lượt 4 nêu giá vé của bé 3 tuổi, giải thích cách tránh mưa, chỉ ra 12 phút đi bộ giữa hai show, nhận diện hai điểm ngoài danh mục và xếp bữa tối B23 lúc 17:00. Người chấm có thể đọc nguyên văn từng đầu vào, tiêu chí và đầu ra trong [demo HTML](../demo.html).

Các lượt dùng lại 25 câu đã dùng để phát triển sản phẩm. Số liệu này chưa đo khả năng tổng quát hóa. Một số lịch còn khoảng trống dài giữa hai hoạt động, ví dụ B02 đợi từ sau bữa trưa tới show 19:30.
