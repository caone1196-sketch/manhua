#!/usr/bin/env python3
"""
build_prompts_v2.py — Bộ prompt MỚI cho toàn bộ 78 lá tarot theo công thức
đã chốt qua các vòng lặp trên lá The Star.

  1. Frameless, edge-to-edge, KHÔNG số / KHÔNG số La Mã — chỉ tên lá bài
     chữ serif vàng cổ điển dưới đáy (template update_no_num.py).
  2. Art style + contour rendering + chữ title: reference major_08_strength.png.
  3. Chi tiết tiếp giáp trang phục–cơ thể (strap tension, mép vải, bóng đổ...).
  4. Vải ướt sũng kiểu test_card_17_the_star.png (opaque, không see-through).
  5. Swimwear micro string bikini theo group; pose S-curve; biểu cảm manhwa.
  6. BACKGROUND_MODE:
       - "bathroom" (mặc định, v2.2): MỖI LÁ một phong cách phòng tắm RIÊNG BIỆT
         (78 style khác nhau — xem BATHROOM_STYLES), pose GỢI CẢM (xoay vòng 12
         pose ALLURING_POSES), LOẠI BỎ TOÀN BỘ GIÁP (strip_armor + negative).
       - "modern"  : bối cảnh streamer penthouse hiện đại (RGB/neon, monitor,
                     hologram, city bokeh) — mapping sẵn cho 8 lá + fallback.
       - "classic" : bối cảnh cổ điển theo scene gốc đã sanitize.

v2.2 thay đổi chính (yêu cầu người dùng):
  * "tư thế gợi cảm"      → ALLURING_POSES (12 pose gợi cảm S-curve, không lộ liễu).
  * "phong cách phòng tắm khác nhau" → BATHROOM_STYLES: 78 style riêng từng lá.
  * "đặc điểm nổi bật của từng lá"   → giữ nguyên FIGURE spec + emblem +
    count lock (được viết lại cho bối cảnh phòng tắm: BATHROOM_LAYOUTS).
  * "loại bỏ toàn bộ giáp" → strip_armor() + câu NO ARMOR trong template.
  * Fix: lá Át (age/hair N/A) giờ có figure mặc định hợp lệ (người trưởng thành).

Output: prompts_frameless_v2/ (<slug>.md, all_prompts.json, README.md).
Không ghi đè cards.json.
"""
import json
import os
import re

OUT_DIR = "prompts_frameless_v2"
BACKGROUND_MODE = "bathroom"  # "bathroom" | "modern" | "classic"

# Tùy chọn bikini (xoay vòng theo thứ tự lá): (màu, chi tiết accent) — luôn opaque + soaked
BIKINI_OPTIONS = [
    ("pearl-white", "with tiny gold star charms"),
    ("midnight-black", "with fine gold chain straps"),
    ("aqua-teal", "with side-tie ribbons"),
    ("rose-pink", "with small satin bow accents"),
    ("metallic gold", "with opaque lace-trim edges"),
    ("cherry-red", "with tiny pearl beads"),
]

# ---------------------------------------------------------------------------
# TƯ THẾ GỢI CẢM (xoay vòng 12 pose — gợi cảm, S-curve, không lộ liễu)
# ---------------------------------------------------------------------------
ALLURING_POSES = [
    "standing with her back against the rain-wet tiled wall, one knee bent and foot flat "
    "against the wall, both hands gliding up into her soaked hair, hips pushed into a deep "
    "S-curve, half-lidded gaze at the viewer",
    "seated sideways on the tub rim leaning back on one straight arm, chest lifted, one knee "
    "drawn up while the other leg trails toe-deep in the water, wet hair cascading down her back",
    "standing in sensual contrapposto, one hand resting on a popped hip, the other trailing "
    "water slowly down her collarbone, looking back over her shoulder with a smoldering half-smile",
    "kneeling upright on the bath mat, thighs close together, torso arched gracefully back, both "
    "arms lifting her wet hair, spine curved like a drawn bow, eyes closed in a soft sigh",
    "reclining along the tub edge on one hip, propped on one elbow, legs stacked in one long "
    "elegant line, chin tilted up, lips softly parted",
    "caught mid-turn stepping out of the shower, glancing back at the viewer over her bare "
    "shoulder, water droplets flicking from her fingertips, hips mid-sway",
    "one bare foot up on the tub rim, both hands sliding slowly down the raised thigh, back "
    "curved, looking down at the viewer through wet lashes",
    "seated in the shallow water facing the viewer, knees together tilted to one side, arms "
    "loosely crossed beneath her chest, shoulders glistening with droplets",
    "rising on tiptoe in a full-body stretch, arms overhead and intertwined, back arched, her "
    "whole figure one long alluring arc of light and water",
    "leaning forward over the vanity on both hands, weight low, looking into the lit mirror "
    "with a teasing smile, hips pushed back",
    "side-lying mermaid pose along the marble ledge, propped on one forearm, legs scissored in "
    "a long line, one hand combing wet hair off her face",
    "wrapping a towel around her hips mid-motion, spine arched, head thrown back, eyes closed, "
    "one shoulder bare, towel still trailing in the water",
]

# ---------------------------------------------------------------------------
# 78 PHONG CÁCH PHÒNG TẮM RIÊNG BIỆT — slug: (tên style, mô tả bối cảnh)
# Biểu tượng tarot của từng lá (emblem + suit objects) được tái dựng trong
# chính phong cách phòng tắm đó → đặc điểm nổi bật của từng lá vẫn giữ nguyên.
# ---------------------------------------------------------------------------
BATHROOM_STYLES = {
    # ------------------------- MAJOR ARCANA (22) -------------------------
    "00-fool": ("Scandi sunrise spa",
        "a playful 19-year-old streamer in a Scandinavian sunrise spa bathroom: pale birch-slat "
        "walls, a round white freestanding tub, floor-to-ceiling frosted glass glowing with a "
        "cyberpunk sunrise city beyond, steam curling off the water, a cute white Pomeranian "
        "puppy waiting on the fluffy bath mat, a single glowing digital white rose in her hand"),
    "01-magician": ("Marble vanity mirror wall",
        "a charismatic 22-year-old streamer in a marble magician's bathroom: a long double "
        "vanity beneath a floor-to-ceiling backlit mirror wall, warm brass fixtures, exactly "
        "four suit objects resting in one row on the vanity — one flaming wand diffuser, one "
        "glowing water cup, one crystal cyber-blade perfume bottle, one golden crypto-coin "
        "paperweight — black roses in an LED vase behind, an infinity symbol glowing on the mirror"),
    "02-priestess": ("Twin-column temple bath",
        "a serene 23-year-old streamer in a temple-of-duality bathroom: standing between two tall "
        "rainfall shower columns — one carved black basalt, one white marble — a glowing holographic "
        "crescent moon projected on the wet floor at her feet, a waterproof digital tablet of secret "
        "lore resting on the ledge, a pomegranate hologram shimmering in the steam"),
    "03-empress": ("Sunlit garden sunroom bath",
        "a luxurious 24-year-old streamer in a garden sunroom bathroom: potted ferns and flowering "
        "vines everywhere, fresh fruit trays on a teak bench, golden morning light through a frosted "
        "skylight, a heart-shaped Venus neon emblem glowing on the vine-tiled wall, a golden "
        "smartphone scepter in her hand"),
    "04-emperor": ("Stone steam-room throne",
        "a poised 25-year-old streamer in a stone steam-room throne bathroom: a carved stone bench "
        "throne beneath a bronze ram-head rainfall fixture, volcanic-red LED backlighting along dark "
        "marble, two ram-head sculptures on the shelf, a barren mountain mural in grey tile, steam "
        "rolling low, a golden ankh stylus in her hand"),
    "05-hierophant": ("Byzantine gilded chapel bath",
        "a wise 24-year-old streamer in a Byzantine chapel bathroom: a gold-leaf mosaic dome ceiling, "
        "twin green-marble columns, a carved stone tub, warm candle-toned sconces, two crossed golden "
        "keys glowing on the mosaic wall above the tub"),
    "06-lovers": ("Rose-petal twin-tub spa",
        "a romantic 21-year-old streamer in a couples' spa bathroom: two copper clawfoot tubs side by "
        "side on rose-quartz tile, fresh red rose petals floating on the water, an apple coiled by a "
        "silver serpent on a marble tray between the tubs, soft blush lantern light"),
    "07-chariot": ("Motorsport penthouse bath",
        "a heroic 22-year-old streamer in a motorsport penthouse bathroom: black-and-white checkered "
        "marble floor, carbon-fiber vanity, a canopy shower with two chrome sphinx-shaped fixtures, a "
        "winged sun-disk neon glowing above the mirror, night racetrack city lights beyond the glass"),
    "08-strength": ("Safari-lodge stone bath",
        "a warm-hearted 20-year-old streamer in a safari-lodge bathroom: rough stone walls and dark "
        "teak, a brass lion-head waterfall faucet filling a copper tub, red rose petals floating on "
        "the water, a garland of red roses laid across the tub tray, warm lantern glow"),
    "09-hermit": ("Candlelit mountain grotto",
        "a reclusive 24-year-old streamer in a candlelit mountain-grotto bathroom: a natural stone "
        "grotto with mineral-crystal walls, a single glowing brass lantern hanging from the ceiling "
        "rock, one warm shaft of lantern light cutting through the steam, deep quiet shadows"),
    "10-wheel": ("Casino-noir roulette",
        "a lucky 25-year-old streamer in a casino-noir bathroom: a giant round roulette-wheel mirror "
        "above the vanity, golden spoke inlay across the black marble floor, a red velvet stool, warm "
        "casino lights, a small sphinx figurine atop the roulette mirror holding one slim crystal "
        "blade upright"),
    "11-justice": ("Monochrome scales bath",
        "a composed 23-year-old streamer in a monochrome justice bathroom: stark black-and-white "
        "striped marble, two gold balance-scale towel racks perfectly level, a vertical sheet of "
        "falling water splitting evenly between twin basins, one slim crystal blade held upright in "
        "her left hand"),
    "12-hanged": ("Inversion silk studio",
        "a dreamy 22-year-old streamer in an inversion-studio bathroom: a mirrored ceiling, a soft "
        "champagne silk aerial hammock hanging beside the tub, a living green branch suspended "
        "upside-down overhead dripping dew into the bath, morning light through a high slot window"),
    "13-death": ("Gothic onyx & lilies",
        "a transformative 23-year-old streamer in a gothic onyx bathroom: black onyx walls, a white "
        "marble tub ringed with white lilies, five-petaled white roses floating on still black "
        "water, a faint silver skull motif etched in the fogged mirror, pale moonlight through a "
        "gothic arched window"),
    "14-temperance": ("Zen ryokan ofuro",
        "a balanced 22-year-old streamer in a zen ryokan bathroom: a hinoki cypress ofuro tub, one "
        "stone waterfall basin pouring in an endless cycle into a second lower basin, irises in a "
        "stone vase, a triangle-within-a-square motif carved on the wooden screen, soft grey-green "
        "light, one golden chalice in each hand trading a thin stream of water between them"),
    "15-devil": ("Crimson neon gothic",
        "a seductive 24-year-old streamer in a crimson gothic bathroom: glossy black tile, an "
        "inverted pentagram glowing crimson neon on the wall, loose golden chain links draped over "
        "the tub rim, dark red candles, wine-red steam light"),
    "16-tower": ("Storm skyscraper glass",
        "a fierce 22-year-old streamer in a storm-skyscraper bathroom: a top-floor wet room with "
        "floor-to-ceiling glass, lightning splitting the night sky outside, a jagged bolt-shaped "
        "chrome light fixture, kintsugi gold-cracked tile accents, rain streaking down the glass"),
    "17-the-star": ("Open-sky stargazer",
        "a serene 21-year-old streamer in an open-sky stargazer bathroom: a circular tub beneath a "
        "glass-dome skylight revealing a star constellation, an eight-pointed star glowing softly "
        "above her, two golden decanters — one in each hand — pouring two thin streams of water, one "
        "into the tub and one across the stone floor"),
    "18-moon": ("Midnight lagoon",
        "a mysterious 22-year-old streamer in a midnight lagoon bathroom: a deep-blue lagoon-pool "
        "tub, a crescent-moon lamp dripping silver dew, moonflowers blooming along the wet tile, two "
        "white tower candles flickering, indigo steam"),
    "19-sun": ("Golden solarium",
        "a radiant 20-year-old streamer in a golden solarium bathroom: a sun-face gold medallion "
        "above the tub, sunflower-yellow zellige tiles, fresh sunflowers in a vase, radiant "
        "perpetual-golden-hour light, sheer white curtains glowing"),
    "20-judgement": ("Celestial trumpet dawn",
        "an awakened 25-year-old streamer in a celestial judgement bathroom: a trumpet-shaped golden "
        "rainfall shower raining soft light, tall rectangular light panels rising like an altar wall "
        "behind the tub, dawn-gold steam, a golden trumpet resting on the vanity"),
    "21-world": ("360° panorama ring",
        "a graceful 24-year-old streamer in a 360-degree panoramic circular bathroom: a curved glass "
        "wall wrapping the circular tub with the full night skyline, a laurel-wreath oval of golden "
        "light ringing her reflection, four pet-avatar screens glowing at four points around the "
        "ring, two slender glowing wands — one in each hand"),
    # ------------------------- WANDS (14) — ember ấm -------------------------
    "wands-ace": ("Volcanic hot spring",
        "in a volcanic hot-spring bathroom: a steaming pool tub carved from black volcanic rock, "
        "ember-orange LED glow beneath the water, one living leafy wand standing upright in a slim "
        "brass holder, a curl of incense smoke rising"),
    "wands-02": ("Explorer's lookout",
        "in an explorer's lookout bathroom: a brass telescope by the rain-streaked window, an antique "
        "world map etched on the shower glass, warm brass fixtures, one leafy wand held upright in "
        "her right hand and one mounted upright on a stone shelf beside her"),
    "wands-03": ("Harbor porthole",
        "in a harbor-view bathroom: round brass porthole windows, mooring-rope towel rings, sea "
        "light mixing with warm lantern glow, three leafy wands planted upright in one straight row "
        "across the wet floor before the tub"),
    "wands-04": ("Garland canopy",
        "in a celebration-garland bathroom: a garland arch of eucalyptus and marigolds over a double "
        "vanity, string lights, four slender wands standing as the four corner posts of a flower "
        "canopy around the tub, festive warm glow"),
    "wands-05": ("Arena star jets",
        "in an arena-spa bathroom: five rainfall jets set in a star burst on the dark tile wall, "
        "dynamic splash patterns on wet stone, five wands crossed together in one star bundle "
        "leaning against the tub rim"),
    "wands-06": ("Victory laureate podium",
        "in a victory-laureate bathroom: a stepped podium-style marble tub platform, a golden "
        "victory wreath hanging on the mirror, one laurel-crowned wand raised high in her hand and "
        "five slender wands standing upright in a golden rack beside the tub, spotlight glow"),
    "wands-07": ("Bamboo palisade terrace",
        "in a bamboo-terrace bathroom: a palisade of live bamboo screening the outdoor tub, green "
        "stone tiles, warm morning light, one wand held in both her hands and six wands rising "
        "upright in a palisade row from behind the tub rim"),
    "wands-08": ("Speed-line yacht wet room",
        "in a racing-yacht wet room: sleek white hull curves, eight parallel chrome towel rails "
        "running like speed lines along the wall, motion-streaked tile, wind-and-water energy, "
        "eight wands flying in one parallel row through the steam overhead"),
    "wands-09": ("Watchtower rampart",
        "in a watchtower bathroom: heavy wooden beams, a small arrow-slit window with dawn light, "
        "eight wands planted upright in one straight palisade row behind her and one wand held "
        "crosswise in front of her chest, guarded calm"),
    "wands-10": ("Apothecary bundle",
        "in an apothecary bathroom: shelves of amber glass bottles, dark wood and copper, heavy "
        "warm air, one great bundle of ten wands tied at the middle leaning against the tub, its "
        "ten tips fanned and countable"),
    "wands-page": ("Art-deco plume",
        "in an art-deco bathroom: fan-feather gold wall panels, playful yellow-gold accents, one "
        "living wand crowned with a bright feather plume standing in a slim vase on the vanity"),
    "wands-knight": ("Equestrian chic",
        "in an equestrian-chic bathroom: a saddle-leather stool, a horseshoe-shaped towel warmer, "
        "warm stable-wood tones, one leafy wand raised gently in her hand and a horseshoe emblem "
        "glowing on the wall behind her"),
    "wands-queen": ("Sunflower terracotta",
        "in a sunflower-queen bathroom: warm terracotta tiles, sunflowers in every vase, two "
        "flame-shaped candles on the tub rim, one sunflower wand standing upright between them, "
        "honey-gold light"),
    "wands-king": ("Lion-head gold",
        "in a lion-head throne bathroom: a gold lion-head wall fountain above the tub, flame-shaped "
        "chandelier sconces, a deep amber palette, one living green wand standing upright in a "
        "brass lion-paw holder"),
    # ------------------------- CUPS (14) — aqua -------------------------
    "cups-ace": ("Shell fountain",
        "in a fountain bathroom: a tiered shell fountain centerpiece filling a round tub, one great "
        "chalice-shaped basin overflowing at the top with five thin sheets of water, soft aqua "
        "light rippling on the ceiling"),
    "cups-02": ("Twin-basin rings",
        "in a twin-basin bathroom: two matching basins with interlocked-ring chrome faucets, a "
        "rose-quartz two-seat vanity, two crystal chalices raised — one in each of her hands — rims "
        "touching above the steam"),
    "cups-03": ("Celebration spa",
        "in a celebration-spa bathroom: a tub tray scattered with petals and confetti, champagne-gold "
        "glow, three crystal chalices floating upright on the water in a wide triangle, each rim "
        "above the surface"),
    "cups-04": ("Still-water zen",
        "in a still-water bathroom: a perfectly still square soaking pool, misty grey-blue calm, "
        "three chalices standing upright in a row on the stone edge before her and a fourth chalice "
        "offered on a small floating wooden tray"),
    "cups-05": ("Rain-window melancholy",
        "in a rain-window bathroom: dark elegant tile, a tall rain-streaked window with melancholy "
        "blue light, three chalices tipped and spilled on the ledge and two still standing full "
        "behind them"),
    "cups-06": ("Retro pastel nostalgia",
        "in a retro pastel bathroom: mint-and-pink fifties tile, vintage chrome faucets, warm "
        "memory-glow light, six chalices in one row along the shelf, each holding a different "
        "flower"),
    "cups-07": ("Dream-cloud",
        "in a dream-cloud bathroom: a cloud-mural ceiling, lavender-violet mist, seven chalices "
        "floating as glowing holograms in two clean rows — four below and three above — each "
        "holding a different tiny wish-symbol"),
    "cups-08": ("Moon-door",
        "in a moon-door bathroom: deep indigo light, an arched doorway in the wet wall opening onto "
        "glowing sea water, eight chalices stacked on the ledge beside it — three, three and two, "
        "one clear gap between the sixth and the seventh"),
    "cups-09": ("Skyline jacuzzi",
        "in a skyline-jacuzzi bathroom: a bubbling jacuzzi facing a panoramic city window, champagne "
        "and violet night glow, nine chalices arranged in a neat three-by-three grid on the glowing "
        "shelf behind the tub"),
    "cups-10": ("Rainbow-glass arc",
        "in a rainbow-glass bathroom: a rainbow-shaped glass shelf backlit in spectrum colors, "
        "family-warm golden light, ten chalices standing along the arc — four on the left half, "
        "four on the right half, two at the apex"),
    "cups-page": ("Kawaii aquarium",
        "in a kawaii-aquarium bathroom: pastel aqua tile, playful bubbles drifting in the air, one "
        "round fishbowl with a curious goldfish on the vanity, one chalice-shaped basin glowing "
        "beside the tub"),
    "cups-knight": ("Riverside stone",
        "in a riverside-stone bathroom: a tub carved like a river basin with a thin flowing water "
        "channel beside it, horseshoe-shaped stones lining the floor path, fresh green-water light, "
        "one golden chalice resting on a horseshoe tray"),
    "cups-queen": ("Ocean grotto",
        "in an ocean-grotto bathroom: a sea-cave grotto tub, wave-pattern blue mosaic, pearl-shell "
        "accents, one lidded golden chalice cradled in a sculpted stone wave on the shelf"),
    "cups-king": ("Aquarium throne",
        "in an aquarium-throne bathroom: a wall-sized aquarium with two bright fish circling, a "
        "high-backed throne-like tub platform, deep teal glow, one great chalice-shaped basin "
        "between two fish-shaped gold faucets"),
    # ------------------------- SWORDS (14) — bạc lạnh -------------------------
    "swords-ace": ("Pristine white blade",
        "in a pristine-white bathroom: blinding clean white marble, sharp morning light, one "
        "vertical chrome rainfall column rising like an upright blade crowned with a gold ring, one "
        "crystal cyber-blade displayed upright on the vanity"),
    "swords-02": ("Starlit X",
        "in a midnight-blue steam bathroom: a starry ceiling, a silk sleep-mask resting on the tub "
        "rim, two slim crystal blades held crossed in a single X before her — one over each "
        "shoulder"),
    "swords-03": ("Heartbreak rain",
        "in a heartbreak-rain bathroom: blue-grey light, a heart-shaped neon glowing pink through "
        "rain-streaked glass, one heart-shaped ice sculpture on the vanity with three slim crystal "
        "blades standing in it — one vertical from above, two angled from left and right"),
    "swords-04": ("Chapel rest",
        "in a chapel-rest bathroom: a soft jewel-toned stained-glass accent window, a stone bench "
        "with a single velvet cushion, hushed candlelight, three crystal blades mounted in a row on "
        "the wall rack above and one lying flat on the bench below"),
    "swords-05": ("Storm victor",
        "in a storm-victor bathroom: dark slate tile, wind-blown spray through an open window, "
        "stormy contrast light, three crystal blades gathered upright and fanned in her hands and "
        "two lying abandoned on the wet floor behind her"),
    "swords-06": ("Ferry boat tub",
        "in a ferry-boat bathroom: a long boat-shaped tub gliding on a rippling water-glass floor, "
        "misty grey-blue shore light ahead, six slim crystal blades standing upright in the tub "
        "rim — three on her left and three on her right"),
    "swords-07": ("Stealth shoji",
        "in a stealth bathroom: charcoal tile, a half-open sliding shoji screen, moon shadows, five "
        "crystal blades gathered upright and fanned in her arms and exactly two crystal blades "
        "planted upright in the planter behind her"),
    "swords-08": ("Ribbon ring",
        "in a ribbon-ring bathroom: dusk light, soft gold ribbon motifs on the tile, eight slim "
        "crystal blades planted in one open ring around the freestanding tub — three in front of "
        "her, one at her left side, one at her right side, three behind her"),
    "swords-09": ("Insomnia midnight",
        "in an insomnia bathroom: midnight-black tile, a single warm lamp glowing beside the tub, "
        "dark 3 a.m. blue light, nine crystal blades mounted on the wall in a neat three-by-three "
        "grid"),
    "swords-10": ("Dawn after storm",
        "in a dawn-after-storm bathroom: first golden light breaking through a horizontal window, a "
        "dark-to-gold gradient in the steam, ten crystal blades lying flat along the foot of the "
        "tub in two staggered rows of five"),
    "swords-page": ("Wind-study",
        "in a windy study bathroom: a cloud-mural ceiling, wind-blown sheer curtains, crisp "
        "daylight, one crystal blade with a feather plume tied to its hilt, gripped in both her "
        "hands"),
    "swords-knight": ("Gale force",
        "in a gale-force bathroom: an open-air wet room with wind blasting a sheer curtain "
        "sideways, cold electric light, a horseshoe emblem glowing on the wall, one crystal blade "
        "pointed forward like a lance in her hand"),
    "swords-queen": ("Marble throne clarity",
        "in a throne-of-clarity bathroom: a high-backed marble tub throne, butterfly motifs on the "
        "white tile, sharp clear light, one upright crystal blade wrapped in a laurel wreath "
        "standing beside the throne"),
    "swords-king": ("Twin-wing hall",
        "in a twin-wing bathroom: a high-ceilinged airy hall of white and gold, two wing-shaped "
        "gold wall sculptures flanking a tall throne chair beside the tub, one upright crystal "
        "blade standing between them"),
    # ------------------------- PENTACLES (14) — vàng đồng -------------------------
    "pentacles-ace": ("Garden-terrace hands",
        "in a garden-terrace bathroom: an outdoor terrace tub beside a small stone fountain shaped "
        "like cupped hands, ivy and wisteria, golden afternoon light, one large golden pentacle "
        "coin resting in the fountain's stone hands"),
    "pentacles-02": ("Wave sway",
        "in a wave-rider bathroom: a tub with a gentle wave-jet swaying the water, harbor-lamp "
        "light, one golden pentacle coin spinning on each of her palms and a chrome "
        "infinity-ribbon tray linking them on the vanity"),
    "pentacles-03": ("Artisan arch",
        "in an artisan-workshop bathroom: a carved stone arch over the tub, work tools on a wooden "
        "shelf, warm workshop lamplight, three golden pentacle coins set into the arch mosaic — one "
        "at the apex and two at the springing points"),
    "pentacles-04": ("Coin vault",
        "in a vault bathroom: a great bank-vault door standing ajar revealing golden shelving, warm "
        "gold-coin light, one pentacle coin held against her chest, one balanced on the vanity edge "
        "and two resting on the tub rim"),
    "pentacles-05": ("Snow stained-glass",
        "in a snow-window bathroom: frosted pale-blue tile, warm tub steam against cold light, a "
        "grand stained-glass window with five golden pentacle coins set into the glass in a "
        "quincunx — one top center, two on the middle row, two on the bottom row"),
    "pentacles-06": ("Charity scales",
        "in a charity-spa bathroom: twin scale-shaped brass basins, warm generous amber light, six "
        "pentacle coins balanced across the scale beam — three stacked in the left pan and three "
        "stacked in the right pan"),
    "pentacles-07": ("Greenhouse vine",
        "in a greenhouse bathroom: a Victorian glasshouse-style bathroom, a living vine climbing a "
        "trellis with seven golden pentacle coins hanging like fruit — three on the left branch, "
        "three on the right branch, one at the top — dappled green-gold light"),
    "pentacles-08": ("Atelier bench",
        "in an atelier bathroom: a jeweler's workbench vanity with chisels and gold dust, focused "
        "lamplight, eight finished pentacle coins inlaid in one straight row along the front edge "
        "of the marble bench, one blank unfinished stone disc on the workbench"),
    "pentacles-09": ("Estate arbor",
        "in an estate-arbor bathroom: a grape-arbor lattice over the tub, a small bronze falcon "
        "statue on the ledge, vine-wrapped gold light, nine pentacle coins fixed in one row along "
        "the arbor beam"),
    "pentacles-10": ("Tree-of-life mosaic",
        "in a family-estate bathroom: a grand tree-of-life wall mosaic in gold and umber, "
        "dynasty-warm light, ten pentacle coins set into the mosaic branches in a pyramid — four on "
        "the bottom row, three above, two above, one at the apex"),
    "pentacles-page": ("Earthy study",
        "in an earthy-study bathroom: clay-tone tiles, herbs on the windowsill, a single warm desk "
        "lamp, one large pentacle coin held up in both her cupped hands"),
    "pentacles-knight": ("Farmhouse oak",
        "in a farmhouse bathroom: oak beams, a brass draft-horse weathervane motif, plaid towels, "
        "slow warm afternoon light, one pentacle coin resting on a horseshoe tray on the tub rim"),
    "pentacles-queen": ("Rose garden",
        "in a rose-garden bathroom: climbing roses through an arched window, soft rosy-gold light, "
        "one pentacle coin entwined with rose stems in a crystal bowl on the vanity"),
    "pentacles-king": ("Bull bronze",
        "in a bull-bronze bathroom: a massive bronze bull-head fountain above the tub, black marble "
        "and gold, commanding warm light, one pentacle coin glowing above the bull's horns"),
}

# ---------------------------------------------------------------------------
# COUNT LOCK cho bối cảnh PHÒNG TẮM (viết lại cho staging 1 người + phòng tắm,
# vẫn giữ đúng số lượng vật phẩm suit như bản gốc)
# ---------------------------------------------------------------------------
BATHROOM_NO_COUNT_LOCK = (
    "COUNT LOCK: This card contains NO loose suit objects in the scene. "
    "Do not add random floating or decorative cups, swords, wands, or pentacles."
)

BATHROOM_LAYOUTS = {
    "01-magician": "exactly four objects in one row on the vanity — one flaming wand diffuser, one "
        "glowing water cup, one crystal cyber-blade perfume bottle, one golden crypto-coin "
        "paperweight; one of each, no duplicates, nothing else on the vanity",
    "10-wheel": "exactly one slim crystal blade, held upright by the small sphinx figurine atop the "
        "roulette mirror; no other blade anywhere",
    "11-justice": "exactly one slim crystal blade, held upright in her left hand; no other blade on "
        "the card",
    "14-temperance": "exactly two chalices, one in each hand, trading one thin stream of water "
        "between them; both bowls fully visible and un-occluded",
    "17-the-star": "exactly two golden decanters, one in each hand, both fully visible",
    "21-world": "exactly two slender glowing wands, one gripped in each hand, both shafts visible "
        "from hand to tip",
    "wands-ace": "exactly one living leafy wand standing upright in the brass holder; no second "
        "staff anywhere, not even as decoration",
    "wands-02": "exactly two wands: one held upright in her right hand and one mounted upright on "
        "the stone shelf beside her — 1 + 1 = 2; both shafts complete from base to tip, they do "
        "not cross",
    "wands-03": "exactly three wands planted upright in one straight row across the wet floor "
        "before the tub, evenly spaced and widely separated, none overlapping — count them left to "
        "right: 1, 2, 3",
    "wands-04": "exactly four wands as the four corner posts of the flower canopy around the tub — "
        "two on the left, two on the right — 2 + 2 = 4; the two rear posts drawn taller so no post "
        "hides another; all four shafts fully visible, tops joined by one flower garland",
    "wands-05": "exactly five wands crossed together in one star bundle leaning against the tub rim "
        "— five shafts, five countable tips, no extra wand anywhere on the card",
    "wands-06": "exactly six wands: one laurel-crowned wand raised in her hand plus five standing "
        "upright in the golden rack beside the tub — 1 + 5 = 6; each rack wand separately "
        "countable, none resting on a shoulder",
    "wands-07": "exactly seven wands: one held in her two hands plus six rising upright from behind "
        "the tub rim in one palisade row — 1 + 6 = 7; the six tips evenly spaced, none overlapping "
        "her body",
    "wands-08": "exactly eight wands flying in ONE single parallel row through the steam above the "
        "tub — evenly spaced, all eight pointing the same way, none crossing, none cropped",
    "wands-09": "exactly nine wands: eight planted upright in one straight palisade row behind her, "
        "evenly spaced and clear of her body, plus the one she holds in front of her — 8 + 1 = 9",
    "wands-10": "exactly ten wands in one natural bundle tied at the middle leaning against the tub "
        "— count the ten fanned tips: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10; no nine, no eleven",
    "wands-page": "exactly one living wand crowned with a feather plume in the slim vase; no second "
        "staff",
    "wands-knight": "exactly one leafy wand, raised gently in her hand; no other staff",
    "wands-queen": "exactly one sunflower wand standing between the two flame candles; no other "
        "staff",
    "wands-king": "exactly one living green wand in the brass lion-paw holder; no other staff",
    "cups-ace": "exactly one great chalice-shaped fountain basin; the five overflowing sheets are "
        "water, not cups — do not draw extra chalices anywhere",
    "cups-02": "exactly two crystal chalices, one raised in each hand, rims touching; no third cup",
    "cups-03": "exactly three chalices floating upright on the water in a wide triangle, each rim "
        "above the surface; no fourth cup",
    "cups-04": "exactly four chalices: three standing upright in a row on the stone edge plus one "
        "offered on the floating wooden tray — 3 + 1 = 4; all four bowls visible",
    "cups-05": "exactly five chalices: three tipped and spilled on the ledge plus two still "
        "standing full behind them — 3 + 2 = 5; all five bowls countable",
    "cups-06": "exactly six chalices in one row along the shelf, each holding a different flower; "
        "all six bowls separate and countable",
    "cups-07": "exactly seven chalices floating as glowing holograms in two clean rows — four on "
        "the lower row and three on the upper — 4 + 3 = 7; each bowl separate and un-occluded",
    "cups-08": "exactly eight chalices stacked on the ledge as 3 + 3 + 2 with one clearly empty "
        "gap between the sixth and the seventh; all eight bowls countable",
    "cups-09": "exactly nine chalices on the glowing shelf in a neat 3 x 3 grid — three rows of "
        "three, 3 + 3 + 3 = 9; evenly spaced, all nine bowls fully visible",
    "cups-10": "exactly ten chalices along the rainbow-arc glass shelf — four on the left half, "
        "four on the right half, two at the apex — 4 + 4 + 2 = 10; all ten bowls countable",
    "cups-page": "exactly one chalice-shaped basin beside the tub; the fishbowl goldfish is a fish, "
        "not a cup; no other cup anywhere",
    "cups-knight": "exactly one golden chalice resting on the horseshoe tray; no other cup",
    "cups-queen": "exactly one lidded golden chalice cradled in the sculpted stone wave; no other "
        "cup",
    "cups-king": "exactly one great chalice-shaped basin between the two fish-shaped faucets; the "
        "aquarium fish are fish, not cups; no other cup",
    "swords-ace": "exactly one crystal cyber-blade displayed upright on the vanity; the chrome "
        "rainfall column is a shower fixture, not a sword; no second blade anywhere",
    "swords-02": "exactly two slim crystal blades held crossed in a single X before her, one over "
        "each shoulder; no third blade",
    "swords-03": "exactly three slim crystal blades standing in the heart-shaped ice sculpture — "
        "one vertical from above and two angled from the left and right; three separate hilts "
        "clearly countable, 1, 2, 3",
    "swords-04": "exactly four crystal blades: three mounted in a row on the wall rack above plus "
        "one lying flat on the bench below — 3 + 1 = 4; all four blades complete and countable",
    "swords-05": "exactly five crystal blades: three gathered upright and fanned in her hands, all "
        "three hilts separate, plus two lying abandoned on the wet floor behind her — 3 + 2 = 5",
    "swords-06": "exactly six crystal blades standing upright in the tub rim — three on her left "
        "and three on her right — 3 + 3 = 6; all six hilts above the rim, none crossing her body",
    "swords-07": "exactly seven crystal blades: five gathered upright and fanned in her arms with "
        "four clear gaps between the five hilts, plus exactly TWO planted upright in the planter "
        "behind her with one wide gap of bare floor between them — never four planted; 5 + 2 = 7",
    "swords-08": "exactly eight crystal blades planted in one open ring around the freestanding tub "
        "— three in front of her, one at her left side, one at her right side, three behind her; "
        "keep the group behind her at exactly THREE, never four; 3 + 1 + 1 + 3 = 8",
    "swords-09": "exactly nine crystal blades mounted on the wall in three rows of three — 3 + 3 + "
        "3 = 9; a neat 3 x 3 grid, all nine countable, none hidden behind her head or hands",
    "swords-10": "exactly ten crystal blades lying flat along the foot of the tub in two staggered "
        "rows of five — 5 + 5 = 10; all ten hilts countable, evenly spaced, none overlapping",
    "swords-page": "exactly one crystal blade with a feather plume tied to its hilt, gripped in "
        "both her hands; no dagger, no second blade",
    "swords-knight": "exactly one crystal blade pointed forward like a lance in her hand; no other "
        "blade",
    "swords-queen": "exactly one upright crystal blade wrapped in a laurel wreath standing beside "
        "the throne; no other blade",
    "swords-king": "exactly one upright crystal blade standing between the twin wing sculptures; no "
        "other blade",
    "pentacles-ace": "exactly one large golden pentacle coin resting in the fountain's cupped stone "
        "hands; no other coin, none scattered in the garden",
    "pentacles-02": "exactly two golden pentacle coins, one spinning on each of her palms; the "
        "chrome infinity ribbon is a tray, not a coin; no third coin",
    "pentacles-03": "exactly three coins set into the arch mosaic — one at the apex and two at the "
        "springing points, 1 + 2 = 3; all three discs fully visible",
    "pentacles-04": "exactly four coins: one held against her chest, one balanced on the vanity "
        "edge, two resting on the tub rim — 1 + 1 + 2 = 4; all four discs fully visible",
    "pentacles-05": "exactly five coins set in the stained-glass window in a quincunx — one at the "
        "top center, two on the middle row, two on the bottom row, 1 + 2 + 2 = 5; all five "
        "separate and countable",
    "pentacles-06": "exactly six coins balanced across the scale beam — three stacked in the left "
        "pan and three stacked in the right pan, 3 + 3 = 6; no coins loose on the floor",
    "pentacles-07": "exactly seven coins hanging on the vine — three on the left branch, three on "
        "the right branch, one at the top center, 3 + 3 + 1 = 7; none hidden by leaves",
    "pentacles-08": "exactly eight finished coins inlaid in ONE straight row along the front edge "
        "of the marble bench; the blank stone disc on the workbench is unfinished and does NOT "
        "count and must not look like a coin",
    "pentacles-09": "exactly nine coins fixed in ONE row along the arbor beam, evenly spaced, all "
        "nine fully visible, none hidden by leaves or by her body — count them left to right: 1 to 9",
    "pentacles-10": "exactly ten coins in the tree-of-life mosaic in a pyramid — four on the bottom "
        "row, three above them, two above those, one at the apex, 4 + 3 + 2 + 1 = 10; all ten "
        "countable",
    "pentacles-page": "exactly one large coin held up in both her cupped hands; no other coin "
        "anywhere",
    "pentacles-knight": "exactly one coin resting on the horseshoe tray; no other coin",
    "pentacles-queen": "exactly one coin entwined with rose stems in the crystal bowl; no other coin",
    "pentacles-king": "exactly one coin glowing above the bull's horns; no other coin",
}

DEPTH_BATHROOM = ("DEPTH & LIGHT: soft steam and light-shaft layers diffusing the bathroom's accent "
                  "lighting (LED, neon, candle or skylight), wet tile and mirror reflections on "
                  "soaked skin, cinematic warm-cool contrast, water droplets sparkling in the light "
                  "shafts, faint golden sparkles in the mist.")

# ---------------------------------------------------------------------------
# LOẠI BỎ TOÀN BỘ GIÁP — thay thế cụm từ giáp trong spec cũ bằng mô tả không giáp
# ---------------------------------------------------------------------------
ARMOR_PHRASES = [
    # hair / signature fields
    ("dark hair streaming wildly back from beneath an open winged helmet",
     "dark hair streaming wildly back, pinned with a slim silver wing hairpin"),
    ("braided under an oak-leaf crested helmet", "braided loosely with a small oak-leaf pin"),
    ("xăm nhỏ hình mũ giáp cánh trên vai trái", "xăm nhỏ hình đôi cánh bạc trên vai trái"),
    # classic scenes
    ("a graceful 22-year-old female knight in winged silver armor riding a calm white steed "
     "beside a stream, extending a golden chalice of peace",
     "a graceful 22-year-old woman wading beside a clear stream, extending a golden chalice of "
     "peace"),
    ("a fierce 21-year-old female knight in gleaming steel armor charging on a galloping horse, "
     "sword held high into the storm winds",
     "a fierce 21-year-old woman charging forward with a blade held high into the storm winds"),
    ("a steadfast 23-year-old female knight in dark armor holding a golden pentacle with calm "
     "reverence in a plowed field",
     "a steadfast 23-year-old woman holding a golden pentacle with calm reverence in a golden "
     "field"),
]
ARMOR_REGEXPS = [
    (re.compile(r"\s*female knight in (?:winged silver|gleaming steel|dark|plate|full|shining) "
                r"armor\s*"), " "),
    (re.compile(r"\s*(?:with |wearing |dressed in )?no armor\b"), ""),
    (re.compile(r"\s*an? open winged helmet"), ""),
    (re.compile(r"\s*an? oak-leaf crested helmet"), ""),
    (re.compile(r"\bhelmet\b"), "hair"),
    (re.compile(r"\barmou?r\b"), ""),
    (re.compile(r"\bgiáp\b"), ""),
    (re.compile(r"\s{2,}"), " "),
]


def strip_armor(text: str) -> str:
    """Xóa mọi mô tả giáp / mũ giáp / trang phục lạ khỏi text (yêu cầu: chỉ swimwear ướt)."""
    s = text
    for old, new in ARMOR_PHRASES:
        s = s.replace(old, new)
    for old, new in GARMENT_PHRASES:
        s = s.replace(old, new)
    for rx, new in ARMOR_REGEXPS:
        s = rx.sub(new, s)
    return s.strip()


# Trang phục lạ trong spec (cloak/vestment/cowl...) — thay bằng mô tả tóc/da thuần túy
GARMENT_PHRASES = [
    ("falling over embroidered ceremonial vestments", "falling loose over one bare shoulder"),
    ("veiled beneath sheer white cowl gauze", "with a thin white ribbon woven through the strands"),
    ("unbound and draping over cloaked shoulders", "unbound and draping over her bare shoulders"),
    ("deep brown hair tucked under a travel cloak", "deep brown hair tucked behind her ears with a small brass pin"),
    ("gathered softly in a misty veil", "gathered softly with a thin pearl hairpin"),
]

# Bối cảnh streamer hiện đại (kế thừa update_modern_manhwa.py, đã sanitize)
MODERN_SCENES = {
    "00-fool": "a playful 19-year-old blonde streamer sitting casually barefoot on the edge of a "
               "high-rise luxury balcony railing overlooking a glowing cyberpunk morning cityscape, "
               "holding a glowing digital white rose, a cute white Pomeranian puppy sitting beside "
               "her gaming chair, skin and bikini still dewy from the rooftop jacuzzi",
    "01-magician": "a charismatic 22-year-old streamer at her multi-monitor streaming desk, one hand "
                   "raising a glowing wand-shaped stream mic to the sky and the other pointing down "
                   "to the desk, exactly four holographic suit icons floating above the desk: one "
                   "flaming wand mic, one glowing water cup, one crystal cyber blade, one golden "
                   "crypto coin, a garden of black roses in LED vases behind her",
    "02-priestess": "a serene 23-year-old streamer sitting gracefully on a sleek obsidian gaming chair "
                    "between two tall RGB light bars (one black, one white), a glowing holographic "
                    "crescent moon beneath her bare feet, a glowing digital tablet of secret lore "
                    "resting in her lap, a pomegranate hologram shimmering beside her",
    "03-empress": "a luxurious 24-year-old streamer reclining in a plush velvet recliner in a modern "
                  "sunlit penthouse garden room, golden sunlight streaming through floor-to-ceiling "
                  "windows, holding a golden smartphone scepter, surrounded by lush indoor plants and "
                  "fresh fruits, a heart-shaped shield of Venus emblem glowing on the wall",
    "04-emperor": "a dominant 25-year-old streamer seated with poised posture in an executive leather "
                  "gaming throne with ram-horn headrest designs, RGB volcanic-red ambient backlighting, "
                  "glowing PC setup, holding a golden ankh stylus, ram-head sculptures on the desk, "
                  "barren mountain mural behind",
    "15-devil": "a seductive succubus streamer in a dark red-neon gaming room, curved black horns and "
                "dark wings, sitting back on a leather gaming seat with arms behind head, loose golden "
                "chain links draped across the desk, glowing crimson pentagram RGB on wall",
    "17-the-star": "a serene star-goddess streamer sitting in a black gaming chair with arms raised "
                   "behind her head, dual curved monitors displaying glowing star constellations, "
                   "pouring two streams of digital light from golden decanters onto a desktop water "
                   "feature, giant holographic eight-pointed star glowing above",
    "21-world": "a graceful streamer posing at the center of a circular RGB ring-light laurel arch in "
                "a panoramic high-rise penthouse studio overlooking a 360-degree night skyline, holding "
                "two glowing stylus wands, four pet avatar screens at the four corners",
}

MODERN_FALLBACK = ("the card's symbolism re-staged in a modern luxury penthouse streamer studio: "
                   "{emblem} rendered as a glowing holographic emblem above her, PC monitors and RGB "
                   "neon ambient lighting, the suit objects arranged on her streaming desk, night city "
                   "skyline bokeh through floor-to-ceiling windows")

DEPTH_MODERN = ("DEPTH & LIGHT: layered neon RGB ambient lighting, glowing monitor and hologram "
                "reflections on wet skin, cinematic warm-cool contrast, night city bokeh through "
                "floor-to-ceiling windows, faint golden sparkles in the air.")

DEPTH_CLASSIC = ("DEPTH & LIGHT: layered atmospheric background receding into mist per the scene, "
                 "glowing ambient reflections on wet skin and water, cinematic warm-cool contrast, "
                 "faint golden sparkles in the air.")


def sanitize_scene(scene: str) -> str:
    """Đổi mô tả nude/semi-nude/see-through của spec cũ thành trang phục swimwear ướt."""
    s = scene.replace("semi-nude", "in a soaking-wet micro string bikini")
    s = s.replace("a nude woman", "a woman in a soaking-wet micro string bikini")
    s = s.replace("nude woman", "woman in a soaking-wet micro string bikini")
    s = s.replace("nude", "swimwear-clad")
    EXTRA = [
        ("draped only in a transparent silk veil so fine it clings and reveals her bare body beneath, "
         "the veil slipping from one shoulder and streaming behind her",
         "wearing a soaking-wet micro string bikini with a fine opaque silk sash slipping from one "
         "shoulder and streaming behind her"),
        ("bare torso with a length of silk slung low across her hips",
         "soaking-wet micro string bikini with a length of silk slung low across her hips"),
        ("one breast bared, ", ""),
        ("one breast bared", ""),
        ("reveals her bare body", "gleams over her soaking-wet micro string bikini"),
        ("transparent silk veil", "opaque silk sash"),
        ("bare shoulders and the soft line of her breasts veiled only by a drift of sheer gauze",
         "bare shoulders, her soaking-wet micro string bikini accented by a drift of opaque silk gauze over one arm"),
        ("draped only in a diaphanous opaque silk sash so fine it clings to her soft curves and glows "
         "with warm light against her skin, the gossamer fabric slipping from one shoulder",
         "wearing a soaking-wet micro string bikini with a silk sash glowing with warm light, "
         "slipping from one shoulder"),
    ]
    for old, new in EXTRA:
        s = s.replace(old, new)
    s = re.sub(r"draped only in [^,.]*", "wearing a soaking-wet micro string bikini with a glowing silk sash", s)
    s = s.replace("her bare back and the curve of one breast veiled and revealed by the golden lantern light",
                  "her wet skin glowing in the golden lantern light")
    s = s.replace("flowing transparent silk", "flowing silk robes")
    s = s.replace("transparent silk", "opaque silk")
    s = s.replace("sheer white silk gauze", "opaque white silk sash")
    s = s.replace("sheer opaque silk", "flowing opaque silk")
    EXTRA2 = [
        ("a length of sheer silk sliding fully off one shoulder to bare one breast and one hip",
         "an opaque silk sash sliding off one shoulder"),
        ("draped in sheer black silk that veils and reveals her bare form",
         "wearing a soaking-wet black micro string bikini with a flowing black silk sash"),
        ("her bare torso turned toward the light", "her wet glossy torso turned toward the light"),
        ("one arm across her breast", "one arm across her chest"),
        ("wearing a gown of antique WHITE SILK GAUZE so sheer and transparent that the light shines "
         "through it and the long line of her body reads clearly beneath",
         "wearing a fully opaque gown of antique white silk glowing softly in the sea light"),
    ]
    for old, new in EXTRA2:
        s = s.replace(old, new)
    s = re.sub(r"veils and reveals her [a-z ]*form", "drapes her swimwear-clad figure", s)
    s = re.sub(r"so sheer and transparent that[^,]*", "fully opaque", s)
    EXTRA3 = [
        ("draped in sheer black silk upon a dark pedestal",
         "wearing a soaking-wet black micro string bikini with a black silk sash upon a dark pedestal"),
        ("in a sheer flowing gown that clings to breast and hip",
         "in a flowing fully opaque gown that clings to her curves"),
        ("in a very thin veil of antique silk gauze, almost transparent, her shoulders bare",
         "in an opaque antique silk gown, her shoulders bare"),
        ("whose body is wrapped in a single sheet of TRANSPARENT antique silk gauze, one shoulder "
         "and the curve of her breast left bare",
         "wearing an opaque antique silk gown with one shoulder bare"),
    ]
    for old, new in EXTRA3:
        s = s.replace(old, new)
    return s


PROMPT_TEMPLATE = """A completely frameless vertical tarot card "{title}", edge-to-edge illustration: no decorative borders, no card frame, no banner ribbon, no numbers, no Roman numerals. The only text is the title "{title}" centered at the very bottom in the same antique-gold serif lettering as the style reference card.

REFERENCE IMAGES: (1) major_08_strength.png — art style, contour rendering, garment-to-body detail, warm golden rim light and bottom title lettering. (2) test_card_17_the_star.png — soaking-wet swimwear fabric benchmark and glossy wet skin finish.

ART STYLE (match reference 1): Korean manhwa webtoon rendering — crisp clean lineart, soft cell shading, bold contour outlines tracing every curve of the body (cinched waist, flared hips, belly line, thigh and knee curves, collarbones and shoulders), glossy specular highlight streaks running along each curve so the body's lines pop, strong three-dimensional modeling, warm golden rim light hugging the figure against the scene palette.

GARMENT-TO-BODY DETAIL: thin strap tension lines pressing gently into shoulders and hips, fabric edges precisely tracing the underbust curve and hip crest, subtle soft skin swell over each bikini edge, delicate cast-shadow lines under the fabric rims, small tension folds in the wet fabric following the body topography, side-tie ribbon knots pulling the hip line with tiny gathers, specular highlights along every seam and strap.

WET FABRIC (match reference 2): soaking-wet {outfit} micro string bikini {accent} — waterlogged darkened tone with a glossy wet sheen, fabric fully opaque, clinging like a second skin with zero loose folds, plastered wet wrinkles, water droplets beading on the fabric surface, tiny drips falling from the fabric edges; whole body wet with droplets and thin rivulets, wet gleaming hair strands; she is mid-shower under the rainfall head or just stepped out of the tub, so the soaked look reads naturally indoors.

FIGURE: {char_spec} Alluring pose: {pose}. Barefoot; blushing cheeks, cat eyeliner, softly parted lips.

SCENE & SYMBOLISM ({style}): {scene}. Tarot emblem integrated naturally: {emblem}. {count_lock}

{depth}

NO ARMOR ANYWHERE ON THE FIGURE — strictly no helmet, no breastplate, no gauntlets, no chainmail, no pauldrons, no metal plates, no knight costume pieces; she wears only the soaking-wet swimwear described above.

ANATOMY & QUALITY LOCK: perfect anatomy — exactly two arms and two legs, exactly five fingers on each hand, natural joint bends, symmetrical face, correct limb count, no extra or fused limbs, no deformed hands, clean crisp lineart; the pose is drawn like a master manhwa figure study.

At the bottom, centered: the title "{title}" in antique-gold serif lettering matching reference 1. No numbers, no Roman numerals, no other text, no frame, no border, no banner, no watermark, no signature. Masterpiece manhwa illustration, portrait 7:12."""

MD_TEMPLATE = """# {title} ({n}) — Frameless Wet-Manhwa v2.2 · mode {mode}

- **Slug:** `{slug}` | **Group:** {group}
- **Emblem:** {emblem}
- **Phong cách phòng tắm:** {style}
- **Reference style/contour/lettering:** `major_08_strength.png`
- **Reference wet fabric/swimwear:** `test_card_17_the_star.png`
- **Outfit:** soaking-wet {outfit} micro string bikini {accent} (opaque swimwear, no see-through)
- **Pose gợi cảm:** {pose}
- **Background mode:** {mode} · **Giáp:** đã loại bỏ hoàn toàn (strip + negative)

## Prompt

```text
{prompt}
```
"""


def nz(value, default):
    """Trả về default nếu giá trị bị thiếu hoặc là 'N/A' (lá Át không có figure spec)."""
    return default if value in (None, "", "N/A", "n/a") else value


def build_char_spec(c):
    age = nz(c.get("age"), "20 years old")
    build = nz(c.get("build"), "slender waist with curvy feminine silhouette")
    hair = nz(c.get("hair"), "flowing golden hair")
    eyes = nz(c.get("eyes"), "alluring eyes")
    skin = nz(c.get("skin"), "porcelain")
    signature = nz(c.get("signature"), "a tiny gold star mark behind her ear")
    aura = nz(c.get("aura"), "warm steam and soft light")
    spec = (
        f"{age}, build: {build}, hair: {hair}, eyes: {eyes}, "
        f"skin: {skin} with glossy wet highlights, signature: {signature}, aura: {aura}."
    )
    return strip_armor(spec)


def bathroom_count_lock(c, slug):
    """Count lock viết riêng cho staging phòng tắm (số lượng giữ nguyên bản gốc)."""
    cnt = c.get("count")
    if not cnt or cnt.get("n") in (None, 0):
        return BATHROOM_NO_COUNT_LOCK
    n = cnt["n"]
    obj = cnt["obj"]
    layout = BATHROOM_LAYOUTS.get(slug)
    if not layout:
        layout = cnt.get("layout", f"exactly {n} {obj}, all fully visible")
    obj_upper = obj.upper() if n > 1 else obj
    lines = [
        f"COUNT LOCK — EXACTLY {n} {obj_upper} (hard constraint; count before you draw).",
        f"The scene contains exactly {n} {obj} — not {n - 1}, not {n + 1}.",
        f"Placement is locked: {layout}",
        f"Every one of the {n} must be fully visible: nothing occluded by a body, limb, cloth, "
        f"steam or another object, nothing fused, broken, cropped or half-hidden behind a figure. "
        f"Keep them at one consistent size, shape, material and color so they read as a single "
        f"countable set, with a clear gap of background between each one. Place no other {obj} "
        f"anywhere else on the card — not in the frame, not in the background, not as decoration. "
        f"The emblem is a separate heraldic motif and does NOT count toward the {n}. Before "
        f"finishing, count them: 1 to {n}. If the total is not {n}, redraw.",
    ]
    return "\n".join(lines)


def build_readme(styles_table):
    return f"""# prompts_frameless_v2 — Bộ prompt công thức The Star áp dụng toàn bộ 78 lá

Thư mục riêng biệt chứa prompt MỚI cho toàn bộ bộ bài, sinh bởi `build_prompts_v2.py`
từ `cards.json`, KHÔNG ghi đè dữ liệu gốc.

## Công thức cốt lõi (v2.2)

1. **Frameless no-num** (template `update_no_num.py`): illustration tràn viền,
   không khung/không banner/không số La Mã; chỉ tên lá bài chữ serif vàng cổ điển dưới đáy.
2. **Style reference `major_08_strength.png`**: manhwa webtoon lineart sắc, cel shading,
   contour viền đậm ôm từng curve + specular streak dọc đường nét, rim light vàng ấm,
   chữ title serif vàng giống lá Strength.
3. **Garment-to-body detail**: vết căng dây trên da, mép vải ôm underbust/hip crest,
   bóng đổ dưới mép vải, nếp tụ ở nút dây hông, highlight dọc đường may/dây đeo.
4. **Wet fabric reference `test_card_17_the_star.png`**: vải ướt sũng tone sẫm ngậm nước,
   sheen bóng, nếp ướt dán sát như da thứ hai, giọt nước đọng và rỉ từ mép vải;
   toàn thân ướt, tóc ướt bóng; justify bởi "vừa bước khỏi bồn tắm / đang xả vòi sen".
5. **Trang phục & pose**: micro string bikini swimwear opaque (màu xoay vòng 6 màu),
   **pose gợi cảm** (xoay vòng 12 pose S-curve gợi cảm, không lộ liễu),
   má hồng + cat eyeliner + môi hé.
6. **An toàn nội dung**: mọi mô tả nude/semi-nude/see-through của spec cũ được thay bằng
   trang phục swimwear ướt opaque; không pose lộ liễu. Toàn bộ nhân vật là người trưởng thành.

## Yêu cầu v2.2 (theo yêu cầu người dùng)

- **Tư thế gợi cảm**: 12 pose alluring S-curve xoay vòng theo thứ tự lá
  (tựa lưng vào tường ướt, ngả người trên thành bồn, nhìn lại qua vai, ưỡn cong như cung,
  nằm nghiêng mermaid, đang bước ra khỏi vòi sen, căng người kiễng chân, ...).
- **Phong cách phòng tắm KHÁC NHAU từng lá**: 78 phong cách riêng biệt, không lá nào lặp
  (xem bảng dưới) — từ Scandi sunrise spa, Byzantine gilded chapel, volcanic hot spring,
  casino-noir roulette, storm skyscraper glass, midnight lagoon... đến aquarium throne.
- **Đặc điểm nổi bật của từng lá được giữ nguyên**: FIGURE spec (tuổi/ body type / tóc /
  mắt / da / signature / aura), emblem tarot, và COUNT LOCK số lượng vật phẩm suit
  (được viết lại cho staging phòng tắm nhưng giữ đúng số lượng: 3 chalice, 7 sword,
  10 pentacle...).
- **Loại bỏ toàn bộ giáp**: `strip_armor()` xóa mọi cụm từ armor/helmet/mũ giáp khỏi spec
  (Knight of Swords/Pentacles...) + câu cấm hard `NO ARMOR ANYWHERE ON THE FIGURE` trong
  mọi prompt.
- **Fix**: lá Át (age/hair N/A) giờ có figure mặc định hợp lệ (20 years old, người trưởng thành).

## Bảng 78 phong cách phòng tắm

{styles_table}

## Màu trang phục (xoay vòng 6, không theo group)

pearl-white · midnight-black · aqua-teal · rose-pink · metallic gold · cherry-red
(với accent: gold star charms / gold chain straps / side-tie ribbons / satin bows /
lace-trim edges / pearl beads)

## Cấu trúc thư mục

- `<slug>.md` — prompt đầy đủ từng lá (kèm metadata + reference)
- `all_prompts.json` — map slug → prompt (machine-readable)
- `README.md` — tài liệu này

## Cách dùng khi sinh ảnh

Đưa kèm 2 ảnh reference cho model: `major_08_strength.png` (style/contour/chữ)
và `test_card_17_the_star.png` (vải ướt/swimwear), rồi dán prompt của lá tương ứng.

## Tái sinh

```bash
python3 build_prompts_v2.py
```
"""


def main():
    with open("cards.json", encoding="utf-8") as f:
        data = json.load(f)

    cards = data["cards"]
    slugs = [c["slug"] for c in cards]

    # Kiểm tra phủ đủ 78 phong cách phòng tắm
    missing = [s for s in slugs if s not in BATHROOM_STYLES]
    if missing:
        raise SystemExit(f"BATHROOM_STYLES thiếu các lá: {missing}")
    extra = [s for s in BATHROOM_STYLES if s not in slugs]
    if extra:
        raise SystemExit(f"BATHROOM_STYLES thừa các slug lạ: {extra}")

    # Kiểm tra tính duy nhất của style (không lá nào trùng phong cách)
    style_names = [BATHROOM_STYLES[s][0] for s in slugs]
    dupes = {n for n in style_names if style_names.count(n) > 1}
    if dupes:
        raise SystemExit(f"Phong cách phòng tắm bị trùng: {dupes}")

    os.makedirs(OUT_DIR, exist_ok=True)
    all_prompts = {}
    styles_rows = []
    armor_hits = 0

    for idx, c in enumerate(cards):
        slug = c["slug"]
        title = c["title"]
        bikini_color, bikini_accent = BIKINI_OPTIONS[idx % len(BIKINI_OPTIONS)]
        pose = ALLURING_POSES[idx % len(ALLURING_POSES)]

        if BACKGROUND_MODE == "bathroom":
            style_name, scene = BATHROOM_STYLES[slug]
            depth = DEPTH_BATHROOM
            count_lock = bathroom_count_lock(c, slug)
        elif BACKGROUND_MODE == "modern":
            style_name = "modern penthouse"
            scene = MODERN_SCENES.get(slug, MODERN_FALLBACK.format(emblem=c["emblem"]))
            depth = DEPTH_MODERN
            count_lock = c.get("count_lock", "")
        else:
            style_name = "classic"
            scene = sanitize_scene(c["scene"])
            depth = DEPTH_CLASSIC
            count_lock = c.get("count_lock", "")

        scene = strip_armor(scene)
        char_spec = build_char_spec(c)  # đã strip_armor bên trong
        prompt = PROMPT_TEMPLATE.format(
            title=title,
            outfit=bikini_color,
            char_spec=char_spec,
            scene=scene,
            emblem=c["emblem"],
            count_lock=count_lock,
            depth=depth,
            accent=bikini_accent,
            pose=pose,
            style=style_name,
        )
        # Kiểm tra giáp: chỉ quét phần mô tả (bỏ qua câu NO ARMOR chủ đích trong template)
        ban = "NO ARMOR ANYWHERE ON THE FIGURE"
        scan = prompt.split(ban)[0] + prompt.split(ban)[-1][prompt.split(ban)[-1].find("\n"):]
        if re.search(r"armou?r|helmet|breastplate|gauntlet|chainmail|giáp", scan, re.I):
            armor_hits += 1
            print(f"[WARN] Vẫn còn từ giáp trong phần mô tả: {slug}")

        all_prompts[slug] = prompt
        styles_rows.append(f"| {c['n']} | {slug} | {title} | {BATHROOM_STYLES[slug][0]} |"
                           if BACKGROUND_MODE == "bathroom" else
                           f"| {c['n']} | {slug} | {title} | (mode {BACKGROUND_MODE}) |")

        md = MD_TEMPLATE.format(
            title=title,
            n=c["n"],
            slug=slug,
            group=c["group"],
            emblem=c["emblem"],
            outfit=bikini_color,
            accent=bikini_accent,
            pose=pose,
            mode=BACKGROUND_MODE,
            style=BATHROOM_STYLES[slug][0] if BACKGROUND_MODE == "bathroom" else BACKGROUND_MODE,
            prompt=prompt,
        )
        with open(os.path.join(OUT_DIR, f"{slug}.md"), "w", encoding="utf-8") as f:
            f.write(md)

    with open(os.path.join(OUT_DIR, "all_prompts.json"), "w", encoding="utf-8") as f:
        json.dump(all_prompts, f, ensure_ascii=False, indent=2)

    header = ("| # | Slug | Lá | Phong cách phòng tắm |\n|---|---|---|---|\n")
    with open(os.path.join(OUT_DIR, "README.md"), "w", encoding="utf-8") as f:
        f.write(build_readme(header + "\n".join(styles_rows)))

    print(f"Wrote {len(all_prompts)} card prompts (mode={BACKGROUND_MODE}) into {OUT_DIR}/")
    print(f"Armor warnings: {armor_hits}")
    print(f"Unique bathroom styles: {len(set(style_names))}/{len(style_names)}")


if __name__ == "__main__":
    main()
