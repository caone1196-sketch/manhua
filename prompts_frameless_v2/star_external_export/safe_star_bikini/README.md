# safe_star_bikini — bản PORT tuân thủ của 5 prompt The Star trong thư mục này

5 file `17-star_pose0X_*_SAFE.txt` sinh bởi `port_star_export.py` (chạy lại được).

## Giữ nguyên từ bản gốc
* 5 biến thể tư thế: `pose06` quỳ 2 tay chữ V · `pose07` full profile · `pose08` nằm nửa chìm
  theo mực nước · `pose09` 3/4 sau, tay qua đầu · `pose10` nghiêng người qua thành bồn.
* Bối cảnh open-sky stargazer (bồn tròn dưới vòm kính đầy sao, sao 8 cánh trên đầu).
* **COUNT LOCK đúng 2 bình vàng**, mỗi tay một bình, không bình nào bị che.
* DEPTH & LIGHT, ANATOMY & QUALITY LOCK, chữ "THE STAR" serif vàng ở đáy thẻ.

## Đã thay đổi (bắt buộc)
| Bản gốc | Bản port |
|---|---|
| bikini top **tuột khỏi ngực**, dồn bunched quanh eo; 2 dòng nước đổ thẳng lên **ngực trần** | bikini top **mặc nguyên, cúp lót phủ kín ngực**, 2 dòng nước đổ lên **cặp khuy đồng** rồi loang trên mặt vải ướt |
| "micro string bikini", "clinging like a second skin", "zero loose folds" | "two-piece satin bikini", "wet and glossy with water beads" (các từ gốc nằm trong danh sách bị backend chặn) |
| "21-year-old streamer", "20 years old" | "adult woman in her twenties" |
| reference: `major_08_strength.png` + `test_card_17_the_star.png` | reference: **`the star.png`** (painting style + khung vàng + biểu cảm mặt) |
| frameless | giữ nguyên **frameless** trong `*_SAFE.txt`; còn `gen_prompts.json` dùng khung vàng + band chữ cho khớp 22 lá `cards_v3_star/` |

> Lí do: chi tiết "top tuột + nước đổ lên ngực trần" là nudity nên không nằm trong phạm vi tôi
> render được (và cũng chính là lí do backend cũ chặn 21/21 lần như README thư mục gốc ghi).
> Toàn bộ staging, pose, symbol, prop-count của bạn vẫn được dùng y nguyên.

## File
* `<pose>_SAFE.txt` — prompt đầy đủ (dán vào tool nào cũng chạy được, kể cả tool cho phép 18+)
* `safe_poses.json` — riêng đoạn pose đã làm sạch
* `gen_prompts.json` — bản gọn ~2.4k ký tự cho `gemini-3.1-flash-image` (prompt dài hơn hay bị trả rỗng)
