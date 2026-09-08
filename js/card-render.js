/**
 * card-render.js — vẽ lá bài tarot lên canvas.
 * Dùng chung cho: preview xưởng thiết kế, lưới bộ bài, spread trải bài.
 */

const imgCache = new Map();

/** Tải ảnh (cache) — resolve HTMLImageElement hoặc null nếu lỗi */
function loadArt(src) {
  if (imgCache.has(src)) return imgCache.get(src);
  const p = new Promise((resolve) => {
    const img = new Image();
    img.onload = () => resolve(img);
    img.onerror = () => resolve(null);
    img.src = src;
  });
  imgCache.set(src, p);
  return p;
}

function roundedRectPath(ctx, x, y, w, h, r) {
  ctx.beginPath();
  ctx.moveTo(x + r, y);
  ctx.arcTo(x + w, y, x + w, y + h, r);
  ctx.arcTo(x + w, y + h, x, y + h, r);
  ctx.arcTo(x, y + h, x, y, r);
  ctx.arcTo(x, y, x + w, y, r);
  ctx.closePath();
}

/** Sao 4 cánh (hoa văn tarot) */
function star4Path(ctx, cx, cy, r) {
  ctx.beginPath();
  ctx.moveTo(cx, cy - r);
  ctx.quadraticCurveTo(cx, cy, cx + r, cy);
  ctx.quadraticCurveTo(cx, cy, cx, cy + r);
  ctx.quadraticCurveTo(cx, cy, cx - r, cy);
  ctx.quadraticCurveTo(cx, cy, cx, cy - r);
  ctx.closePath();
}

function withAlpha(hex, a) {
  const n = parseInt(hex.slice(1), 16);
  const r = (n >> 16) & 255;
  const g = (n >> 8) & 255;
  const b = n & 255;
  return `rgba(${r},${g},${b},${a})`;
}

function setTracking(ctx, px) {
  try { ctx.letterSpacing = `${px}px`; } catch (e) { /* browser cũ bỏ qua */ }
}

/**
 * Vẽ lá bài hoàn chỉnh.
 * card: { name, numeral, frame, fit }
 * artImg: HTMLImageElement (đã load) hoặc null
 */
function drawCard(ctx, W, H, card, artImg) {
  const f = FRAMES[card.frame] || FRAMES.classic;

  ctx.clearRect(0, 0, W, H);
  ctx.save();

  // Nền lá bài + bo góc (mọi thứ đều clip trong lá)
  const R = W * 0.042;
  roundedRectPath(ctx, 0.5, 0.5, W - 1, H - 1, R);
  ctx.fillStyle = f.bg;
  ctx.fill();
  ctx.clip();

  // Viền ngoài (dày, vàng)
  const m1 = W * 0.026;
  roundedRectPath(ctx, m1, m1, W - 2 * m1, H - 2 * m1, R * 0.75);
  ctx.lineWidth = W * 0.01;
  ctx.strokeStyle = f.border;
  ctx.stroke();

  // Viền trong (mảnh)
  const m2 = W * 0.048;
  roundedRectPath(ctx, m2, m2, W - 2 * m2, H - 2 * m2, R * 0.5);
  ctx.lineWidth = Math.max(1, W * 0.0032);
  ctx.strokeStyle = withAlpha(f.border, 0.7);
  ctx.stroke();

  // Hoa văn sao ở 4 góc
  ctx.fillStyle = withAlpha(f.border, 0.9);
  const cs = W * 0.0095;
  const gc = W * 0.037;
  [[gc, gc], [W - gc, gc], [gc, H - gc], [W - gc, H - gc]].forEach(([x, y]) => {
    star4Path(ctx, x, y, cs);
    ctx.fill();
  });

  ctx.textAlign = "center";
  ctx.textBaseline = "middle";

  // Tên bài
  if (card.name) {
    ctx.fillStyle = f.text;
    ctx.font = `600 ${W * 0.066}px "Playfair Display", serif`;
    setTracking(ctx, W * 0.006);
    ctx.fillText(card.name, W / 2, H * 0.072, W * 0.84);
    setTracking(ctx, 0);
  } else {
    // Chưa đặt tên: hoa văn nhỏ thay thế
    ctx.fillStyle = withAlpha(f.border, 0.8);
    star4Path(ctx, W / 2, H * 0.068, W * 0.014);
    ctx.fill();
  }

  // Số La Mã
  if (card.numeral) {
    ctx.fillStyle = withAlpha(f.text, 0.85);
    ctx.font = `700 ${W * 0.046}px "Cinzel", serif`;
    setTracking(ctx, W * 0.005);
    ctx.fillText(card.numeral, W / 2, H * 0.115);
    setTracking(ctx, 0);
  }

  // Vùng artwork
  const ax = W * 0.085;
  const ay = H * 0.143;
  const aw = W * 0.83;
  const ah = H * 0.655;
  const ar = aw * 0.028;

  ctx.save();
  roundedRectPath(ctx, ax, ay, aw, ah, ar);
  ctx.clip();
  ctx.fillStyle = f.bg;
  ctx.fillRect(ax, ay, aw, ah);
  if (artImg && artImg.naturalWidth) {
    const s = card.fit === "contain"
      ? Math.min(aw / artImg.naturalWidth, ah / artImg.naturalHeight)
      : Math.max(aw / artImg.naturalWidth, ah / artImg.naturalHeight);
    const dw = artImg.naturalWidth * s;
    const dh = artImg.naturalHeight * s;
    ctx.drawImage(artImg, ax + (aw - dw) / 2, ay + (ah - dh) / 2, dw, dh);
  }
  ctx.restore();

  // Viền quanh artwork
  roundedRectPath(ctx, ax, ay, aw, ah, ar);
  ctx.lineWidth = Math.max(1, W * 0.0045);
  ctx.strokeStyle = withAlpha(f.border, 0.9);
  ctx.stroke();

  // Hoa văn dưới cùng
  ctx.fillStyle = withAlpha(f.border, 0.9);
  star4Path(ctx, W / 2, H * 0.877, W * 0.016);
  ctx.fill();
  [W / 2 - W * 0.055, W / 2 + W * 0.055].forEach((x) => {
    ctx.beginPath();
    ctx.arc(x, H * 0.877, W * 0.004, 0, Math.PI * 2);
    ctx.fill();
  });

  ctx.restore();
}
