# Tiến độ sinh ảnh — 22 lá Ẩn Chính, phục trang theo `the star.png`

Ảnh lưu tại `cards_v3_star/<slug>.png`, prompt sinh ảnh thật: `prompts_frameless_v3_star/tool_prompts.json`.

| # | Slug | Ảnh | Ghi chú |
|---|---|---|---|
| 0 | 00-fool | ✅ | phục trang copy đúng reference, voan viền sao, cũi Pomeranian, mép hồ |
| I | 01-magician | ⏳ retry | backend trả "no images" 2 lần (lỗi may rủi, không phải từ khoá) |
| II | 02-priestess | ✅ | |
| III | 03-empress | ✅ | |
| IV | 04-emperor | ⏳ retry | |
| V–XXI | 05 → 21 | ⏳ chờ lượt sau | 17 lá còn lại |

## Lưu ý vận hành (đã kiểm chứng)

* Backend `gemini-3.1-flash-image` **giới hạn 10 ảnh / lượt** → chia 6 batch (4+4+4+4+4+2).
* Đôi khi trả `Response contains no images` — đây là **lỗi transient**, chỉ cần retry nguyên prompt.
* Bản prompt `tool_prompts.json` là bản an toàn nhất: tránh các chữ `bikini / bandeau / chest /
  wet micro string` (những chữ này + ảnh reference dễ bị moderation chặn như ghi chú trong
  `prompts_frameless_v2/star_external_export/README.md`).
* Luôn đính kèm reference: `the star.png`.
