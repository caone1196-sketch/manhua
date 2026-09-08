import json
import re

with open('cards.json', 'r', encoding='utf-8') as f:
    cards_data = json.load(f)

# The signature outfit keywords extracted directly from Capture3.PNG
OUTFIT_DIRECTIVE = "wearing the exact signature outfit from Capture3.PNG: an intricate white strappy harness lingerie cage bikini top, a white leather buckled choker collar necklace, crisscross white body harness straps around the waist, garter straps, and sheer white lace-trimmed thigh-high stockings"

MASTER_PROMPT_TEMPLATE = """A single tarot card built upon the FIRST reference image (the deck's ornamental card template): keep its symmetric ornamental golden frame, the four corner filigree flourishes, the top-center medallion and the bottom band with the small skull ornament EXACTLY as they are — do not redraw, move, recolor or resize any part of the frame. FULL BLEED: the card itself fills the entire image EDGE TO EDGE, corner to corner — there is no background, no margin, no dark band, no drop shadow and no second border outside the ornamental frame; every pixel of the image belongs to the card. Fill the center panel with the new scene, painted in the EXACT master art style and character design of the SECOND reference image (Capture3.PNG Korean adult manhwa webtoon style): identical crisp lineart, alluring character design, seductive blushing expression, glossy skin highlights, soft cell shading, glowing volumetric rim lighting, and the signature white strappy harness lingerie outfit.

LAYOUT (draw in this order):
— TOP: inside the top-center ornamental medallion place this card's EMBLEM: {EMBLEM} — small antique-gold heraldic emblem, centered, no text, no numerals.
— MIDDLE (the empty center panel only): {SCENE}. {CHARACTER_SPEC}
— BOTTOM: in the bottom band, directly beneath the small skull ornament, the title "{TITLE}" — centered, on one line, spelled exactly like that.

TITLE LOCK: the title must be rendered in the EXACT lettering of the title in the reference image — identical typeface, weight, letter-spacing and tracking, gold tone and shading, cap height and stroke width, identical position directly beneath the skull ornament. Copy that letterform character by character for the new words; do not invent a different font, do not use a modern sans-serif. The only text on the card is this title.

{COUNT_LOCK}

{FEMME_DIRECTIVE}

ANATOMY LOCK (HARD CONSTRAINT): exactly two arms, two legs, one head, one torso. Every joint (shoulders, elbows, wrists, hips, knees, ankles) connects naturally to the body. No extra limbs, no fused limbs, no hands merging into torso, no missing fingers, no six-fingered hands. Both arms must be clearly separated from the torso.

THEME: sensual classic tarot in the tradition of vintage art-nude tarot decks and Korean adult manhwa aesthetic — gorgeous young woman entirely at ease in her body, alluring seductive poses, dressed in signature white strappy harness lingerie, buckled choker collar, and lace thigh-high stockings matching Capture3.PNG, warm lighting against subtle shadows, painterly glowing skin with specular glossy highlights.

NEGATIVE: wrong outfit, robes covering body, full dress, medieval cloth, wrong or mismatched title font, modern or sans-serif lettering, extra words, misspelled title, dark margin, empty band, background or mat around the card, drop shadow, vignette, card floating inside the frame, extra or miscounted suit objects, duplicated, fused, cropped or half-hidden objects, extra limbs, extra arms, three arms, extra hand, more than two arms, extra fingers, six-fingered hands, extra heads, distorted anatomy, plastic 3D render, text or numbers anywhere except the bottom title band, watermark, signature, artist name, double border, multiple cards, collage.

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
Character & Outfit design matching Capture3.PNG: gorgeous voluptuous woman ({age}), hair: {hair}, eyes: {eyes}, build: {build}, skin: {skin} with glossy specular highlights, signature: {signature}. Outfit: white strappy leather harness lingerie, buckled choker collar necklace, crisscross waist straps, garter straps, and sheer white lace-trimmed thigh-high stockings."""

for c in cards_data['cards']:
    slug = c['slug']
    title = c['title']
    emblem = c['emblem']
    scene = c['scene']
    count_lock = c['count_lock']
    femme_directive = build_femme_directive(c)
    
    char_spec_inline = f"She is {c.get('age', 'young')}, with {c.get('hair', 'golden hair')}, {c.get('eyes', 'alluring eyes')}, glowing {c.get('skin', 'porcelain')} skin, {OUTFIT_DIRECTIVE}."
    
    full_prompt = MASTER_PROMPT_TEMPLATE.format(
        TITLE=title,
        EMBLEM=emblem,
        SCENE=scene,
        CHARACTER_SPEC=char_spec_inline,
        COUNT_LOCK=count_lock,
        FEMME_DIRECTIVE=femme_directive
    )
    c['master_prompt'] = full_prompt

# Save updated cards.json
with open('cards.json', 'w', encoding='utf-8') as f:
    json.dump(cards_data, f, ensure_ascii=False, indent=2)

print("Updated cards.json with signature Capture3.PNG outfit directive!")
