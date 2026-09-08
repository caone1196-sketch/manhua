# Manhua — Dark Fantasy Tarot

Bộ bài tarot chủ đề **dark fantasy**, lấy lá **XV The Devil** (bản Rider-Waite-Smith 1909, public domain) làm mẫu phong cách: khung viền cổ điển, dải số La Mã trên nền sáng, tông giấy cũ sepia ấm, đường mực lithograph đầu thế kỷ 20.

## 6 lá mẫu (đợt 1)

| Tệp | Lá | Mô tả ngắn |
|---|---|---|
| `cards/major_00_the_fool.png` | 0 · The Fool | Kẻ lang thang gầy tái bước khỏi vách đá sụp đổ, chó đen u hồn, bông hồng gai |
| `cards/major_01_the_magician.png` | I · The Magician | Phù thủy gộc sau bàn thờ đá, vô cực vàng, 4 pháp khí bằng hắc diện thạch & xương |
| `cards/major_13_death.png` | XIII · Death | Kỵ sĩ xương tàn cưỡi ngựa xác chết, cờ đen hoa hồng trắng, vua ngã xuống |
| `cards/major_15_the_devil.png` | XV · The Devil | **Lá mẫu** (RWS 1909 gốc) |
| `cards/major_16_the_tower.png` | XVI · The Tower | Tháp gothic bị tia chớp đen bổ đôi, lửa xanh lục, vương miện rơi |
| `cards/major_18_the_moon.png` | XVIII · The Moon | Mặt trăng mặt người, sói đen & chó trắng tru, quái giáp xác bò từ ao đen |
| `cards/major_19_the_sun.png` | XIX · The Sun | Nhật thực đen vầng hào quang, đứa trẻ u hồn cưỡi ngựa trắng, hướng dương héo úa |

Xem trước toàn bộ: `cards/preview_contact_sheet.png`

## Cấu trúc

```
cards/
├── major_15_the_devil.png      # lá mẫu (template) — RWS 1909
├── major_00_the_fool.png       # tạo mới — dark fantasy
├── major_01_the_magician.png
├── major_13_death.png
├── major_16_the_tower.png
├── major_18_the_moon.png
├── major_19_the_sun.png
└── preview_contact_sheet.png   # bảng tổng duyệt phong cách
```

Quy ước đặt tên: `major_<số>_<tên_lá>.png` — theo đúng cách đặt tên `major_15_the_devil.png`.

## Kế hoạch

- ✅ Đợt 1: 6 lá mẫu để duyệt phong cách
- ⏳ Đợt 2: 16 lá Major Arcana còn lại (02 High Priestess → 21 The World) sau khi chốt phong cách
- ⏳ Tùy chọn: lưng bài (card back) thống nhất cho cả bộ
