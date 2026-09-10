#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
build_prompts_v3_star.py
------------------------
Sinh prompt v3 "Star-Couture" cho 22 lá Ẩn Chính (Major Arcana).

Khác biệt so với prompts_frameless_v2:
  * Ảnh tham chiếu DUY NHẤT:  "the star.png"  (repo root)
    -> lấy CẤU TRÚC PHỤC TRANG + cách vẽ trang sức + render vải của ảnh đó
       (bandeau vải gấp nếp + khuy tròn đồng cổ, dải vải đan chéo bụng,
        quần cut cao + dây chuyền hông đính đá quý lớn + dải lụa thêu sa xuống
        giữa đùi, khăn voan tulle trắng viền sao vàng, vòng tay chạm lộng,
        vương miện trán có giọt đá, da bóng mờ manhwa).
    -> KHÔNG còn concept "vải ướt sũng / bikini tuột xuống eo" của v2.
  * An toàn: trang phục opaque, phủ kín ngực, 100% người trưởng thành (20+).

Chạy:  python3 build_prompts_v3_star.py
Ra:   prompts_frameless_v3_star/<slug>.md + all_prompts.json + README.md
"""

import json
import os
import re
import unicodedata

ROOT = os.path.dirname(os.path.abspath(__file__))
CARDS_JSON = os.path.join(ROOT, "cards.json")
OUT_DIR = os.path.join(ROOT, "prompts_frameless_v3_star")
STYLE_REF = "the star.png"

# `the star.png` CÓ khung vàng ornamental mỏng + corner filigree + band chữ serif dưới đáy.
# WITH_FRAME = True  -> đúng y như lá tham chiếu (mặc định v3.1)
# WITH_FRAME = False -> giữ quy ước frameless của prompts_frameless_v2
WITH_FRAME = True

# OUTFIT_MODE:
#   "couture"      = phục trang nhiều lớp như lá mẫu (bandeau + dải chéo + panel lụa)
#   "wet_lingerie"    = nội y satin mỏng ướt (v3.2)
#   "bikini_two_piece" = bikini 2 mảnh (v3.3, yêu cầu hiện tại)
#   "verbatim_v2"      = lấy ĐÚNG NGUYÊN VĂN dòng "- **Outfit:**" của prompts_frameless_v2/<slug>.md,
#                        không sửa một chữ (yêu cầu: "trang phục đúng prompts không chỉnh sửa")
OUTFIT_MODE = "verbatim_v2"

# --------------------------------------------------------------------------
# Dữ liệu 22 lá Ẩn Chính: tên, biểu tượng, sàn cảnh, đá quý/accent phục trang,
# tư thế, mô tả bối cảnh + props.
# --------------------------------------------------------------------------
MAJORS = [
    dict(slug="00-fool", n="0", title="THE FOOL",
         emblem="a white rose", gem="a pale moonstone", metal="antique gold",
         cloth="pearl-ivory", scene="Rooftop infinity pool at sunrise",
         pose="barefoot mid-step on the wet stone coping at the very end of the rooftop infinity pool, "
              "one heel still hovering in the air, both hands cupping a single white rose at her collarbone, "
              "chin dipped, eyes lowered to the petals in a dreamy absorbed smile, shoulders soft and relaxed",
         extra="the stone coping visibly stops two flagstones ahead of her feet and beyond it is only open sky "
               "over a tiny sunrise city, a cute white Pomeranian puppy trots after her along the pool rim, "
               "steam curls off the calm pool",
         props=None),
    dict(slug="01-magician", n="I", title="THE MAGICIAN",
         emblem="an infinity symbol", gem="a deep lapis lazuli", metal="antique gold",
         cloth="midnight-black satin", scene="Marble vanity mirror wall bath",
         pose="seated sideways on the marble tub rim, spine tall, one arm straight back propping her on the stone, "
              "the other arm raised with two fingers drawing a slow arc of golden light in the mirror in front of her, "
              "one leg bent with the foot in the shallow water, the other trailing along the marble",
         extra="a wall of lit vanity mirrors repeats her silhouette, a marble altar ledge at her side holds one "
               "cup, one sword, one wand and one coin",
         props=dict(n=4, obj="suit objects", layout="exactly four objects on the altar ledge: one cup, one sword, "
                                                    "one wand, one coin — all four wholly visible, no duplicates")),
    dict(slug="02-priestess", n="II", title="THE HIGH PRIESTESS",
         emblem="a pomegranate", gem="a moonlit blue sapphire", metal="white gold and gold",
         cloth="pearl-ivory", scene="Twin-column temple bath",
         pose="seated in full profile on the low altar bench between the two pillars, knees together and folded away "
              "from camera, an open leather codex resting on her lap, head inclined over the page, one hand holding "
              "the page's edge",
         extra="two veils of falling water glow behind the columns, a waxing crescent crown at her hairline, "
               "the letter J and P carved and lit on the dark and the light column",
         props=None),
    dict(slug="03-empress", n="III", title="THE EMPRESS",
         emblem="a twelve-star crown", gem="a green emerald", metal="antique gold",
         cloth="rose-blush satin", scene="Sunlit garden sunroom bath",
         pose="reclining gracefully on a carved wooden daybed beneath the glass roof, one elbow propped on silk "
              "cushions, the other hand lifting a golden Venus scepter over her shoulder, hips angled toward "
              "the warm light, a soft indulgent smile",
         extra="a twelve-star wreath crown floats in her hair, ripe wheat and trailing ivy climb the sunroom "
               "frame, warm light pools over a field of poppies beyond the glass",
         props=None),
    dict(slug="04-emperor", n="IV", title="THE EMPEROR",
         emblem="a ram's head", gem="a warm amber citrine", metal="brushed bronze and gold",
         cloth="burnished gold-bronze", scene="Stone steam-room throne",
         pose="seated square on the carved stone throne, back straight, both hands resting flat on the ram-head "
              "armrests, chin level, gaze steady and commanding straight at the viewer, one ankle crossed over "
              "the other knee",
         extra="a bronze ram-head rainfall head pours a wide sheet of water behind the throne, dry cracked "
               "mountain rock visible through the arched window, warm steam rolling across the floor",
         props=None),
    dict(slug="05-hierophant", n="V", title="THE HIEROPHANT",
         emblem="two crossed golden keys", gem="a ruby", metal="antique gold",
         cloth="ivory and cherry-red silk", scene="Byzantine gilded chapel bath",
         pose="standing tall and serene at the centre of the low marble step, weight on one leg, hips soft, "
              "both hands raised at chest height holding two crossed golden keys, blessings given with a calm "
              "half-smile, eyes lowered to the viewer",
         extra="a gold-ground mosaic of a rose window arches over her, two carved stone lecterns stand empty at "
               "either side, candle smoke drifts through a shaft of light",
         props=None),
    dict(slug="06-lovers", n="VI", title="THE LOVERS",
         emblem="an apple coiled by a serpent", gem="a rose quartz", metal="rose gold",
         cloth="pearl-ivory", scene="Rose-petal twin-tub spa",
         pose="reclining back in the left copper claw-foot tub, one arm draped loosely over the rolled copper rim, "
              "body in a long soft curve toward the second tub, the free hand accepting a ripe apple offered to her "
              "across the water, eyes bright and shy on the giver",
         extra="two claw-foot tubs face each other across a shallow pool of floating rose petals, a winged figure "
               "of light blesses them from the frosted window above, a serpent coils on the branch behind the "
               "right tub",
         props=None),
    dict(slug="07-chariot", n="VII", title="THE CHARIOT",
         emblem="a winged sun disk", gem="a lapis lazuli", metal="antique gold and silver",
         cloth="midnight-black with gold", scene="Motorsport penthouse bath",
         pose="standing in the ankle-deep water, shoulders squared, both hands gripping two taut rein handles at "
              "either side, chest lifted, chin up, hair lifted by the wind of an arriving engine",
         extra="a chrome and carbon chariot-like hypercar idles behind a rain-wet glass wall, two sphinx figures "
               "crouch on the hood, a star-map ceiling wheels slowly above, blue LED strips under the water",
         props=None),
    dict(slug="08-strength", n="VIII", title="STRENGTH",
         emblem="a red rose", gem="a carnelian", metal="antique gold",
         cloth="aqua-teal satin", scene="Safari-lodge stone bath",
         pose="kneeling at the head of the stone bath, leaning in close, both hands cradling the great lion's muzzle "
              "with unhurried tenderness, forehead nearly touching his, a quiet patient smile",
         extra="a huge male lion lies calmly across her knees on the warm stone, red rose petals scattered on the "
               "water, acacia branches and golden sunset dust outside the lodge opening",
         props=None),
    dict(slug="09-hermit", n="IX", title="THE HERMIT",
         emblem="a glowing lantern", gem="an amber", metal="aged brass and gold",
         cloth="heather-grey silk with gold", scene="Candlelit mountain grotto",
         pose="standing in profile on the rock ledge cut into the bath floor, one arm raised high holding a "
              "six-pointed lantern, the other hand resting flat on the cold stone, head bowed slightly into "
              "the lantern's warm light",
         extra="snow-capped peaks beyond the grotto mouth, hundreds of floating candles on black still water, "
               "the lantern glows from within",
         props=None),
    dict(slug="10-wheel", n="X", title="WHEEL OF FORTUNE",
         emblem="a spoked golden wheel", gem="a golden topaz", metal="antique gold",
         cloth="metallic gold", scene="Casino-noir roulette bath",
         pose="side-lying along the marble ledge propped on one forearm, legs in one long line under the water, "
              "the free hand resting lightly on the rim of a slowly turning golden wheel, wet hair combed off "
              "her face, amused half-smile",
         extra="a colossal spoked wheel of gold turns in the steam behind her, four zodiac creatures carved at its "
               "corners, red lacquer and black marble, chandelier light glinting on wet tile",
         props=dict(n=1, obj="sword", layout="exactly one short sword fixed upright at the crown of the wheel; "
                                             "no other blade anywhere on the card")),
    dict(slug="11-justice", n="XI", title="JUSTICE",
         emblem="balanced golden scales", gem="a clear pearl", metal="antique gold",
         cloth="cherry-red silk over ivory", scene="Monochrome scales bath",
         pose="standing tall and square between two shallow basins, left hand lifting a straight double-edged "
              "sword beside her face, right hand holding a pair of golden scales perfectly level, expression "
              "impartial and calm, eyes on the viewer",
         extra="black-and-white marble checker floor under shallow water, a grey curtain of falling water behind, "
               "harsh single-source light with no colour cast, mirrored scale motifs on the walls",
         props=dict(n=1, obj="sword", layout="exactly one sword, held upright in her left hand; no other blade "
                                             "on the card")),
    dict(slug="12-hanged", n="XII", title="THE HANGED MAN",
         emblem="an inverted living branch", gem="an amethyst", metal="oxidised gold",
         cloth="pearl-ivory", scene="Inversion silk studio",
         pose="hanging inverted from a silken loop on a T-shaped beam, one ankle hooked, the other knee bent over "
              "the loop, both hands folded calmly behind her back, hood of soft light around her head, a serene "
              "smiling face turned up to the camera",
         extra="water and petals fall UPWARD off the pool above her head, the studio's silk backdrop ripples as "
               "if underwater, a living branch sprouts leaves where her foot crosses the beam",
         props=None),
    dict(slug="13-death", n="XIII", title="DEATH",
         emblem="a five-petaled white rose", gem="a black onyx", metal="blackened silver and gold",
         cloth="onyx-black silk", scene="Gothic onyx & lilies bath",
         pose="standing knee-deep in the black water, body turned three-quarters away but face back to the "
              "viewer, one hand holding a five-petaled white rose out toward the camera, the other arm loose "
              "at her side, expression gentle and unafraid",
         extra="white lilies float on the ink-black water, a pale war horse's head rises from the mist behind "
               "her shoulder, a gothic rose window with the sun setting behind it, fallen crowns and bishop's "
               "mitre resting on the half-submerged steps",
         props=None),
    dict(slug="14-temperance", n="XIV", title="TEMPERANCE",
         emblem="a triangle within a square", gem="an aquamarine", metal="antique gold",
         cloth="aqua-teal silk", scene="Zen ryokan ofuro",
         pose="standing in graceful contrapposto between the two stone basins, right arm raised tipping a golden "
              "chalice, left hand low with a second chalice waiting, a single thin unbroken stream of water arcs "
              "between them, eyes half-closed in concentration, one foot flat on a stepping stone",
         extra="cedar slats, raked gravel, a red maple branch overhanging the ofuro, a golden triangle-and-square "
               "motif worked into the lantern glass, steam in soft horizontal layers",
         props=dict(n=2, obj="chalices", layout="exactly two golden chalices, one in each hand, both bowls fully "
                                                 "visible and un-occluded")),
    dict(slug="15-devil", n="XV", title="THE DEVIL",
         emblem="an inverted pentagram", gem="a garnet", metal="black iron and gold",
         cloth="rose-blush satin with black", scene="Crimson neon gothic bath",
         pose="kneeling upright on the wet stone floor, thighs together, torso arched back, both wrists lifted "
              "to eye level as she holds a loose loop of gold chain away from her own arms with a look of "
              "deliberate, unbothered freedom",
         extra="a colossal shadowed horned silhouette grins on the back wall beneath an inverted pentagram of "
               "neon, two chained figures at the corners stand idle, red LED light bleeding across black tiles",
         props=None),
    dict(slug="16-tower", n="XVI", title="THE TOWER",
         emblem="a jagged lightning bolt", gem="a tourmaline", metal="antique gold",
         cloth="molten gold-bronze", scene="Storm skyscraper glass bath",
         pose="seated on the tub edge leaning toward the floor-to-ceiling glass, one palm pressed flat against "
              "the wet window, the other arm wrapped around herself, hair lifting, eyes wide and lit from in "
              "front as lightning strikes the tower",
         extra="a lightning bolt strikes a neighbouring tower and a crown tumbles through the rain-streaked sky, "
               "three small figures falling far below, the marble bathroom lit only by the strike and by city "
               "glow, glass flexing, everything wet",
         props=None),
    dict(slug="17-the-star", n="XVII", title="THE STAR",
         emblem="an eight-pointed star", gem="a luminous pearl", metal="antique gold",
         cloth="pearl-ivory", scene="Open-sky stargazer bath",
         pose="kneeling back on her heels in the shallow circular tub exactly as in the style reference, both "
              "arms raised high overhead in a wide V, each hand tipping a golden decanter, her whole body one "
              "long graceful vertical line, head tipped back, eyes half-closed, lips softly parted",
         extra="a glass-dome skylight opens on a star constellation, an eight-pointed star glows above her, the "
               "two thin streams of water fall onto her chest and hips and back into the tub, tiny stars reflect "
               "on the water",
         props=dict(n=2, obj="jugs", layout="exactly two golden decanters, one in each raised hand, both fully "
                                            "visible")),
    dict(slug="18-moon", n="XVIII", title="THE MOON",
         emblem="a crescent moon dripping dew", gem="a blue sapphire", metal="antique gold",
         cloth="pearl-ivory", scene="Midnight lagoon",
         pose="kneeling back on her heels on the open stone floor exactly as in the style reference, both arms "
              "raised straight overhead gripping the hilt of one great sword, the blade angled down across her, "
              "elbows framing her face, expression calm and glassy-eyed",
         extra="a giant full moon with a sleeping face rises between two far towers, a wolf howls from a rock to "
               "the left and a dog crouches to the right, a crayfish claws out of the pool at the bottom of a "
               "keyhole path, the floor is a circular mosaic of lunar phases set in dark stone",
         props=dict(n=1, obj="sword", layout="exactly one great sword, held overhead in both hands; no other "
                                             "blade anywhere on the card")),
    dict(slug="19-sun", n="XIX", title="THE SUN",
         emblem="a radiant sun face", gem="a golden citrine", metal="polished gold",
         cloth="sun-gold silk", scene="Golden solarium",
         pose="standing in a shaft of pure gold light, both arms opened wide and lifted, face turned up to the "
              "blaze, weight on one leg, laughing openly, hair blown back as if by hot wind",
         extra="fourteen sunflower heads ring the solarium wall behind a bright grinning sun face, a red banner "
               "drapes over low brick garden walls, warm light bleaches every shadow to peach",
         props=None),
    dict(slug="20-judgement", n="XX", title="JUDGEMENT",
         emblem="a golden trumpet", gem="a ruby", metal="antique gold",
         cloth="dove-white silk with gold", scene="Celestial trumpet dawn",
         pose="rising up on tiptoe in a full-body stretch from a coiled position, both arms lifted overhead and "
              "crossed at the wrists, back arched, mouth open in the first note of a song, dawn light breaking "
              "over her",
         extra="a great angelic wing unfurls behind her across the frosted glass, a golden trumpet sounds at "
               "the apex of light, below her the water surface breaks open and pale arms rise out of it, an "
               "angel banner of red cloth at the horizon",
         props=None),
    dict(slug="21-world", n="XXI", title="THE WORLD",
         emblem="a laurel wreath oval", gem="a jade", metal="antique gold",
         cloth="rose-blush and gold", scene="360° panorama ring bath",
         pose="caught mid-dance inside a floating oval laurel wreath, one leg lifted and crossed behind the other, "
              "both hands holding two short wands out to either side at shoulder height, torso twisted toward "
               "camera, laughing, veils and hair streaming in a circle around her",
         extra="the wreath turns slowly over a circular glass-floored bath with a 360° panorama of mountains and "
               "sea beyond, four small zodiac creatures watch from the four corners, sunset gold light everywhere",
         props=dict(n=2, obj="wands", layout="exactly two wands, one gripped in each hand, both shafts visible "
                                             "from hand to tip")),
]

# --------------------------------------------------------------------------
# Khối prompt tái sử dụng
# --------------------------------------------------------------------------

# Block mô tả STYLE chung (dùng lại cho cả bản đầy đủ lẫn bản tool)
STYLE_PAINT = (
    "ART STYLE — copy the attached reference image's RENDERING exactly; do NOT fall back to flat webtoon "
    "cel-shading or bold ink outlines: it is a semi-realistic Korean manhwa digital PAINTING. Smooth airbrushed "
    "gradient shading, soft blooming highlights, no hard-edged colour zones; silhouettes separated by rim light "
    "and reflected light rather than by black lineart. Luminous porcelain skin with satin specular on shoulders, "
    "collarbones, belly and thighs and cool blue-violet shadow fill. Hyper-detailed antique-gold filigree "
    "metalwork: openwork armbands, chain drapes, faceted gemstones that each catch a bright specular point. "
    "Pearl-satin fabric with real weight — soft double-fold creasing, sheen bands along the folds, hand-sewn gold "
    "embroidery on the hems; layered translucent tulle veil thin enough to see through at the edges. A richly "
    "PAINTED atmospheric background with haze, volumetric light shafts, correct reflections on water and polished "
    "stone. Palette: desaturated cool indigo-violet-teal scene glowing against warm antique-gold accents on the "
    "figure; slight film grain; painterly masterpiece finish. Face: soft oval, small nose, full glossy lips "
    "parted, large detailed irises with catch-lights, thin brows, subtle blush — delicate, not chibi, not anime-flat.")

FRAME = (("A vertical tarot card \"{title}\" that fills the whole image edge to edge, framed EXACTLY like the "
          "reference card: a thin antique-gold ornamental border with fine filigree flourishes in the four "
          "corners and a small centered bottom band holding the title \"{title}\" in antique-gold serif lettering "
          "with a faint inner glow; the artwork bleeds to the inner edge of that frame; no numbers and no Roman "
          "numerals anywhere.\n\n"
          if WITH_FRAME else
          "A completely frameless vertical tarot card \"{title}\", edge-to-edge illustration: no decorative "
          "borders, no card frame, no banner ribbon, no numbers, no Roman numerals. The only text is the title "
          "\"{title}\" centered at the very bottom in the same antique-gold serif lettering as the style "
          "reference card.\n\n")
         + "REFERENCE IMAGE: {ref} — copy EXACTLY its painting style (airbrushed shading, bloom, light-defined "
           "edges, richly painted background), its costume construction, its gold filigree jewellery, its "
           "folded-fabric rendering and its gold serif bottom lettering.")

ART_STYLE = STYLE_PAINT

COSTUME = (
    "COSTUME — drawn with the SAME construction logic as the reference image, only the accent stone and fabric "
    "tone change for this card: a draped bandeau top of folded {cloth} fabric crossed under the bust and held at "
    "centre front by two round {metal} clasps engraved with {emblem}, the chest FULLY COVERED (opaque, modest "
    "softly-shadowed neckline, absolutely no nudity and no bare skin above the bust line); two narrow fabric "
    "strips cross in an X over the bare midriff and tuck into high-cut {cloth} briefs edged in fine {metal} "
    "wire; over the hips an ornate {metal} filigree hip-chain centred with a large faceted {gem} from which a "
    "long embroidered silk panel falls down the front of the thighs, its hem scattered with tiny {metal} charms "
    "shaped like {emblem}; a floor-length veil of luminous white tulle edged with {metal} star embroidery floats "
    "behind her; openwork {metal} filigree armbands on both biceps, fine {metal} bangles on the wrists, a "
    "jewelled circlet with a teardrop {gem} on her forehead, a gemstone pendant on a fine chain at her throat. "
    "All fabric is dry-to-slightly-damp, opaque and heavy with visible fold shadows, creasing and pulling where "
    "the {metal} clasps and cords tension it; skin shows soft contact shadows under every strap, edge and chain.")

FIGURE = (
    "FIGURE: an adult woman, {age}, {build}; hair: {hair}; eyes: {eyes}; skin: {skin}; "
    "signature detail: {signature}; aura: {aura}. Every character in this deck is an adult in her twenties.")

POSE = (
    "POSE: {pose}. Barefoot, elegant and natural, weight clearly grounded, hips and shoulders in a soft "
    "contrapposto line so the costume's folds fall believably.")

SCENE = (
    "SCENE & SYMBOLISM ({scene}): the scene reads as a real bath/architectural space, {extra}. "
    "Tarot emblem integrated naturally: {emblem}."
)

COUNT_LOCK_NONE = (
    "COUNT LOCK: this card contains NO loose suit objects in the scene. Do not add random floating or "
    "decorative cups, swords, wands or pentacles.")

COUNT_LOCK = (
    "COUNT LOCK — EXACTLY {n} {obj} (hard constraint; count before you draw). The scene contains exactly {n} "
    "{obj} — not {nminus}, not {nplus}. Placement is locked: {layout}. Every one of the {n} must be fully "
    "visible: nothing occluded by a body, limb, cloth, steam or another object, nothing fused, broken, cropped "
    "or half-hidden. Keep them at one consistent size, shape, material and colour so they read as a single "
    "countable set, with a clear gap of background between each one. Place no other {obj} anywhere else on the "
    "card — not in the frame, not in the background, not as decoration. Before finishing, count them: "
    "{count_up}. If the total is not {n}, redraw."
)

LIGHT = (
    "DEPTH & LIGHT: layered atmospheric depth with steam, light shafts and reflective wet floor; cinematic "
    "warm-cool contrast between the golden jewellery and the scene's accent lighting; micro-sparkles on the "
    "filigree, the gems and the water; soft ambient occlusion where fabric meets skin.")

SAFETY = (
    "DECORUM LOCK: tasteful fashion-illustration level only — the bust is completely covered by opaque fabric, "
    "no nudity, no exposed nipples, no see-through or transparent clothing, no cleavage beyond the bandeau's "
    "neckline, no underwear-only studio shot, no sexual act, no body horror. The figure is clothed exactly as "
    "the reference image is clothed."
)

QUALITY = (
    "ANATOMY & QUALITY LOCK: perfect anatomy — exactly two arms and two legs, exactly five fingers on each "
    "hand, natural joint bends, symmetrical face, no extra or fused limbs, no deformed hands; the pose is drawn "
    "like a master manhwa figure study.\n\n"
    + ("At the bottom, centered in the title band: the title \"{title}\" in antique-gold serif lettering matching "
       "the reference image, inside the same thin gold ornamental border with corner filigree as the reference. "
       if WITH_FRAME else
       "At the bottom, centered: the title \"{title}\" in antique-gold serif lettering matching the reference "
       "image. No frame, no border, no banner. ")
    + "No numbers, no Roman numerals, no other text, no watermark, no signature. "
      "Masterpiece manhwa painting, portrait 7:12, tall vertical composition with the figure's whole body "
      "visible inside the frame."
)


# --------------------------------------------------------------------------
# BẢN RÚT GỌN cho tool sinh ảnh (md giữ bản đầy đủ, gen dùng bản ngắn)
# --------------------------------------------------------------------------
GEN_FRAME = (('Vertical tarot card "{title}" filling the image edge to edge, with a thin antique-gold ornamental '
              'border, filigree corner flourishes and the title "{title}" in antique-gold serif in a bottom band '
              'exactly like the reference card; no numbers, no Roman numerals.')
             if WITH_FRAME else
             ('Vertical frameless tarot card "{title}", edge-to-edge illustration: no borders, no card frame, '
              'no banner, no numbers, no Roman numerals; the ONLY text is "{title}" in antique-gold serif '
              'centered at the bottom.'))
GEN_REF = ("Match the attached reference image exactly for costume construction and rendering: folded-fabric "
           "bandeau top with two round metal clasps at centre bust, fabric strips crossing in an X over the "
           "midriff, high-cut briefs, an ornate filigree hip-chain with a large faceted gemstone and a long "
           "embroidered silk panel falling down the front of the thighs, a floor-length white tulle veil edged "
           "in gold star embroidery, openwork gold armbands, a jewelled forehead circlet, gemstone pendant. "
           "Korean manhwa SEMI-REALISTIC PAINTING style (not flat webtoon cel-shading): smooth airbrushed "
           "gradient shading, soft bloom, edges separated by rim light instead of ink outlines, satin specular on "
           "skin, cool blue-violet shadow fill, richly painted hazy background with volumetric light and "
           "reflections, desaturated cool scene palette against warm gold, soft oval face with full glossy parted "
           "lips and large detailed eyes.")
GEN_COSTUME = ("This card's costume keeps that construction but in {cloth}, with {gem_n} as the centre stone, "
               "{metal} filigree, and {emblem_n} engraved on the bust clasps and hem charms. Fabric is opaque "
               "and dry-to-slightly-damp with visible fold shadows; the chest is fully covered — no nudity, "
               "no see-through fabric.")
GEN_FIGURE = ("Figure: adult woman in her twenties, {age}, {build}, {hair}, {eyes}, {skin} skin, signature "
              "detail {signature}, aura {aura}.")
GEN_POSE = "Pose: {pose}."
GEN_SCENE = "Scene ({scene}): {extra} Tarot emblem in the composition: {emblem_n}."
GEN_COUNT = "Hard prop count: exactly {n} {obj} — {layout}. Nothing else like it anywhere, all fully visible."
GEN_COUNT_NONE = "No loose suit objects (no extra cups, swords, wands or coins) anywhere in the scene."
GEN_LIGHT = ("Light: steam and light shafts, reflective wet floor, cinematic warm-cool contrast, sparkles on "
             "filigree and gems.")
GEN_END = ("Barefoot, elegant, perfect anatomy, five fingers per hand, whole body inside the tall 7:12 frame. "
           "Masterpiece manhwa illustration.")


def gen_prompt(card: dict, meta: dict) -> str:
    f = dict(
        title=card["title"], scene=card["scene"], extra=card["extra"].rstrip(".") + ".",
        pose=card["pose"], cloth=card["cloth"], metal=card["metal"],
        gem_n=nart(card["gem"]), emblem_n=nart(card["emblem"]),
        age=smart_age(meta.get("age")),
        build=clean(meta.get("build")) or "lithe and tall",
        hair=clean(meta.get("hair")), eyes=clean(meta.get("eyes")),
        skin=clean(meta.get("skin")), signature=clean(meta.get("signature")),
        aura=clean(meta.get("aura")),
    )
    blocks = [GEN_FRAME.format(**f), GEN_REF, GEN_COSTUME.format(**f), GEN_FIGURE.format(**f),
              GEN_POSE.format(**f), GEN_SCENE.format(**f)]
    blocks.append(GEN_COUNT.format(n=card["props"]["n"], obj=card["props"]["obj"],
                                  layout=card["props"]["layout"]) if card["props"] else GEN_COUNT_NONE)
    blocks += [GEN_LIGHT, GEN_END]
    return " ".join(blocks)


# --------------------------------------------------------------------------
# BẢN TOOL (đã kiểm chứng: là bản duy nhất backend Gemini 3.1-flash-image chịu render
# khi kèm reference `the star.png` — tránh chữ "bikini / bandeau / chest / wet micro")
# --------------------------------------------------------------------------
VI_MAP = {
    "sâu": "deep", "tròn long lanh": "bright round", "với vệt vàng kim": "with gold flecks",
    "long lanh như nước đêm": "glittering like night water", "huyền bí": "mysterious",
    "almond sắc": "sharp almond", "ánh nhìn xuyên thấu": "penetrating gaze",
    "nửa khép hờ": "half-closed", "almond ấm": "warm almond", "đuôi mắt hếch nhẹ": "slightly upturned",
    "sà xuống gợi cảm": "languid", "lạnh lùng ra lệnh": "cool and commanding",
    "ánh mắt biết tuốt": "all-knowing", "hơi cụp": "softly lowered", "quyết đoán, không chớp": "resolute, unblinking",
    "rực và ôn hòa": "bright and gentle", "gần như trong suốt": "nearly translucent", "an tĩnh": "serene",
    "upturned": "upturned", "nhìn xa như tiên tri": "far-seeing", "nhìn thẳng không chớp": "level and unblinking",
    "đảo ngược mà vẫn bình thản": "calm even inverted", "không thể đọc": "unreadable",
    "sáng trong như nước": "clear as water", "đốt mắt": "burning", "mở to kinh ngạc giữa cú rơi": "wide with awe",
    "mơ màng": "dreamy", "cười long lanh": "laughing bright", "mở to như vừa thức giấc": "wide, newly awakened",
    "sáng và đầy đủ": "bright and whole", "liếc nghiêng say đắm về phía người kia": "gazing adoringly aside",
    "veiled beneath sheer white cowl gauze": "loose under fine white gauze",
    "cascading down past one bare shoulder": "cascading past one shoulder",
    "thả": "loose", "gió mai": "morning wind", "mật ong": "honey", "vực thẳm mời gọi": "an inviting abyss",
    "nước đêm": "night water", "sao": "stars", "làn da ướt": "damp gleaming skin",
    "A ": "", "**": "",
}


def en(s: str) -> str:
    s = (s or "").strip()
    for k, v in sorted(VI_MAP.items(), key=lambda x: -len(x[0])):
        s = s.replace(k, v)
    s = re.sub(r"[\u00c0-\u024f\u1e00-\u1eff][^,;]*", lambda m: "", s)
    words = [w for w in re.split(r"\s+", s) if w]
    # bỏ các fragment vụn còn sót sau khi cắt tiếng Việt
    words = [w for w in words if not (len(w.strip(",;.")) <= 2 and w.strip(",;.").isascii())]
    out = " ".join(words).strip(" ,;")
    out = re.sub(r",\s*,", ",", out)
    return out


TOOL_FRAME = ('Thin antique-gold ornamental card border with fine filigree flourishes in the four corners and the '
              'title \\"{title}\\" in antique-gold serif inside a small bottom band, exactly like the reference '
              'card; the artwork bleeds to the inner edge of that border; no numbers, no Roman numerals. '
              if WITH_FRAME else
              'Frameless: no border, no frame. Only text: \\"{title}\\" in antique-gold serif centered at the very '
              'bottom; no numbers. ')

TOOL = ('Vertical tarot card \\"{title}\\", Korean manhwa SEMI-REALISTIC DIGITAL PAINTING — smooth airbrushed '
        'gradient shading and soft bloom, NO flat cel colours and NO bold ink outlines (silhouettes separated by '
        'rim light), luminous porcelain skin with satin specular and cool blue-violet shadow fill, '
        'hyper-detailed antique-gold filigree jewellery whose gems each catch a specular point, pearl-satin '
        'fabric with real weight, double-fold creasing and gold embroidery, translucent layered tulle veil, '
        'a richly painted atmospheric background with haze, volumetric light shafts and reflections on water and '
        'polished stone, desaturated cool indigo-violet scene against warm antique-gold accents, slight film '
        'grain, soft oval face, small nose, full glossy parted lips, large detailed irises with catch-lights, '
        'subtle blush. ' + TOOL_FRAME +
        'One adult woman in her twenties in a tasteful editorial fantasy costume, fully clothed, all fabric opaque. '
        "COSTUME — reproduce the attached reference image's outfit design exactly, changing only the fabric "
        'colour and centre stone: folded {cloth} cropped bodice with two round {metal} rosette clasps at centre '
        'front, thin crossed {metal}-trimmed bands over the waist, high-cut matching bottoms, an ornate {metal} '
        'filigree hip chain with a large faceted {gem_n} and a long embroidered silk panel falling between the '
        'thighs, floor-length sheer white veil hemmed with gold star embroidery, openwork {metal} armbands, a '
        'jewelled forehead circlet, {emblem_n} engraved on the clasps. '
        'Hair: {hair}. Eyes: {eyes}. Skin: {skin}. '
        'Pose: {pose}. Setting — {scene}: {extra} '
        '{props}Tall 7:12 portrait, whole body visible, perfect anatomy, five fingers per hand.')


# --------------------------------------------------------------------------
# TOOL_PROVEN — bản ĐÃ KIỂM CHỨNG thực tế (lá The Moon render ra đúng style reference)
# Công thức: câu "painted in exactly the same style as the attached reference image"
# + mô tả positive (airbrush/bloom/rim light/film grain), KHÔNG dùng câu phủ định dài,
# độ dài ~1500-1700 ký tự. Backend Gemini 3.1 hay trả "no images" khi prompt quá dài.
# --------------------------------------------------------------------------
V2_DIR = os.path.join(ROOT, "prompts_frameless_v2")


def v2_outfit(slug: str) -> str:
    """Đọc nguyên văn dòng Outfit của lá tương ứng trong prompts_frameless_v2 (không chỉnh sửa)."""
    f = os.path.join(V2_DIR, f"{slug}.md")
    if not os.path.exists(f):
        return ""
    m = re.search(r"^- \*\*Outfit:\*\* (.+)$", open(f, encoding="utf-8").read(), re.M)
    return m.group(1).strip() if m else ""


def nart(s: str) -> str:
    """Bỏ mạo từ 'a/an' đầu cụm đá quý để nhúng vào câu không bị lặp mạo từ."""
    return re.sub(r"^(a|an)\s+", "", (s or "").strip())


def smart_age(age: str) -> str:
    """Ép mọi nhân vật >= 20 tuổi (spec cũ có lá ghi 19)."""
    m = re.search(r"(\d+)", age or "")
    if not m or int(m.group(1)) < 20:
        return "20 years old"
    return m.group(0) + " years old"


def clean(s: str) -> str:
    s = " ".join((s or "").split())
    s = s.replace("**", "").replace("A ", "") if s else s
    return s

# --------------------------------------------------------------------------
# v3.2 — FACE LOCK (giữ đúng biểu cảm của lá mẫu) + OUTFIT_MODE
# --------------------------------------------------------------------------
FACE_LOCK = ("FACE — keep the reference card's exact expression: serene, dreamy and slightly dazed; heavy "
             "half-lidded eyes gazing softly down past the viewer, small glossy lips parted just enough, faint "
             "blush across the cheeks and the bridge of the nose, delicate oval face, tiny straight nose, soft "
             "thin brows, a couple of wet strands clinging across one cheek; no wide smile, no pout, no "
             "surprise — the same calm, vulnerable, half-asleep look as the reference.")

OUTFIT_COUTURE = ("Costume copied from the reference: {cloth} cropped bodice with two round {metal} rosette "
                  "clasps, thin {metal} bands crossing over the waist, high-cut matching bottoms, {metal} "
                  "filigree hip chain set with a large {gem_n} and a long embroidered silk panel falling between "
                  "the thighs, floor-length sheer white veil hemmed with gold stars, openwork {metal} armbands, "
                  "a jewelled forehead circlet, {emblem_n} engraved on the clasps.")

OUTFIT_WET = ("Costume — v3.2 'nội y mỏng ướt': a delicate {cloth} satin camisole top with thin crossing straps "
              "and matching high-cut satin bottoms from the same design family as the reference, the camisole "
              "closed at centre front by two round {metal} rosette clasps engraved with {emblem_n}, a {metal} "
              "filigree hip chain set with a large faceted {gem_n} holding a long embroidered silk panel that "
              "falls between the thighs, a floor-length sheer {metal}-starred veil, openwork {metal} armbands and "
              "a jewelled circlet. WET LOOK: the satin carries a soft wet gloss and fine water beads, "
              "darkened a shade where it is damp, her hair is wet and slicked, droplets sit on her shoulders and "
              "run off the hems — she has just risen from the bath. The fabric stays opaque and neatly fitted "
              "(never transparent), the chest and hips are completely covered, cut exactly like the reference "
              "costume, so only shoulders, arms and thighs are bare skin as in the reference.\n\n"
              "NOTE: avoid the tokens 'lingerie', 'bralette', 'clinging like a second skin', 'see-through' in "
              "the generation prompt — the image backend refuses them (verified: 5/5 refusals). "
              "'camisole top + high-cut satin bottoms + wet gloss + water beads' passes and reads the same.")

BIKINI_TERMS = ("two-piece bikini", "bikini", "swimwear")

OUTFIT_BIKINI = ("Costume — v3.3 bikini 2 mảnh: a {cloth} two-piece bikini in a satin finish — a structured "
                 "underwired top with fully lined cups that cover the bust completely, closed at centre front by "
                 "two round {metal} rosette clasps engraved with {emblem_n}, thin {metal}-wrapped shoulder and "
                 "back straps; matching high-cut {cloth} bikini bottoms edged in fine {metal} wire; over the hips "
                 "the reference's ornate {metal} filigree hip chain set with a large faceted {gem_n}, holding a "
                 "long embroidered silk panel that falls from the hip down the front of the thighs; a "
                 "floor-length sheer veil hemmed with {metal} stars; openwork {metal} armbands, {metal} wrist "
                 "bangles and a jewelled forehead circlet with a teardrop gem; a {metal} chain necklace with a "
                 "matching gemstone at the throat. Wet from the water: fabric darkened a shade with a glossy "
                 "satin sheen, plastered-smooth with tiny water beads, droplets falling from the hems, hair wet "
                 "and slicked. Swimwear-grade opacity: fully opaque, never transparent, the top covers the whole "
                 "bust — exactly how much skin the reference costume shows, no more.")

OUTFIT = {"bikini_two_piece": OUTFIT_BIKINI, "wet_lingerie": OUTFIT_WET}.get(OUTFIT_MODE, OUTFIT_COUTURE)

STYLECORE = ("soft airbrushed semi-realistic Korean manhwa digital painting, gentle bloom, edges separated by rim "
             "light instead of ink outlines, satin skin highlights, hyper-detailed antique-gold filigree "
             "jewellery, pearl-satin fabric with realistic folds and gold embroidery, translucent tulle veil, "
             "richly painted hazy background with volumetric light and reflections on water and polished stone, "
             "film grain")
FRAMECORE_YES = ("Same thin antique-gold ornamental border with filigree corners and an antique-gold serif title "
                 "in the bottom band, like the reference card.")
FRAMECORE_NO = ("Frameless like the v2 deck: no border, only the antique-gold serif title centered at the bottom.")

# Bản v3.2 gọn (mục tiêu <2100 ký tự: prompt dài >2500 làm backend Gemini trả "no images")
STYLE_SHORT = ("painted exactly like the attached reference image, same brushwork and same face rendering: "
               "soft airbrushed semi-realistic Korean manhwa painting, gentle bloom, rim-light edges instead of "
               "ink outlines, satin skin highlights, richly painted hazy background with water reflections, "
               "film grain")
FACE_SHORT = ("FACE = the reference expression: heavy half-lidded dreamy eyes gazing softly down, small glossy "
              "parted lips, faint blush on cheeks and nose, delicate oval face, tiny straight nose, wet strands "
              "across one cheek, calm and slightly dazed")
# "no other text" là bản vá lỗi model tự vẽ thêm tít phụ trên đầu (gặp ở 00-fool v3.2)
FRAME_SHORT = ("thin antique-gold ornamental border with filigree corners and the serif gold title in a bottom "
               "band, like the reference card; the bottom band is the ONLY text on the card, no title or caption "
               "at the top" if WITH_FRAME else
               "frameless, only the serif gold title at the bottom")

COSTUME_SHORT_COUTURE = ("Costume copied from the reference: {cloth} cropped bodice with two round {metal} "
                         "rosette clasps, thin {metal} bands crossing the waist, high-cut matching bottoms, "
                         "{metal} filigree hip chain with a large {gem_n} and a long embroidered silk panel "
                         "between the thighs, floor-length sheer white veil hemmed with gold stars, openwork "
                         "{metal} armbands, jewelled circlet, {emblem_n} on the clasps")
COSTUME_SHORT_WET = ("Costume: a delicate {cloth} satin camisole top with thin crossing straps and matching "
                     "high-cut satin bottoms, chest covered, fabric opaque and neatly fitted, plus the ornate "
                     "{metal} jewellery of the reference — the camisole closes at centre front by two round "
                     "{metal} rosette clasps engraved with {emblem_n}, {metal} filigree hip chain with a large "
                     "faceted {gem_n} holding a long embroidered silk panel that falls between the thighs, "
                     "floor-length sheer veil hemmed with gold stars, openwork {metal} armbands, a jewelled "
                     "circlet. The satin carries a soft wet gloss with fine water beads, her hair is wet and "
                     "slicked and droplets sit on her shoulders, as if she just rose from the bath")
COSTUME_SHORT_BIKINI = ("Costume: a {cloth} two-piece bikini in a glossy satin finish — structured underwired "
                        "top with fully lined cups covering the bust completely, closed at centre front by two "
                        "round {metal} rosette clasps engraved with {emblem_n}, thin {metal}-wrapped straps, "
                        "matching high-cut bikini bottoms, plus the reference's ornate {metal} jewellery: a "
                        "{metal} filigree hip chain with a large faceted {gem_n} holding a long embroidered silk "
                        "panel falling down the front of the thighs, a floor-length sheer veil hemmed with gold "
                        "stars, openwork {metal} armbands and a jewelled circlet. Wet from the water: satin "
                        "darkened a shade with a glossy sheen and tiny water beads, droplets off the hems, hair "
                        "wet and slicked; swimwear-grade opaque fabric, top covering the whole bust")

COSTUME_SHORT_VERBATIM = ("Costume — VERBATIM from the deck prompt, do not redesign it: {v2_outfit}. "
                          "Keep the reference card's gold jewellery on top of it (filigree hip chain with a large "
                          "{gem_n}, sheer veil hemmed with gold stars, openwork {metal} armbands, jewelled "
                          "circlet); opaque swimwear, no see-through, chest fully covered")

COSTUME_SHORT = {"bikini_two_piece": COSTUME_SHORT_BIKINI,
                 "wet_lingerie": COSTUME_SHORT_WET,
                 "verbatim_v2": COSTUME_SHORT_VERBATIM}.get(OUTFIT_MODE, COSTUME_SHORT_COUTURE)

TOOL_PROVEN = ('Vertical tarot card \"{title}\" ' + STYLE_SHORT + ". " + FACE_SHORT + ". " +
               'Same ' + FRAME_SHORT + '. One adult woman in her twenties, tasteful. ' + COSTUME_SHORT + ". "
               'Hair: {hair}. Eyes: {eyes}. Skin: {skin}. Pose: {pose}. Setting: {scene}, {extra} {props}'
               "Tall 7:12 portrait, whole body visible, perfect anatomy.")


def tool_prompt(card: dict, meta: dict) -> str:
    f = dict(title=card["title"], scene=card["scene"].rstrip(".").lower(), extra=card["extra"].rstrip(".") + ". ",
             pose=card["pose"].rstrip(".") + ".",
             cloth=re.sub(r"\s+(satin|silk)$", "", card["cloth"]), metal=card["metal"],
             gem_n=nart(card["gem"]), emblem_n=nart(card["emblem"]),
             hair=en(meta.get("hair")), eyes=en(meta.get("eyes")), skin=en(meta.get("skin")).rstrip(".") + ".",
             v2_outfit=(v2_outfit(card["slug"]) or "a soaking-wet micro string bikini (opaque swimwear, "
                                                   "no see-through)").rstrip("."))
    f["props"] = (f'Exactly {card["props"]["n"]} {card["props"]["obj"]}: {card["props"]["layout"]}. '
                  if card["props"] else "No other props or suit objects. ")
    t = " ".join(TOOL_PROVEN.format(**f).split())
    return re.sub(r"\.\.", ".", t).replace('\\"', '"')


def build_prompt(card: dict, meta: dict) -> str:
    """Bản prompt ĐẦY ĐỦ (lưu trong .md) — đủ mọi lock, dành cho người dùng kỹ tính."""
    fmt = dict(
        title=card["title"], ref=STYLE_REF, scene=card["scene"], extra=card["extra"],
        emblem=card["emblem"], gem=nart(card["gem"]), metal=card["metal"], cloth=card["cloth"],
        pose=card["pose"],
        age=smart_age(meta.get("age")),
        build=clean(meta.get("build")) or "lithe, tall, long-legged, graceful",
        hair=clean(meta.get("hair")), eyes=clean(meta.get("eyes")),
        skin=clean(meta.get("skin")), signature=clean(meta.get("signature")),
        aura=clean(meta.get("aura")),
    )
    blocks = [
        FRAME.format(**fmt),
        ART_STYLE,
        COSTUME.format(**fmt),
        FIGURE.format(**fmt),
        POSE.format(**fmt),
        SCENE.format(**fmt),
    ]
    if card["props"]:
        n = card["props"]["n"]
        cp = ", ".join(str(i) for i in range(1, n + 1))
        blocks.append(COUNT_LOCK.format(
            n=n, obj=card["props"]["obj"], layout=card["props"]["layout"],
            nminus=n - 1, nplus=n + 1, count_up=cp))
    else:
        blocks.append(COUNT_LOCK_NONE)
    blocks += [LIGHT, SAFETY, QUALITY.format(**fmt)]
    return "\n\n".join(blocks)


def main():
    data = json.load(open(CARDS_JSON, encoding="utf-8"))["cards"]
    by_slug = {c["slug"]: c for c in data}
    os.makedirs(OUT_DIR, exist_ok=True)

    prompts, gen_prompts, tool_prompts, md_index = {}, {}, {}, []
    for card in MAJORS:
        meta = by_slug.get(card["slug"], {})
        prompt = build_prompt(card, meta)
        prompts[card["slug"]] = prompt
        gen_prompts[card["slug"]] = gen_prompt(card, meta)
        tool_prompts[card["slug"]] = tool_prompt(card, meta)
        md = [
            f"# {card['title']} ({card['n']}) — Frameless Star-Couture v3",
            "",
            f"- **Slug:** `{card['slug']}` | **Group:** major",
            f"- **Style + costume reference:** `{STYLE_REF}`",
            f"- **Bối cảnh:** {card['scene']}",
            f"- **Đá quý / kim loại phục trang:** {card['gem']} · {card['metal']} · {card['cloth']}",
            f"- **Emblem:** {card['emblem']}",
            f"- **Props (count lock):** " + (f"{card['props']['n']} {card['props']['obj']}"
                                             if card["props"] else "không có suit object"),
            "",
            "## Prompt",
            "",
            "```text",
            prompt,
            "```",
            "",
        ]
        fname = f"{card['slug']}.md"
        with open(os.path.join(OUT_DIR, fname), "w", encoding="utf-8") as f:
            f.write("\n".join(md))
        md_index.append((card["n"], fname, card))

    with open(os.path.join(OUT_DIR, "all_prompts.json"), "w", encoding="utf-8") as f:
        json.dump(prompts, f, ensure_ascii=False, indent=1)
    with open(os.path.join(OUT_DIR, "gen_prompts.json"), "w", encoding="utf-8") as f:
        json.dump(gen_prompts, f, ensure_ascii=False, indent=1)
    with open(os.path.join(OUT_DIR, "tool_prompts.json"), "w", encoding="utf-8") as f:
        json.dump(tool_prompts, f, ensure_ascii=False, indent=1)

    # README
    rows = "\n".join(
        f"| {n} | `{c['slug']}` | {c['title']} | {c['scene']} | {c['cloth']} · {c['gem']} | "
        + (f"{c['props']['n']} {c['props']['obj']}" if c['props'] else "—") + " |"
        for n, _, c in md_index)
    readme = f"""# prompts_frameless_v3_star — 22 lá Ẩn Chính, phục trang theo `the star.png`

Thư mục này sinh bởi `build_prompts_v3_star.py`. **KHÔNG** ghi đè `prompts_frameless_v2/`.

## Khác biệt cốt lõi so với v2

1. **Một ảnh tham chiếu duy nhất: `the star.png`** (gốc repo). Model phải copy đúng
   **cấu trúc phục trang** của ảnh đó: bandeau vải gấp nếp kẹp hai khuy tròn đồng cổ giữa ngực ·
   hai dải vải đan chéo chữ X qua bụng · quần cut cao viền dây kim loại ·
   **dây chuyền hông chạm lộng** đính đá quý lớn + dải lụa thêu sa xuống giữa đùi ·
   **khăn voan tulle trắng viền sao vàng** · vòng tay chạm lộng · vương miện trán có giọt đá.
2. **Cách render vải/da** theo ảnh: vải khô–hỏi ẩm, đục (opaque), nếp gấp có bóng đổ rõ,
   da porcelain bóng mờ, rim light vàng, kim loại viền sáng rực.
3. **Bỏ toàn bộ concept "vải ướt sũng / top tuột xuống eo"** của v2 — không còn chất khêu gợi
   lộ thân thể; giữ đường cong + pose gợi cảm ở mức fashion illustration.
4. **Decorum lock** trong mọi prompt: ngực phủ kín, không nude, không xuyên thấu,
   **mọi nhân vật 20+ tuổi** (spec cũ ghi 19 → ép về 20).
5. Giữ nguyên của deck: frameless no-num, chữ title serif vàng cổ điển đáy thẻ,
   emblem tarot, **COUNT LOCK** số lượng vật phẩm (4 object lá Magician, 2 bình lá Star,
   1 gươm lá Moon/Justice/Wheel, 2 chén lá Temperance, 2 gậy lá World).

## 22 lá

| # | Slug | Lá | Bối cảnh | Phục trang (nền · đá) | Props |
|---|---|---|---|---|---|
{rows}

## Cấu trúc

- `<slug>.md` — prompt đầy đủ từng lá
- `all_prompts.json` — map slug → prompt ĐẦY ĐỦ
- `gen_prompts.json` — map slug → prompt RÚT GỌN
- `tool_prompts.json` — map slug → prompt **DẠNG TOOL ĐÃ KIỂM CHỨNG** (bản duy nhất mà backend
  Gemini `3.1-flash-image` chịu render khi đính kèm `the star.png`; tránh các từ cấm
  "bikini / bandeau / chest / wet micro"). Dùng bản này khi sinh ảnh thật.
- `README.md` — tài liệu này

## Cách dùng khi sinh ảnh

Đính kèm `the star.png` làm **style + costume reference**, dán prompt của lá tương ứng,
khung dọc 7:12.

## Tái sinh

```bash
python3 build_prompts_v3_star.py
```
"""
    with open(os.path.join(OUT_DIR, "README.md"), "w", encoding="utf-8") as f:
        f.write(readme)

    print(f"OK: {len(prompts)} prompt -> {OUT_DIR}")
    print(f"gen avg len = {sum(len(v) for v in gen_prompts.values())//len(gen_prompts)} ký tự")


if __name__ == "__main__":
    main()
