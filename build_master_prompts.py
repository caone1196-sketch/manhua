import json
import re

# Load base reference cards from cards_ref.json
with open('cards_ref.json', 'r', encoding='utf-8') as f:
    cards_ref_data = json.load(f)

# Parse CHARACTER_SPECS_REF.md to get eyes, skin, signature, aura for each card slug
with open('CHARACTER_SPECS_REF.md', 'r', encoding='utf-8') as f:
    char_specs_text = f.read()

char_rows = re.findall(r'\|\s*\*\*([^*]+)\*\*\s*`([^`]+)`\s*\|\s*(\d+)\s*\|\s*([^|]+)\|\s*([^|]+)\|\s*([^|]+)\|\s*([^|]+)\|\s*([^|]+)\|\s*([^|]+)\|', char_specs_text)
print(f"Parsed {len(char_rows)} character specs rows from CHARACTER_SPECS_REF.md")

specs_dict = {}
for row in char_rows:
    card_name, slug, age, eyes, hair, build, skin, signature, aura = [x.strip() for x in row]
    specs_dict[slug] = {
        "card_name": card_name,
        "age": f"{age} years old",
        "eyes": eyes,
        "hair": hair,
        "build": build,
        "skin": skin,
        "signature": signature,
        "aura": aura
    }

# Master Prompt Template Builder
MASTER_PROMPT_TEMPLATE = """A single tarot card built upon the FIRST reference image (the deck's ornamental card template): keep its symmetric ornamental golden frame, the four corner filigree flourishes, the top-center medallion and the bottom title ribbon band EXACTLY as they are — do not redraw, move, recolor or resize any part of the frame. FULL BLEED: the card itself fills the entire image EDGE TO EDGE, corner to corner — there is no background, no margin, no dark band, no drop shadow and no second border outside the ornamental frame; every pixel of the image belongs to the card. Fill the center panel with the new scene, painted in the EXACT master art style of the SECOND reference image (Capture3.PNG Korean adult manhwa webtoon style): identical crisp lineart, alluring character design, seductive blushing expression, glossy skin highlights, soft cell shading and glowing volumetric rim lighting.

LAYOUT (draw in this order):
— TOP: inside the top-center ornamental medallion place this card's EMBLEM: {EMBLEM} — small antique-gold heraldic emblem, centered, no text, no numerals.
— MIDDLE (the open center panel): {SCENE} {CHARACTER_SPEC}
— BOTTOM: in the bottom ribbon band, the title "{TITLE}" — centered, on one line, spelled exactly like that.

TITLE LOCK: the title must be rendered in clean antique gold lettering inside the bottom ribbon band — identical typeface, identical weight, identical letter-spacing and tracking, gold tone and shading, cap height and stroke width. The only text on the card is this title.

{COUNT_LOCK}

{FEMME_DIRECTIVE}

ANATOMY LOCK (HARD CONSTRAINT): exactly two arms, two legs, one head, one torso. Every joint (shoulders, elbows, wrists, hips, knees, ankles) connects naturally to the body. No extra limbs, no fused limbs, no hands merging into torso, no missing fingers, no six-fingered hands. Both arms must be clearly separated from the torso.

THEME: sensual adult Korean manhwa tarot in the alluring aesthetic of Capture3.PNG — gorgeous young woman with delicate features, winged eyeliner, blushing cheeks, seductive gaze, translucent silk and white strappy harness lingerie accents, warm ambient lighting against soft shadows, glowing rim light, high gloss finish.

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
Every one of the {n} must be fully visible: nothing occluded by a body, limb, cloth, cloud or another object, nothing fused, broken, cropped by the golden frame, or half-hidden behind a figure. Keep them at one consistent size, shape, material and color so they read as a single countable set, with a clear gap of background between each one. Place no other {obj} anywhere else on the card. The emblem in the top medallion is a separate heraldic motif and does NOT count toward the {n}. Before finishing, count them: 1 to {n}. If the total is not {n}, redraw."""

def build_femme_directive(card_slug, spec, card_item):
    if not spec:
        if card_item.get("femme"):
            return "FEMALE FIGURE DIRECTIVE: a stunningly beautiful young woman (18–25 years old), alluring sensual poise, flawless porcelain/fair glowing skin, expressive eyes, manhwa webtoon aesthetic."
        return "SCENE ONLY: Divine relic / landscape card with no central human figure."
    
    return f"""FEMALE FIGURE DIRECTIVE — 100% FEMALE (age {spec['age']}):
Character design: {spec['card_name']} ({spec['age']}), hair: {spec['hair']}, eyes: {spec['eyes']}, build: {spec['build']}, skin tone: {spec['skin']} with glossy specular highlights, signature feature: {spec['signature']}, aura: {spec['aura']}. Seductive, alluring poise inspired by the manhwa style of Capture3.PNG."""

# Generate full list of 78 cards
processed_cards = []
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
        char_spec_inline = f"She is {spec['age']}, {spec['build']}, with {spec['hair']}, {spec['eyes']} eyes, {spec['skin']} skin, and {spec['signature']}."
    
    full_prompt = MASTER_PROMPT_TEMPLATE.format(
        TITLE=title,
        EMBLEM=emblem,
        SCENE=scene,
        CHARACTER_SPEC=char_spec_inline,
        COUNT_LOCK=count_lock,
        FEMME_DIRECTIVE=femme_directive
    )
    
    processed_cards.append({
        "id": slug,
        "n": c['n'],
        "slug": slug,
        "group": c['group'],
        "title": title,
        "name_vi": spec['card_name'] if spec else title,
        "emblem": emblem,
        "femme": c.get('femme', True),
        "age": spec['age'] if spec else (c.get('age') or "N/A"),
        "hair": spec['hair'] if spec else (c.get('hair') or "N/A"),
        "eyes": spec['eyes'] if spec else "N/A",
        "build": spec['build'] if spec else (c.get('build') or "N/A"),
        "skin": spec['skin'] if spec else "N/A",
        "signature": spec['signature'] if spec else "N/A",
        "aura": spec['aura'] if spec else "N/A",
        "scene": scene,
        "count": c.get('count'),
        "count_lock": count_lock,
        "master_prompt": full_prompt
    })

print(f"Processed all {len(processed_cards)} cards with Master Prompt Template!")

# Save to cards_full_master.json
with open('cards_full_master.json', 'w', encoding='utf-8') as f:
    json.dump({
        "meta": {
            "deck": "Sensual Manhwa Tarot — 78 Cards",
            "style_source": "Capture3.PNG (Korean Adult Manhwa Webtoon Style)",
            "template_version": "Master Prompt Specification v2"
        },
        "cards": processed_cards
    }, f, ensure_ascii=False, indent=2)

print("Saved cards_full_master.json successfully!")
