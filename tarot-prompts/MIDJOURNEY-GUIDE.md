# Dùng ảnh THE STAR (`2.png`) làm Reference trong Midjourney

Ảnh gốc của bạn (`2.png` trên nhánh `main`) chính là artwork THE STAR chuẩn:
gái tóc bạch kim quỳ, 2 bình vàng, sao 8 cánh, thành phố Gothic tím.
Ta sẽ dùng nó để **khóa mặt + khóa style** cho cả 21 lá còn lại.

## File reference trong repo

| File | Dùng cho | Ghi chú |
|---|---|---|
| `ref/2.png` (gốc 4MB) | Lưu trữ | Còn khung viền + chữ THE STAR |
| `ref/2-mj-clean.png` (2.2MB, 900x1350) | **Dùng trong MJ** | Đã cắt khung viền + dải chữ, giữ tỉ lệ 2:3 |

> Vì sao phải cắt? Nếu để nguyên, MJ sẽ copy khung viền và có thể nhả chữ
> "THE STAR" nhầm sang các lá khác. Bản clean chỉ giữ **mặt nhân vật + style vẽ**.

## Bước 1 — Lấy link ảnh cho Midjourney (chọn 1 trong 2)

**Cách A — Upload lên Discord (khuyên dùng, ổn định nhất):**
1. Mở Discord → chat riêng với Midjourney Bot (hoặc server riêng của bạn).
2. Kéo thả file `ref/2-mj-clean.png` vào khung chat → Enter để gửi.
3. Chuột phải vào ảnh → **Copy Link** → được link dạng
   `https://cdn.discordapp.com/attachments/.../2-mj-clean.png`.

**Cách B — Dùng link GitHub có sẵn (nhanh, khỏi upload):**
```
https://raw.githubusercontent.com/caone1196-sketch/manhua/arena/01a08b50-manhua/tarot-prompts/ref/2-mj-clean.png
```
*(Link này sống sau khi push — đã push ở cuối task này.)*

## Bước 2 — Lệnh mẫu (copy, thay REF_URL = link ảnh ở Bước 1)

```
/imagine prompt: REF_URL <paste prompt lá bài ở đây> --ar 2:3 --cref REF_URL --cw 0 --sref REF_URL --sw 300 --style raw --stylize 200 --v 6.1
```

Ý nghĩa từng tham số:

| Tham số | Tác dụng | Vì sao chọn vậy |
|---|---|---|
| `REF_URL` ở đầu prompt | Image prompt trộn chung | Neo bố cục/màu sắc tổng thể |
| `--cref REF_URL` | Character Reference: giữ gương mặt | Cùng 1 cô gái cho cả bộ |
| `--cw 0` | Chỉ giữ **khuôn mặt**, thả tóc/áo | Vì mỗi lá **đổi màu tóc** theo yêu cầu của bạn (`--cw 100` sẽ khóa luôn tóc → sai) |
| `--sref REF_URL` | Style Reference: giữ chất vẽ | Cùng chất semi-realistic painterly |
| `--sw 300` | Độ mạnh style (0–1000) | 300 = theo style mẫu nhưng vẫn nghe prompt lá mới; tăng 500–600 nếu muốn giống hệt |
| `--ar 2:3` | Khổ dọc tarot | Chuẩn lá bài |
| `--style raw --stylize 200` | Bám prompt chữ tốt hơn | Prompt dài, cần MJ nghe lời |
| `--v 6.1` | Model mới, vẽ tay/chữ tốt hơn | |

## Bước 3 — Xử lý chữ tiêu đề (quan trọng)

Midjourney **hay viết sai chữ**. Có 2 cách:

- **Cách 1 — Gen kèm chữ (hên xui):** dùng lệnh trong file
  `midjourney/commands-with-title.txt`. Nếu chữ sai → bấm `Vary (Subtle)` + sửa, hoặc sang Cách 2.
- **Cách 2 — Gen art sạch, ghép chữ sau (khuyên dùng cho bộ bài thật):** dùng lệnh trong
  `midjourney/commands-clean-art.txt` (đã xóa câu chữ tiêu đề + thêm `--no text,letters,words`),
  rồi ghép chữ THE FOOL... bằng Canva/Photoshop với font serif vàng.

## Bước 4 — Gen 22 lá ở đâu?

- `midjourney/commands-with-title.txt` — 22 lệnh, mỗi lệnh = 1 lá (gen kèm chữ).
- `midjourney/commands-clean-art.txt` — 22 lệnh, gen art sạch (ghép chữ sau).
- Mỗi lệnh đã gắn sẵn link GitHub Cách B — chỉ cần thay bằng link Discord của bạn
  (Find/Replace chuỗi `REF_URL`).

## Mẹo đồng bộ tối đa

1. Gen lá **THE FOOL trước** → ưng ảnh nào thì lấy ảnh đó làm thêm `--sref` thứ 2 cho các lá sau
   (càng nhiều ref cùng bộ, càng đều).
2. Giữ nguyên `--seed` không hiệu quả bằng `--cref + --sref` — cứ dùng ref ảnh.
3. Nếu MJ vẽ sai đạo cụ (thiếu bình, sai số lượng): thêm cụm `::2` sau vật quan trọng,
   vd: `two ornate golden pitchers::2`.
4. Nếu mặt bị khác mẫu: tăng `--cw` lên 20–50 (nhưng tóc có thể bị kéo về bạch kim —
   lúc đó nhấn mạnh màu tóc mới bằng `::2`, vd: `copper-red ponytail::2`).
5. Vẽ xong → Upscale → `Vary (Region)` để sửa tay/chữ lỗi cục bộ.
