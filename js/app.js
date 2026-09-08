/**
 * Manhua Gallery — front-end logic.
 * Thêm ảnh mới: chỉ cần đặt file vào /images rồi thêm 1 dòng vào IMAGES dưới đây.
 */
const IMAGES = [
  { src: "images/capture2.png", title: "Manhua #1", tag: "portrait", note: "Đã thêm 08/09/2026" },
  { src: "images/capture3.png", title: "Manhua #2", tag: "portrait", note: "Đã thêm 08/09/2026" },
  { src: "images/capture4.png", title: "Manhua #3", tag: "portrait", note: "Đã thêm 08/09/2026" },
  { src: "images/capture5.png", title: "Manhua #4", tag: "landscape", note: "Đã thêm 08/09/2026" },
];

const gallery = document.getElementById("gallery");
const emptyNote = document.getElementById("emptyNote");
const countLabel = document.getElementById("countLabel");
const lightbox = document.getElementById("lightbox");
const lbImage = document.getElementById("lbImage");
const lbCaption = document.getElementById("lbCaption");
const lbCounter = document.getElementById("lbCounter");
const lbClose = document.getElementById("lbClose");
const lbPrev = document.getElementById("lbPrev");
const lbNext = document.getElementById("lbNext");

let currentFilter = "all";
let visibleImages = [...IMAGES];
let currentIndex = 0;

function render() {
  gallery.innerHTML = "";
  visibleImages = IMAGES.filter((img) => currentFilter === "all" || img.tag === currentFilter);

  visibleImages.forEach((img, i) => {
    const card = document.createElement("article");
    card.className = "card";
    card.tabIndex = 0;
    card.setAttribute("role", "button");
    card.setAttribute("aria-label", `Phóng to ${img.title}`);
    card.innerHTML = `
      <img class="thumb" src="${img.src}" alt="${img.title}" loading="lazy" />
      <span class="index-badge">${String(i + 1).padStart(2, "0")}</span>
      <div class="overlay">
        <span class="title">${img.title}</span>
        <span class="meta">${img.note}</span>
      </div>
    `;
    const open = () => openLightbox(i);
    card.addEventListener("click", open);
    card.addEventListener("keydown", (e) => {
      if (e.key === "Enter" || e.key === " ") {
        e.preventDefault();
        open();
      }
    });
    gallery.appendChild(card);
  });

  emptyNote.hidden = visibleImages.length > 0;
  countLabel.textContent = `${visibleImages.length}/${IMAGES.length} ảnh`;
}

function openLightbox(i) {
  currentIndex = i;
  updateLightbox();
  lightbox.hidden = false;
  document.body.style.overflow = "hidden";
}

function closeLightbox() {
  lightbox.hidden = true;
  document.body.style.overflow = "";
  const activeCard = gallery.querySelector(".card");
  if (activeCard) activeCard.focus();
}

function step(delta) {
  if (!visibleImages.length) return;
  currentIndex = (currentIndex + delta + visibleImages.length) % visibleImages.length;
  updateLightbox();
}

function updateLightbox() {
  const img = visibleImages[currentIndex];
  if (!img) return;
  lbImage.src = img.src;
  lbImage.alt = img.title;
  lbCaption.textContent = `${img.title} — ${img.note}`;
  lbCounter.textContent = `${currentIndex + 1} / ${visibleImages.length}`;
}

// Filter chips
document.querySelectorAll(".chip").forEach((chip) => {
  chip.addEventListener("click", () => {
    currentFilter = chip.dataset.filter;
    document.querySelectorAll(".chip").forEach((c) => c.classList.toggle("is-active", c === chip));
    render();
  });
});

// Lightbox controls
lbClose.addEventListener("click", closeLightbox);
lbPrev.addEventListener("click", () => step(-1));
lbNext.addEventListener("click", () => step(1));
lightbox.addEventListener("click", (e) => {
  if (e.target === lightbox) closeLightbox();
});

// Keyboard navigation
document.addEventListener("keydown", (e) => {
  if (lightbox.hidden) return;
  if (e.key === "Escape") closeLightbox();
  if (e.key === "ArrowLeft") step(-1);
  if (e.key === "ArrowRight") step(1);
});

render();
