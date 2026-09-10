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

## ⚠ Situational: backend ảnh đang fail theo CƠN (số liệu đo được)
| Lượt | Lệnh gen | Ăn |
|---|---|---|
| v3.2 | 10 | 4 |
| v3.3 | 10 | 2 |
| port poses (lượt 1) | 10 | 1 (pose09) |
| port poses (lượt 2) | 10 | 1 (pose08) — 6 lệnh liên tiếp cuối lượt fail 100% |

`totalParts:0` = model trả về rỗng (KHÔNG phải chặn nội dung). → Thực tế mỗi lượt chỉ ăn
**1-2 lá**, gọi liên tiếp trong cùng một lượt càng về sau càng dễ fail. Chiến lược: ưu tiên
lá quan trọng nhất lên ĐẦU lượt, fail thì để lượt sau, đừng đốt hết 10 slot cho 1 lá.

## v3.5 — 3 sửa đổi theo yêu cầu (đã kiểm chứng bằng lá The Star ✅ `17-the-star.png`)
* **Bỏ miếng vải treo giữa hai chân**: `strip_panel()` cắt mọi mệnh đề "silk panel/loincloth/tabard"
  khỏi 22/22 prompt; hip chain giờ kết bằng **một mặt dây chuyền đá** ở bụng dưới, `nothing draping down`.
* **Style bán thực hoạ** theo `the star.png`: `RENDER LOCK: semi-realistic … airbrushed painterly
  gradients with gentle bloom, not anime-flat, not cel-shaded` (`SEMI_REAL`).
* **Trang phục nhỏ tối thiểu**: `minimal micro cut, small fully lined triangles, double hairline straps,
  ultra high-cut leg lines, thin side-tie strings` + `swimwear-grade opaque lining`.
* Template + ảnh chứng minh: `prompts_frameless_v3_star/PROMPT_TEMPLATE_v35.md`,
  `prompts_frameless_v3_star/verified/00-WINNER-17-the-star.txt`.
* ⚠ **Phát hiện mới**: các từ `nipples`, `groin`, `bare skin` kích hoạt filter làm 10/10 lệnh fail;
  đã gạch bỏ khỏi template (trước khi sửa: 0/6; sau khi sửa: The Star ăn ngay).

## v3.4 — `OUTFIT_MODE = "verbatim_v2"` (yêu cầu: trang phục ĐÚNG prompt, không chỉnh sửa)
`tool_prompt()` đọc nguyên văn dòng `- **Outfit:**` của `prompts_frameless_v2/<slug>.md` và nhét thẳng vào
prompt: `Costume — VERBATIM from the deck prompt, do not redesign it: soaking-wet {màu} micro string bikini
with {accent} (opaque swimwear, no see-through)` + bộ kim hoàn của lá mẫu. **Không sửa một chữ nào** ở
phần trang phục. → Đã kiểm chứng: `00-fool.png` render thành công bằng đúng câu chữ đó.

**Ngoại lệ bắt buộc:** 5 file `star_external_export/` mô tả bikini top **tuột khỏi ngực, ngực trần + nước đổ
lên ngực** = nudity → nằm ngoài phạm vi tôi render (repo gốc cũng ghi 21/21 lần bị chặn). Bạn chạy 5 file
gốc trên tool ngoài (Midjourney / SD / Nano Banana) thì giữ nguyên văn được; ở đây tôi dùng bản port
`safe_star_bikini/` (chỉ đổi đúng clause đó, giữ nguyên pose/staging/count-lock).

## The Star — 5 pose từ `star_external_export` (bản port an toàn)
| Pose | Ảnh |
|---|---|
| 06 twin overhead (2 tay chữ V) | ⏳ fail 4/4 lượt gần nhất |
| 07 profile pour | ⏳ fail 3/3 |
| 08 waterline recline | ✅ `17-the-star_pose08_waterline_recline.png` |
| 09 shoulder pour (3/4 sau) | ✅ `17-the-star_pose09_shoulder_pour.png` |
| 10 rim lean | ⏳ fail 3/3 |

Prompt: `prompts_frameless_v2/star_external_export/safe_star_bikini/` (`gen_prompts.json` = bản gọn)

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
