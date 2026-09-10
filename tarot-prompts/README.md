# Bộ Prompt Tarot — 22 lá Major Arcana (phong cách THE STAR mẫu)

Bộ prompt đồng bộ, lấy lá **THE STAR** của bạn làm chuẩn Style-Lock:
cùng 1 mẫu nhân vật nữ, cùng váy ivory-champagne, cùng thành phố Gothic về đêm —
mỗi lá chỉ khác **màu/kiểu tóc, màu/ánh mắt, tư thế, đạo cụ, biểu tượng và chữ tiêu đề**.
**Màu da khóa cứng 100% mọi lá.**

## Cấu trúc thư mục

| File | Nội dung |
|---|---|
| `_STYLE-LOCK.md` | Luật khóa/mở: cái gì giữ nguyên, cái gì được đổi + negative prompt + thông số |
| `PART-1_FOOL-to-HIEROPHANT.md` | Lá 0 → V (kèm bảng biến đổi riêng từng lá) |
| `PART-2_LOVERS-to-JUSTICE.md` | Lá VI → XI |
| `PART-3_HANGED-to-STAR.md` | Lá XII → XVII (gồm prompt gốc THE STAR) |
| `PART-4_MOON-to-WORLD.md` | Lá XVIII → XXI |
| `cards/*.txt` | 22 file prompt thuần, mỗi lá 1 file, copy-paste trực tiếp |
| `prompts.json` | Toàn bộ 22 prompt dạng JSON (chạy batch / gọi API) |
| `MIDJOURNEY-GUIDE.md` | **Dùng ảnh THE STAR làm reference trong Midjourney (`--cref/--sref`)** |
| `midjourney/*.txt` | 22 lệnh `/imagine` build sẵn (bản kèm chữ + bản art sạch) |
| `ref/2.png` + `ref/2-mj-clean.png` | Ảnh reference gốc + bản đã cắt khung/chữ để nạp vào MJ |

## Danh sách 22 lá (biến đổi riêng)

| # | Lá | Tóc | Mắt |
|---|---|---|---|
| 0 | THE FOOL | vàng mật ong gợn sóng + hoa trắng | xanh hạt dẻ, vui tươi ngước lên |
| I | THE MAGICIAN | đen huyền thẳng + băng ouroboros | hổ phách, sắc sảo nhìn thẳng |
| II | THE HIGH PRIESTESS | đen xanh midnight + mạng bạc | xám bạc, khép hờ bí ẩn |
| III | THE EMPRESS | nâu đỏ đồng xoăn + hoa hồng/lúa | xanh lục bảo, hiền từ |
| IV | THE EMPEROR | bạch kim tết vương miện + mũ đế chế | xanh thép, uy nghi |
| V | THE HIEROPHANT | vàng tro búi + mũ 3 tầng | xám-xanh, ban phước |
| VI | THE LOVERS | vàng hồng 2 bím + nụ hồng | nâu-tím, âu yếm |
| VII | THE CHARIOT | đỏ đồng đuôi ngựa + nguyệt quế | xanh băng, quyết đoán |
| VIII | STRENGTH | cam-hoàng hôn bồng như bờm | hổ phách, hiền từ |
| IX | THE HERMIT | xám bạc + mũ trùm | xanh nhạt, khôn ngoan |
| X | WHEEL OF FORTUNE | nâu hạt dẻ + trâm bánh xe | tím-xanh, tiên tri |
| XI | JUSTICE | đen rẽ ngôi + vương miện cân | xám-xanh, sắc lạnh |
| XII | THE HANGED MAN | vàng nhạt buông ngược + hào quang | nhắm thiền an nhiên |
| XIII | DEATH | trắng tuyết + vương miện xương + mạng đen | tím-băng phát sáng |
| XIV | TEMPERANCE | vàng mềm + vòng nhật-nguyệt | xanh-xám, nhìn dòng nước |
| XV | THE DEVIL | đen-tím hoang dại + sừng cừu | đỏ ruby rực cháy |
| XVI | THE TOWER | vàng xám rối bão | xanh bão, sững sờ |
| XVII | THE STAR ★ | bạch kim-bạc (GỐC) | thiền (GỐC) |
| XVIII | THE MOON | trắng ánh trăng + vương miện lưỡi liềm | tím oải hương mơ màng |
| XIX | THE SUN | vàng rực + hoa hướng dương | nâu-hổ phách cười rạng rỡ |
| XX | JUDGEMENT | trắng-vàng bay lên + cánh mini | xanh da trời ngỡ ngàng |
| XXI | THE WORLD | nâu hạt dẻ + vòng nguyệt quế hành tinh | xanh-vàng vũ trụ viên mãn |

## Cách dùng nhanh

1. **Gen tay từng lá:** mở `cards/NN-ten-la.txt` → copy toàn bộ → dán vào Midjourney / SD / DALL-E.
2. **Gen đồng bộ cả bộ:** gen lá THE STAR trước cho ưng ý, rồi dùng ảnh đó làm
   `--cref` (Midjourney) / ControlNet-IP-Adapter (SD) cho 21 lá còn lại.
3. **Gen hàng loạt:** đọc `prompts.json` bằng script (mỗi object có `title` + `prompt`).
4. Tỉ lệ khuyên dùng: **2:3 dọc**. Negative prompt chung nằm trong `_STYLE-LOCK.md`.

## Ghi chú sáng tác

- Các lá vốn là nam (Emperor, Hierophant, Hanged Man, Magician, Devil, Hermit...)
  được vẽ thành **phiên bản nữ hóa** nhưng giữ nguyên đạo cụ/biểu tượng gốc,
  đúng yêu cầu "giữ mẫu nhân vật".
- Trang phục luôn có lớp vải opaque bên trong + veil phủ ngoài → kín đáo, thanh lịch.
- Lá THE DEVIL và DEATH giữ tông dark-fantasy nhưng không hở hang, không máu me.
