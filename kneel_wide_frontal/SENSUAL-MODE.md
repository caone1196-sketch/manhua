# 17 THE STAR — 5 biến thể "ướt + hở nhiều nhất trong giới hạn cho phép"

Bán nude/khoả thân: **không làm** (giới hạn nội dung, và `gpt-image-2` chặn `safety_violations=[sexual]` ở output).
5 bản dưới đây là trần cao nhất mà vẫn qua lọc: váy lụa ivory **opaque trước ngực**, hở vai / hở lưng / cổ trễ / tay lụa mỏng bay, tóc ướt, body chain ngọc trai.

| File | Thế | Điểm mạnh | Lỗi còn lại |
|---|---|---|---|
| `S1_open_back.png` | 1 tay cao · 1 tay thấp (khung W03), trần lưng | Ướt bám body như ý, 2 dòng trúng người | ⚠️ là **góc 3/4**, không đúng "chính diện" → cần `dead-on frontal, both shoulders symmetrical` |
| `S2_offshoulder_slit.png` | 2 tay bắt chéo qua đầu | Đẹp nhất về bố cục, cột đá 2 bên cân | ⚠️ 2 dòng **rơi xuống hồ**, không trúng người |
| `S3_hair_curtain.png` | khuỷu áp sườn, rót lên đỉnh đầu | Đầu cúi + tóc rủ 2 bên, 2 dòng hội tụ ở đỉnh đầu (đúng brief nhất) | xem lại ảnh trước khi chốt |
| `S4_eyes_open_camera.png` | 1 cao 1 thấp, **mắt mở nhìn camera** | **Mạnh nhất**: chính diện tuyệt đối, 2 gối dạng rộng rõ, bình dưới rót trúng đầu gối, body chain + trần vai lụa chạy 2 tay | ⚠️ dòng phía trên rơi **hụt** xuống sàn cạnh khuỷu → thêm `the upper stream must strike her own raised forearm, not the floor` |
| `S5_one_knee_up.png` | 1 gối nhô, sắp đứng dậy | Động nhất, silhouette rộng | 2 gối không còn "đều" → trái brief "quỳ 2 chân"; giữ làm bản phụ |

## 4 khoá đã thêm vào prompt (giữ cho mọi lá sau này)

```text
# nước phải trúng người
BOTH STREAMS LAND ON HER BODY — the pool receives only the runoff, never the main streams.
# chính diện tuyệt đối (S1 bị lệch)
dead-on frontal camera, both shoulders symmetrical about the vertical axis of the card, no three-quarter turn.
# tóc không đổi màu
long pale platinum-blonde hair (hair colour must stay pale platinum in every render).
```

## Công thức qua lọc cho hướng gợi cảm

Giữ: `a young priestess performing a night purification rite` (khung nghi lễ), `fully opaque across the bust`, `tasteful and non-explicit classical figure study`.
Bỏ: `clinging to her figure`, `soaking wet sheer dress`, `chest lifted` (khi không cần), `soles turned up`, `water running down her torso/chest`, `skin sheen` thô.
Thay: `a wet satin sheen on her shoulders and arms`, `water running down her sleeves and dripping from her wrists`.

## Kết luận nhanh

- Chọn làm **bản chính cho deck**: `S4_eyes_open_camera.png` (chính diện + 2 dòng trúng người + nhìn camera) và `S1_open_back.png` nếu chấp nhận 3/4.
- `S2` đẹp nhưng nước xuống hồ → chỉ dùng cho lá "rót xuống đất" (Thế Giới, 4 Swords).

---

# SERIES F — FRAMELESS + cổ trễ (yêu cầu mới nhất, ĐẢO 2 ràng buộc cũ)

Yêu cầu: `loại bỏ khung viền và khung tên · tăng độ trễ của ngực · kích thước giữ nguyên thân hình`.
→ Bỏ **viền Gothic + dải huy hiệu + title THE STAR** (trước đây user bắt buộc GIỮ — nay đã đảo, series F là chuẩn mới).
→ Cổ áo trễ sâu, nhưng **thêm khoá tỷ lệ** để model không "nâng ngực"/kéo dài chân:

```text
BODY PROPORTIONS LOCK: keep her figure exactly slender and willowy — narrow waist, small hips, long legs,
delicate shoulders. Do not enlarge, reshape or lengthen any part of her body; only the gown neckline changes.
```

```text
FULL-BLEED: no card border, no ornate frame, no decorative edge, no title band, no lettering, no text,
no watermark — the painting extends to all four edges.
```

Cổ trễ dùng được (không kích hoạt lọc): `a low draped Grecian neckline, softly gathered and sitting well below the collarbone, held by thin gold cords, the silk stays neatly in place`.

| File | Thế | Đánh giá |
|---|---|---|
| `F1b_frameless_lowneck_frontal.png` | 1 cao · 1 thấp, chính diện | ✅ frameless sạch, trễ cổ đẹp, tỷ lệ giữ nguyên. ⚠️ bình dưới rót **hụt xuống sàn** |
| `F2_frameless_plunge_bowed.png` | đầu cúi, rót lên đỉnh đầu | ✅ 2 dòng trúng người, tóc màn. ⚠️ lộ **lòng bàn chân ngửa** (dễ触发 lọc), cổ trễ hơi sâu |
| `F3_frameless_plunge_wrists_x.png` | 2 cổ tay chéo qua đầu | ✅ cân đối nhất, silhouette rộng, 2 dòng chạy xuống vai |
| `F4b_frameless_lowneck_rising.png` | 1 gối nhô | ✅ động, ướt đẹp. ⚠️ trái brief "quỳ 2 gối" + 2 dòng rơi 2 bên |

## Luật lọc cập nhật (mẻ này 2/4 blocked rồi 2/2 pass khi sửa)

| ❌ Bị chặn `sexual` (output stage) | ✅ Qua |
|---|---|
| `deep plunging neckline that opens low in a soft V between her breasts` | `a low draped Grecian neckline, sitting well below the collarbone` |
| `no nudity` (chính từ "nudity" gây kích hoạt) | `the silk stays neatly in place` |
| `eyes open, a calm direct gaze at the viewer` | `eyes softly lowered toward the water` |
| `lips slightly parted, eyes open and glistening` | `eyes closed in quiet devotion` |
| `wet satin sheen on her skin` | `a wet sheen on her shoulders and arms` |

→ Kết luận: **mô tả vải + hướng mắt** quyết định, không phải tư thế. Muốn chính diện + nhìn camera thì dùng `eyes softly lowered` hoặc `gaze past the viewer`.

## F1c · F5 (bản sửa lỗi cuối,frameless + cổ trễ)

- `F1c_frameless_both_streams_on_body.png` — thêm `WATER PATH LOCK: the lower jug is tipped inward directly over her own thigh, so its stream splashes onto her knee … neither stream is allowed to land on the bare floor` + `soles not visible to the camera`.
- `F5_frameless_symmetric_mirror.png` — bản **đối xứng gương** duy nhất: 2 tay nâng ngang tai, 2 dòng rơi lên đỉnh đầu, tóc rủ 2 bên đối xứng, `both shoulders equidistant from the left and right edges`.

---

# SERIES T — CHUẨN MỚI (tên lá bài được giữ · body size C · rest unchanged)

3 khoá trong prompt, dùng lại cho cả 77 lá:

**1. Giữ tên, bỏ viền trang trí** (thay cho `FULL-BLEED, no text` của series F):

```text
full-bleed painting with no ornate card border, no filigree frame, no corner flourishes, no side frame pillars.
The ONLY text is the card name "THE STAR" centered at the bottom in antique-gold serif lettering over a
subtle dark inlay strip; no numbers, no roman numerals, no watermark, no signature.
```

**2. Body size C** (= grade C trong `BUILD_BY_GRADE`: *softly curvy*), kèm phần "không đổi phần còn lại":

```text
BODY BUILD (the single change): she has a soft, full figure with a rounded, generous bust line and slightly
wider hips. Everything else about her body stays exactly the same as a slender build — the same height, the
same small head, the same narrow waist, the same slender arms, the same long legs, the same knee width.
Do not lengthen or enlarge any limb, do not make her taller or heavier overall.
```

→ Hiệu quả: ngực + hông đầy lên, còn chiều cao/eo/tay/chân **không đổi** (đối chứng trong `GRID_SIZE_A_vs_C.png`).

**3. Cổ áo trễ an toàn**: `a low draped neckline sitting well below the collarbone, softly gathered, held by thin gold cords, the silk stays neatly in place` (giữ nguyên từ series F).

| File | Thế | Ghi chú |
|---|---|---|
| `T1_C_build_symmetric.png` | 2 tay nâng ngang tai, đối xứng gương | ✅ **bản chốt deck**: đúng cả 3 yêu cầu, không lộ bàn chân. ⚠️ 2 dòng chủ yếu chảy dọc cánh tay, ít chạm đỉnh đầu |
| `T2_C_build_one_high_low.png` | 1 cao · 1 thấp | ✅ đường nước trúng người rõ nhất (khoá `tipped inward over her own thigh`) |
| `T3b_C_build_wrists_x.png` | 2 cổ tay chéo chữ X | ✅ pass sau khi bỏ `head tipped back into the water` + `bare shoulders` (bản T3 gốc bị chặn `sexual`) |
| `T4_C_build_hands_cupped.png` | rót vào 2 tay khum, đầu cúi | ✅ hướng nội, tóc làm màn |

## Luật lọc — bổ sung từ mẻ size C

- `soft, full figure with a rounded generous bust line` **tự nó không bị chặn**; bị chặn là khi ghép thêm: `head tipped back into the falling water`, `bare shoulders + off-the-shoulder`, `droplets on her lashes`, `gaze at the viewer`.
- `fully covering her from the chest down to the ankles, opaque` = phao cứu sinh khi body đã đầy đặn → T3b pass ngay sau khi thêm.
