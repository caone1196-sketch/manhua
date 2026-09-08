import json

with open('cards.json', 'r', encoding='utf-8') as f:
    cards_data = json.load(f)

suit_styles = {
    "major": {
        "00-fool": {
            "hair": "sun-kissed honey-blonde wavy twintails with playful loose strands",
            "eyes": "sparkling emerald green doe eyes, cheerful blushing face",
            "expression": "bright flirtatious smile, playful wink, glowing cheeks",
            "bikini_color": "sheer pastel peach translucent chiffon",
            "bikini_style": "ruffled micro-string triangle bikini with side-tie strings",
            "theme": "sunrise luxury penthouse infinity pool with floating petals"
        },
        "01-magician": {
            "hair": "sleek waist-length raven-black straight hair with straight bangs",
            "eyes": "mystic amethyst-violet cat eyes, sharp winged eyeliner",
            "expression": "smug confident smirk, intense penetrating gaze",
            "bikini_color": "sheer crimson-red translucent wet chiffon",
            "bikini_style": "cross-wrap halter micro-bikini with gold ring accents",
            "theme": "misty ambient penthouse studio with four glowing holographic elemental relics"
        },
        "02-priestess": {
            "hair": "deep auburn-burgundy silky hair in loose elegant cascades",
            "eyes": "mysterious sea-blue heavy-lidded eyes, calm allure",
            "expression": "serene enigmatic half-smile, thoughtful and alluring",
            "bikini_color": "sheer deep sapphire-blue translucent chiffon",
            "bikini_style": "minimalist plunging triangle bikini with silver micro-chains",
            "theme": "monochrome marble bath between obsidian and ivory illuminated pillars"
        },
        "03-empress": {
            "hair": "voluminous ripe-wheat golden blonde cascading curls",
            "eyes": "warm honey-amber almond eyes, radiant feminine warmth",
            "expression": "luxurious sensual smile, soft parted lips, flushed cheeks",
            "bikini_color": "sheer rose-pink translucent wet chiffon",
            "bikini_style": "scalloped micro-bikini with pearl-string waist accents",
            "theme": "lush sunlit greenhouse spa pool with tropical flowers and waterfalls"
        },
        "04-emperor": {
            "hair": "sleek dark chocolate-brown high ponytail with gold hairband",
            "eyes": "piercing storm-grey almond eyes, sharp cat-eye look",
            "expression": "commanding dominant smirk, haughty gaze",
            "bikini_color": "sheer scarlet-crimson translucent chiffon",
            "bikini_style": "high-cut strappy micro-bikini with golden buckle details",
            "theme": "luxury volcanic-rock sauna spa with glowing amber embers"
        },
        "05-hierophant": {
            "hair": "silky espresso-brown wavy bob haircut framing delicate jawline",
            "eyes": "golden-hazel upturned eyes, disciplined yet seductive",
            "expression": "composed graceful smile, dignified allure",
            "bikini_color": "sheer ivory-gold translucent chiffon",
            "bikini_style": "halter-neck micro-string bikini with sacred geometric lace trim",
            "theme": "cathedral-inspired modern glass bath with stained glass reflections"
        },
        "06-lovers": {
            "hair": "soft strawberry-blonde loose beach waves over shoulders",
            "eyes": "dreamy lavender-pink doe eyes, flushed rosy cheeks",
            "expression": "lovestruck passionate expression, softly parted lips",
            "bikini_color": "sheer blush-pink translucent wet chiffon",
            "bikini_style": "sweetheart micro-string bikini with delicate floral lace edge",
            "theme": "romantic rose-water infinity jacuzzi under starry twilight"
        },
        "07-chariot": {
            "hair": "jet-black sporty high ponytail with loose side bangs",
            "eyes": "blazing electric-blue fierce eyes, determined and bold",
            "expression": "confident triumphant smirk, fearless direct gaze",
            "bikini_color": "sheer midnight-navy translucent chiffon with silver sheen",
            "bikini_style": "athletic crisscross strappy micro-bikini with side ties",
            "theme": "modern glass hydro-chamber with glowing blue and white neon tracks"
        },
        "08-strength": {
            "hair": "burnished copper-red thick wild waves flowing past waist",
            "eyes": "warm tiger-amber feline eyes, gentle yet fierce",
            "expression": "tender dominant smile, relaxed confident aura",
            "bikini_color": "sheer golden-yellow translucent wet chiffon",
            "bikini_style": "minimalist sliding micro-triangle bikini with gold cord ties",
            "theme": "golden-hour open-air bath with golden lion sculpture fountain"
        },
        "09-hermit": {
            "hair": "ethereal icy platinum-silver sleek long hair",
            "eyes": "crystal-grey introspective eyes, calm deep wisdom",
            "expression": "mysterious quiet gaze, subtle alluring smile",
            "bikini_color": "sheer smoky-silver translucent chiffon",
            "bikini_style": "delicate micro-bandeau string bikini with frosted accents",
            "theme": "private panoramic snow-view glass onsen with glowing warm lantern"
        },
        "10-wheel": {
            "hair": "multi-tone caramel-gold highlighted wavy locks",
            "eyes": "mesmerizing golden-green hazel eyes, sparkling with fate",
            "expression": "playful unpredictable smirk, teasing gaze",
            "bikini_color": "sheer holographic iridescent translucent chiffon",
            "bikini_style": "asymmetrical micro-string bikini with metallic sheen",
            "theme": "futuristic rotunda pool with rotating holographic constellation wheel"
        },
        "11-justice": {
            "hair": "flawless platinum-blonde straight blunt cut",
            "eyes": "sharp steel-blue discerning eyes, piercing and cold",
            "expression": "cool intellectual smirk, perfectly balanced poise",
            "bikini_color": "sheer emerald-green translucent wet chiffon",
            "bikini_style": "clean geometric micro-triangle bikini with gold ring connectors",
            "theme": "minimalist high-tech glass bath with floating laser-scale lights"
        },
        "12-the-hanged": {
            "hair": "light ash-blonde flowing hair floating upward around head",
            "eyes": "dreamy sky-blue upside-down gaze, euphoric trance",
            "expression": "blissful surrendered smile, completely relaxed",
            "bikini_color": "sheer seafoam-mint translucent chiffon",
            "bikini_style": "wraparound micro-string bikini with suspended sheer ribbons",
            "theme": "underwater zero-gravity glass flotation tank with glowing cyan aura"
        },
        "12-hanged": {
            "hair": "light ash-blonde flowing hair floating upward around head",
            "eyes": "dreamy sky-blue upside-down gaze, euphoric trance",
            "expression": "blissful surrendered smile, completely relaxed",
            "bikini_color": "sheer seafoam-mint translucent chiffon",
            "bikini_style": "wraparound micro-string bikini with suspended sheer ribbons",
            "theme": "underwater zero-gravity glass flotation tank with glowing cyan aura"
        },
        "13-death": {
            "hair": "striking jet-black hair with pure white side-streaks",
            "eyes": "deep onyx-black eyes with obsidian reflections, intense gothic beauty",
            "expression": "captivating mysterious smirk, dangerous fatal allure",
            "bikini_color": "sheer gothic-black translucent wet chiffon",
            "bikini_style": "extreme micro-string triangle bikini with black lace filigree",
            "theme": "dark obsidian bath with floating white mystic roses and sunrise mist"
        },
        "14-temperance": {
            "hair": "soft coral-pink wavy hair gently drifting in breeze",
            "eyes": "serene turquoise-blue eyes, harmonious and gentle",
            "expression": "pure tranquil smile, soothing peaceful aura",
            "bikini_color": "sheer gradient lavender-to-peach translucent chiffon",
            "bikini_style": "two-tone micro-chiffon bikini with floating water-drop beads",
            "theme": "tranquil indoor waterfall stream with dual crystal pouring pools"
        },
        "15-devil": {
            "hair": "vibrant crimson-ruby long wavy hair with dark undertones",
            "eyes": "smoldering fiery ruby-red cat eyes, hypnotic and dangerous",
            "expression": "devilish seductive grin, biting lower lip playfully",
            "bikini_color": "sheer midnight-black and crimson translucent chiffon",
            "bikini_style": "daring cut-out micro-string bikini with red metal rings",
            "theme": "dark luxury red-neon spa with floating golden chains and glowing embers"
        },
        "16-tower": {
            "hair": "wild dynamic platinum-gold wind-blown hair",
            "eyes": "electrifying topaz-gold wide eyes, adrenaline rush",
            "expression": "thrilled ecstatic gasp, wild untamed excitement",
            "bikini_color": "sheer electric-orange and gold translucent chiffon",
            "bikini_style": "strappy high-leg micro-bikini with lightning-inspired lines",
            "theme": "penthouse infinity pool during dramatic neon thunderstorm"
        },
        "17-the-star": {
            "hair": "shimmering platinum-golden long hair cascading to lower back",
            "eyes": "star-bright radiant blue almond eyes, crystalline clarity",
            "expression": "angelic seductive smile, serene hopeful gaze",
            "bikini_color": "sheer pure white translucent wet chiffon",
            "bikini_style": "classic micro-triangle string bikini hugging every curve",
            "theme": "nighttime rooftop infinity pool overlooking city skyline beneath giant star"
        },
        "18-moon": {
            "hair": "honey-blonde wet hair framing cheeks, dripping water",
            "eyes": "alluring hazel-grey hooded eyes, flushed rosy cheeks",
            "expression": "intoxicated sultry half-smile, parted lips, heavy gaze",
            "bikini_color": "sheer lilac-purple translucent wet chiffon",
            "bikini_style": "delicate low-rise string micro-bikini with side ties",
            "theme": "luxury glass rain-shower with neon purple lighting and moon phases"
        },
        "19-sun": {
            "hair": "radiant sunburst golden-yellow voluminous flowing locks",
            "eyes": "warm sparkling amber-brown doe eyes, overflowing vitality",
            "expression": "ecstatic beaming smile, radiant joyful sensuality",
            "bikini_color": "sheer bright marigold-gold translucent wet chiffon",
            "bikini_style": "sunny micro-bikini with tiny golden sunflower charm at center",
            "theme": "sun-drenched poolside terrace bathed in brilliant golden sunbeams"
        },
        "20-judgement": {
            "hair": "silvery-white long hair floating like a cloud of silk",
            "eyes": "luminescent golden-hazel wide eyes, profound awakening",
            "expression": "reborn ecstatic expression, head tilted up toward light",
            "bikini_color": "sheer pearlescent white translucent chiffon",
            "bikini_style": "ethereal micro-string bikini with pearl-drop connectors",
            "theme": "illuminated crystal bath rising with golden mist and heavenly rays"
        },
        "21-world": {
            "hair": "luxurious chestnut-brown hair woven with golden threads",
            "eyes": "kaleidoscopic multi-faceted emerald-gold eyes, ultimate perfection",
            "expression": "triumphant goddess-like smile, supreme confidence",
            "bikini_color": "sheer emerald-and-gold translucent wet chiffon",
            "bikini_style": "regal micro-bikini with delicate golden filigree chain trims",
            "theme": "panoramic 360-degree glass penthouse rotunda pool with RGB ring light"
        }
    },
    "wands": {
        "color": "sheer fiery-orange / flame-red / warm amber translucent chiffon",
        "style": "sporty cross-tie micro-string bikinis with fiery accents",
        "hair_theme": "auburn, copper-red, chestnut, and warm golden tones"
    },
    "cups": {
        "color": "sheer ocean-cyan / aqua-blue / lagoon-teal translucent chiffon",
        "style": "graceful scalloped and ruffled micro-string bikinis with water-drop charms",
        "hair_theme": "silky black, deep brunette, and soft flowing wavy locks"
    },
    "swords": {
        "color": "sheer icy-silver / crystal-cyan / steel-blue translucent chiffon",
        "style": "sleek geometric sharp-cut micro-string bikinis with metallic ring connectors",
        "hair_theme": "platinum-blonde, ash-grey, and razor-sharp sleek straight styles"
    },
    "pentacles": {
        "color": "sheer emerald-green / olive-gold / champagne-bronze translucent chiffon",
        "style": "luxurious low-rise micro-string bikinis with golden chain links and coin charms",
        "hair_theme": "rich honey-brown, chocolate, and golden-bronze braided styles"
    }
}

for c in cards_data['cards']:
    slug = c['slug']
    group = c['group']
    
    # Handle THE HANGED title and file
    if 'hanged' in slug:
        c['title'] = 'THE HANGED'
        c['file'] = 'major_12_the_hanged.png'

    if group == 'major' and slug in suit_styles['major']:
        custom = suit_styles['major'][slug]
        c['hair_style'] = custom['hair']
        c['eyes_style'] = custom['eyes']
        c['expression_style'] = custom['expression']
        c['bikini_color'] = custom['bikini_color']
        c['bikini_style'] = custom['bikini_style']
    elif group in suit_styles:
        suit_info = suit_styles[group]
        c['bikini_color'] = suit_info['color']
        c['bikini_style'] = suit_info['style']
        c['hair_style'] = c.get('hair') or f"stylish {suit_info['hair_theme']}"
        c['eyes_style'] = c.get('eyes') or "alluring cat eyes, winged eyeliner"
        c['expression_style'] = "seductive charming smile, blushing rosy cheeks, parted lips"

with open('cards.json', 'w', encoding='utf-8') as f:
    json.dump(cards_data, f, ensure_ascii=False, indent=2)

print("cards.json updated successfully!")
