# QA — 56 prompt lá Minor (Wands · Cups · Swords · Pentacles)

Kiểm tra tự động toàn bộ 56 prompt sinh ảnh còn lại (`prompts_frameless_v2/all_prompts.json`),
sau khi đã vá 2 lỗi thật phát hiện được (xem cuối trang).

## Kết quả: ✅ 0 vấn đề trên 56/56 lá

Bộ kiểm tra mỗi lá: không từ giáp/helm (ngoài câu cấm chủ đích) · không trang phục lạ
(vestment/cloak/cowl) · đủ 7 khối bắt buộc (Frameless/Reference/Art style/Garment-to-body/
Wet fabric/Figure+pose/Scene+lock) · title khớp cards.json · 1 nhân vật nữ (không đa nhân vật,
không đại từ nam, không ám chỉ người thứ hai) · COUNT LOCK đúng số cards.json (1–10, viết HOA) ·
tuổi ≥ 18 · 78 phong cách phòng tắm duy nhất · pose gợi cảm xoay vòng 12 · bikini xoay vòng 6 màu.

## WANDS 🔥 (14 lá)

| # | Slug | Lá | Phong cách phòng tắm | Bikini ướt | Pose gợi cảm | Count lock | QA |
|---|---|---|---|---|---|---|---|
| A | wands-ace | ACE OF WANDS | Volcanic hot spring | vàng kim + ren | mermaid trên ledge | 1× wand | ✅ |
| 2 | wands-02 | TWO OF WANDS | Explorer's lookout | đỏ + hạt ngọc | quấn khăn giữa chừng | 2× wands | ✅ |
| 3 | wands-03 | THREE OF WANDS | Harbor porthole | trắng ngọc + sao vàng | tựa lưng tường ướt, tay vuốt tóc | 3× wands | ✅ |
| 4 | wands-04 | FOUR OF WANDS | Garland canopy | đen + dây vàng | ngả trên thành bồn | 4× wands | ✅ |
| 5 | wands-05 | FIVE OF WANDS | Arena star jets | xanh ngọc + nút hông | contrapposto nhìn lại qua vai | 5× wands | ✅ |
| 6 | wands-06 | SIX OF WANDS | Victory laureate podium | hồng + nơ satin | quỳ ưỡn cong như cung | 6× wands | ✅ |
| 7 | wands-07 | SEVEN OF WANDS | Bamboo palisade terrace | vàng kim + ren | nằm nghiêng chống khuỷu | 7× wands | ✅ |
| 8 | wands-08 | EIGHT OF WANDS | Speed-line yacht wet room | đỏ + hạt ngọc | bước ra vòi sen ngoái lại | 8× wands | ✅ |
| 9 | wands-09 | NINE OF WANDS | Watchtower rampart | trắng ngọc + sao vàng | chân kê thành bồn tay lướt đùi | 9× wands | ✅ |
| 10 | wands-10 | TEN OF WANDS | Apothecary bundle | đen + dây vàng | ngồi nước nông tay khoanh | 10× wands | ✅ |
| P | wands-page | PAGE OF WANDS | Art-deco plume | xanh ngọc + nút hông | kiễng chân căng người | 1× wand | ✅ |
| N | wands-knight | KNIGHT OF WANDS | Equestrian chic | hồng + nơ satin | nghiêng người vào vanity | 1× wand | ✅ |
| Q | wands-queen | QUEEN OF WANDS | Sunflower terracotta | vàng kim + ren | mermaid trên ledge | 1× wand | ✅ |
| K | wands-king | KING OF WANDS | Lion-head gold | đỏ + hạt ngọc | quấn khăn giữa chừng | 1× wand | ✅ |

## CUPS 💧 (14 lá)

| # | Slug | Lá | Phong cách phòng tắm | Bikini ướt | Pose gợi cảm | Count lock | QA |
|---|---|---|---|---|---|---|---|
| A | cups-ace | ACE OF CUPS | Shell fountain | trắng ngọc + sao vàng | tựa lưng tường ướt, tay vuốt tóc | 1× chalice | ✅ |
| 2 | cups-02 | TWO OF CUPS | Twin-basin rings | đen + dây vàng | ngả trên thành bồn | 2× chalices | ✅ |
| 3 | cups-03 | THREE OF CUPS | Celebration spa | xanh ngọc + nút hông | contrapposto nhìn lại qua vai | 3× chalices | ✅ |
| 4 | cups-04 | FOUR OF CUPS | Still-water zen | hồng + nơ satin | quỳ ưỡn cong như cung | 4× chalices | ✅ |
| 5 | cups-05 | FIVE OF CUPS | Rain-window melancholy | vàng kim + ren | nằm nghiêng chống khuỷu | 5× chalices | ✅ |
| 6 | cups-06 | SIX OF CUPS | Retro pastel nostalgia | đỏ + hạt ngọc | bước ra vòi sen ngoái lại | 6× chalices | ✅ |
| 7 | cups-07 | SEVEN OF CUPS | Dream-cloud | trắng ngọc + sao vàng | chân kê thành bồn tay lướt đùi | 7× chalices | ✅ |
| 8 | cups-08 | EIGHT OF CUPS | Moon-door | đen + dây vàng | ngồi nước nông tay khoanh | 8× chalices | ✅ |
| 9 | cups-09 | NINE OF CUPS | Skyline jacuzzi | xanh ngọc + nút hông | kiễng chân căng người | 9× chalices | ✅ |
| 10 | cups-10 | TEN OF CUPS | Rainbow-glass arc | hồng + nơ satin | nghiêng người vào vanity | 10× chalices | ✅ |
| P | cups-page | PAGE OF CUPS | Kawaii aquarium | vàng kim + ren | mermaid trên ledge | 1× chalice | ✅ |
| N | cups-knight | KNIGHT OF CUPS | Riverside stone | đỏ + hạt ngọc | quấn khăn giữa chừng | 1× chalice | ✅ |
| Q | cups-queen | QUEEN OF CUPS | Ocean grotto | trắng ngọc + sao vàng | tựa lưng tường ướt, tay vuốt tóc | 1× chalice | ✅ |
| K | cups-king | KING OF CUPS | Aquarium throne | đen + dây vàng | ngả trên thành bồn | 1× chalice | ✅ |

## SWORDS 🗡️ (14 lá)

| # | Slug | Lá | Phong cách phòng tắm | Bikini ướt | Pose gợi cảm | Count lock | QA |
|---|---|---|---|---|---|---|---|
| A | swords-ace | ACE OF SWORDS | Pristine white blade | xanh ngọc + nút hông | contrapposto nhìn lại qua vai | 1× sword | ✅ |
| 2 | swords-02 | TWO OF SWORDS | Starlit X | hồng + nơ satin | quỳ ưỡn cong như cung | 2× swords | ✅ |
| 3 | swords-03 | THREE OF SWORDS | Heartbreak rain | vàng kim + ren | nằm nghiêng chống khuỷu | 3× swords | ✅ |
| 4 | swords-04 | FOUR OF SWORDS | Chapel rest | đỏ + hạt ngọc | bước ra vòi sen ngoái lại | 4× swords | ✅ |
| 5 | swords-05 | FIVE OF SWORDS | Storm victor | trắng ngọc + sao vàng | chân kê thành bồn tay lướt đùi | 5× swords | ✅ |
| 6 | swords-06 | SIX OF SWORDS | Ferry boat tub | đen + dây vàng | ngồi nước nông tay khoanh | 6× swords | ✅ |
| 7 | swords-07 | SEVEN OF SWORDS | Stealth shoji | xanh ngọc + nút hông | kiễng chân căng người | 7× swords | ✅ |
| 8 | swords-08 | EIGHT OF SWORDS | Ribbon ring | hồng + nơ satin | nghiêng người vào vanity | 8× swords | ✅ |
| 9 | swords-09 | NINE OF SWORDS | Insomnia midnight | vàng kim + ren | mermaid trên ledge | 9× swords | ✅ |
| 10 | swords-10 | TEN OF SWORDS | Dawn after storm | đỏ + hạt ngọc | quấn khăn giữa chừng | 10× swords | ✅ |
| P | swords-page | PAGE OF SWORDS | Wind-study | trắng ngọc + sao vàng | tựa lưng tường ướt, tay vuốt tóc | 1× sword | ✅ |
| N | swords-knight | KNIGHT OF SWORDS | Gale force | đen + dây vàng | ngả trên thành bồn | 1× sword | ✅ |
| Q | swords-queen | QUEEN OF SWORDS | Marble throne clarity | xanh ngọc + nút hông | contrapposto nhìn lại qua vai | 1× sword | ✅ |
| K | swords-king | KING OF SWORDS | Twin-wing hall | hồng + nơ satin | quỳ ưỡn cong như cung | 1× sword | ✅ |

## PENTACLES 🪙 (14 lá)

| # | Slug | Lá | Phong cách phòng tắm | Bikini ướt | Pose gợi cảm | Count lock | QA |
|---|---|---|---|---|---|---|---|
| A | pentacles-ace | ACE OF PENTACLES | Garden-terrace hands | vàng kim + ren | nằm nghiêng chống khuỷu | 1× pentacle coin | ✅ |
| 2 | pentacles-02 | TWO OF PENTACLES | Wave sway | đỏ + hạt ngọc | bước ra vòi sen ngoái lại | 2× pentacle coins | ✅ |
| 3 | pentacles-03 | THREE OF PENTACLES | Artisan arch | trắng ngọc + sao vàng | chân kê thành bồn tay lướt đùi | 3× pentacle coins | ✅ |
| 4 | pentacles-04 | FOUR OF PENTACLES | Coin vault | đen + dây vàng | ngồi nước nông tay khoanh | 4× pentacle coins | ✅ |
| 5 | pentacles-05 | FIVE OF PENTACLES | Snow stained-glass | xanh ngọc + nút hông | kiễng chân căng người | 5× pentacle coins | ✅ |
| 6 | pentacles-06 | SIX OF PENTACLES | Charity scales | hồng + nơ satin | nghiêng người vào vanity | 6× pentacle coins | ✅ |
| 7 | pentacles-07 | SEVEN OF PENTACLES | Greenhouse vine | vàng kim + ren | mermaid trên ledge | 7× pentacle coins | ✅ |
| 8 | pentacles-08 | EIGHT OF PENTACLES | Atelier bench | đỏ + hạt ngọc | quấn khăn giữa chừng | 8× pentacle coins | ✅ |
| 9 | pentacles-09 | NINE OF PENTACLES | Estate arbor | trắng ngọc + sao vàng | tựa lưng tường ướt, tay vuốt tóc | 9× pentacle coins | ✅ |
| 10 | pentacles-10 | TEN OF PENTACLES | Tree-of-life mosaic | đen + dây vàng | ngả trên thành bồn | 10× pentacle coins | ✅ |
| P | pentacles-page | PAGE OF PENTACLES | Earthy study | xanh ngọc + nút hông | contrapposto nhìn lại qua vai | 1× pentacle coin | ✅ |
| N | pentacles-knight | KNIGHT OF PENTACLES | Farmhouse oak | hồng + nơ satin | quỳ ưỡn cong như cung | 1× pentacle coin | ✅ |
| Q | pentacles-queen | QUEEN OF PENTACLES | Rose garden | vàng kim + ren | nằm nghiêng chống khuỷu | 1× pentacle coin | ✅ |
| K | pentacles-king | KING OF PENTACLES | Bull bronze | đỏ + hạt ngọc | bước ra vòi sen ngoái lại | 1× pentacle coin | ✅ |

## 2 lỗi thật đã phát hiện & vá trong đợt kiểm tra này

1. **cups-03 (Three of Cups)** — spec gốc mô tả *3 thiếu nữ* (3 dáng người, 3 màu tóc,
   3 đôi mắt, 'mỗi cô cài một bông hoa') mâu thuẫn staging 1 nhân vật → viết lại thành một nàng
   giữ đúng tinh thần lá: tóc nâu socola pha highlight vàng-bạc-đồng, 3 bông hoa cài tóc
   (hồng · tím · cúc). `MULTIFIGURE_PHRASES` trong `build_prompts_v2.py`.
2. **cups-02 (Two of Cups)** — mắt 'say mê nhìn người kia' ám chỉ người thứ hai → đổi thành
   'say mê hướng về phía trước, ánh mắt giao hòa'.
3. *(cosmetic)* COUNT LOCK n=1 giờ viết HOA: `EXACTLY 1 WAND` thay vì `1 wand`.

Lưu ý các batch trước đó không bị ảnh hưởng: 22 lá Major đã sinh ảnh dùng prompt đúng bản của chúng.
