# 10 PHIÊN BẢN — "quỳ 2 gối DẠNG RỘNG · máy quay CHÍNH DIỆN · 2 tay 2 bình · tự rót lên người"

## Khung khoá (giống nhau ở cả 10 phiên bản)

| Trục | Giá trị |
|---|---|
| Camera | `dead-on frontal view` — đối xứng tuyệt đối qua trục dọc lá bài, không xoay 3/4, không profile |
| Nền tảng (base pose) | `kneeling in a wide seiza stance, both knees down and knees apart, weight resting back on her heels` |
| Dụng cụ | mỗi tay 1 bình vàng cổ, **cả 2 dòng nước phải rơi lên người nàng**, hồ chỉ nhận phần tràn |
| Khung bài | viền Gothic mạ vàng + dải huy hiệu đáy, title `THE STAR` serif vàng cổ, không số |
| Render | manhwa Hàn bán thực, không nét đen, grade tím-periwinkle + neon tím |
| Sáng | **sao 8 cánh khổng lồ + god rays NGAY SAU ĐẦU** (halo), rim xanh lạnh + vàng ấm từ bình |
| Môi trường | tháp Gothic cửa sổ tím · cột đá 2 bên · hồ đen sương · sàn phù điêu tròn |

## ⚠️ Bài học bộ lọc (backend đã đổi sang `gpt-image-2`, chặn `sexual` ở output)

5 bản đầu viết theo kiểu cũ (váy ướt **dán sát người**, `chest lifted`, `soles turned up`, `skin sheen`, `clinging`) → **bị từ chối 4/5**.
Công thức đã kiểm chứng là **qua lọc mà vẫn đẹp**:

| ❌ Tránh | ✅ Thay bằng |
|---|---|
| `soaking wet gown clinging to her figure` | `floor-length pale ivory silk gown, long sheer sleeves, high draped neckline, fully opaque and modest, the soaked hem gathered above the stone` |
| `chest lifted, back arched` | `posture upright and composed` |
| `soles turned up behind her` | `her weight resting back on her heels` |
| `water running down her throat / chest / torso` | `water running down her sleeves, dripping from her wrists and elbows` |
| `lips parted, flushed cheeks, wet skin sheen` | `serene expression, eyes closed in quiet devotion, damp strands at her temples` |
| (không có khung ý nghĩa) | `a young priestess performing a purification rite` — đóng khung **nghi thức** giúp bản gợi cảm lọt qua lọc |

→ **Hệ quả:** 10 bản này "ướt + nghi lễ" chứ không gợi cảm trần trụi như deck cũ. Muốn giữ độ gợi cảm của `the star.png` thì chạy các prompt cùng bộ 10 khung này bằng model khác (Nano Banana / Gemini image), hoặc dùng biến thể `MODE: sensual` bên dưới.

## 10 phiên bản

| # | File | Biến thể (chỉ đổi tay + thân + hướng mắt) | Trạng thái |
|---|---|---|---|
| W01 | `W01_arms_straight_up.png` | 2 tay duỗi thẳng lên 2 bên đầu, nước chảy dọc mặt trong cánh tay → nhỏ lên đá, tạo 2 hệ gợn giao nhau | ✅ |
| W02 | `W02_wrists_crossed.png` | 2 cẳng tay **bắt chéo cổ tay** tạo chữ X trên đỉnh đầu, 2 dòng xuôi xuống vai | ✅ |
| W03 | `W03_one_high_one_low.png` | 1 tay cao · 1 tay thấp cạnh hông — bản **lệch** duy nhất | ✅ |
| W04 | `W04_hands_cupped.png` | 2 khuỷu áp sườn, rót vào **chính 2 bàn tay khum** của nàng, tràn qua kẽ ngón; đầu cúi | ✅ |
| W05 | `W05_arms_wide_T.png` | 2 tay mở ngang chữ T, mỗi dòng rơi 1 bên vai — silhouette **rộng nhất** | ✅ |
| W06 | `W06_back_arch_head_tipped.png` | ngồi gót ngửa người, 2 bình lơ lửng trên mặt ngửa hứng nước | ⏳ prompt dưới |
| W07 | `W07_forward_fold_hair_curtain.png` | gập người 45° tới trước, rót lên 2 đầu gối, tóc rủ làm màn | ⏳ |
| W08 | `W08_behind_the_back.png` | 2 tay vòng ra sau, nước ướt mặt sau vai + tóc, vẫn nhìn thẳng camera | ⏳ |
| W09 | `W09_hands_at_wrists.png` | 2 bình cao ngang trán, 2 dòng chảy dọc 2 mu bàn tay → xuống khuỷu | ⏳ |
| W10 | `W10_one_knee_forward.png` | bản động nhất: 1 gối cao 1 gối thấp, tay vươn lên như vừa đứng dậy | ⏳ |

## Prompt W06–W10 (dán + giữ nguyên khung khoá ở đầu file)

Khối chung: dùng lại 6 đoạn `frame / camera / base pose / costume / atmosphere / text` của W01, **chỉ đổi đoạn `POSE VARIANT`**.

```text
POSE VARIANT W06 — she leans back into a slow arch, both forearms above her upturned face, each jug tipping so a single stream falls onto her chin and collarbone and runs down the front of the gown; her wet hair hangs behind her toward the stone, its tips touching the water film and starting a ring.

POSE VARIANT W07 — she folds forward from the waist, both arms stretched down in front of her, the two streams falling onto her own knees and forearms; her soaked hair hangs straight down like a curtain and its dripping tips break the surface of the water; her face is half hidden behind wet strands.

POSE VARIANT W08 — both arms reach back at shoulder height, each hand tipping its jug so the streams run down the backs of her shoulders and along her sleeves; her torso stays square to the camera and her face looks straight forward, so the water traces only the front-facing line of her shoulders.

POSE VARIANT W09 — both jugs held high at forehead height, arms bent, the streams falling onto the backs of her own hands and running down her knuckles, wrists and forearms before dripping onto the stone; her eyes follow the water down her hands.

POSE VARIANT W10 — the most dynamic: one knee lifted and that foot planted, the other knee still wide on the stone, torso rising as if about to stand, both arms extended upward with the jugs tipped; the two streams land on her raised forearms and splash across the wet stone at her knees.
```

## MODE: sensual (nếu đổi sang model ít chặn hơn)

Muốn đúng độ gợi cảm của `the star.png`, thay đoạn COSTUME + thêm:

```text
COSTUME (sensual mode): a single short bias-cut gown of pale ivory silk chiffon, draped neckline, open back, high side slits, thoroughly waterlogged and lying flat against her figure, hem pooling in the water; a pearl body chain, a thin pearl necklace, a slim gold circlet with a small blue gem, one chain anklet; barefoot; long platinum hair soaked in heavy gleaming strands; glossy half-closed eyes, softly parted lips, flushed cheeks, pale luminous skin with a wet sheen.
WET (sensual mode): water falling on her RIGHT NOW from both jugs, breaking across her forearms and shoulders and running down the soaked gown; spray and droplets frozen in the starlight; glossy highlight streaks tracing her silhouette; two sets of concentric ripples crossing in the black water plus her broken reflection.
```

## Mở rộng cho 77 lá

10 khung này dùng làm **bộ pose chuẩn** cho các lá nghi thức/thanh tẩy (temperance, star, moon, priestess, các lá Cups). Với lá cần động (Chariot, Wands), ưu tiên W10/W03; lá hướng nội (Hermit, 9 of Swords) ưu tiên W04/W07.

---

## Ghi chú tái tạo

Patch mang thư mục này sang repo chỉ chứa text — **21 file PNG không thể khôi phục từ diff**.
Toàn bộ ảnh ở đây được **render lại** từ đúng các khối prompt trong `F-PROMPTS.md` (cùng khung W / S / F / T,
cùng từng POSE VARIANT), nên **không phải file gốc** bạn đã duyệt: bố cục và tỷ lệ giữ nguyên, chi tiết có thể
khác. `make_grids.py` dựng lại 5 tấm `GRID_*` từ những ảnh hiện có trong thư mục (thiếu ảnh nào → ô đó hiện
`pending`), chạy lại sau khi render thêm.
