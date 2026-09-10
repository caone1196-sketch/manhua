# prompts_frameless_v3_star — 22 lá Ẩn Chính, phục trang theo `the star.png`

> **v3.1 — STYLE FIX.** Yêu cầu của người dùng: "phong cách vẽ không đúng lá tham chiếu".
> Backend từ chối render đúng nếu prompt dùng `crisp lineart + soft cell shading` (ra ảnh
> flat kiểu vector). Bản **chuẩn** là `tool_prompts.json`: mở đầu bằng
> *"painted in exactly the same style as the attached reference image"* + mô tả
> **airbrushed semi-realistic painting, bloom, rim-light edges, film grain**, và **có khung
> vàng ornamental** (`the star.png` có khung — `WITH_FRAME=True` trong script; đặt `False`
> để frameless). Chi tiết: `cards_v3_star/PROGRESS.md`.

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
| 0 | `00-fool` | THE FOOL | Rooftop infinity pool at sunrise | pearl-ivory · a pale moonstone | — |
| I | `01-magician` | THE MAGICIAN | Marble vanity mirror wall bath | midnight-black satin · a deep lapis lazuli | 4 suit objects |
| II | `02-priestess` | THE HIGH PRIESTESS | Twin-column temple bath | pearl-ivory · a moonlit blue sapphire | — |
| III | `03-empress` | THE EMPRESS | Sunlit garden sunroom bath | rose-blush satin · a green emerald | — |
| IV | `04-emperor` | THE EMPEROR | Stone steam-room throne | burnished gold-bronze · a warm amber citrine | — |
| V | `05-hierophant` | THE HIEROPHANT | Byzantine gilded chapel bath | ivory and cherry-red silk · a ruby | — |
| VI | `06-lovers` | THE LOVERS | Rose-petal twin-tub spa | pearl-ivory · a rose quartz | — |
| VII | `07-chariot` | THE CHARIOT | Motorsport penthouse bath | midnight-black with gold · a lapis lazuli | — |
| VIII | `08-strength` | STRENGTH | Safari-lodge stone bath | aqua-teal satin · a carnelian | — |
| IX | `09-hermit` | THE HERMIT | Candlelit mountain grotto | heather-grey silk with gold · an amber | — |
| X | `10-wheel` | WHEEL OF FORTUNE | Casino-noir roulette bath | metallic gold · a golden topaz | 1 sword |
| XI | `11-justice` | JUSTICE | Monochrome scales bath | cherry-red silk over ivory · a clear pearl | 1 sword |
| XII | `12-hanged` | THE HANGED MAN | Inversion silk studio | pearl-ivory · an amethyst | — |
| XIII | `13-death` | DEATH | Gothic onyx & lilies bath | onyx-black silk · a black onyx | — |
| XIV | `14-temperance` | TEMPERANCE | Zen ryokan ofuro | aqua-teal silk · an aquamarine | 2 chalices |
| XV | `15-devil` | THE DEVIL | Crimson neon gothic bath | rose-blush satin with black · a garnet | — |
| XVI | `16-tower` | THE TOWER | Storm skyscraper glass bath | molten gold-bronze · a tourmaline | — |
| XVII | `17-the-star` | THE STAR | Open-sky stargazer bath | pearl-ivory · a luminous pearl | 2 jugs |
| XVIII | `18-moon` | THE MOON | Midnight lagoon | pearl-ivory · a blue sapphire | 1 sword |
| XIX | `19-sun` | THE SUN | Golden solarium | sun-gold silk · a golden citrine | — |
| XX | `20-judgement` | JUDGEMENT | Celestial trumpet dawn | dove-white silk with gold · a ruby | — |
| XXI | `21-world` | THE WORLD | 360° panorama ring bath | rose-blush and gold · a jade | 2 wands |

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
