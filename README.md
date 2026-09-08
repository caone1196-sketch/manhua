# Tarot Studio — Xưởng thiết kế lá bài Tarot

Trang web quản lý & xuất lá bài tarot từ các artwork đã vẽ:

- **Artwork** — thư viện ảnh gốc (xem chi tiết trong lightbox)
- **Thiết kế bài** — ghép khung cho artwork:
  - 4 khung: Kinh điển, Huyền bí, Hoàng gia, Tối giản
  - Đặt tên + số La Mã (có sẵn 22 Major Arcana để chọn nhanh)
  - Ảnh "cắt vừa khung" hoặc "giữ nguyên tỉ lệ"
  - Preview canvas thời gian thực, tỉ lệ chuẩn tarot 70 × 120 mm
  - **Xuất PNG 1050 × 1800 px** · **Lưu vào bộ bài**
- **Bộ bài** — các lá đã hoàn thiện (lưu localStorage, bấm để mở lại, xóa được)
- **Trải bài** — trải ngẫu nhiên 3 lá (Quá khứ / Hiện tại / Tương lai) với hiệu ứng lật 3D

## Chạy local

Không cần build:

```bash
python3 -m http.server 8080
# mở http://localhost:8080
```

## Thêm artwork mới

1. Đặt file vào `images/`.
2. Thêm 1 dòng vào `ARTWORK` trong `js/cards.js`:

```js
{ src: "images/anh-moi.png", label: "Artwork 05" },
```

## Thêm khung bài mới

Thêm vào `FRAMES` trong `js/cards.js`:

```js
newframe: { name: "Tên khung", bg: "#0f1420", border: "#d4af37", text: "#ead9a6" },
```

## Cấu trúc

```
manhua/
├── index.html          # Bố cục 4 tab + lightbox
├── css/style.css       # Giao diện (dark theme, vàng gold, hiệu ứng lật)
├── js/cards.js         # Dữ liệu: artwork, khung bài, Major Arcana
├── js/card-render.js   # Engine vẽ lá bài lên canvas (dùng chung)
├── js/composer.js      # Tab Thiết kế: preview, xuất PNG, lưu bộ bài
├── js/app.js           # Tabs, artwork, lightbox, bộ bài, spread
└── images/             # Artwork gốc (capture2-5.png, the-star.png)
```
