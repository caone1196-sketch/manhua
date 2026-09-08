import json

with open('cards.json', 'r', encoding='utf-8') as f:
    cards_data = json.load(f)

# Master prompt template strictly matching the standard of The Moon & The Star (Wet sheer white chiffon triangle bikini, frameless, no numbers)
WET_CHIFFON_MASTER_PROMPT_TEMPLATE = """A vertical Korean adult webtoon illustration in manhwa art style matching Capture3.PNG. 
COMPLETELY FRAMELESS: no decorative borders, no card frames, no banner ribbon, edge-to-edge illustration. Only the clean title text '{TITLE}' in elegant antique gold lettering centered at the bottom (NO numbers, NO Roman numerals).

Character & Outfit: An alluring, voluptuous young woman with long golden hair, cat eyeliner, blushing cheeks, parted lips, and glowing porcelain skin with glossy specular highlights. She is barefoot with completely bare feet and legs. She wears a form-fitting wet translucent sheer white chiffon triangle bikini top and matching low-rise string bottoms hugging her figure tightly, emphasizing bust contours, narrow waist, and rosy glowing skin highlights through the wet translucent fabric, with glistening water droplets on her skin.

Scene & Atmosphere: {SCENE}. {CHARACTER_SPEC}

Tarot Symbolism: {EMBLEM} integrated naturally into the modern luxury environment with glowing ambient lighting.
{COUNT_LOCK}

High-gloss specular wet skin highlights, crisp webtoon lineart, cinematic ambient lighting, masterpiece manhwa illustration.

NEGATIVE: numbers, roman numerals, borders, frames, banner, ribbon, margin, outer box, shoes, boots, sandals, socks, heavy clothes, casual street clothes, deformed hands, extra limbs, bad anatomy, low quality, watermark, signature."""

for c in cards_data['cards']:
    title = c['title']
    emblem = c['emblem']
    count_lock = c['count_lock']
    scene = c['scene']
    char_spec = f"She is {c.get('age', '20 years old')}, {c.get('build', 'slender waist with curvy feminine silhouette')}, with {c.get('hair', 'flowing golden hair')}, {c.get('eyes', 'alluring eyes')}, glowing porcelain skin."
    
    c['master_prompt'] = WET_CHIFFON_MASTER_PROMPT_TEMPLATE.format(
        TITLE=title,
        EMBLEM=emblem,
        SCENE=scene,
        CHARACTER_SPEC=char_spec,
        COUNT_LOCK=count_lock
    )

with open('cards.json', 'w', encoding='utf-8') as f:
    json.dump(cards_data, f, ensure_ascii=False, indent=2)

print("Updated cards.json with wet sheer chiffon triangle bikini standard!")
