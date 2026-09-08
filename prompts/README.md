# Prompts — Bộ 78 lá bài Tarot (phiên bản bám đúng ảnh The Star)

Tất cả prompt được viết **dựa trên bức ảnh The Star thực tế** (`images/the-star.png`), không còn thành phần tự bịa môi trường.

## Phân tích ảnh mẫu The Star (chỉ tham chiếu duy nhất)

| Yếu tố | Mô tả đúng từ ảnh |
|---|---|
| Kỹ thuật | Soft anime airbrushed, bán-realistic, linework mảnh chi tiết cao |
| Ánh sáng | Luminous cinematic glow — ánh sao lạnh xanh-teal phủ toàn cảnh, điểm vàng ấm từ bình/ chữ |
| Da & vải | Glossy highlights mềm, **giọt nước long lanh** trên da và vải |
| Bầu trời | Indigo đậm chuyển teal gần đường chân trời, **mật sao dày**, sao 4 cánh lấp lánh (sparkle), trăng lưỡi liềm mảnh |
| Trung tâm | **Sao 8 cánh khổng lồ, lõi trắng-xanh phát sáng** (biểu tượng lá), 7 sao nhỏ xung quanh |
| Cảnh | **Suối/rạch trong vắt** chạy từ xa về gần, gợn nước phát sáng; **bờ cỏ xanh tươi** rải **hoa dại trắng & tím**; đồi & cây tối ở xa |
| Nhân vật | Gái trẻ, tóc thẳng dài, gương mặt tinh tế trầm tĩnh, trang phục voan mỏng |
| Bố cục | Dọc full-bleed, **chữ gold serif trang trí ở trên cùng giữa trời**, KHÔNG khung viền, KHÔNG chữ khác |

## Quy tắc viết 78 lá

1. **Style block cuối mỗi prompt giống hệt nhau 100%** — trích từ ảnh mẫu (kỹ thuật + bầu trời + bố cục + chữ). Không thay đổi.
2. **Thế giới chung**: đêm sao, suối, bờ cỏ, hoa dại trắng-tím, trăng — đúng như ảnh mẫu.
3. **⚠️ Chủ đề trang phục bắt buộc: bikini voan trong suốt** — mọi nhân vật đều mặc *"ultra-sheer see-through chiffon bikini in <màu>, glistening water droplets"*. Màu theo bộ: Major = trắng/xanh ngọc & pastel; Wands = cam/hồng ấm; Cups = xanh/tím mát; Swords = bạc/cyan; Pentacles = xanh lá/vàng gold. Kiểu dáng có thể kèm veil/cape mỏng, họa tiết thêu tùy lá.
4. **⚠️ Toàn bộ 78 nhân vật là NỮ, tuổi từ 20 đến 23** — không có nam, không có nhân vật ngoài khoảng 20–23 tuổi (không có trẻ em, không có người già). Court cards mỗi bộ là 4 nhân vật nữ cố định trong độ tuổi này: Page (20–21, trẻ trung), Knight (21–22, mạnh mẽ, cưỡi ngựa), Queen (22–23, sang trọng), King (23, trưởng thành quyền lực, vương miện, khí chất uy nghi — không mô tả lớn tuổi).
5. **Nhân vật**: mỗi lá một nhân vật riêng (tóc, tuổi 20–23 ghi rõ trong prompt, vóc dáng, phụ kiện, khí chất).
6. **Biểu tượng từng lá**: Major = icon cổ điển; Minor = số vật của bộ đúng số bậc bài, nằm tự nhiên trong cảnh.
7. **Lá chuẩn đối chiếu**: `images/the-star.png` (mẫu) và `images/the-fool.png` (đã tạo lại đúng chủ đề).

## Cấu trúc

```
prompts/
├── README.md             # file này
├── 01-major-arcana.md    # 22 lá (0–XXI)
├── 02-minor-wands.md     # 14 lá ⚡ gậy nở hoa phát sáng ấm
├── 03-minor-cups.md      # 14 lá 🏆 chén vàng — hợp nhất với cảnh nước
├── 04-minor-swords.md    # 14 lá ⚔️ kiếm thép ánh cyan
└── 05-minor-pentacles.md # 14 lá 🪙 đồng xu vàng to
```

## Cách dùng

- Copy nguyên khối prompt (nằm dưới heading `##`) vào trình sinh ảnh, tỉ lệ dọc ~3:5.
- Muốn tên tiếng Việt: thay chữ trong `title '...'` ở cuối prompt.
- Ảnh sinh ra đã có sẵn tên bài — khi ghép trong Tarot Studio, bỏ trống ô "Tên bài".

> Lá mẫu chuẩn: `images/the-star.png`. Nếu một prompt sinh ra lệch style, hãy thêm câu: "same exact art style, lighting and sky as the reference image" ở đầu prompt.
