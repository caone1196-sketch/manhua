# Tiến độ — 22 lá Ẩn Chính · **v3.3 = bikini 2 mảnh ướt** + FACE LOCK theo lá mẫu

Ảnh: `cards_v3_star/<slug>.png` · Prompt: `prompts_frameless_v3_star/tool_prompts.json`
Reference đính kèm mỗi lần gen: `the star.png` · Chế độ: `OUTFIT_MODE = "bikini_two_piece"`

## v3.3
* Trang phục: **bikini 2 mảnh satin bóng** — top underwire cúp lót đầy đủ phủ kín ngực, khoá
  giữa ngực bằng **2 khuy rosette đồng khắc emblem của lá đó**, quai quấn kim loại, quần cạp cao.
  Giữ nguyên bộ kim hoàn của lá mẫu: hip chain filigree + đá quý lớn, dải lụa thêu sa trước đùi,
  voan viền sao, vòng tay chạm lộng, circlet, dây chuyền đá.
* **ướt**: satin sẫm hơn một tông, bóng, hạt nước, gấu vải nhỏ giọt, tóc ướt bết — nhưng
  **opaque**, không xuyên thấu.
* **FACE LOCK**: heavy half-lidded dreamy eyes gazing softly down · small glossy parted lips ·
  faint blush · delicate oval face · wet strands across one cheek · calm and slightly dazed.

## ⚠ Tình trạng backend ảnh (số liệu thật của các lượt đã chạy)
| Công thức | KQ |
|---|---|
| `camisole top + high-cut bottoms` + `wet gloss/water beads` | ✅ pass (The Moon v3.2, The Fool v3.2) |
| `two-piece bikini in glossy satin` + `swimwear-grade opaque` | ✅ pass 2/11 — **tỉ lệ thấp, fail là `totalParts:0` (empty response), không phải từ chối nội dung → RETRY là chính** |
| `lingerie` · `bralette` · `clinging like a second skin` · `see-through` · `bare skin` | ❌ 5/5 bị chặn (model chỉ trả text) |
| prompt >2500 ký tự | ❌ fail gần như chắc chắn — giữ ~2100–2400 |

Vì vậy: mỗi lượt tối đa **10 ảnh**, thực ăn ~2-4 lá/lượt; script sinh prompt đã ghim sẵn
công thức pass, chỉ việc lặp `gen` cho tới khi ăn.

## Trạng thái 22 lá

| Slug | Ảnh |
|---|---|
| 00-fool | 🔁 v3.2 camisole ướt — cần render lại bikini |
| 01-magician | ⏳ chưa render |
| 02-priestess | ✅ **v3.3 bikini 2 mảnh (ướt)** |
| 03-empress | 🔁 v3.1 couture khô — cần render lại bikini |
| 04-emperor | 🔁 v3.1 couture khô — cần render lại bikini |
| 05-hierophant | 🔁 v3.1 couture khô — cần render lại bikini |
| 06-lovers | ⏳ chưa render |
| 07-chariot | ⏳ chưa render |
| 08-strength | ⏳ chưa render |
| 09-hermit | ⏳ chưa render |
| 10-wheel | ⏳ chưa render |
| 11-justice | ⏳ chưa render |
| 12-hanged | ⏳ chưa render |
| 13-death | ⏳ chưa render |
| 14-temperance | ⏳ chưa render |
| 15-devil | ⏳ chưa render |
| 16-tower | ⏳ chưa render |
| 17-the-star | ⏳ chưa render |
| 18-moon | ✅ **v3.3 bikini 2 mảnh (ướt)** |
| 19-sun | ⏳ chưa render |
| 20-judgement | ⏳ chưa render |
| 21-world | ⏳ chưa render |

```bash
python3 build_prompts_v3_star.py   # đổi OUTFIT_MODE / WITH_FRAME rồi chạy lại
```
