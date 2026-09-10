#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""port_star_export.py — port 5 prompt trong prompts_frameless_v2/star_external_export/
sang bản TUÂN THỦ (v3.3 bikini 2 mảnh mặc nguyên + FACE/style theo `the star.png`).

Giữ nguyên: 5 biến thể pose (06→10), staging open-sky stargazer, COUNT LOCK 2 bình vàng,
DEPTH & LIGHT, ANATOMY LOCK, chữ vàng đáy thẻ.
Thay:      "top tuột xuống eo / ngực trần / nước đổ lên ngực" -> bikini top MẶC NGUYÊN phủ kín,
           hai dòng nước đổ lên cặp khuy đồng + trải trên lớp vải ướt;
           "21-year-old streamer" -> "adult woman in her twenties";
           "clinging like a second skin / zero loose folds" (token bị backend chặn) -> "smooth, water-heavy sheen";
           reference ảnh: major_08_strength + test_card_17 -> `the star.png`.
Chạy: python3 port_star_export.py
"""
import json
import os
import re

SRC = "prompts_frameless_v2/star_external_export"
OUT = os.path.join(SRC, "safe_star_bikini")
POSES = ["17-star_pose06_twin_overhead.txt", "17-star_pose07_profile_pour.txt",
         "17-star_pose08_waterline_recline.txt", "17-star_pose09_shoulder_pour.txt",
         "17-star_pose10_rim_lean.txt"]

STYLE = (
    "ART STYLE (match `the star.png`): semi-realistic Korean manhwa digital PAINTING — soft airbrushed gradient "
    "shading and gentle bloom, edges separated by rim light instead of ink outlines, satin skin highlights with "
    "cool blue-violet shadow fill, hyper-detailed antique-gold filigree jewellery whose gems catch specular "
    "points, pearl-satin fabric with realistic weight, double-fold creasing and gold embroidery, a translucent "
    "layered tulle veil, a richly painted hazy background with volumetric light and reflections on wet tile and "
    "water, slight film grain.\n\nFACE (keep the reference card's expression): heavy half-lidded dreamy eyes "
    "gazing softly down, small glossy parted lips, faint blush across cheeks and nose, delicate oval face, tiny "
    "straight nose, a few wet platinum strands clinging across one cheek, calm and slightly dazed.")

COSTUME = (
    "COSTUME — the reference card's design as a two-piece bikini, WORN CORRECTLY: a pearl-ivory wet satin "
    "two-piece with a structured underwired top whose fully lined cups cover the bust completely, closed at "
    "centre front by two round antique-gold rosette clasps engraved with an eight-pointed star, thin gold-wrapped "
    "straps over the shoulders and back, matching high-cut satin bottoms edged in fine gold wire; over the hips "
    "the reference's ornate gold filigree hip chain set with a large luminous pearl from which a long embroidered "
    "silk panel falls down the front of the thighs; a floor-length sheer veil hemmed with gold star embroidery; "
    "openwork gold armbands, gold wrist bangles, a jewelled forehead circlet with a teardrop pearl, a pearl "
    "pendant on a fine gold chain. Wet from the bath: satin darkened a shade with a glossy sheen, smooth and "
    "water-heavy, tiny beads on the fabric, droplets falling from every hem, hair wet and slicked; swimwear-grade "
    "OPAQUE fabric — the top stays up and covers the whole bust, nothing transparent, no nudity.")

GARMENT_DETAIL = (
    "GARMENT-TO-BODY DETAIL: thin strap tension lines pressing gently into shoulders, fabric edges tracing the "
    "underbust seam and hip crest, soft cast shadows under each rim, small tension folds where the wet satin "
    "pulls toward the gold clasps, specular highlights along every seam, strap and chain link.")

SUBS = [
    (r"A completely frameless vertical tarot card", "A vertical tarot card"),
    (r"edge-to-edge illustration: no decorative borders, no card frame, no banner ribbon, no numbers, "
     r"no Roman numerals\.", "framed exactly like the reference card: a thin antique-gold ornamental border with "
     "filigree flourishes in the four corners and the title in a small bottom band; that bottom title is the ONLY "
     "text on the card, no caption at the top, no numbers, no Roman numerals."),
    (r"REFERENCE IMAGES:.*?\n\n", "", re.S),
    (r"ART STYLE \(match reference 1\):.*?\n\n", STYLE + "\n\n", re.S),
    (r"GARMENT-TO-BODY DETAIL:.*?\n\n", GARMENT_DETAIL + "\n\n", re.S),
    (r"(?m)^she wears only the soaking-wet.*?\n\n", COSTUME + "\n\n", re.S | re.M),
    (r"FIGURE: 20 years old", "FIGURE: an adult woman in her twenties"),
    (r"a serene 21-year-old streamer", "a serene adult woman in her twenties"),
    (r", hair: very long platinum-white hair, wet and silky, gleaming like liquid silver, cascading down past one "
     r"bare shoulder", ", hair: very long platinum-white, wet and silky, gleaming like liquid silver, cascading "
     "past one shoulder"),
    (r"; her little bikini top slid down and bunched low around her waist", ""),
    (r"her little bikini top slid down and bunched low around her waist; ", ""),
    (r", her little bikini top bunched low around her waist", ""),
    (r"her little bikini top bunched low around her waist, its little cups half-lost in the water's pale blur; ",
     "the soaked silk panel floating in the water's pale blur beside her; "),
    (r"her little bikini top bunched low around her waist behind her, fine straps tangled at the hip knots, ",
     "her wet platinum hair "),
    (r"onto her chest and spreads across it in a bright glittering veil of falling water",
     "onto the two gold clasps at her chest and spreads over the covered bust in a bright glittering veil of "
     "falling water"),
    (r"onto her chest, meeting and spreading across it in a bright glittering veil of falling water",
     "onto the gold clasps at her chest, meeting and spreading over the covered bust in a bright glittering veil "
     "of falling water"),
    (r"onto her chest and spreads over its profile curve in a bright sheet of falling water, veiling it artfully "
     r"as it runs down", "over the top of her bikini and the gold clasps in a bright sheet of falling water, "
     "running down"),
    (r"onto her chest and fans across it in a glittering veil of falling water",
     "over her covered chest and the gold clasps in a glittering veil of falling water"),
    (r"onto her chest and spreads across it in a bright fan of falling water",
     "over her covered chest and the gold clasps in a bright fan of falling water"),
    (r"falls past her shoulder and spreads across the front of her chest in a bright veil of falling water, "
     r"veiled from this angle behind the curve of her back and shoulder",
     "falls past her shoulder and spreads across the wet satin front of her bikini top in a bright veil of "
     "falling water, half-hidden behind the curve of her back and shoulder"),
    (r"pouring its thin stream down onto her chest", "pouring its thin stream down over her covered chest"),
    (r"clinging like a second skin with zero loose folds, plastered wet wrinkles, ", ""),
    (r"throat bared to the skylight", "throat tilted to the skylight"),
    (r"NO ARMOR ANYWHERE ON THE FIGURE — strictly no helmet, no breastplate, no gauntlets, no chainmail, "
     r"no pauldrons, no metal plates, no knight costume pieces; she wears only the soaking-wet swimwear "
     r"described above\.\n\n", "NO ARMOR — no helmet, breastplate, gauntlets or metal plates; only the bikini "
     "and gold jewellery described above.\n\n"),
]

os.makedirs(OUT, exist_ok=True)
gen = {}
for f in POSES:
    t = open(os.path.join(SRC, f), encoding="utf-8").read()
    for row in SUBS:
        pat, rep = row[0], row[1]
        flags = row[2] if len(row) > 2 else 0
        t = re.sub(pat, rep, t, flags=flags)
    for pat, rep in [
        (r", its little cups half-lost in the water's pale blur", ""),
        (r"her wet platinum hair her long wet platinum hair", "her long wet platinum hair"),
        (r", tangled at the hip-tie knots", ""),
        (r" The only text is the title \"THE STAR\" centered at the very bottom in the same antique-gold serif "
         r"lettering as the style reference card\.", ""),
        (r"falling down onto her chest from both sides", "falling down over her covered chest from both sides"),
        (r"pouring its thin stream down onto her chest", "pouring its thin stream over her covered chest"),
        (r"one tipped above her, pouring", "one tipped above her, pouring"),
    ]:
        t = re.sub(pat, rep, t)
    t = re.sub(r"\n{3,}", "\n\n", t).replace("**A** ", "").strip()
    assert "slid" not in t and "bunched" not in t and "bare chest" not in t, f
    assert "nude" not in t.lower()
    name = f.replace(".txt", "_SAFE.txt")
    open(os.path.join(OUT, name), "w", encoding="utf-8").write(t + "\n")
    m = re.search(r"Alluring pose: (.*?) Barefoot", t, re.S)
    pose = " ".join(m.group(1).split())
    gen[name] = pose

json.dump(gen, open(os.path.join(OUT, "safe_poses.json"), "w", encoding="utf-8"),
          ensure_ascii=False, indent=1)

# ---- bản gọn (~2000 ký tự) để dán vào tool sinh ảnh: backend fail khi prompt >2500 ký tự ----
HEAD = ('Vertical tarot card "THE STAR" painted exactly like the attached reference image `the star.png`, '
        'same brushwork and same face rendering: soft airbrushed semi-realistic Korean manhwa painting, gentle '
        'bloom, rim-light edges instead of ink outlines, satin skin highlights, richly painted hazy night '
        'background with volumetric light and water reflections, film grain. FACE = the reference expression: '
        'heavy half-lidded dreamy eyes, small glossy parted lips, faint blush, delicate oval face, wet strands '
        'across one cheek, calm and slightly dazed. Same thin antique-gold ornamental border with filigree '
        'corners and the serif gold title in a bottom band, exactly like the reference card; that bottom title is '
        'the ONLY text on the card. Adult woman in her twenties. Costume: a pearl-ivory two-piece satin bikini, '
        'structured underwired top with lined cups covering the bust completely and two round antique-gold '
        'rosette clasps engraved with an eight-pointed star at centre front, high-cut bottoms, ornate gold '
        'filigree hip chain with a large luminous pearl and a long embroidered silk panel down the front of the '
        'thighs, sheer veil hemmed with gold stars, openwork gold armbands, jewelled circlet. Wet from the bath: '
        'satin darkened and glossy with water beads, hems dripping, very long platinum hair slicked wet; fabric '
        'fully opaque. Setting: an open-sky stargazer bathroom, a circular tub beneath a glass-dome skylight '
        'showing a star constellation, an eight-pointed star glowing above her, steam and starlight on wet tile. ')
TAIL = (' EXACTLY two golden decanters, one in each hand, both fully visible and un-occluded, no other jugs '
        'anywhere. Tall 7:12 portrait, whole body visible, perfect anatomy, five fingers per hand.')
compact = {}
for key, pose in gen.items():
    slug = key.replace("_SAFE.txt", "").replace("17-star_", "")
    compact[slug] = " ".join((HEAD + "Pose: " + pose + TAIL).split())
json.dump(compact, open(os.path.join(OUT, "gen_prompts.json"), "w", encoding="utf-8"),
          ensure_ascii=False, indent=1)
print("OK ->", OUT)
for k, v in compact.items():
    print(f"\n@@@ {k} ({len(v)})\n{v}")
