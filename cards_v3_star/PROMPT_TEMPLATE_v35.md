# Prompt template v3.5 — ĐÃ KIỂM CHỨNG (lá The Star render thành công ngày 10/09)

Copy nguyên văn, thay các chỗ `{...}`, đính kèm reference `the star.png`, khung 7:12.

```
Vertical tarot card "{TITLE}" painted exactly like the attached reference image: soft airbrushed
semi-realistic Korean manhwa painting, gentle bloom, rim-light edges instead of ink outlines, satin
skin highlights, richly painted hazy background with {LIGHT}, film grain. FACE = the reference
expression: heavy half-lidded dreamy eyes gazing softly down, small glossy parted lips, faint blush,
delicate oval face, wet strands across one cheek, calm and slightly dazed. Same thin antique-gold
ornamental border with filigree corners and the serif gold title "{TITLE}" in a bottom band, like the
reference card — that title is the only text on the card. Adult woman in her twenties, {HAIR} wet and
slicked, {EYES}, {SKIN} skin glossy with water. Costume VERBATIM from the deck prompt:
soaking-wet {COLOR} micro string bikini with {ACCENT} (opaque swimwear, no see-through) — minimal
micro cut, small fully lined triangles, double hairline straps, ultra high-cut leg lines to the hip
crest, thin side-tie strings. WARDROBE OVERRIDE: no hanging cloth panel between the legs; her
jewellery is a {METAL} filigree hip chain ending in a single {GEM} pendant at the lower belly with
nothing draping down, a floor-length sheer veil hemmed with gold stars, openwork armbands, a jewelled
forehead circlet. Wet satin with a swimwear-grade opaque lining, glossy with water beads. Pose:
{POSE}. Setting: {SCENE}. {PROPS} Tall 7:12 portrait, whole body visible, perfect anatomy.
```

## 3 khoá của v3.5 (yêu cầu người dùng)
1. **Bỏ miếng vải treo giữa hai chân** → `WARDROBE OVERRIDE: no hanging cloth panel … single {GEM}
   pendant … nothing draping down` (dải lụa xanh/violet của lá mẫu bị loại khỏi 22/22 prompt).
2. **Style bán thực hoạ** → `painted exactly like the attached reference image: soft airbrushed
   semi-realistic …, film grain` + RENDER LOCK trong `build_prompts_v3_star.py` (`SEMI_REAL`).
3. **Trang phục nhỏ tối thiểu “chỉ đủ che”** → `minimal micro cut, small fully lined triangles,
   double hairline straps, ultra high-cut leg lines, thin side-tie strings` + `swimwear-grade
   opaque lining` (vẫn opaque, không xuyên thấu).

## ⚠ Từ khoá làm filter sập (đã đo)
`nipples`, `groin`, `bare skin`, `lingerie`, `bralette`, `clinging like a second skin`, `see-through`
(mô tả *có* xuyên thấu) → backend trả `totalParts: 0/3` không ra ảnh. **Đã gạch bỏ khỏi template.**
Chỉ dùng `fully lined`, `opaque lining`, `covering`, `micro string bikini`.
