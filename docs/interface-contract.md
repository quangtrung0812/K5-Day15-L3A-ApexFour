# Hợp đồng dữ liệu & công cụ — Nhóm ApexFour (Track C · C1)

> File này chốt cứng cấu trúc `data/park_data.json` (Bình làm) và chữ ký 5 hàm `@tool` trong `codebase/tools.py` (Hưng làm) để khớp 100% với `codebase/agent.py` (Trung làm), ghép lúc 18:55 chạy ngay không sửa lại.

---

## 1. Cấu trúc `data/park_data.json` (Bình sinh có seed, nhãn `synthetic`)

Tên khu vui chơi dựng: **"SunWonder Mẫu"** (không dùng dữ liệu nội bộ thật của hãng).

```json
{
  "ten_khu_vui_choi": "SunWonder Mẫu",
  "seed": 42,
  "ve_cong": {
    "nguoi_lon": 750000,
    "tre_em": 550000,
    "ghi_chu": "Vé vào cổng trọn gói hầu hết trò cơ bản; một số trò VIP và bữa ăn có phụ thu riêng"
  },
  "cac_khu": ["Khu Biển", "Khu Cổ Tích", "Khu Phiêu Lưu", "Khu Ẩm Thực"],
  "diem_choi": [
    {
      "ma": "D01",
      "ten": "Thủy Cung Đại Dương",
      "khu": "Khu Biển",
      "loai": "tham_quan",
      "gio_mo": "09:00",
      "gio_dong": "17:30",
      "thoi_luong_phut": 60,
      "gia_nguoi_lon": 0,
      "gia_tre_em": 0,
      "tuoi_toi_thieu": 0,
      "trong_nha": true,
      "bao_tri": false,
      "mo_ta": "Thủy cung trong nhà mát mẻ, phù hợp trẻ nhỏ và tránh mưa"
    }
  ],
  "lich_show": [
    {
      "ma": "S01",
      "ten": "Show Cá Heo Thông Minh",
      "khu": "Khu Biển",
      "ngay_ap_dung": ["hom_nay", "cuoi_tuan", "ngay_mua"],
      "gio_bat_dau": "10:30",
      "gio_ket_thuc": "11:00",
      "gia_nguoi_lon": 0,
      "gia_tre_em": 0,
      "tuoi_toi_thieu": 0,
      "trong_nha": true,
      "trang_thai": "hoat_dong",
      "mo_ta": "Biểu diễn cá heo trong mái vòm"
    }
  ],
  "thoi_gian_di_bo_phut": {
    "Khu Biển|Khu Cổ Tích": 10,
    "Khu Biển|Khu Phiêu Lưu": 15,
    "Khu Biển|Khu Ẩm Thực": 8,
    "Khu Cổ Tích|Khu Phiêu Lưu": 12,
    "Khu Cổ Tích|Khu Ẩm Thực": 7,
    "Khu Phiêu Lưu|Khu Ẩm Thực": 10
  },
  "thoi_tiet": {
    "hom_nay": {
      "ngay": "hom_nay",
      "tom_tat": "Sáng nắng nhẹ, chiều mát, không mưa",
      "khung_gio_mua": [],
      "canh_bao": "Thời tiết thuận lợi cả trong nhà và ngoài trời"
    },
    "ngay_mua": {
      "ngay": "ngay_mua",
      "tom_tat": "Sáng nắng nhẹ, mưa rào từ 14:00 đến 16:00",
      "khung_gio_mua": [["14:00", "16:00"]],
      "canh_bao": "Không xếp điểm/show ngoài trời trong khung 14:00-16:00"
    }
  }
}
```

**Gợi ý gài bẫy tối thiểu trong `park_data.json` (15–20 mục):**
- ≥2 điểm đặt `bao_tri: true` (kiểm tra AI không xếp vào điểm đang đóng bảo trì).
- ≥3 điểm cảm giác mạnh đặt `tuoi_toi_thieu: 10` hoặc `12` (kiểm tra ràng buộc trẻ nhỏ 4–8 tuổi).
- Có đủ điểm `trong_nha: true` và `trong_nha: false` (kiểm tra kịch bản mưa từ 14:00–16:00).
- Có ≥2 điểm ăn uống/dịch vụ VIP có `gia_nguoi_lon > 0` (kiểm tra ràng buộc ngân sách sát).
- Có ≥3 suất show cố định giờ (sáng, đầu chiều, cuối chiều) trong đó ≥1 show ngoài trời.

---

## 2. Chữ ký 5 hàm `@tool` trong `codebase/tools.py` (Hưng code)

Tất cả 5 hàm đều gắn `@tool` từ `tracing`, **chỉ đọc / tính toán bằng code, KHÔNG tác động ra ngoài**.

| # | Tên hàm & chữ ký | Kiểu trả về chuẩn |
|---|---|---|
| 1 | `tra_diem_choi(khu: str = "", do_tuoi_tre_em: int | None = None, trong_nha_only: bool = False) -> list` | `list[dict]` các điểm trong `diem_choi` thoả bộ lọc (nếu `khu=""` lấy mọi khu; vẫn giữ hoặc ghi rõ điểm `bao_tri` để báo khách khi khách hỏi đích danh). |
| 2 | `tra_lich_show(ngay: str = "hom_nay") -> list` | `list[dict]` các show áp dụng cho `ngay`. |
| 3 | `tra_thoi_tiet(ngay: str = "hom_nay") -> dict` | `{"ngay": str, "tom_tat": str, "khung_gio_mua": [[str, str], ...], "canh_bao": str}`. |
| 4 | `uoc_thoi_gian_di(diem_a: str, diem_b: str) -> dict` | `{"tu": str, "den": str, "phut": int}` (chấp nhận cả mã điểm `D01` lẫn tên khu `"Khu Biển"`, cùng khu trả `phut: 5`). |
| 5 | `kiem_lich_trinh(lich_trinh: list, so_nguoi_lon: int, so_tre_em: int, tuoi_tre_em=None, ngan_sach: int = 0, thoi_tiet: dict | None = None) -> dict` | `{"hop_le": bool, "vi_pham": list[str], "tong_tien": int, "chi_tiet_tien": {"ve_cong": int, "phu_thu_va_an_uong": int, "tong_tien": int}}`. |

### Quy tắc kiểm tra cứng trong `kiem_lich_trinh` (chạy hoàn toàn bằng Python code)
Mỗi phần tử trong `lich_trinh` có dạng: `{"ma": "D01", "bat_dau": "09:00", "ket_thuc": "10:00"}`.
Hàm phải kiểm tra đủ **6 điều kiện**:
1. **Tồn tại & bảo trì:** `ma` có trong `diem_choi` hoặc `lich_show` không; `bao_tri` có phải `True` hoặc `trang_thai != "hoat_dong"` không.
2. **Giờ mở cửa / giờ show:** `bat_dau >= gio_mo` và `ket_thuc <= gio_dong` (với show: khớp đúng `gio_bat_dau` và `gio_ket_thuc`).
3. **Chồng giờ & thời gian di chuyển:** mục sau có `bat_dau >= muc_truoc.ket_thuc + uoc_thoi_gian_di(muc_truoc, muc_sau)["phut"]`.
4. **Độ tuổi trẻ em:** nếu `so_tre_em > 0` và có `tuoi_tre_em` (int hoặc list int), mọi mục phải có `tuoi_toi_thieu <= min_tuoi`.
5. **Thời tiết mưa:** nếu `thoi_tiet["khung_gio_mua"]` không rỗng, không có mục nào `trong_nha == False` giao với khung giờ mưa.
6. **Ngân sách:** `tong_tien = ve_cong_nl * so_nguoi_lon + ve_cong_te * so_tre_em + sum(phu_thu)` phải `<= ngan_sach` (khi `ngan_sach > 0`).
