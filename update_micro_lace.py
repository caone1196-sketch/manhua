import json

with open('cards.json', 'r', encoding='utf-8') as f:
    cards_data = json.load(f)

# Ultra-minimalist sheer white lace micro lingerie directive
MICRO_LACE_DIRECTIVE = "wearing ultra-minimalist sheer white micro-lace lingerie, tiny translucent micro lace bralette barely covering the bust, tiny sheer micro lace bottoms, thin white lace choker, and sheer white lace thigh-high stockings, maximizing skin exposure with minimal coverage"

MASTER_PROMPT_TEMPLATE = """A single tarot card built upon the FIRST reference image (the deck's ornamental card template): keep its symmetric ornamental golden frame, the four corner filigree flourishes, the top-center medallion and the bottom band with the small skull ornament EXACTLY as they are — do not redraw, move, recolor or resize any part of the frame. FULL BLEED: the card itself fills the entire image EDGE TO EDGE, corner to corner. Fill the center panel with the new scene, painted in the EXACT master art style of the SECOND reference image (Korean adult manhwa webtoon style): identical crisp lineart, alluring character design, seductive blushing expression, glossy skin highlights, soft cell shading, glowing volumetric rim lighting, and ultra-minimalist sheer white micro-lace lingerie barely covering sensitive areas.

LAYOUT (draw in this order):
— TOP: inside the top-center ornamental medallion place this card's EMBLEM: {EMBLEM} — small antique-gold heraldic emblem, centered, no text, no numerals.
— MIDDLE (the empty center panel only): {SCENE}. {CHARACTER_SPEC}
— BOTTOM: in the bottom band, directly beneath the small skull ornament, the title "{TITLE}" — centered, on one line, spelled exactly like that.

TITLE LOCK: the title must be rendered in the EXACT lettering of the title in the reference image — identical typeface, weight, letter-spacing and tracking, gold tone and shading, cap height and stroke width, identical position directly beneath the skull ornament. The only text on the card is this title.

{COUNT_LOCK}

{FEMME_DIRECTIVE}

ANATOMY LOCK (HARD CONSTRAINT): exactly two arms, two legs, one head, one torso. Every joint connects naturally to the body. No extra limbs, no fused limbs, no hands merging into torso, no missing fingers, no six-fingered hands. Both arms clearly separated from the torso.

THEME: sensual classic tarot in the tradition of vintage art-nude tarot decks and Korean adult manhwa aesthetic — gorgeous young woman entirely at ease in her body, alluring seductive poses, dressed in ultra-minimalist sheer white micro-lace lingerie, thin lace choker, and lace thigh-high stockings maximizing bare skin, warm lighting against subtle shadows, painterly glowing skin with specular glossy highlights.

NEGATIVE: thick heavy armor, heavy cloth robes, medieval heavy dresses, full coverage clothes, wrong or mismatched title font, modern or sans-serif lettering, extra words, misspelled title, dark margin, empty band, background or mat around the card, drop shadow, vignette, card floating inside the frame, extra or miscounted suit objects, duplicated, fused, cropped or half-hidden objects, extra limbs, extra arms, three arms, extra hand, more than two arms, extra fingers, six-fingered hands, extra heads, distorted anatomy, plastic 3D render, text or numbers anywhere except the bottom title band, watermark, signature, artist name, double border, multiple cards, collage.

No other text, no watermark, single card only."""

def build_femme_directive(card):
    if not card.get("femme"):
        return "SCENE ONLY: Divine relic / landscape card with no central human figure."
    age = card.get('age', '20 years old')
    hair = card.get('hair', 'long golden blonde waves')
    eyes = card.get('eyes', 'amber-brown alluring eyes')
    build = card.get('build', 'voluptuous, slender waist, curvy feminine physique')
    skin = card.get('skin', 'porcelain with glossy highlights')
    signature = card.get('signature', 'winged cat eyeliner, flushed cheeks')
    
    return f"""FEMALE FIGURE DIRECTIVE — 100% FEMALE ({age}):
Character & Outfit design: gorgeous voluptuous woman ({age}), hair: {hair}, eyes: {eyes}, build: {build}, skin: {skin} with glossy specular highlights, signature: {signature}. Outfit: ultra-minimalist sheer white micro-lace lingerie, tiny micro lace top, tiny micro lace bottoms, thin lace choker collar, and sheer white lace thigh-high stockings with maximum bare skin."""

for c in cards_data['cards']:
    title = c['title']
    emblem = c['emblem']
    scene = c['scene']
    count_lock = c['count_lock']
    femme_directive = build_femme_directive(c)
    
    char_spec_inline = f"She is {c.get('age', 'young')}, with {c.get('hair', 'golden hair')}, {c.get('eyes', 'alluring eyes')}, glowing {c.get('skin', 'porcelain')} skin, {MICRO_LACE_DIRECTIVE}."
    
    full_prompt = MASTER_PROMPT_TEMPLATE.format(
        TITLE=title,
        EMBLEM=emblem,
        SCENE=scene,
        CHARACTER_SPEC=char_spec_inline,
        COUNT_LOCK=count_lock,
        FEMME_DIRECTIVE=femme_directive
    )
    c['master_prompt'] = full_prompt

with open('cards.json', 'w', encoding='utf-8') as f:
    json.dump(cards_data, f, ensure_ascii=False, indent=2)

print("Updated cards.json with ultra-minimalist micro-lace lingerie!")
