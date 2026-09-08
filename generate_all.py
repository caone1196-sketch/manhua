import json
import re

# Load base reference cards from cards_ref.json
with open('cards_ref.json', 'r', encoding='utf-8') as f:
    cards_ref_data = json.load(f)

# Parse CHARACTER_SPECS_REF.md
with open('CHARACTER_SPECS_REF.md', 'r', encoding='utf-8') as f:
    text = f.read()

sections = re.split(r"##\s+[34567]\.\s+BẢNG CHÍNH", text)
specs_dict = {}

for s in sections[1:]:
    rows = [l for l in s.split("\n") if l.startswith("|") and "`" in l and not l.startswith("| Lá")]
    for r in rows:
        parts = [p.strip() for p in r.strip("|").split("|")]
        if len(parts) >= 8:
            card_info = parts[0]
            slug_match = re.search(r"`([^`]+)`", card_info)
            slug = slug_match.group(1) if slug_match else ""
            age = parts[1]
            eyes = parts[2]
            hair = parts[3]
            build = parts[4]
            skin = parts[5]
            signature = parts[6]
            aura = parts[7]
            specs_dict[slug] = {
                "card_raw": card_info,
                "age": f"{age} years old",
                "eyes": eyes,
                "hair": hair,
                "build": build,
                "skin": skin,
                "signature": signature,
                "aura": aura
            }

print(f"Loaded {len(specs_dict)} character specs.")

MASTER_PROMPT_TEMPLATE = """A single tarot card built upon the FIRST reference image (the deck's ornamental card template): keep its symmetric ornamental golden frame, the four corner filigree flourishes, the top-center medallion and the bottom band with the small skull ornament EXACTLY as they are — do not redraw, move, recolor or resize any part of the frame. FULL BLEED: the card itself fills the entire image EDGE TO EDGE, corner to corner — there is no background, no margin, no dark band, no drop shadow and no second border outside the ornamental frame; every pixel of the image belongs to the card. Fill the center panel with the new scene, painted in the EXACT master art style of the SECOND reference image (Capture3.PNG Korean adult manhwa webtoon style): identical crisp lineart, alluring character design, seductive blushing expression, glossy skin highlights, soft cell shading and glowing volumetric rim lighting.

LAYOUT (draw in this order):
— TOP: inside the top-center ornamental medallion place this card's EMBLEM: {EMBLEM} — small antique-gold heraldic emblem, centered, no text, no numerals.
— MIDDLE (the empty center panel only): {SCENE}. {CHARACTER_SPEC}
— BOTTOM: in the bottom band, directly beneath the small skull ornament, the title "{TITLE}" — centered, on one line, spelled exactly like that.

TITLE LOCK: the title must be rendered in the EXACT lettering of the title in the reference image — identical typeface, weight, letter-spacing and tracking, gold tone and shading, cap height and stroke width, identical position directly beneath the skull ornament. Copy that letterform character by character for the new words; do not invent a different font, do not use a modern sans-serif. The only text on the card is this title.

{COUNT_LOCK}

{FEMME_DIRECTIVE}

THEME: sensual classic tarot in the tradition of vintage art-nude tarot decks and Korean adult manhwa aesthetic — elegant adult female figures entirely at ease in their bodies, graceful nude and semi-nude poses, silk and sheer gauze and stylish strappy lingerie harness accents that follow the body's line, warm lighting against subtle shadows, painterly skin in golden light with glossy specular highlights.

ANATOMY LOCK (HARD CONSTRAINT): exactly two arms, two legs, one head, one torso. Every joint (shoulders, elbows, wrists, hips, knees, ankles) connects naturally to the body. No extra limbs, no fused limbs, no hands merging into torso, no missing fingers, no six-fingered hands. Both arms must be clearly separated from the torso.

NEGATIVE: wrong or mismatched title font, modern or sans-serif lettering, extra words, misspelled title, dark margin, empty band, background or mat around the card, drop shadow, vignette, card floating inside the frame, extra or miscounted suit objects, duplicated, fused, cropped or half-hidden objects, extra limbs, extra arms, three arms, extra hand, more than two arms, extra fingers, six-fingered hands, extra heads, distorted anatomy, modern casual clothing, plastic 3D render, text or numbers anywhere except the bottom title band, watermark, signature, artist name, double border, multiple cards, collage.

No other text, no watermark, single card only."""

def build_count_lock(count_obj):
    if not count_obj:
        return "COUNT LOCK: This card contains NO loose suit objects in the scene. Do not add random floating or decorative cups, swords, wands, or pentacles."
    n = count_obj.get("n", 1)
    obj = count_obj.get("obj", "suit object")
    layout = count_obj.get("layout", "")
    return f"""COUNT LOCK — EXACTLY {n} {obj.upper()} (hard constraint; count before you draw).
The scene contains exactly {n} {obj} — not {n-1}, not {n+1}.
Placement is locked: {layout}.
Every one of the {n} must be fully visible: nothing occluded by a body, limb, cloth, cloud or another object, nothing fused, broken, cropped by the golden frame, or half-hidden behind a figure. Keep them at one consistent size, shape, material and color so they read as a single countable set, with a clear gap of background between each one. Place no other {obj} anywhere else on the card — not in the frame, not in the background, not held by a figure, not as decoration. The emblem in the top medallion is a separate heraldic motif and does NOT count toward the {n}. Before finishing, count them: 1 to {n}. If the total is not {n}, redraw."""

def build_femme_directive(card_slug, spec, card_item):
    if not spec:
        if card_item.get("femme"):
            return "FEMALE FIGURE DIRECTIVE: a stunningly beautiful young woman (18–25 years old), alluring sensual poise, flawless glowing skin, expressive eyes, manhwa webtoon aesthetic."
        return "SCENE ONLY: Divine relic / landscape card with no central human figure."
    
    return f"""FEMALE FIGURE DIRECTIVE — 100% FEMALE ({spec['age']}):
Character design: {spec['card_raw'].split('`')[0].strip()} ({spec['age']}), hair: {spec['hair']}, eyes: {spec['eyes']}, build: {spec['build']}, skin tone: {spec['skin']} with glossy specular highlights, signature feature: {spec['signature']}, aura: {spec['aura']}. Seductive, alluring poise inspired by the manhwa style of Capture3.PNG."""

all_cards = []
for c in cards_ref_data['cards']:
    slug = c['slug']
    spec = specs_dict.get(slug)
    title = c['title']
    emblem = c['emblem']
    scene = c['scene']
    count_lock = build_count_lock(c.get('count'))
    femme_directive = build_femme_directive(slug, spec, c)
    
    char_spec_inline = ""
    if spec:
        char_spec_inline = f"Character details: {spec['age']}, {spec['build']}, hair: {spec['hair']}, eyes: {spec['eyes']}, skin: {spec['skin']} with glossy highlights, signature: {spec['signature']}."
    
    full_prompt = MASTER_PROMPT_TEMPLATE.format(
        TITLE=title,
        EMBLEM=emblem,
        SCENE=scene,
        CHARACTER_SPEC=char_spec_inline,
        COUNT_LOCK=count_lock,
        FEMME_DIRECTIVE=femme_directive
    )
    
    all_cards.append({
        "n": c['n'],
        "slug": slug,
        "group": c['group'],
        "title": title,
        "emblem": emblem,
        "femme": c.get('femme', True),
        "count": c.get('count'),
        "scene": scene,
        "hair": spec['hair'] if spec else (c.get('hair') or "N/A"),
        "age": spec['age'] if spec else (c.get('age') or "N/A"),
        "eyes": spec['eyes'] if spec else "N/A",
        "build": spec['build'] if spec else (c.get('build') or "N/A"),
        "skin": spec['skin'] if spec else "N/A",
        "signature": spec['signature'] if spec else "N/A",
        "aura": spec['aura'] if spec else "N/A",
        "count_lock": count_lock,
        "master_prompt": full_prompt
    })

# Write cards.json
with open('cards.json', 'w', encoding='utf-8') as f:
    json.dump({
        "meta": {
            "deck": "Sensual Manhwa Tarot — 78 cards",
            "version": "v2 (count-locked, manhwa sensual edition)",
            "refs": [
                "card-blank.png (blank ornamental template, position 1)",
                "Capture3.PNG (manhwa style anchor — character, skin, lighting, position 2)",
                "title-style.png (lettering sample, position 3)"
            ],
            "master_template": MASTER_PROMPT_TEMPLATE
        },
        "cards": all_cards
    }, f, ensure_ascii=False, indent=2)

print("Saved cards.json!")

# Generate TAROT_78_PROMPTS.md
md_lines = [
    "# 🔮 SENSUAL MANHWA TAROT 78 LÁ — MASTER PROMPT SPECIFICATION v2",
    "",
    "> **Chuẩn hóa quy chuẩn tạo hình và bố cục toàn bộ 78 lá bài Tarot theo Master Prompt chuẩn từ phiên trước, tích hợp phong cách Manhwa quyến rũ từ ảnh `Capture3.PNG`.**",
    "",
    "---",
    "",
    "## 📌 1. CẤU TRÚC MASTER PROMPT TEMPLATE v2",
    "",
    "```text",
    MASTER_PROMPT_TEMPLATE,
    "```",
    "",
    "---",
    "",
    "## 🎴 2. TOÀN BỘ 78 PROMPTS HOÀN CHỈNH (THEO THỨ TỰ CHUẨN)",
    ""
]

groups = [
    ("MAJOR ARCANA (22 LÁ)", "major"),
    ("SUIT OF WANDS (14 LÁ)", "wands"),
    ("SUIT OF CUPS (14 LÁ)", "cups"),
    ("SUIT OF SWORDS (14 LÁ)", "swords"),
    ("SUIT OF PENTACLES (14 LÁ)", "pentacles")
]

for g_name, g_key in groups:
    md_lines.append(f"### 🌟 {g_name}\n")
    g_cards = [c for c in all_cards if c['group'] == g_key]
    for card in g_cards:
        md_lines.append(f"#### 🃏 [{card['n']}] {card['title']} (`{card['slug']}`)")
        md_lines.append(f"- **Emblem:** {card['emblem']}")
        md_lines.append(f"- **Scene:** {card['scene']}")
        if card['age'] != "N/A":
            md_lines.append(f"- **Character Specs:** {card['age']} | Hair: {card['hair']} | Eyes: {card['eyes']} | Build: {card['build']} | Skin: {card['skin']} | Signature: {card['signature']}")
        md_lines.append(f"- **Count Lock:** `{card['count_lock'].splitlines()[0]}`")
        md_lines.append("")
        md_lines.append("```text")
        md_lines.append(card['master_prompt'])
        md_lines.append("```")
        md_lines.append("")
    md_lines.append("---\n")

with open('TAROT_78_PROMPTS.md', 'w', encoding='utf-8') as f:
    f.write('\n'.join(md_lines))

print("Saved TAROT_78_PROMPTS.md successfully!")
