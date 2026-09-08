# Manhua Gallery

Trang web gallery xem bộ sưu tập manhua/artwork — dark theme, grid responsive, lightbox xem ảnh phóng to với điều khiển bàn phím.

## Chạy local

Không cần build. Chọn 1 trong 2 cách:

```bash
# Cách 1: Python
python3 -m http.server 8080
# mở http://localhost:8080

# Cách 2: Node
npx serve .
```

Hoặc mở trực tiếp `index.html` bằng trình duyệt.

## Thêm ảnh mới

1. Đặt file ảnh vào thư mục `images/`.
2. Thêm 1 dòng vào mảng `IMAGES` trong `js/app.js`:

```js
{ src: "images/ten-anh.png", title: "Manhua #5", tag: "portrait", note: "Ghi chú tùy ý" },
```

`tag` dùng cho bộ lọc: `portrait` (dọc) hoặc `landscape` (ngang).

## Cấu trúc

```
manhua/
├── index.html      # Trang chủ
├── css/style.css   # Giao diện (dark theme, grid, lightbox)
├── js/app.js       # Logic: render gallery, lọc, lightbox, phím tắt
└── images/         # Ảnh gốc
    ├── capture2.png
    ├── capture3.png
    ├── capture4.png
    └── capture5.png
```

## Tính năng

- Grid responsive, hiệu ứng hover
- Lọc theo tỉ lệ ảnh (dọc/ngang)
- Lightbox: phóng to, ảnh trước/sau, phím `←` `→` `Esc`
- Hỗ trợ keyboard access (Tab + Enter trên từng card)
