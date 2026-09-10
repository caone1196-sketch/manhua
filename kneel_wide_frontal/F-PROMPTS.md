# F-PROMPTS — khối prompt dùng để sinh 21 ảnh trong thư mục này

Cách dùng: **ghép 1 khung (FRAME BLOCK) + 1 khối chung (BLOCK A) + 1 biến thế (POSE VARIANT)**.
Không bao giờ sửa BLOCK A giữa các ảnh — mọi khác biệt nằm ở POSE VARIANT và FRAME BLOCK.

---

## BLOCK A — khối chung (dùng cho mọi ảnh)

```text
ART STYLE: Korean manhwa semi-realistic painting, soft painterly shading with no black lineart outlines,
periwinkle-violet and neon-violet colour grade, crisp specular highlights on the water.

CAMERA LOCK: dead-on frontal view, perfectly symmetrical about the vertical axis of the card,
no three-quarter turn, no profile, both shoulders equidistant from the left and right edges,
a wide full-body shot from her knees to the top of the raised jugs.

SUBJECT: a young priestess performing a night purification rite, serene expression,
eyes closed in quiet devotion, damp strands of hair at her temples.

BASE POSE: kneeling in a wide seiza stance, both knees down and knees apart,
her weight resting back on her heels, soles not visible to the camera, posture upright and composed.

HAIR: long pale platinum-blonde hair, heavy and soaked, falling in gleaming strands
(hair colour must stay pale platinum in every render).

PROPS: exactly 2 antique gold jugs, one in each hand, both fully visible, nothing occluded;
BOTH STREAMS LAND ON HER BODY — the pool receives only the runoff, never the main streams.

LIGHTING: a giant eight-pointed star with god rays directly behind her head like a halo,
cool blue rim light on one side, warm gold light spilling from the jugs,
spray and droplets caught in the starlight.

SCENE: a gothic tower interior with tall violet stained-glass windows, stone pillars at both sides,
a misty black reflecting pool, a circular carved relief floor under a thin film of water.

ANATOMY LOCK: exactly two arms and two legs, one head, five fingers on each hand, natural joints,
no extra or fused limbs, no deformed hands.

CONTENT: tasteful, non-explicit classical figure study; the gown is fully opaque and modest.
```

---

## FRAME BLOCK — 4 khung

### W (có viền + title) — W01…W10

```text
FRAME: the painting sits inside a thin gilded gothic line-art border with a heraldic band along the
bottom; the title "THE STAR" is centered in that band in antique-gold serif lettering, no number,
no roman numeral, no watermark.

COSTUME: a floor-length pale ivory silk gown, long sheer sleeves, a high draped neckline,
fully opaque and modest, the soaked hem gathered on the stone.
```

### S (ướt + hở tối đa trong giới hạn) — S1…S5

```text
FRAME: full-bleed painting, no border, no text.

COSTUME: a floor-length pale ivory silk gown with a low draped neckline sitting well below the
collarbone, softly gathered, held by thin gold cords, the silk stays neatly in place and stays fully
opaque across the bust; long sheer silk sleeves; a pearl body chain, a thin pearl necklace,
a slim gold circlet with a small blue gem. Water runs down her sleeves and drips from her wrists;
a wet sheen on her shoulders and arms. Tasteful, non-explicit classical figure study.
```

### F (frameless + cổ trễ + giữ tỷ lệ) — F1b, F1c, F2, F3, F4b, F5

```text
FULL-BLEED: no card border, no ornate frame, no decorative edge, no title band, no lettering, no text,
no watermark — the painting extends to all four edges.

BODY PROPORTIONS LOCK: keep her figure exactly slender and willowy — narrow waist, small hips, long legs,
delicate shoulders. Do not enlarge, reshape or lengthen any part of her body; only the gown neckline changes.

COSTUME: a floor-length pale ivory silk gown with a low draped Grecian neckline, softly gathered and
sitting well below the collarbone, held by thin gold cords, the silk stays neatly in place and fully
opaque across the bust; long sheer sleeves; the soaked hem gathered on the stone.
```

### T (chuẩn mới: giữ tên · body size C · còn lại không đổi) — T1, T2, T3b, T4

```text
FRAME: full-bleed painting with no ornate card border, no filigree frame, no corner flourishes,
no side frame pillars. The ONLY text is the card name "THE STAR" centered at the bottom in antique-gold
serif lettering over a subtle dark inlay strip; no numbers, no roman numerals, no watermark, no signature.

BODY BUILD (the single change): she has a soft, full figure with a rounded, generous bust line and
slightly wider hips. Everything else about her body stays exactly the same as a slender build — the same
height, the same small head, the same narrow waist, the same slender arms, the same long legs,
the same knee width. Do not lengthen or enlarge any limb, do not make her taller or heavier overall.

COSTUME: a floor-length pale ivory silk gown with a low draped neckline sitting well below the
collarbone, softly gathered, held by thin gold cords, the silk stays neatly in place, long sheer sleeves,
fully covering her from the chest down to the ankles, opaque; the soaked hem gathered on the stone.
```

---

## POSE VARIANT

### W01 — `W01_arms_straight_up.png`

```text
POSE VARIANT: both arms raised straight up beside her head, each jug tipped inward, so the two streams
run down the inside of her forearms and drip from her elbows onto the stone, starting two sets of
concentric ripples that cross each other in the black water.
```

### W02 — `W02_wrists_crossed.png`

```text
POSE VARIANT: both forearms lifted and crossed at the wrists, forming a clear X above the top of her
head, the two streams falling from the crossed wrists down onto her shoulders and along her sleeves.
```

### W03 — `W03_one_high_one_low.png`

```text
POSE VARIANT: one arm raised high above her head and the other held low beside her hip, the upper
stream landing on her raised forearm and the lower stream tipped inward over her own thigh so it
splashes onto her knee — the only deliberately asymmetric version.
```

### W04 — `W04_hands_cupped.png`

```text
POSE VARIANT: both elbows tucked against her ribs, each jug pouring into her own cupped palm,
the water overflowing between her fingers and running down her wrists; her head bowed, watching her hands.
```

### W05 — `W05_arms_wide_T.png`

```text
POSE VARIANT: both arms opened wide into a T, each jug tipped so one stream falls onto each shoulder —
the widest silhouette of the set.
```

### W06 — `W06_back_arch_head_tipped.png`

```text
POSE VARIANT: she leans back into a slow arch, both forearms above her upturned face, each jug tipping so
a single stream falls onto her chin and collarbone and runs down the front of the gown; her wet hair
hangs behind her toward the stone, its tips touching the water film and starting a ring.
```

### W07 — `W07_forward_fold_hair_curtain.png`

```text
POSE VARIANT: she folds forward from the waist, both arms stretched down in front of her, the two
streams falling onto her own knees and forearms; her soaked hair hangs straight down like a curtain and
its dripping tips break the surface of the water; her face is half hidden behind wet strands.
```

### W08 — `W08_behind_the_back.png`

```text
POSE VARIANT: both arms reach back at shoulder height, each hand tipping its jug so the streams run down
the backs of her shoulders and along her sleeves; her torso stays square to the camera and her face
looks straight forward, so the water traces only the front-facing line of her shoulders.
```

### W09 — `W09_hands_at_wrists.png`

```text
POSE VARIANT: both jugs held high at forehead height, arms bent, the streams falling onto the backs of
her own hands and running down her knuckles, wrists and forearms before dripping onto the stone; her
eyes follow the water down her hands.
```

### W10 — `W10_one_knee_forward.png`

```text
POSE VARIANT: the most dynamic — one knee lifted and that foot planted, the other knee still wide on the
stone, torso rising as if about to stand, both arms extended upward with the jugs tipped; the two streams
land on her raised forearms and splash across the wet stone at her knees.
```

### S1 — `S1_open_back.png`

```text
POSE VARIANT: one arm raised high and the other held low beside her hip, her back turned far enough to
show the open back of the gown while the camera stays dead-on frontal, both shoulders symmetrical about
the vertical axis; both streams land on her body.
```

### S2 — `S2_offshoulder_slit.png`

```text
POSE VARIANT: both forearms crossed at the wrists above her head, the gown slipped off both shoulders
with a high side slit, the two streams falling clear of her body into the pool and its reflection.
```

### S3 — `S3_hair_curtain.png`

```text
POSE VARIANT: both elbows tucked against her ribs, both jugs tipped inward over the crown of her head so
the two streams converge on the top of her head and run down through her soaked hair, which falls on both
sides like a curtain; her head is bowed, face hidden behind wet strands.
```

### S4 — `S4_eyes_open_camera.png`

```text
POSE VARIANT: one arm raised high and the other held low, her eyes open with a calm gaze past the viewer,
the upper stream striking her own raised forearm and never the floor, the lower jug tipped inward over her
own thigh so its stream splashes onto her knee; both knees wide apart and clearly visible.
```

### S5 — `S5_one_knee_up.png`

```text
POSE VARIANT: one knee lifted and that foot planted, the other knee still wide on the stone, torso rising
as if about to stand, both arms extended upward with the jugs tipped — the most dynamic silhouette.
```

### F1b — `F1b_frameless_lowneck_frontal.png`

```text
POSE VARIANT: one arm raised high above her head and the other held low beside her hip, dead-on frontal,
both shoulders symmetrical about the vertical axis of the card.
```

### F1c — `F1c_frameless_both_streams_on_body.png`

```text
POSE VARIANT: one arm raised high above her head and the other held low beside her hip, dead-on frontal.

WATER PATH LOCK: the lower jug is tipped inward directly over her own thigh, so its stream splashes onto
her knee; the upper stream strikes her raised forearm; neither stream is allowed to land on the bare floor.
Soles not visible to the camera.
```

### F2 — `F2_frameless_plunge_bowed.png`

```text
POSE VARIANT: her head bowed, both elbows tucked against her ribs with both jugs tipped inward over the
crown of her head, the two streams converging on the top of her head and running down her soaked hair,
which falls on both sides like a curtain. Soles not visible to the camera.
```

### F3 — `F3_frameless_plunge_wrists_x.png`

```text
POSE VARIANT: both forearms lifted and crossed at the wrists into a clear X above her head, the two
streams falling from the crossed wrists down onto her shoulders and along her sleeves — the most balanced
silhouette of the series.
```

### F4b — `F4b_frameless_lowneck_rising.png`

```text
POSE VARIANT: one knee lifted and that foot planted, the other knee still wide on the stone, torso rising
as if about to stand, both arms extended upward with the jugs tipped, the water running down her sleeves.
```

### F5 — `F5_frameless_symmetric_mirror.png`

```text
POSE VARIANT: the only true mirror-symmetric version — both hands raised level with her ears, both jugs
tipped inward so the two streams fall onto the crown of her head, her soaked hair falling symmetrically on
both sides, both shoulders equidistant from the left and right edges.
```

### T1 — `T1_C_build_symmetric.png`

```text
POSE VARIANT: the mirror-symmetric version — both hands raised level with her ears, both jugs tipped
inward so the two streams fall onto the crown of her head and run down her arms, her soaked hair falling
symmetrically on both sides, both shoulders equidistant from the left and right edges.
Soles not visible to the camera.
```

### T2 — `T2_C_build_one_high_low.png`

```text
POSE VARIANT: one arm raised high and the other held low beside her hip.

WATER PATH LOCK: the lower jug is tipped inward directly over her own thigh, so its stream splashes onto
her knee; the upper stream strikes her raised forearm; neither stream is allowed to land on the bare floor.
```

### T3b — `T3b_C_build_wrists_x.png`

```text
POSE VARIANT: both forearms lifted and crossed at the wrists into a clear X above her head, the two
streams falling from the crossed wrists down onto her shoulders and along her sleeves.
```

### T4 — `T4_C_build_hands_cupped.png`

```text
POSE VARIANT: both elbows tucked against her ribs, each jug pouring into her own cupped palm, the water
overflowing between her fingers; her head bowed, her soaked hair falling forward like a curtain.
```

### probe_toned — `probe_toned.png`

```text
POSE VARIANT (probe): the plain reference pose — both jugs held level at shoulder height and tipped
inward, both streams landing on her forearms, nothing else changed. Rendered as a neutral colour probe:
the same scene with a toned-down, desaturated grade so the palette can be checked against the deck.
```

---

## Ghi chú lọc (nhắc lại, vì prompt nào cũng phải tuân theo)

| ❌ Tránh | ✅ Dùng |
|---|---|
| `soaking wet gown clinging to her figure` | `fully opaque and modest, the soaked hem gathered on the stone` |
| `chest lifted, back arched` | `posture upright and composed` |
| `soles turned up behind her` | `weight resting back on her heels, soles not visible to the camera` |
| `water running down her throat / chest / torso` | `water running down her sleeves, dripping from her wrists` |
| `lips parted, flushed cheeks, skin sheen` | `serene expression, eyes closed in quiet devotion` |
| `no nudity` | `the silk stays neatly in place` (đừng nhắc từ "nudity") |
| `deep plunging neckline … between her breasts` | `a low draped neckline sitting well below the collarbone` |
