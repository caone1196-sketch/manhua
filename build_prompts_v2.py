#!/usr/bin/env python3
"""
build_prompts_v2.py — Sinh bộ prompt MỚI cho toàn bộ 78 lá tarot theo công thức
đã chốt qua 10 vòng lặp trên lá The Star:

  1. Frameless, edge-to-edge, KHÔNG số / KHÔNG số La Mã — chỉ tên lá bài
     chữ serif vàng cổ điển dưới đáy (template update_no_num.py).
  2. Art style + contour rendering + chữ title: reference major_08_strength.png
     (viền contour đậm, specular streak dọc curve, rim light vàng ấm).
  3. Chi tiết tiếp giáp trang phục–cơ thể: căng dây, mép vải ôm curve,
     bóng đổ dưới mép vải, nếp tụ ở nút dây hông.
  4. Vải ướt sũng kiểu test_card_17_the_star.png: tone sẫm ngậm nước,
     sheen bóng, nếp ướt dán sát, giọt nước đọng trên vải.
  5. Trang phục: micro string bikini swimwear (opaque, không see-through),
     màu theo group; pose S-curve contrapposto; biểu cảm má hồng + cat eyeliner.

Output: thư mục riêng biệt prompts_frameless_v2/
  - prompts_frameless_v2/<slug>.md   : prompt đầy đủ từng lá
  - prompts_frameless_v2/all_prompts.json : bản machine-readable
  - prompts_frameless_v2/README.md   : tài liệu công thức
Không ghi đè cards.json.
"""
import json
import os
import re

OUT_DIR = "prompts_frameless_v2"

GROUP_OUTFIT = {
    "major": "pearl-white",
    "cups": "aqua-pearl",
    "wands": "ember-gold",
    "swords": "silver-white",
    "pentacles": "bronze-gold",
}


def sanitize_scene(scene: str) -> str:
    """Đổi mô tả nude/semi-nude/see-through của spec cũ thành trang phục swimwear ướt."""
    s = scene.replace("semi-nude", "in a soaking-wet micro string bikini")
    s = s.replace("a nude woman", "a woman in a soaking-wet micro string bikini")
    s = s.replace("nude woman", "woman in a soaking-wet micro string bikini")
    s = s.replace("nude", "swimwear-clad")
    # Các cụm lộ liễu / xuyên thấu còn sót sau vòng replace thô
    EXTRA = [
        ("draped only in a transparent silk veil so fine it clings and reveals her bare body beneath, "
         "the veil slipping from one shoulder and streaming behind her",
         "wearing a soaking-wet micro string bikini with a fine opaque silk sash slipping from one "
         "shoulder and streaming behind her"),
        ("bare torso with a length of silk slung low across her hips",
         "soaking-wet micro string bikini with a length of silk slung low across her hips"),
        ("one breast bared, ", ""),
        ("one breast bared", ""),
        ("reveals her bare body", "gleams over her soaking-wet micro string bikini"),
        ("transparent silk veil", "opaque silk sash"),
        ("bare shoulders and the soft line of her breasts veiled only by a drift of sheer gauze",
         "bare shoulders, her soaking-wet micro string bikini accented by a drift of opaque silk gauze over one arm"),
        ("draped only in a diaphanous opaque silk sash so fine it clings to her soft curves and glows "
         "with warm light against her skin, the gossamer fabric slipping from one shoulder",
         "wearing a soaking-wet micro string bikini with a silk sash glowing with warm light, "
         "slipping from one shoulder"),
    ]
    for old, new in EXTRA:
        s = s.replace(old, new)
    # Quy tắc tổng quát: mọi cụm "draped only in ..." (vải mỏng che thân) -> swimwear + sash
    s = re.sub(r"draped only in [^,.]*", "wearing a soaking-wet micro string bikini with a glowing silk sash", s)
    s = s.replace("her bare back and the curve of one breast veiled and revealed by the golden lantern light",
                  "her wet skin glowing in the golden lantern light")
    s = s.replace("flowing transparent silk", "flowing silk robes")
    s = s.replace("transparent silk", "opaque silk")
    s = s.replace("sheer white silk gauze", "opaque white silk sash")
    EXTRA2 = [
        ("a length of sheer silk sliding fully off one shoulder to bare one breast and one hip",
         "an opaque silk sash sliding off one shoulder"),
        ("draped in sheer black silk that veils and reveals her bare form",
         "wearing a soaking-wet black micro string bikini with a flowing black silk sash"),
        ("her bare torso turned toward the light", "her wet glossy torso turned toward the light"),
        ("one arm across her breast", "one arm across her chest"),
        ("wearing a gown of antique WHITE SILK GAUZE so sheer and transparent that the light shines "
         "through it and the long line of her body reads clearly beneath",
         "wearing a fully opaque gown of antique white silk glowing softly in the sea light"),
    ]
    for old, new in EXTRA2:
        s = s.replace(old, new)
    s = re.sub(r"veils and reveals her [a-z ]*form", "drapes her swimwear-clad figure", s)
    s = re.sub(r"so sheer and transparent that[^,]*", "fully opaque", s)
    s = s.replace("sheer opaque silk", "flowing opaque silk")
    EXTRA3 = [
        ("draped in sheer black silk upon a dark pedestal",
         "wearing a soaking-wet black micro string bikini with a black silk sash upon a dark pedestal"),
        ("in a sheer flowing gown that clings to breast and hip",
         "in a flowing fully opaque gown that clings to her curves"),
        ("in a very thin veil of antique silk gauze, almost transparent, her shoulders bare",
         "in an opaque antique silk gown, her shoulders bare"),
        ("whose body is wrapped in a single sheet of TRANSPARENT antique silk gauze, one shoulder "
         "and the curve of her breast left bare",
         "wearing an opaque antique silk gown with one shoulder bare"),
    ]
    for old, new in EXTRA3:
        s = s.replace(old, new)
    return s


PROMPT_TEMPLATE = """A completely frameless vertical tarot card "{title}", edge-to-edge illustration: no decorative borders, no card frame, no banner ribbon, no numbers, no Roman numerals. The only text is the title "{title}" centered at the very bottom in the same antique-gold serif lettering as the style reference card.

REFERENCE IMAGES: (1) major_08_strength.png — art style, contour rendering, garment-to-body detail, warm golden rim light and bottom title lettering. (2) test_card_17_the_star.png — soaking-wet swimwear fabric benchmark and glossy wet skin finish.

ART STYLE (match reference 1): Korean manhwa webtoon rendering — crisp clean lineart, soft cell shading, bold contour outlines tracing every curve of the body (cinched waist, flared hips, belly line, thigh and knee curves, collarbones and shoulders), glossy specular highlight streaks running along each curve so the body's lines pop, strong three-dimensional modeling, warm golden rim light hugging the figure against the scene palette.

GARMENT-TO-BODY DETAIL: thin strap tension lines pressing gently into shoulders and hips, fabric edges precisely tracing the underbust curve and hip crest, subtle soft skin swell over each bikini edge, delicate cast-shadow lines under the fabric rims, small tension folds in the wet fabric following the body topography, side-tie ribbon knots pulling the hip line with tiny gathers, specular highlights along every seam and strap.

WET FABRIC (match reference 2): soaking-wet {outfit} micro string bikini — waterlogged darkened tone with a glossy wet sheen, fabric fully opaque, clinging like a second skin with zero loose folds, plastered wet wrinkles, water droplets beading on the fabric surface, tiny drips falling from the fabric edges; whole body wet with droplets and thin rivulets, wet gleaming hair strands.

FIGURE: {char_spec} Pose: graceful S-curve contrapposto where the scene allows (hip popped, back slightly arched, one knee softly bent, barefoot); blushing cheeks, cat eyeliner, softly parted lips with a confident gentle smile.

SCENE & SYMBOLISM: {scene}. Tarot emblem integrated naturally: {emblem}. {count_lock}

DEPTH & LIGHT: layered atmospheric background receding into mist per the scene, glowing ambient reflections on wet skin and water, cinematic warm-cool contrast, faint golden sparkles in the air.

At the bottom, centered: the title "{title}" in antique-gold serif lettering matching reference 1. No numbers, no Roman numerals, no other text, no frame, no border, no banner, no watermark, no signature. Masterpiece manhwa illustration, portrait 7:12."""

MD_TEMPLATE = """# {title} ({n}) — Frameless Wet-Manhwa v2

- **Slug:** `{slug}` | **Group:** {group}
- **Emblem:** {emblem}
- **Reference style/contour/lettering:** `major_08_strength.png`
- **Reference wet fabric/swimwear:** `test_card_17_the_star.png`
- **Outfit:** soaking-wet {outfit} micro string bikini (opaque swimwear, no see-through)

## Prompt

```text
{prompt}
```
"""

README = """# prompts_frameless_v2 — Bộ prompt công thức The Star (v10) áp dụng toàn bộ 78 lá

Thư mục riêng biệt chứa prompt MỚI cho toàn bộ bộ bài, sinh bởi `build_prompts_v2.py`
từ `cards.json`, KHÔNG ghi đè dữ liệu gốc.

## Công thức (chốt qua 10 vòng lặp trên lá The Star)

1. **Frameless no-num** (template `update_no_num.py`): illustration tràn viền,
   không khung/không banner/không số La Mã; chỉ tên lá bài chữ serif vàng cổ điển dưới đáy.
2. **Style reference `major_08_strength.png`**: manhwa webtoon lineart sắc, cel shading,
   contour viền đậm ôm từng curve + specular streak dọc đường nét, rim light vàng ấm,
   chữ title serif vàng giống lá Strength.
3. **Garment-to-body detail**: vết căng dây trên da, mép vải ôm underbust/hip crest,
   bóng đổ dưới mép vải, nếp tụ ở nút dây hông, highlight dọc đường may/dây đeo.
4. **Wet fabric reference `test_card_17_the_star.png`**: vải ướt sũng tone sẫm ngậm nước,
   sheen bóng mờ, nếp ướt dán sát như da thứ hai, giọt nước đọng và rỉ từ mép vải;
   toàn thân ướt, tóc ướt bóng.
5. **Trang phục & pose**: micro string bikini swimwear opaque (màu theo group),
   pose S-curve contrapposto, má hồng + cat eyeliner + môi hé nụ cười tự tin.
6. **An toàn nội dung**: mọi mô tả nude/semi-nude của spec cũ được thay bằng
   trang phục swimwear ướt; không see-through, không pose lộ liễu.

## Màu trang phục theo group

| Group | Màu vải ướt |
|---|---|
| major | pearl-white |
| cups | aqua-pearl |
| wands | ember-gold |
| swords | silver-white |
| pentacles | bronze-gold |

## Cấu trúc thư mục

- `<slug>.md` — prompt đầy đủ từng lá (kèm metadata + reference)
- `all_prompts.json` — map slug → prompt (machine-readable)
- `README.md` — tài liệu này

## Cách dùng khi sinh ảnh

Đưa kèm 2 ảnh reference cho model: `major_08_strength.png` (style/contour/chữ)
và `test_card_17_the_star.png` (vải ướt/swimwear), rồi dán prompt của lá tương ứng.

## Tái sinh

```bash
python3 build_prompts_v2.py
```
"""


def build_char_spec(c):
    return (
        f"{c.get('age', '20 years old')}, build: {c.get('build', 'slender waist with curvy feminine silhouette')}, "
        f"hair: {c.get('hair', 'flowing golden hair')}, eyes: {c.get('eyes', 'alluring eyes')}, "
        f"skin: {c.get('skin', 'porcelain')} with glossy wet highlights, signature: {c.get('signature', '')}, aura: {c.get('aura', '')}."
    )


def main():
    with open("cards.json", encoding="utf-8") as f:
        data = json.load(f)

    os.makedirs(OUT_DIR, exist_ok=True)
    all_prompts = {}

    for c in data["cards"]:
        slug = c["slug"]
        title = c["title"]
        outfit = GROUP_OUTFIT.get(c["group"], "pearl-white")
        prompt = PROMPT_TEMPLATE.format(
            title=title,
            outfit=outfit,
            char_spec=build_char_spec(c),
            scene=sanitize_scene(c["scene"]),
            emblem=c["emblem"],
            count_lock=c.get("count_lock", ""),
        )
        all_prompts[slug] = prompt
        md = MD_TEMPLATE.format(
            title=title,
            n=c["n"],
            slug=slug,
            group=c["group"],
            emblem=c["emblem"],
            outfit=outfit,
            prompt=prompt,
        )
        with open(os.path.join(OUT_DIR, f"{slug}.md"), "w", encoding="utf-8") as f:
            f.write(md)

    with open(os.path.join(OUT_DIR, "all_prompts.json"), "w", encoding="utf-8") as f:
        json.dump(all_prompts, f, ensure_ascii=False, indent=2)

    with open(os.path.join(OUT_DIR, "README.md"), "w", encoding="utf-8") as f:
        f.write(README)

    print(f"Wrote {len(all_prompts)} card prompts + all_prompts.json + README.md into {OUT_DIR}/")


if __name__ == "__main__":
    main()
