# prompts_frameless_v2 — Bộ prompt công thức The Star áp dụng toàn bộ 78 lá

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
  (xem bảng dưới) — từ rooftop infinity pool sunrise, Byzantine gilded chapel, volcanic hot spring,
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

| # | Slug | Lá | Phong cách phòng tắm |
|---|---|---|---|
| 0 | 00-fool | THE FOOL | Rooftop infinity pool sunrise |
| I | 01-magician | THE MAGICIAN | Marble vanity mirror wall |
| II | 02-priestess | THE HIGH PRIESTESS | Twin-column temple bath |
| III | 03-empress | THE EMPRESS | Sunlit garden sunroom bath |
| IV | 04-emperor | THE EMPEROR | Stone steam-room throne |
| V | 05-hierophant | THE HIEROPHANT | Byzantine gilded chapel bath |
| VI | 06-lovers | THE LOVERS | Rose-petal twin-tub spa |
| VII | 07-chariot | THE CHARIOT | Motorsport penthouse bath |
| VIII | 08-strength | STRENGTH | Safari-lodge stone bath |
| IX | 09-hermit | THE HERMIT | Candlelit mountain grotto |
| X | 10-wheel | WHEEL OF FORTUNE | Casino-noir roulette |
| XI | 11-justice | JUSTICE | Monochrome scales bath |
| XII | 12-hanged | THE HANGED MAN | Inversion silk studio |
| XIII | 13-death | DEATH | Gothic onyx & lilies |
| XIV | 14-temperance | TEMPERANCE | Zen ryokan ofuro |
| XV | 15-devil | THE DEVIL | Crimson neon gothic |
| XVI | 16-tower | THE TOWER | Storm skyscraper glass |
| XVII | 17-the-star | THE STAR | Open-sky stargazer |
| XVIII | 18-moon | THE MOON | Midnight lagoon |
| XIX | 19-sun | THE SUN | Golden solarium |
| XX | 20-judgement | JUDGEMENT | Celestial trumpet dawn |
| XXI | 21-world | THE WORLD | 360° panorama ring |
| A | wands-ace | ACE OF WANDS | Volcanic hot spring |
| 2 | wands-02 | TWO OF WANDS | Explorer's lookout |
| 3 | wands-03 | THREE OF WANDS | Harbor porthole |
| 4 | wands-04 | FOUR OF WANDS | Garland canopy |
| 5 | wands-05 | FIVE OF WANDS | Arena star jets |
| 6 | wands-06 | SIX OF WANDS | Victory laureate podium |
| 7 | wands-07 | SEVEN OF WANDS | Bamboo palisade terrace |
| 8 | wands-08 | EIGHT OF WANDS | Speed-line yacht wet room |
| 9 | wands-09 | NINE OF WANDS | Watchtower rampart |
| 10 | wands-10 | TEN OF WANDS | Apothecary bundle |
| P | wands-page | PAGE OF WANDS | Art-deco plume |
| N | wands-knight | KNIGHT OF WANDS | Equestrian chic |
| Q | wands-queen | QUEEN OF WANDS | Sunflower terracotta |
| K | wands-king | KING OF WANDS | Lion-head gold |
| A | cups-ace | ACE OF CUPS | Shell fountain |
| 2 | cups-02 | TWO OF CUPS | Twin-basin rings |
| 3 | cups-03 | THREE OF CUPS | Celebration spa |
| 4 | cups-04 | FOUR OF CUPS | Still-water zen |
| 5 | cups-05 | FIVE OF CUPS | Rain-window melancholy |
| 6 | cups-06 | SIX OF CUPS | Retro pastel nostalgia |
| 7 | cups-07 | SEVEN OF CUPS | Dream-cloud |
| 8 | cups-08 | EIGHT OF CUPS | Moon-door |
| 9 | cups-09 | NINE OF CUPS | Skyline jacuzzi |
| 10 | cups-10 | TEN OF CUPS | Rainbow-glass arc |
| P | cups-page | PAGE OF CUPS | Kawaii aquarium |
| N | cups-knight | KNIGHT OF CUPS | Riverside stone |
| Q | cups-queen | QUEEN OF CUPS | Ocean grotto |
| K | cups-king | KING OF CUPS | Aquarium throne |
| A | swords-ace | ACE OF SWORDS | Pristine white blade |
| 2 | swords-02 | TWO OF SWORDS | Starlit X |
| 3 | swords-03 | THREE OF SWORDS | Heartbreak rain |
| 4 | swords-04 | FOUR OF SWORDS | Chapel rest |
| 5 | swords-05 | FIVE OF SWORDS | Storm victor |
| 6 | swords-06 | SIX OF SWORDS | Ferry boat tub |
| 7 | swords-07 | SEVEN OF SWORDS | Stealth shoji |
| 8 | swords-08 | EIGHT OF SWORDS | Ribbon ring |
| 9 | swords-09 | NINE OF SWORDS | Insomnia midnight |
| 10 | swords-10 | TEN OF SWORDS | Dawn after storm |
| P | swords-page | PAGE OF SWORDS | Wind-study |
| N | swords-knight | KNIGHT OF SWORDS | Gale force |
| Q | swords-queen | QUEEN OF SWORDS | Marble throne clarity |
| K | swords-king | KING OF SWORDS | Twin-wing hall |
| A | pentacles-ace | ACE OF PENTACLES | Garden-terrace hands |
| 2 | pentacles-02 | TWO OF PENTACLES | Wave sway |
| 3 | pentacles-03 | THREE OF PENTACLES | Artisan arch |
| 4 | pentacles-04 | FOUR OF PENTACLES | Coin vault |
| 5 | pentacles-05 | FIVE OF PENTACLES | Snow stained-glass |
| 6 | pentacles-06 | SIX OF PENTACLES | Charity scales |
| 7 | pentacles-07 | SEVEN OF PENTACLES | Greenhouse vine |
| 8 | pentacles-08 | EIGHT OF PENTACLES | Atelier bench |
| 9 | pentacles-09 | NINE OF PENTACLES | Estate arbor |
| 10 | pentacles-10 | TEN OF PENTACLES | Tree-of-life mosaic |
| P | pentacles-page | PAGE OF PENTACLES | Earthy study |
| N | pentacles-knight | KNIGHT OF PENTACLES | Farmhouse oak |
| Q | pentacles-queen | QUEEN OF PENTACLES | Rose garden |
| K | pentacles-king | KING OF PENTACLES | Bull bronze |

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
