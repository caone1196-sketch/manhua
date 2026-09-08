/**
 * app.js — điều hướng tabs, lưới artwork + lightbox,
 * bộ bài (localStorage), spread trải 3 lá.
 */

/* ================= Tabs ================= */
function switchTab(name) {
  document.querySelectorAll(".tab").forEach((b) =>
    b.classList.toggle("is-active", b.dataset.tab === name)
  );
  document.querySelectorAll(".tab-panel").forEach((p) =>
    p.classList.toggle("is-active", p.id === "tab-" + name)
  );
  if (name === "deck") renderDeck();
}

document.querySelectorAll(".tab").forEach((btn) => {
  btn.addEventListener("click", () => switchTab(btn.dataset.tab));
});

/* ================= Toast ================= */
let toastTimer;
function toast(msg) {
  const t = document.getElementById("toast");
  t.textContent = msg;
  t.classList.add("show");
  clearTimeout(toastTimer);
  toastTimer = setTimeout(() => t.classList.remove("show"), 2600);
}

/* ================= Artwork + Lightbox ================= */
const artGrid = document.getElementById("artGrid");
const lightbox = document.getElementById("lightbox");
const lbImage = document.getElementById("lbImage");
const lbCaption = document.getElementById("lbCaption");
const lbCounter = document.getElementById("lbCounter");
let lbIndex = 0;

function buildArtwork() {
  artGrid.innerHTML = "";
  ARTWORK.forEach((a, i) => {
    const card = document.createElement("figure");
    card.className = "art-card";
    card.tabIndex = 0;
    card.innerHTML = `
      <img src="${a.src}" alt="${a.label}" loading="lazy" />
      <span class="index-badge">ART ${String(i + 1).padStart(2, "0")}</span>
      <div class="overlay">
        <span class="title">${a.label}</span>
        <span class="meta">Bấm để xem chi tiết</span>
      </div>`;
    const open = () => openLightbox(i);
    card.addEventListener("click", open);
    card.addEventListener("keydown", (e) => {
      if (e.key === "Enter" || e.key === " ") {
        e.preventDefault();
        open();
      }
    });
    artGrid.appendChild(card);
  });
  document.getElementById("artCount").textContent = `${ARTWORK.length} artwork`;
}

function openLightbox(i) {
  lbIndex = i;
  updateLightbox();
  lightbox.hidden = false;
  document.body.style.overflow = "hidden";
}

function closeLightbox() {
  lightbox.hidden = true;
  document.body.style.overflow = "";
}

function stepLightbox(delta) {
  lbIndex = (lbIndex + delta + ARTWORK.length) % ARTWORK.length;
  updateLightbox();
}

function updateLightbox() {
  const a = ARTWORK[lbIndex];
  lbImage.src = a.src;
  lbImage.alt = a.label;
  lbCaption.textContent = a.label;
  lbCounter.textContent = `${lbIndex + 1} / ${ARTWORK.length}`;
}

document.getElementById("lbClose").addEventListener("click", closeLightbox);
document.getElementById("lbPrev").addEventListener("click", () => stepLightbox(-1));
document.getElementById("lbNext").addEventListener("click", () => stepLightbox(1));
lightbox.addEventListener("click", (e) => {
  if (e.target === lightbox) closeLightbox();
});
document.addEventListener("keydown", (e) => {
  if (lightbox.hidden) return;
  if (e.key === "Escape") closeLightbox();
  if (e.key === "ArrowLeft") stepLightbox(-1);
  if (e.key === "ArrowRight") stepLightbox(1);
});

/* ================= Bộ bài (localStorage) ================= */
const DECK_KEY = "tarot.deck.v1";

function getDeck() {
  try {
    return JSON.parse(localStorage.getItem(DECK_KEY)) || [];
  } catch (e) {
    return [];
  }
}

function setDeck(deck) {
  localStorage.setItem(DECK_KEY, JSON.stringify(deck));
  document.getElementById("deckCount").textContent = deck.length;
}

async function renderDeck() {
  const grid = document.getElementById("deckGrid");
  const empty = document.getElementById("deckEmpty");
  const deck = getDeck();
  grid.innerHTML = "";
  empty.hidden = deck.length > 0;

  for (const c of deck) {
    const item = document.createElement("div");
    item.className = "deck-item";

    const canvas = document.createElement("canvas");
    canvas.width = 525;
    canvas.height = 900;
    canvas.title = "Mở trong xưởng thiết kế";
    const art = await loadArt(c.src);
    drawCard(canvas.getContext("2d"), canvas.width, canvas.height, c, art);
    canvas.addEventListener("click", () => {
      composerLoad(c);
      switchTab("design");
    });
    item.appendChild(canvas);

    const meta = document.createElement("div");
    meta.className = "deck-meta";
    const label = document.createElement("span");
    label.textContent = `${c.name || "Chưa đặt tên"} · Khung ${FRAMES[c.frame].name}`;
    const del = document.createElement("button");
    del.className = "del";
    del.type = "button";
    del.textContent = "✕";
    del.title = "Xóa bài";
    del.addEventListener("click", () => {
      setDeck(getDeck().filter((x) => x.id !== c.id));
      renderDeck();
      toast("Đã xóa bài khỏi bộ bài");
    });
    meta.appendChild(label);
    meta.appendChild(del);
    item.appendChild(meta);
    grid.appendChild(item);
  }
}

document.getElementById("btnGotoDesign").addEventListener("click", () => switchTab("design"));

/* ================= Spread 3 lá ================= */
const SLOT_LABELS = ["QUÁ KHỨ", "HIỆN TẠI", "TƯƠNG LAI"];

function buildSpread() {
  const spread = document.getElementById("spread");
  spread.innerHTML = "";
  SLOT_LABELS.forEach((label) => {
    const slot = document.createElement("div");
    slot.className = "slot";
    slot.innerHTML = `<div class="slot-label">${label}</div>
      <div class="card-flip">
        <div class="flip-inner">
          <div class="card-back"></div>
          <div class="card-face"><canvas width="420" height="720"></canvas></div>
        </div>
      </div>`;
    slot.querySelector(".card-flip").addEventListener("click", (e) => {
      e.currentTarget.classList.toggle("flipped");
    });
    spread.appendChild(slot);
  });
}

document.getElementById("btnSpread").addEventListener("click", async () => {
  const deck = getDeck();
  if (deck.length < 3) {
    toast(`Cần ít nhất 3 lá bài trong bộ bài (hiện có ${deck.length})`);
    return;
  }
  const picked = [...deck].sort(() => Math.random() - 0.5).slice(0, 3);
  const flips = document.querySelectorAll(".card-flip");

  // Xáo: hạ hết bài trước rồi lật lên
  flips.forEach((f) => f.classList.remove("flipped"));
  await new Promise((r) => setTimeout(r, 80));

  for (let i = 0; i < 3; i++) {
    const c = picked[i];
    const canvas = flips[i].querySelector("canvas");
    const art = await loadArt(c.src);
    drawCard(canvas.getContext("2d"), canvas.width, canvas.height, c, art);
    flips[i].classList.add("flipped");
  }
  toast("✦ Đã trải 3 lá — bấm lá để lật xem");
});

/* ================= Khởi động ================= */
async function init() {
  // Chờ font canvas (kể cả subset tiếng Việt của Playfair Display)
  try {
    await Promise.all([
      document.fonts.load('600 72px "Playfair Display"', "ÁàơưệTarot"),
      document.fonts.load('700 48px "Cinzel"', "IVXXI"),
      document.fonts.load('500 20px "Be Vietnam Pro"', "Việt"),
    ]);
  } catch (e) { /* dùng font dự phòng */ }

  buildArtwork();
  buildComposer();
  buildSpread();
  setDeck(getDeck());
  renderDeck();
  renderPreview();
}

document.addEventListener("DOMContentLoaded", init);
