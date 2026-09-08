import json

with open('cards.json', 'r', encoding='utf-8') as f:
    cards_data = json.load(f)

# Frameless without numbers
FRAMELESS_NO_NUM_TEMPLATE = """A vertical Korean adult webtoon illustration in manhwa art style matching Capture3.PNG. 
COMPLETELY FRAMELESS: no decorative borders, no card borders, no banner ribbon, edge-to-edge illustration. Only the clean title text '{TITLE}' in elegant antique gold lettering centered at the bottom (NO numbers, NO Roman numerals).

Character & Outfit: An alluring, voluptuous young woman with long golden hair, cat eyeliner, blushing cheeks, parted lips, and glowing porcelain skin with glossy specular highlights. She wears a form-fitting translucent sheer white chiffon micro-bikini hugging her figure tightly, emphasizing bust contours, narrow waist, and glowing skin highlights through the thin fabric.

Scene & Atmosphere: {SCENE}. {CHARACTER_SPEC}

Tarot Symbolism: {EMBLEM} integrated naturally into the modern environment with neon/RGB lighting and ambient reflections.
{COUNT_LOCK}

High-gloss specular skin highlights, crisp webtoon lineart, cinematic ambient lighting, masterpiece manhwa illustration.

NEGATIVE: numbers, roman numerals, borders, frames, banner, ribbon, margin, outer box, shoes, heavy clothes, casual street clothes, deformed hands, extra limbs, bad anatomy, low quality, watermark, signature."""

for c in cards_data['cards']:
    title = c['title']
    emblem = c['emblem']
    count_lock = c['count_lock']
    scene = c['scene']
    char_spec = f"She is {c.get('age', '20 years old')}, {c.get('build', 'slender waist with curvy feminine silhouette')}, with {c.get('hair', 'flowing golden hair')}, {c.get('eyes', 'alluring eyes')}, glowing porcelain skin."
    
    c['master_prompt'] = FRAMELESS_NO_NUM_TEMPLATE.format(
        TITLE=title,
        EMBLEM=emblem,
        SCENE=scene,
        CHARACTER_SPEC=char_spec,
        COUNT_LOCK=count_lock
    )

with open('cards.json', 'w', encoding='utf-8') as f:
    json.dump(cards_data, f, ensure_ascii=False, indent=2)

print("Updated cards.json with frameless no-numbers template!")
