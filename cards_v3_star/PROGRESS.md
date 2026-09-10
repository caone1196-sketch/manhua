# Tiến độ — 22 lá Ẩn Chính, style + phục trang theo `the star.png`

**v3.1 (STYLE FIX):** ảnh render phải theo đúng cách **VẼ** của lá tham chiếu, không phải
flat webtoon cel-shading. Backend chỉ nhận bản prompt `TOOL_PROVEN` (xem dưới).

## Công thức style đã kiểm chứng (lá The Moon ra ảnh khớp reference nhất)

1. Mở đầu: `Vertical tarot card "<TITLE>" painted in exactly the same style as the attached
   reference image:` rồi **mô tả positive** — `soft airbrushed semi-realistic Korean manhwa
   digital painting, gentle bloom, edges separated by rim light instead of ink outlines,
   satin skin highlights, hyper-detailed antique-gold filigree jewellery, pearl-satin fabric
   with realistic folds and gold embroidery, translucent tulle veil, richly painted hazy
   background with volumetric light and reflections, film grain`.
2. **Khung vàng ornamental + band chữ serif dưới đáy = CÓ** (`WITH_FRAME = True`), vì
   `the star.png` có khung; bật `False` nếu muốn frameless như v2.
3. Độ dài prompt **~1500–1900 ký tự**. Bản >2500 ký tự có cụm phủ định dài
   ("NO flat cel colours and NO bold ink outlines") bị backend trả `no images`.
4. Phục trang: `Costume copied from the reference:` + 8 thành phần lõi (bodice gấp nếp +
   2 khuy rosette, dải băng chéo eo, quần cut cao, hip chain đá quý lớn + dải lụa sa giữa
   đùi, voan viền sao, vòng tay chạm lộng, circlet, emblem khắc trên khuy).
5. Không dùng từ `bikini / bandeau / chest / wet micro` (dễ bị moderation chặn).

## Ảnh

`cards_v3_star/<slug>.png` — file `.png` đã có là bản v3.1.

| Slug | Trạng thái |
|---|---|
| 00-fool | ✅ done (v3.1 style) |
| 01-magician | ⏳ chờ lượt sau |
| 02-priestess | ✅ done (v3.1 style) |
| 03-empress | ✅ done (v3.1 style) |
| 04-emperor | ✅ done (v3.1 style) |
| 05-hierophant | ✅ done (v3.1 style) |
| 06-lovers | ⏳ chờ lượt sau |
| 07-chariot | ⏳ chờ lượt sau |
| 08-strength | ⏳ chờ lượt sau |
| 09-hermit | ⏳ chờ lượt sau |
| 10-wheel | ⏳ chờ lượt sau |
| 11-justice | ⏳ chờ lượt sau |
| 12-hanged | ⏳ chờ lượt sau |
| 13-death | ⏳ chờ lượt sau |
| 14-temperance | ⏳ chờ lượt sau |
| 15-devil | ⏳ chờ lượt sau |
| 16-tower | ⏳ chờ lượt sau |
| 17-the-star | ⏳ chờ lượt sau |
| 18-moon | ✅ done (v3.1 style) |
| 19-sun | ⏳ chờ lượt sau |
| 20-judgement | ⏳ chờ lượt sau |
| 21-world | ⏳ chờ lượt sau |

## Còn lại

16 lá: `", ".join(s for s in all_slugs if s not in done)`.
Mỗi lượt sinh tối đa 10 ảnh, prompt lấy nguyên văn từ `prompts_frameless_v3_star/tool_prompts.json`,
đính kèm reference `the star.png`. Lỗi `Response contains no images` là transient → retry.

## Tái sinh prompt

```bash
python3 build_prompts_v3_star.py   # -> prompts_frameless_v3_star/
```
