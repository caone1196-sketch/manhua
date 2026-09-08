import json

with open('tarot_cards_data.json', 'r', encoding='utf-8') as f:
    cards = json.load(f)

md_content = """# 🔮 BỘ PROMPTS 78 LÁ BÀI TAROT THEO PHONG CÁCH MANHWA (NGUỒN ẢNH: CAPTURE3.PNG)

> **Tài liệu tạo ảnh AI chuyên sâu:** Bộ 78 lá bài Tarot chuẩn Rider-Waite-Smith được chuyển thể nghệ thuật sang phong cách **Korean Adult Manhwa / Webtoon Digital Art** (dựa trên nguồn phong cách từ ảnh `Capture3.PNG`: nhân vật quyến rũ, nét vẽ sắc nét, bóng đổ mềm mại, da bắt sáng bóng bẩy, trang phục đan dây/ren cách điệu, ánh sáng tương phản rực rỡ và khung viền bài Tarot ma thuật).

---

## 🎨 1. PHÂN TÍCH & GIẢI MÃ PHONG CÁCH GỐC (STYLE DECODING TỪ CAPTURE3.PNG)

| Thành phần thị giác | Đặc điểm phân tích từ Capture3.PNG | Ứng dụng vào bộ bài Tarot |
| :--- | :--- | :--- |
| **Nét vẽ & Thể loại (Art Style)** | Korean Modern Webtoon / Adult Manhwa illustration (Toptoon, Lezhin style). | Đường nét viền rõ nét (crisp clean lineart), kết hợp gradient shading và cell shading mượt mà. |
| **Nhân vật & Biểu cảm (Character & Expression)** | Nữ chính tóc vàng quyến rũ, mắt xếch kẻ eyeliner quyến rũ, má ửng hồng (blush), bờ môi hé mở gợi cảm, thần thái cuốn hút. | Giữ nguyên phong thái mê hoặc, tự tin, đa dạng hóa theo tính chất từng lá bài (hoàng gia, bí ẩn, kiêu hãnh, cuồng nhiệt). |
| **Trang phục & Phụ kiện (Outfit & Accessories)** | Đồ lót/dây đai harness trắng tinh tế, vòng cổ choker, tất đùi viền ren (thigh-high stockings). | Cách điệu trang phục truyền thống của Tarot thành các thiết kế hiện đại, quyến rũ với chất liệu lụa, voan trong suốt, dây harness và kim loại vàng/bạc. |
| **Ánh sáng & Màu sắc (Lighting & Palette)** | Ánh sáng mềm kết hợp viền sáng (rim lighting), điểm nhấn phản chiếu bóng (specular highlights), hào quang phát sáng nhẹ. | Phối màu rực rỡ theo 4 nguyên tố: Lửa (Đỏ cam vàng - Gậy), Nước (Xanh dương ngọc - Cốc), Khí (Bạc tím lam - Kiếm), Đất (Vàng kim xanh lục - Tiền). |
| **Bố cục khung bài (Tarot Card Framing)** | Tỷ lệ dọc chuẩn bài Tarot (2:3 hoặc 9:16), trọng tâm nhân vật nổi bật. | Bổ sung khung viền hoa văn vàng ma thuật (ornate golden filigree tarot border), biểu tượng chiêm tinh và tên lá bài. |

---

## ⚙️ 2. HƯỚNG DẪN SỬ DỤNG VỚI CÁC CÔNG CỤ AI

### A. Midjourney (v6.1 / Niji 6)
- **Tỷ lệ khung hình:** `--ar 2:3` hoặc `--ar 9:16`
- **Phong cách:** `--v 6.1 --style raw --stylize 250`
- **Sử dụng ảnh mẫu Capture3 làm nguồn tham chiếu (Style Reference / Image Prompt):**
  - Đưa link ảnh `Capture3.PNG` lên Discord hoặc dùng URL:
  - Cú pháp: `[Link_Ảnh_Capture3] [Nội dung prompt lá bài] --sref [Link_Ảnh_Capture3] --sw 150 --ar 2:3 --v 6.1`

### B. Stable Diffusion (SDXL / NovelAI / SeaArt / Civitai Webtoon Checkpoints)
- **Model đề xuất:** Các Checkpoint/LoRA Webtoon như *Animagine XL*, *Pony Diffusion V6*, *AOM3*, *Webtoon manhwa LoRA*.
- **Cấu trúc Prompt:** `masterpiece, best quality, manhwa art, korean webtoon style, [Prompt chi tiết của lá bài], volumetric lighting, ray tracing`
- **Negative Prompt chung đề xuất:**
  `low quality, worst quality, bad anatomy, deformed hands, extra limbs, bad proportions, blurry, watermark, signature, text, mutation, deformed eyes`
- **Sampling & Steps:** DPM++ 2M Karras, 28-35 steps, CFG Scale: 6.5 - 7.5.

---

## 🌟 3. DANH SÁCH PROMPTS CHI TIẾT 78 LÁ BÀI TAROT

"""

# Group by arcana/suit
categories = [
    ("🔮 PHẦN I: MAJOR ARCANA (BỘ ẨN CHÍNH - 22 LÁ)", [c for c in cards if c["suit"] == "Major"]),
    ("🔥 PHẦN II: SUIT OF WANDS (BỘ GẬY - NGUYÊN TỐ LỬA / ĐAM MÊ - 14 LÁ)", [c for c in cards if c["suit"] == "Wands"]),
    ("💧 PHẦN III: SUIT OF CUPS (BỘ CỐC - NGUYÊN TỐ NƯỚC / TÌNH CẢM - 14 LÁ)", [c for c in cards if c["suit"] == "Cups"]),
    ("⚔️ PHẦN IV: SUIT OF SWORDS (BỘ KIẾM - NGUYÊN TỐ KHÍ / LÝ TRÍ & XUNG ĐỘT - 14 LÁ)", [c for c in cards if c["suit"] == "Swords"]),
    ("🪙 PHẦN V: SUIT OF PENTACLES (BỘ TIỀN - NGUYÊN TỐ ĐẤT / TÀI CHÍNH & VẬT CHẤT - 14 LÁ)", [c for c in cards if c["suit"] == "Pentacles"]),
]

for cat_title, cat_cards in categories:
    md_content += f"\n---\n\n## {cat_title}\n\n"
    for c in cat_cards:
        md_content += f"### 🎴 {c['number']}. {c['name_en']} ({c['name_vi']})\n\n"
        md_content += f"- **Ý nghĩa cốt lõi:** {c['meaning']}\n"
        md_content += f"- **Ý tưởng tạo hình:** {c['concept']}\n\n"
        md_content += f"#### 🚀 Midjourney Prompt:\n"
        md_content += f"```text\n{c['prompt_mj']}\n```\n\n"
        md_content += f"#### 🎨 Stable Diffusion / NovelAI Tags:\n"
        md_content += f"```text\n{c['prompt_sd']}\n```\n\n"

md_content += """
---

## 💡 4. MẸO TỐI ƯU HÓA HÌNH ẢNH (PRO-TIPS)

1. **Giữ tính đồng bộ nhân vật (Character Consistency):**
   - Nếu bạn muốn tạo nguyên bộ bài với đúng cô gái tóc vàng trong `Capture3.PNG`, hãy thêm vào prompt các đặc điểm nhận dạng cố định: `blonde wavy hair, seductive hooded amber-brown eyes, winged eyeliner, choker collar, hourglass figure, pale glowing skin`.
   - Trong Midjourney: Dùng thêm tham số `--cref [Link_Ảnh_Capture3] --cw 80`.
2. **Tạo hiệu ứng bài Tarot chân thực:**
   - Thêm cụm từ: `tarot card format, ornate golden art-nouveau border, banner at bottom with text '[Tên lá bài]'` để bài có khung viền hoa văn vàng kim cổ điển sang trọng.
3. **Chỉnh sửa bàn tay & chi tiết nhỏ (Inpainting):**
   - Với các lá bài cầm gươm, cốc, gậy hoặc tiền, sử dụng chức năng Inpaint/Vary (Region) để tái tạo ngón tay thon dài mượt mà chuẩn nét vẽ Manhwa.
"""

with open('TAROT_78_PROMPTS.md', 'w', encoding='utf-8') as f:
    f.write(md_content)

print("Generated TAROT_78_PROMPTS.md successfully!")
