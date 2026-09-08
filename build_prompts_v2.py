#!/usr/bin/env python3
"""
build_prompts_v2.py — Bộ prompt MỚI cho toàn bộ 78 lá tarot theo công thức
đã chốt qua các vòng lặp trên lá The Star:

  1. Frameless, edge-to-edge, KHÔNG số / KHÔNG số La Mã — chỉ tên lá bài
     chữ serif vàng cổ điển dưới đáy (template update_no_num.py).
  2. Art style + contour rendering + chữ title: reference major_08_strength.png.
  3. Chi tiết tiếp giáp trang phục–cơ thể (strap tension, mép vải, bóng đổ...).
  4. Vải ướt sũng kiểu test_card_17_the_star.png (opaque, không see-through).
  5. Swimwear micro string bikini theo group; pose S-curve; biểu cảm manhwa.
  6. BACKGROUND_MODE:
       - "modern"  : bối cảnh streamer penthouse hiện đại (RGB/neon, monitor,
                     hologram, city bokeh) — mapping sẵn cho 8 lá + fallback.
       - "classic" : bối cảnh cổ điển theo scene gốc đã sanitize.

Output: prompts_frameless_v2/ (<slug>.md, all_prompts.json, README.md).
Không ghi đè cards.json.
"""
import json
import os
import re

OUT_DIR = "prompts_frameless_v2"
BACKGROUND_MODE = "bathroom"  # "bathroom" | "modern" | "classic"

# Tùy chọn bikini (xoay vòng theo thứ tự lá): (màu, chi tiết accent) — luôn opaque + soaked
BIKINI_OPTIONS = [
    ("pearl-white", "with tiny gold star charms"),
    ("midnight-black", "with fine gold chain straps"),
    ("aqua-teal", "with side-tie ribbons"),
    ("rose-pink", "with small satin bow accents"),
    ("metallic gold", "with opaque lace-trim edges"),
    ("cherry-red", "with tiny pearl beads"),
]

# Tư thế nghệ thuật (figure-study / dance) xoay vòng theo thứ tự lá
ARTISTIC_POSES = [
    "seated on the tub edge in a figure-study diagonal — one knee drawn up, the other leg extended "
    "toe-deep in the water, arms forming a soft diagonal line",
    "standing arabesque-like balance — weight on one leg, the other extended back resting on the tub "
    "rim, arms held in a high-low axis line like a dancer",
    "mermaid sit on the marble ledge — knees together tilted to one side, torso upright with a gentle "
    "twist, one arm extended along the ledge",
    "reclining diagonal across the tub edge — hip line lifted, one leg extended in a long elegant line, "
    "one arm arched overhead",
    "seated cross-knee figure study — back straight, one arm resting on the knee, the other extended "
    "along the seat, chin slightly lifted",
    "kneeling stretch pose — one knee on the bath mat, torso arched back gracefully, both arms curving "
    "overhead like a dancer",
]

# Bối cảnh nhà tắm hiện đại (symbolism từng lá được re-stage)
BATHROOM_SCENES = {
    "00-fool": "a playful 19-year-old streamer in a modern luxury bathroom at sunrise: a glowing digital "
               "white rose in one hand, a cute white Pomeranian puppy on the fluffy bath mat beside her, "
               "steam curling off the water, floor-to-ceiling frosted glass with a cyberpunk city glow beyond",
    "01-magician": "a charismatic 22-year-old streamer in a modern luxury bathroom: beside a long marble "
                   "vanity with a lit mirror wall, one hand raising a glowing wand-shaped stream mic, the "
                   "other pointing to the vanity where exactly four objects rest: one flaming wand diffuser, "
                   "one glowing water cup, one crystal cyber-blade perfume bottle, one golden crypto coin "
                   "paperweight, black roses in an LED vase behind",
    "02-priestess": "a serene 23-year-old streamer in a modern luxury bathroom: between two tall rainfall "
                    "shower columns (one black stone, one white marble), a glowing holographic crescent moon "
                    "projected on the wet floor beneath her feet, a waterproof digital tablet of secret lore "
                    "resting in her lap, a pomegranate hologram shimmering in the steam",
    "03-empress": "a luxurious 24-year-old streamer in a sunlit modern bathroom garden: amid potted plants "
                  "and fresh fruit trays, golden morning light through frosted skylights, holding a golden "
                  "smartphone scepter, a heart-shaped Venus neon emblem glowing on the tiled wall",
    "04-emperor": "a poised 25-year-old streamer in a modern luxury steam bathroom: on a stone bench throne "
                  "beneath a bronze ram-head shower fixture, volcanic-red LED backlighting along the marble, "
                  "holding a golden ankh stylus, two ram-head sculptures on the vanity shelf, a barren "
                  "mountain tile mural behind, steam rolling low",
}
BATHROOM_FALLBACK = ("the card's symbolism re-staged in a modern luxury bathroom: {emblem} rendered as a "
                     "glowing mirror hologram, suit objects arranged on the marble vanity, rainfall shower "
                     "steam and warm LED accents, night city glow through frosted glass")

DEPTH_BATHROOM = ("DEPTH & LIGHT: soft steam layers diffusing warm LED and neon accents, wet marble and "
                  "mirror reflections on soaked skin, cinematic warm-cool contrast, water droplets sparkling "
                  "in the light shafts, faint golden sparkles in the mist.")

GROUP_OUTFIT = {
    "major": "pearl-white",
    "cups": "aqua-pearl",
    "wands": "ember-gold",
    "swords": "silver-white",
    "pentacles": "bronze-gold",
}

# Bối cảnh streamer hiện đại (kế thừa update_modern_manhwa.py, đã sanitize)
MODERN_SCENES = {
    "00-fool": "a playful 19-year-old blonde streamer sitting casually barefoot on the edge of a "
               "high-rise luxury balcony railing overlooking a glowing cyberpunk morning cityscape, "
               "holding a glowing digital white rose, a cute white Pomeranian puppy sitting beside "
               "her gaming chair, skin and bikini still dewy from the rooftop jacuzzi",
    "01-magician": "a charismatic 22-year-old streamer at her multi-monitor streaming desk, one hand "
                   "raising a glowing wand-shaped stream mic to the sky and the other pointing down "
                   "to the desk, exactly four holographic suit icons floating above the desk: one "
                   "flaming wand mic, one glowing water cup, one crystal cyber blade, one golden "
                   "crypto coin, a garden of black roses in LED vases behind her",
    "02-priestess": "a serene 23-year-old streamer sitting gracefully on a sleek obsidian gaming chair "
                    "between two tall RGB light bars (one black, one white), a glowing holographic "
                    "crescent moon beneath her bare feet, a glowing digital tablet of secret lore "
                    "resting in her lap, a pomegranate hologram shimmering beside her",
    "03-empress": "a luxurious 24-year-old streamer reclining in a plush velvet recliner in a modern "
                  "sunlit penthouse garden room, golden sunlight streaming through floor-to-ceiling "
                  "windows, holding a golden smartphone scepter, surrounded by lush indoor plants and "
                  "fresh fruits, a heart-shaped shield of Venus emblem glowing on the wall",
    "04-emperor": "a dominant 25-year-old streamer seated with poised posture in an executive leather "
                  "gaming throne with ram-horn headrest designs, RGB volcanic-red ambient backlighting, "
                  "glowing PC setup, holding a golden ankh stylus, ram-head sculptures on the desk, "
                  "barren mountain mural behind",
    "15-devil": "a seductive succubus streamer in a dark red-neon gaming room, curved black horns and "
                "dark wings, sitting back on a leather gaming seat with arms behind head, loose golden "
                "chain links draped across the desk, glowing crimson pentagram RGB on wall",
    "17-the-star": "a serene star-goddess streamer sitting in a black gaming chair with arms raised "
                   "behind her head, dual curved monitors displaying glowing star constellations, "
                   "pouring two streams of digital light from golden decanters onto a desktop water "
                   "feature, giant holographic eight-pointed star glowing above",
    "21-world": "a graceful streamer posing at the center of a circular RGB ring-light laurel arch in "
                "a panoramic high-rise penthouse studio overlooking a 360-degree night skyline, holding "
                "two glowing stylus wands, four pet avatar screens at the four corners",
}

MODERN_FALLBACK = ("the card's symbolism re-staged in a modern luxury penthouse streamer studio: "
                   "{emblem} rendered as a glowing holographic emblem above her, PC monitors and RGB "
                   "neon ambient lighting, the suit objects arranged on her streaming desk, night city "
                   "skyline bokeh through floor-to-ceiling windows")

DEPTH_MODERN = ("DEPTH & LIGHT: layered neon RGB ambient lighting, glowing monitor and hologram "
                "reflections on wet skin, cinematic warm-cool contrast, night city bokeh through "
                "floor-to-ceiling windows, faint golden sparkles in the air.")

DEPTH_CLASSIC = ("DEPTH & LIGHT: layered atmospheric background receding into mist per the scene, "
                 "glowing ambient reflections on wet skin and water, cinematic warm-cool contrast, "
                 "faint golden sparkles in the air.")


def sanitize_scene(scene: str) -> str:
    """Đổi mô tả nude/semi-nude/see-through của spec cũ thành trang phục swimwear ướt."""
    s = scene.replace("semi-nude", "in a soaking-wet micro string bikini")
    s = s.replace("a nude woman", "a woman in a soaking-wet micro string bikini")
    s = s.replace("nude woman", "woman in a soaking-wet micro string bikini")
    s = s.replace("nude", "swimwear-clad")
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
    s = re.sub(r"draped only in [^,.]*", "wearing a soaking-wet micro string bikini with a glowing silk sash", s)
    s = s.replace("her bare back and the curve of one breast veiled and revealed by the golden lantern light",
                  "her wet skin glowing in the golden lantern light")
    s = s.replace("flowing transparent silk", "flowing silk robes")
    s = s.replace("transparent silk", "opaque silk")
    s = s.replace("sheer white silk gauze", "opaque white silk sash")
    s = s.replace("sheer opaque silk", "flowing opaque silk")
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

WET FABRIC (match reference 2): soaking-wet {outfit} micro string bikini {accent} — waterlogged darkened tone with a glossy wet sheen, fabric fully opaque, clinging like a second skin with zero loose folds, plastered wet wrinkles, water droplets beading on the fabric surface, tiny drips falling from the fabric edges; whole body wet with droplets and thin rivulets, wet gleaming hair strands; she is mid-shower under the rainfall head or just stepped out of the tub, so the soaked look reads naturally indoors.

FIGURE: {char_spec} Pose (artistic figure study): {pose}; barefoot; blushing cheeks, cat eyeliner, softly parted lips with a confident gentle smile.

SCENE & SYMBOLISM: {scene}. Tarot emblem integrated naturally: {emblem}. {count_lock}

{depth}

At the bottom, centered: the title "{title}" in antique-gold serif lettering matching reference 1. No numbers, no Roman numerals, no other text, no frame, no border, no banner, no watermark, no signature. Masterpiece manhwa illustration, portrait 7:12."""

MD_TEMPLATE = """# {title} ({n}) — Frameless Wet-Manhwa v2 · mode {mode}

- **Slug:** `{slug}` | **Group:** {group}
- **Emblem:** {emblem}
- **Reference style/contour/lettering:** `major_08_strength.png`
- **Reference wet fabric/swimwear:** `test_card_17_the_star.png`
- **Outfit:** soaking-wet {outfit} micro string bikini {accent} (opaque swimwear, no see-through)
- **Pose nghệ thuật:** {pose}
- **Background mode:** {mode}

## Prompt

```text
{prompt}
```
"""

README = """# prompts_frameless_v2 — Bộ prompt công thức The Star áp dụng toàn bộ 78 lá

Thư mục riêng biệt chứa prompt MỚI cho toàn bộ bộ bài, sinh bởi `build_prompts_v2.py`
từ `cards.json`, KHÔNG ghi đè dữ liệu gốc.

## Công thức cốt lõi

1. **Frameless no-num** (template `update_no_num.py`): illustration tràn viền,
   không khung/không banner/không số La Mã; chỉ tên lá bài chữ serif vàng cổ điển dưới đáy.
2. **Style reference `major_08_strength.png`**: manhwa webtoon lineart sắc, cel shading,
   contour viền đậm ôm từng curve + specular streak dọc đường nét, rim light vàng ấm,
   chữ title serif vàng giống lá Strength.
3. **Garment-to-body detail**: vết căng dây trên da, mép vải ôm underbust/hip crest,
   bóng đổ dưới mép vải, nếp tụ ở nút dây hông, highlight dọc đường may/dây đeo.
4. **Wet fabric reference `test_card_17_the_star.png`**: vải ướt sũng tone sẫm ngậm nước,
   sheen bóng, nếp ướt dán sát như da thứ hai, giọt nước đọng và rỉ từ mép vải;
   toàn thân ướt, tóc ướt bóng; justify bởi "vừa bước khỏi jacuzzi penthouse".
5. **Trang phục & pose**: micro string bikini swimwear opaque (màu theo group),
   pose S-curve contrapposto, má hồng + cat eyeliner + môi hé nụ cười tự tin.
6. **An toàn nội dung**: mọi mô tả nude/semi-nude/see-through của spec cũ được thay bằng
   trang phục swimwear ướt opaque; không pose lộ liễu.

## Background mode

- `BACKGROUND_MODE = "modern"` (hiện tại): bối cảnh streamer penthouse hiện đại —
  RGB/neon, multi-monitor, hologram, gaming throne, city bokeh; mapping sẵn cho
  8 lá (fool, magician, priestess, empress, emperor, devil, star, world) + fallback
  penthouse studio cho các lá còn lại.
- `BACKGROUND_MODE = "classic"`: bối cảnh cổ điển theo scene gốc đã sanitize.

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
        idx = data["cards"].index(c)
        bikini_color, bikini_accent = BIKINI_OPTIONS[idx % len(BIKINI_OPTIONS)]
        pose = ARTISTIC_POSES[idx % len(ARTISTIC_POSES)]
        if BACKGROUND_MODE == "modern":
            scene = MODERN_SCENES.get(slug, MODERN_FALLBACK.format(emblem=c["emblem"]))
            depth = DEPTH_MODERN
        elif BACKGROUND_MODE == "bathroom":
            scene = BATHROOM_SCENES.get(slug, BATHROOM_FALLBACK.format(emblem=c["emblem"]))
            depth = DEPTH_BATHROOM
        else:
            scene = sanitize_scene(c["scene"])
            depth = DEPTH_CLASSIC
        outfit = bikini_color
        prompt = PROMPT_TEMPLATE.format(
            title=title,
            outfit=outfit,
            char_spec=build_char_spec(c),
            scene=scene,
            emblem=c["emblem"],
            count_lock=c.get("count_lock", ""),
            depth=depth,
            accent=bikini_accent,
            pose=pose,
        )
        all_prompts[slug] = prompt
        md = MD_TEMPLATE.format(
            title=title,
            n=c["n"],
            slug=slug,
            group=c["group"],
            emblem=c["emblem"],
            outfit=outfit,
            accent=bikini_accent,
            pose=pose,
            mode=BACKGROUND_MODE,
            prompt=prompt,
        )
        with open(os.path.join(OUT_DIR, f"{slug}.md"), "w", encoding="utf-8") as f:
            f.write(md)

    with open(os.path.join(OUT_DIR, "all_prompts.json"), "w", encoding="utf-8") as f:
        json.dump(all_prompts, f, ensure_ascii=False, indent=2)

    with open(os.path.join(OUT_DIR, "README.md"), "w", encoding="utf-8") as f:
        f.write(README)

    print(f"Wrote {len(all_prompts)} card prompts (mode={BACKGROUND_MODE}) into {OUT_DIR}/")


if __name__ == "__main__":
    main()
