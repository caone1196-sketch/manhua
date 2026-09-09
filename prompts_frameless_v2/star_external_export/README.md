# The Star — 5 prompt chạy trên công cụ ngoài (Midjourney / DALL·E / SD / Leonardo…)

Bộ 5 prompt **"áo tuột xuống eo"** (top slid down, bunched at the hip-tie knots) cho lá The Star —
concept bị moderation của backend Gemini chặn (21/21 lần thử), nên đóng gói ra đây để bạn tự chạy
trên bất kỳ công cụ sinh ảnh nào bạn có tài khoản.

## Cách dùng

1. Mở file prompt tương ứng (pose06 → pose10), copy **toàn bộ** nội dung.
2. Dán vào công cụ của bạn (Midjourney / ChatGPT DALL·E / Stable Diffusion / Leonardo / NovelAI…).
3. **Đính kèm 2 ảnh style reference** (nếu công cụ hỗ trợ ảnh tham chiếu / img2img):
   - `cards_v2_bathroom/08-strength.png` → phong cách manhwa, đường nét, ánh sáng rim, chữ tiêu đề vàng antique
   - `test_card_17_the_star.png` → benchmark vải ướt + da bóng ướt
   (Prompt đã ghi sẵn vai trò của 2 ảnh trong phần REFERENCE IMAGES.)
4. Đặt tỉ lệ khung **dọc ~7:12** (Midjourney: `--ar 7:12`; các tool khác: chọn portrait 2:3 hoặc 9:16).

## 5 phiên bản

| File | Tư thế |
|---|---|
| `17-star_pose06_twin_overhead.txt` | Quỳ, 2 tay chữ V, 2 bình đổ 2 dòng nước xuống ngực |
| `17-star_pose07_profile_pour.txt` | Nghiêng người full profile, silhouette ánh sao |
| `17-star_pose08_waterline_recline.txt` | Nằm nửa chìm trong bồn, mực nước ngang ngực |
| `17-star_pose09_shoulder_pour.txt` | Góc 3/4 sau, tay qua đầu đổ nước vòng qua vai |
| `17-star_pose10_rim_lean.txt` | Nghiêng người qua thành bồn về phía người xem |

Đặc điểm chung (đã ghi trong prompt): tóc bạch kim như bạc lỏng · bikini trắng ngọc ướt sũng
(chỉ còn quần, top tuột dồn xuống eo vướng dây hông) · nước đổ lên ngực chảy theo da ·
mặt ngửa nhẹ về sau, mắt nhắm hờ · đúng 2 bình vàng · không khung, chỉ chữ "THE STAR" vàng antique cuối thẻ.

## Sau khi có ảnh

Đặt tên file `17-the-star.png` (hoặc gửi lại cho tôi) rồi thay vào `cards_v2_bathroom/`.
Nếu bạn tải ảnh lên repo, tôi sẽ ghép contact sheet + commit như thường lệ.
