# STYLE LOCK — Luật đồng bộ toàn bộ Tarot (dựa trên lá THE STAR mẫu)

> Mục tiêu: mọi lá bài nhìn vào là biết **cùng 1 bộ bài, cùng 1 linh hồn nhân vật**, chỉ khác
> khí chất / tóc / mắt / đạo cụ / biểu tượng theo ý nghĩa từng lá.

## 1. LOCKED — KHÔNG được thay đổi giữa các lá

| Nhóm | Mô tả khóa (copy nguyên văn vào mọi prompt) |
|---|---|
| Chất liệu tranh | `semi-realistic digital painting, high-end fantasy card art, painterly realism, classical fantasy illustration` |
| Vẻ đẹp | `elegant idealized human beauty, realistic but stylized anatomy, realistic proportions with subtle fantasy beautification, softly rendered facial features, refined delicate face, natural hands and fingers` |
| **Da (LOCKED)** | `smooth luminous fair ivory skin, SAME SKIN TONE AS THE STAR REFERENCE, unchanged skin color` — **màu da giữ nguyên 100% mọi lá** |
| Trang phục gốc | `elegant ivory-white and champagne silk ceremonial fantasy gown, layered silk chiffon, translucent outer layers, softly flowing fabric, delicate semi-transparent veils layered over opaque inner fabric, soft Renaissance-inspired drapery, fitted bodice with intricate antique-gold edging, fine gold embroidery, ornamental gold cords, thin gold waist belt, central antique-gold ornament, long vertical decorative gold chain, luxurious fabric texture` — chỉ được thêm áo choàng/veil ngoài MỜ theo lá, không đổi màu nền váy |
| Trang sức gốc | `thin gold armlets, delicate bracelets, pearl necklace, small antique-gold pendant, subtle fantasy jewelry, elegant and refined rather than excessive` |
| Bối cảnh | `enormous dark gothic fantasy cathedral city at night, tall narrow Gothic towers and pointed spires, dark stone architecture, violet and purple illuminated windows, deep midnight-blue sky, tiny scattered stars, violet atmospheric mist, massive carved Gothic stone pillars on the extreme left and right edges creating a cathedral portal` |
| Tiền cảnh | `shallow mirror-like ceremonial pool, dark reflective water, circular ancient stone platform beneath the figure, multiple concentric engraved rings, subtle geometric sacred patterns, wet black-violet stone, reflections, small circular ripples, thin mist hovering over the surface` |
| Ánh sáng | `semi-realistic fantasy cinematic lighting, warm golden backlight, cool midnight-blue ambient light, soft violet reflected light, gentle rim light around hair and shoulders, soft highlights on wet skin and silk, subtle bloom, volumetric golden rays, deep cinematic shadows, soft painterly transitions, luminous atmosphere` |
| Palette nền | `deep midnight blue, indigo, dark violet, royal purple, antique gold, bronze, ivory white, champagne, soft silver highlights, warm celestial gold` |
| Bố cục | `strict central symmetry, perfect bilateral balance, woman exactly centered, matching props on both sides, matching Gothic pillars, large reflective foreground, strong vertical hierarchy, clean readable silhouette, elegant negative space, majestic sacred atmosphere` |
| Trình bày lá bài | `full-bleed artwork, vertical portrait card, absolutely no frame, no border, no edge vignette, no title panel, no text box, no plaque, no dark banner, artwork bleeding fully to all edges, only the card name floating directly over the artwork at the bottom, large centered antique-gold serif typography, elegant classical Roman capitals, engraved metallic gold appearance, clean readable lettering` — **KHÔNG khung viền, KHÔNG khung chữ, chỉ giữ tên lá bài** |

## 2. VARIABLE — Được phép thay đổi theo từng lá

1. **Màu + kiểu tóc** — mỗi lá 1 màu/kiểu riêng (ghi rõ trong prompt).
2. **Màu + ánh mắt** — mỗi lá 1 màu/biểu cảm riêng (ví dụ: nhắm thiền, nhìn thẳng, ngước lên...).
3. **Tư thế** — đứng / ngồi / quỳ / treo ngược / nhảy múa, nhưng LUÔN chính diện, đối xứng.
4. **Vật cầm / đạo cụ** — đối xứng 2 bên (2 bình, 2 chén, 2 gậy, kiếm + cân...).
5. **Vật trang trí đầu** — vương miện / vòng nguyệt / sừng / khăn trùm... theo ý nghĩa lá.
6. **Biểu tượng trung tâm khổng lồ phía sau** — ngôi sao / mặt trăng / mặt trời / bánh xe...
7. **1–2 màu điểm nhấn riêng** của lá (accent) cộng thêm vào palette nền.
8. **Chữ tiêu đề** — tên lá bài viết HOA (THE FOOL, THE MAGICIAN...).
9. **Cảm xúc tổng thể** — danh sách tính từ cuối prompt.

## 3. Quy tắc nhân vật nữ thống nhất

- Mọi lá đều là **adult ethereal woman** (kể cả THE EMPEROR, THE HIEROPHANT, THE HANGED,
  THE DEVIL... đều vẽ thành **phiên bản nữ tính hóa** nhưng giữ nguyên biểu tượng gốc).
- Không vẽ nam giới, không vẽ trẻ em, không vẽ thêm nhân vật phụ (ngoại lệ: thiên thần,
  bóng ma mờ, tượng đá, sư tử, nhân sư... làm phông nền/biểu tượng, không phải nhân vật chính).
- Dáng người thanh thoát, tư thế trang trọng, trang phục kín đáo:
  `opaque inner fabric` luôn có, veil chỉ phủ ngoài.

## 4. Negative prompt dùng chung (cho SD / Midjourney --no)

```
photorealistic, photo, 3d render, plastic skin, oversharpened, deformed hands,
extra fingers, fused fingers, asymmetrical composition, off-center, cropped head,
cropped feet, male figure, child, nude, exposed breasts, modern clothes,
white margin, parchment border, thick black frame, watermark, signature, blurry text,
misspelled text, double title, daytime, bright sky
```

## 5. Thông số gợi ý

- Tỉ lệ: **2:3 dọc** (`--ar 2:3`, SD: 768x1152 hoặc 832x1248)
- Midjourney: `--style raw --stylize 250 --v 6.1`
- SDXL: sampler DPM++ 2M Karras, steps 40, CFG 6.5, Denoise…. tuỳ
- Luôn giữ seed/style-reference từ lá THE STAR đầu tiên cho cả bộ.

## 6. EXPORT LOCK — Chuẩn xuất bản in final (🔒 ĐÃ CHỐT 2026-09-11, v2: 9:16 + AI upscale)

> Mọi lá khi chốt vào `tarot-final/` đều xuất kèm bản in theo chuẩn này.

| Thông số | Giá trị LOCKED |
|---|---|
| Tỉ lệ | **9:16 dọc** |
| Kích thước chuẩn (mặc định) | **1536 × 2752 px — PNG ~5.4MB** (AI x2, siêu lấy mẫu từ LapSRN x4) |
| Kích thước master (tùy chọn) | 3072 × 5461 px — PNG ~20MB (thêm `--width 3072 --height 5461`) |
| DPI | **300** (118.11 px/cm) → 1536×2752 in ~13×23 cm; 3072×5461 in ~26×46 cm |
| Định dạng | PNG lossless, sRGB (JPEG q90 ~2.4MB nếu ưu tiên dung lượng tối đa) |
| Sharpen | **max chi tiết**: `-unsharp 0x0.8+1.5+0.003` |

### 6.1 Pipeline (ĐÃ KIỂM CHỨNG — chạy bằng script trong repo)

**Bước 1 — Gen ở tỉ lệ 9:16 ngay từ prompt**: mọi prompt final mở đầu bằng:

```
OUTPUT FORMAT REQUIREMENT: render this image in a vertical 9:16 PORTRAIT
aspect ratio (width:height = 9:16, tall narrow phone-wallpaper shape);
absolutely NOT a square, NOT wide; compose everything to fit the tall 9:16 frame.
```

→ Output thật: **768×1376 px** (tỉ lệ 0.558 ≈ 9:16). Kiểm tra `identify` mỗi lần gen, sai tỉ lệ thì gen lại.

**Bước 2 — AI upscale + xuất in (một lệnh, script có sẵn trong repo):**

```bash
python3 tarot-final/tools/upscale-print.py INPUT.png tarot-final/NN-ten-la-1536x2752-300dpi.png
```

Script tự: LapSRN x4 AI (chia tile 2×3 overlap 32 chống seam) → resize chính xác kích thước đích
(mặc định **1536×2752**) + unsharp `0x0.8+1.5+0.003` (MAX CHI TIẾT) + metadata 300 DPI.
Bản master 3072×5461: thêm `--width 3072 --height 5461`.
Model `LapSRN_x4.pb` đã lưu sẵn tại `tarot-final/tools/models/` (nguồn: fannymonori/TF-LapSRN).
Cần `pip install opencv-contrib-python-headless` (kèm `--break-system-packages` nếu pip chặn).

- Tên file: `NN-ten-la-3072x5461-300dpi.png` trong `tarot-final/`.
- Mẫu kiểm chứng: `tarot-prompts/preview/print-9x16-maxdetail-3072x5461-300dpi.png` (+ sheet so sánh `compare-9x16-detail.png`).
- Bản cũ (7:12 crop 2 bên) KHÔNG dùng nữa; THE FOOL sẽ xuất lại khi chuyển 9:16.
