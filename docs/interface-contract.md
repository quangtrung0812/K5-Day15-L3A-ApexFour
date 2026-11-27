# Hợp đồng dữ liệu và công cụ CP2

Bình cung cấp dữ liệu SunWonder Mẫu, Hưng viết các công cụ và Trung phụ trách luồng gọi chúng trong agent. Các công cụ chỉ đọc dữ liệu và ghi trace qua `@tool`. [Dữ liệu mô phỏng](../data/park_data.json) · [Data card](../data/DATA_CARD.md)

## Dữ liệu

| Trường JSON | Nội dung |
|---|---|
| `park_hours`, `ticket_prices` | Giờ mở/đóng cửa và vé cổng theo nhóm tuổi, tính bằng VND. Trẻ dưới 4 tuổi dùng mức toddler. |
| `zones`, `walk_minutes` | Mã khu và ma trận số phút đi bộ theo chiều từ khu xuất phát tới khu đích. |
| `attractions` | Mỗi điểm có `id`, `name`, `zone`, `open_time`, `close_time`, `duration_min`, `maintenance`, `indoor`, `min_age` và phụ thu người lớn/trẻ em. |
| `shows` | Mỗi suất có mã riêng, `start_time`, `end_time`, `cancelled_on_rain`, phân khu, điều kiện tuổi, trong/ngoài trời và phụ thu. |
| `weather_by_date` | Dự báo từng ngày ISO, gồm `summary`, `rain_from`, `rain_to` và `outdoor_ok`. Hai mốc mưa bằng null khi dự báo khô ráo. |

## Năm hàm trong `codebase/tools.py`

| Lời gọi | Kết quả |
|---|---|
| `tra_diem_choi(khu=None, do_tuoi_tre_em=None, trong_nha_only=False, *, bao_gom_bao_tri=False)` | Danh sách điểm theo mã khu, tuổi hoặc danh sách tuổi và điều kiện trong nhà. Bật `bao_gom_bao_tri` để tra trạng thái khi khách hỏi một điểm đang đóng. |
| `tra_lich_show(ngay)` | Danh sách suất có thêm `ngay` và cờ `huy`. Ngày chưa có dữ liệu trả danh sách rỗng. |
| `tra_thoi_tiet(ngay)` | Trả `ngay`, `co_du_lieu` và các trường dự báo nếu có. Hai công cụ tra ngày nhận chuỗi YYYY-MM-DD. |
| `uoc_thoi_gian_di(diem_a, diem_b)` | Nhận hai ID điểm hoặc show. Trả số phút, 0 nếu trùng điểm, hoặc `None` nếu thiếu điểm/tuyến. |
| `kiem_lich_trinh(lich_trinh, so_nguoi_lon, so_tre_em, tuoi_tre_em, ngan_sach, thoi_tiet, *, khung_gio=None, show_da_huy=(), chieu_cao_tre_em=None)` | Trả `hop_le`, danh sách lỗi có mã `loi`, `tong_tien`, phụ thu từng mục trong `chi_tiet` và `tien_ve_cong` khi tính được. Tổng tiền chưa tính được là `None`. |

Mỗi mục lịch dùng dạng `{"diem_id": "A01", "bat_dau": "09:00", "ket_thuc": "09:40"}`. Tuổi được truyền theo từng trẻ, nhóm chỉ có người lớn dùng danh sách rỗng. Agent truyền khung giờ chuyến đi cho bộ kiểm.

Bộ kiểm đối chiếu giờ mở cửa, thời lượng, giờ show, bảo trì, tuổi/chiều cao, thời gian đi bộ, thời tiết và ngân sách với dữ liệu. Khoảng thời gian bao gồm giờ bắt đầu và kết thúc ngay trước mốc cuối. Có thể bổ sung `mua_tu` vào thời tiết theo báo cáo của khách hoặc truyền các suất bị hủy qua `show_da_huy`. Tổng tiền gồm vé cổng và phụ thu từng mục.
