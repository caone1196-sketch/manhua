/**
 * composer.js — tab "Thiết kế bài": chọn artwork, đặt tên, khung,
 * preview canvas thời gian thực, xuất PNG, lưu vào bộ bài.
 */

const state = { art: 0, name: "", numeral: "", frame: "classic", fit: "cover" };

const preview = document.getElementById("previewCanvas");
const pctx = preview.getContext("2d");

function currentCard() {
  return {
    src: ARTWORK[state.art].src,
    name: state.name,
    numeral: state.numeral,
    frame: state.frame,
    fit: state.fit,
  };
}

async function renderPreview() {
  const art = await loadArt(ARTWORK[state.art].src);
  drawCard(pctx, preview.width, preview.height, state, art);
}

function syncComposerUI() {
  document.querySelectorAll("#artPick .art-thumb").forEach((el, i) =>
    el.classList.toggle("is-active", i === state.art)
  );
  document.querySelectorAll("#framePick .chip").forEach((el) =>
    el.classList.toggle("is-active", el.dataset.frame === state.frame)
  );
  document.querySelectorAll(".fit-chip").forEach((el) =>
    el.classList.toggle("is-active", el.dataset.fit === state.fit)
  );
  document.getElementById("cName").value = state.name;
  document.getElementById("cNumeral").value = state.numeral;
}

function buildComposer() {
  // 1 · Chọn artwork
  const pick = document.getElementById("artPick");
  ARTWORK.forEach((a, i) => {
    const b = document.createElement("button");
    b.className = "art-thumb";
    b.type = "button";
    b.title = a.label;
    b.innerHTML = `<img src="${a.src}" alt="${a.label}" /><span>${i + 1}</span>`;
    b.addEventListener("click", () => {
      state.art = i;
      syncComposerUI();
      renderPreview();
    });
    pick.appendChild(b);
  });

  // 3 · Khung bài
  const fp = document.getElementById("framePick");
  Object.entries(FRAMES).forEach(([key, f]) => {
    const b = document.createElement("button");
    b.className = "chip frame-chip";
    b.type = "button";
    b.dataset.frame = key;
    b.innerHTML = `<i style="background:${f.bg};box-shadow:inset 0 0 0 2px ${f.border}"></i>${f.name}`;
    b.addEventListener("click", () => {
      state.frame = key;
      syncComposerUI();
      renderPreview();
    });
    fp.appendChild(b);
  });

  // 4 · Cách đặt ảnh
  document.querySelectorAll(".fit-chip").forEach((b) => {
    b.addEventListener("click", () => {
      state.fit = b.dataset.fit;
      syncComposerUI();
      renderPreview();
    });
  });

  // 2 · Tên + số La Mã + chọn nhanh
  const sel = document.getElementById("cArcana");
  MAJOR_ARCANA.forEach((a) => {
    const o = document.createElement("option");
    o.value = a.numeral;
    o.textContent = `${a.numeral} — ${a.vi} (${a.en})`;
    sel.appendChild(o);
  });
  sel.addEventListener("change", () => {
    const a = MAJOR_ARCANA.find((x) => x.numeral === sel.value);
    if (a) {
      state.name = a.vi;
      state.numeral = a.numeral;
      syncComposerUI();
      renderPreview();
    }
  });

  document.getElementById("cName").addEventListener("input", (e) => {
    state.name = e.target.value.trim();
    renderPreview();
  });
  document.getElementById("cNumeral").addEventListener("input", (e) => {
    state.numeral = e.target.value.trim();
    renderPreview();
  });

  // Nút xuất & lưu
  document.getElementById("btnDownload").addEventListener("click", downloadCard);
  document.getElementById("btnSave").addEventListener("click", saveCard);

  syncComposerUI();
}

function slugify(s) {
  return (s || "")
    .toLowerCase()
    .normalize("NFD")
    .replace(/[\u0300-\u036f]/g, "")
    .replace(/đ/g, "d")
    .replace(/[^a-z0-9]+/g, "-")
    .replace(/^-+|-+$/g, "");
}

function downloadCard() {
  preview.toBlob((blob) => {
    if (!blob) return toast("Không thể xuất ảnh 😢");
    const url = URL.createObjectURL(blob);
    const a = document.createElement("a");
    a.href = url;
    a.download = `tarot-${slugify(state.name) || "card"}.png`;
    document.body.appendChild(a);
    a.click();
    a.remove();
    setTimeout(() => URL.revokeObjectURL(url), 5000);
    toast("Đã xuất PNG 1050 × 1800 ✓");
  }, "image/png");
}

function saveCard() {
  if (!state.name && !state.numeral) {
    toast("Hãy đặt tên (hoặc số La Mã) cho bài trước khi lưu");
    return;
  }
  const deck = getDeck();
  deck.push({
    ...currentCard(),
    id: Date.now().toString(36) + Math.random().toString(36).slice(2, 6),
    ts: Date.now(),
  });
  setDeck(deck);
  renderDeck();
  toast("Đã lưu vào bộ bài ✓");
}

/** Mở một lá đã lưu từ bộ bài trở lại xưởng */
function composerLoad(c) {
  const idx = ARTWORK.findIndex((a) => a.src === c.src);
  state.art = idx >= 0 ? idx : 0;
  state.name = c.name || "";
  state.numeral = c.numeral || "";
  state.frame = FRAMES[c.frame] ? c.frame : "classic";
  state.fit = c.fit || "cover";
  document.getElementById("cArcana").value = "";
  syncComposerUI();
  renderPreview();
}
