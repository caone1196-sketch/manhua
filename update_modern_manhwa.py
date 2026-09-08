import json

with open('cards.json', 'r', encoding='utf-8') as f:
    cards_data = json.load(f)

# Modern Manhwa Streamer Art-Nude style directive matching Capture3.PNG
MODERN_MANHWA_ART_NUDE_DIRECTIVE = "modern Korean adult manhwa webtoon aesthetic matching Capture3.PNG: alluring blonde woman with cat eyeliner, blushing cheeks, parted lips, and glossy glowing skin, artistic fine-art nude aesthetic with minimal gossamer sheer draping, barefoot, in a modern streamer studio / luxury penthouse setting with glowing RGB and neon ambient lighting, integrating tarot elemental symbolism into the modern environment"

MASTER_PROMPT_TEMPLATE = """A single vertical tarot card titled '{TITLE}' in modern Korean adult manhwa webtoon style matching Capture3.PNG. Symmetrical ornamental gold modern tarot frame with '{TITLE}' and '{NUM}' on the bottom banner. Full bleed card filling the frame edge to edge.

In the center panel: an alluring, voluptuous young woman with long golden hair, cat eyeliner, blushing cheeks, parted lips, and glowing porcelain skin with glossy specular highlights. She is depicted in an artistic fine-art nude aesthetic with minimal sheer translucent draping, barefoot, seated or posed seductively in a modern Korean streamer room / high-tech penthouse setup with PC monitors, ambient neon lights, and luxury modern furniture.

Tarot Symbolism Integration:
— TOP Emblem: {EMBLEM} rendered as a glowing holographic emblem above.
— Scene & Objects: {SCENE}. {CHARACTER_SPEC}
— {COUNT_LOCK}

High-gloss specular skin highlights, crisp webtoon lineart, vibrant modern neon-pastel lighting, cinematic depth, masterpiece manhwa illustration.

NEGATIVE: shoes, heavy medieval dresses, heavy armor, low quality, bad anatomy, deformed hands, extra limbs, modern casual clothes covering body, dark border, floating frame, text outside bottom banner, watermark, signature."""

def build_modern_scene(card):
    slug = card['slug']
    title = card['title']
    n = card['n']
    emblem = card['emblem']
    
    # Modernized scenes
    modern_scenes = {
        "00-fool": "She is a playful 19-year-old blonde streamer sitting casually barefoot on the edge of a high-rise luxury balcony railing overlooking a glowing cyberpunk morning cityscape, holding a glowing digital white rose, a cute white Pomeranian puppy sitting beside her gaming chair.",
        "01-magician": "She is a charismatic 22-year-old streamer at her multi-monitor streaming desk, arms raised in a commanding pose, four glowing holographic elemental icons floating on her desk: flaming wand stream mic, glowing water cup, crystal cyber blade, and golden crypto coin.",
        "02-priestess": "She sits sensually on a sleek obsidian gaming chair between two tall RGB light bars (one black, one white), a glowing holographic crescent moon beneath her bare feet, holding a glowing digital tablet of secret lore, deep indigo streaming lights.",
        "03-empress": "She reclines luxuriously in a plush velvet recliner in a modern sunlit penthouse garden room, golden sunlight streaming through floor-to-ceiling windows, holding a golden smartphone/scepter, surrounded by lush indoor plants and fresh fruits.",
        "04-emperor": "She sits with dominant poised posture in an executive leather gaming throne with ram-horn headrest designs, RGB volcanic red ambient backlighting, glowing PC setup, holding an Ankh golden stylus and tech orb.",
        "15-devil": "She is a seductive succubus streamer in a dark red-neon gaming room, curved black horns and dark wings, sitting back on a leather gaming seat with arms behind head, loose golden chain links draped across the desk, glowing crimson pentagram RGB on wall.",
        "17-the-star": "She sits in a black gaming chair with arms raised behind her head in the exact pose of Capture3.PNG, dual curved monitors displaying glowing star constellations, pouring two streams of digital light from golden decanters onto a desktop water feature, giant holographic eight-pointed star glowing above.",
        "21-world": "She poses gracefully at the center of a circular RGB ring-light laurel arch in a panoramic high-rise penthouse studio overlooking a 360-degree night skyline, holding two glowing stylus wands, four pet avatar screens at the four corners."
    }
    
    return modern_scenes.get(slug, f"She is in a modern luxury penthouse studio setup, posed seductively in fine-art nude aesthetic, interacting with {emblem} and modern studio setup: {card['scene']}")

for c in cards_data['cards']:
    slug = c['slug']
    title = c['title']
    n = c['n']
    emblem = c['emblem']
    count_lock = c['count_lock']
    
    modern_scene = build_modern_scene(c)
    char_spec = f"She is {c.get('age', '20 years old')}, {c.get('build', 'slender waist with curvy feminine silhouette')}, with {c.get('hair', 'flowing golden hair')}, {c.get('eyes', 'alluring eyes')}, glowing porcelain skin."
    
    c['master_prompt'] = MASTER_PROMPT_TEMPLATE.format(
        TITLE=title,
        NUM=n,
        EMBLEM=emblem,
        SCENE=modern_scene,
        CHARACTER_SPEC=char_spec,
        COUNT_LOCK=count_lock
    )

with open('cards.json', 'w', encoding='utf-8') as f:
    json.dump(cards_data, f, ensure_ascii=False, indent=2)

print("Updated cards.json with Modern Manhwa Streamer Art-Nude style!")
