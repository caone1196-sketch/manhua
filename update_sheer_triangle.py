import json

with open('cards.json', 'r', encoding='utf-8') as f:
    cards_data = json.load(f)

# Translucent sheer white chiffon triangle micro-bikini with prominent contours
SHEER_CHIFFON_CONTOUR_DIRECTIVE = "wearing a form-fitting translucent sheer white chiffon triangle bikini top and matching low-rise string bottoms hugging her figure tightly, emphasizing bust contours, narrow waist, and glowing skin highlights through the sheer fabric, bare shoulders, white choker, and white thigh-high stockings"

MASTER_PROMPT_TEMPLATE = """A single vertical tarot card titled '{TITLE}' in modern Korean adult manhwa webtoon style matching Capture3.PNG. Symmetrical ornamental gold modern tarot frame with '{TITLE}' and '{NUM}' on the bottom banner. Full bleed card filling the frame edge to edge.

In the center panel: an alluring, voluptuous young woman with long golden hair, cat eyeliner, blushing cheeks, parted lips, and glowing porcelain skin with glossy specular highlights. She wears a form-fitting translucent sheer white chiffon triangle bikini top and matching low-rise string bottoms hugging her figure tightly, emphasizing bust contours, narrow waist, and glowing skin highlights through the sheer fabric, bare shoulders, white choker, and white thigh-high stockings. Seated or posed seductively in a modern Korean streamer room with multi-monitors, gaming PC desk, ambient RGB neon lights, and luxury streaming setup.

Tarot Symbolism Integration:
— TOP Emblem: {EMBLEM} rendered as a glowing holographic emblem above.
— Scene & Objects: {SCENE}. {CHARACTER_SPEC}
— {COUNT_LOCK}

High-gloss specular skin highlights, crisp webtoon lineart, vibrant modern neon-pastel lighting, cinematic depth, masterpiece manhwa illustration.

NEGATIVE: shoes, heavy medieval dresses, heavy armor, low quality, bad anatomy, deformed hands, extra limbs, modern casual clothes covering body, dark border, floating frame, text outside bottom banner, watermark, signature."""

for c in cards_data['cards']:
    title = c['title']
    n = c['n']
    emblem = c['emblem']
    count_lock = c['count_lock']
    scene = c['scene']
    char_spec = f"She is {c.get('age', '20 years old')}, {c.get('build', 'slender waist with curvy feminine silhouette')}, with {c.get('hair', 'flowing golden hair')}, {c.get('eyes', 'alluring eyes')}, glowing porcelain skin, {SHEER_CHIFFON_CONTOUR_DIRECTIVE}."
    
    c['master_prompt'] = MASTER_PROMPT_TEMPLATE.format(
        TITLE=title,
        NUM=n,
        EMBLEM=emblem,
        SCENE=scene,
        CHARACTER_SPEC=char_spec,
        COUNT_LOCK=count_lock
    )

with open('cards.json', 'w', encoding='utf-8') as f:
    json.dump(cards_data, f, ensure_ascii=False, indent=2)

print("Updated cards.json with sheer chiffon triangle micro-bikini directive!")
