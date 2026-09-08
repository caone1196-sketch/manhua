import json

with open('cards.json', 'r', encoding='utf-8') as f:
    cards_data = json.load(f)

# Sample images mapping
sample_map = {
    "01-magician": "card_01_the_magician.png",
    "02-priestess": "card_02_the_high_priestess.png",
    "03-empress": "card_03_the_empress.png",
    "17-the-star": "card_04_the_star.png",
    "15-devil": "card_05_the_devil.png"
}

for c in cards_data['cards']:
    if c["slug"] in sample_map:
        c["sample_img"] = sample_map[c["slug"]]

html_template = """<!DOCTYPE html>
<html lang="vi">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>🔮 Sensual Manhwa Tarot — 78 Master Prompts v2</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Cinzel:wght@500;700;900&family=Plus+Jakarta+Sans:wght@300;400;500;600;700&display=swap" rel="stylesheet">
  <style>
    :root {
      --bg-main: #0b0c10;
      --bg-card: #151821;
      --bg-card-hover: #1c2130;
      --border-gold: #c6a052;
      --gold-glow: rgba(198, 160, 82, 0.35);
      --accent-purple: #a855f7;
      --accent-gold: #fbbf24;
      --text-main: #f3f4f6;
      --text-muted: #9ca3af;
      --font-title: 'Cinzel', serif;
      --font-body: 'Plus Jakarta Sans', sans-serif;
    }

    * { box-sizing: border-box; margin: 0; padding: 0; }
    body {
      background-color: var(--bg-main);
      color: var(--text-main);
      font-family: var(--font-body);
      min-height: 100vh;
      background-image: 
        radial-gradient(circle at 15% 15%, rgba(168, 85, 247, 0.08) 0%, transparent 40%),
        radial-gradient(circle at 85% 85%, rgba(245, 158, 11, 0.06) 0%, transparent 40%);
      background-attachment: fixed;
    }

    header {
      padding: 2.2rem 1.5rem 1.5rem;
      text-align: center;
      border-bottom: 1px solid rgba(198, 160, 82, 0.2);
      background: linear-gradient(180deg, rgba(21, 24, 33, 0.95) 0%, rgba(11, 12, 16, 0.98) 100%);
      backdrop-filter: blur(12px);
      position: sticky;
      top: 0;
      z-index: 100;
    }

    .header-badge {
      display: inline-flex;
      align-items: center;
      gap: 0.5rem;
      background: rgba(198, 160, 82, 0.15);
      border: 1px solid var(--border-gold);
      color: #fce7b0;
      padding: 0.35rem 1.2rem;
      border-radius: 9999px;
      font-size: 0.85rem;
      font-weight: 600;
      letter-spacing: 0.05em;
      text-transform: uppercase;
      margin-bottom: 0.75rem;
      box-shadow: 0 0 15px var(--gold-glow);
    }

    h1 {
      font-family: var(--font-title);
      font-size: clamp(1.8rem, 3.5vw, 2.7rem);
      font-weight: 900;
      background: linear-gradient(135deg, #fff2c6 0%, #d4af37 50%, #aa7c11 100%);
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
      margin-bottom: 0.5rem;
    }

    .header-desc {
      color: var(--text-muted);
      max-width: 850px;
      margin: 0 auto 1.25rem;
      font-size: 0.92rem;
      line-height: 1.5;
    }

    /* Controls */
    .controls {
      display: flex;
      flex-direction: column;
      align-items: center;
      gap: 0.9rem;
      max-width: 1200px;
      margin: 0 auto;
    }

    .search-input {
      width: 100%;
      max-width: 550px;
      padding: 0.75rem 1.25rem;
      background: #1e2230;
      border: 1px solid rgba(198, 160, 82, 0.3);
      border-radius: 12px;
      color: white;
      font-size: 0.95rem;
      outline: none;
      transition: all 0.3s;
    }

    .search-input:focus {
      border-color: var(--accent-gold);
      box-shadow: 0 0 15px var(--gold-glow);
    }

    .filter-pills {
      display: flex;
      flex-wrap: wrap;
      justify-content: center;
      gap: 0.5rem;
    }

    .filter-btn {
      background: rgba(30, 35, 48, 0.8);
      color: var(--text-muted);
      border: 1px solid rgba(255, 255, 255, 0.08);
      padding: 0.45rem 1rem;
      border-radius: 9999px;
      font-size: 0.85rem;
      font-weight: 600;
      cursor: pointer;
      transition: all 0.2s;
    }

    .filter-btn.active {
      background: linear-gradient(135deg, #c6a052 0%, #8b6b23 100%);
      color: #0b0c10;
      font-weight: 700;
      border-color: transparent;
      box-shadow: 0 4px 15px var(--gold-glow);
    }

    main {
      max-width: 1400px;
      margin: 1.5rem auto;
      padding: 0 1.5rem 5rem;
    }

    .stats-bar {
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 1.5rem;
      color: var(--text-muted);
      font-size: 0.92rem;
    }

    .cards-grid {
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(380px, 1fr));
      gap: 2rem;
    }

    .tarot-card-item {
      background: var(--bg-card);
      border: 1px solid rgba(198, 160, 82, 0.25);
      border-radius: 18px;
      padding: 1.5rem;
      display: flex;
      flex-direction: column;
      gap: 1.1rem;
      transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
      box-shadow: 0 10px 25px rgba(0, 0, 0, 0.5);
    }

    .tarot-card-item:hover {
      transform: translateY(-6px);
      border-color: var(--border-gold);
      background: var(--bg-card-hover);
      box-shadow: 0 15px 35px rgba(0, 0, 0, 0.7), 0 0 20px var(--gold-glow);
    }

    .card-top {
      display: flex;
      justify-content: space-between;
      align-items: flex-start;
      gap: 1rem;
    }

    .card-number-badge {
      font-family: var(--font-title);
      font-size: 1.1rem;
      font-weight: 900;
      color: var(--accent-gold);
      background: rgba(198, 160, 82, 0.12);
      border: 1px solid rgba(198, 160, 82, 0.3);
      width: 44px;
      height: 44px;
      display: flex;
      align-items: center;
      justify-content: center;
      border-radius: 10px;
      flex-shrink: 0;
    }

    .card-title-group { flex: 1; }
    .card-name-en {
      font-family: var(--font-title);
      font-size: 1.35rem;
      font-weight: 700;
      color: #fff;
    }

    .card-slug {
      font-size: 0.8rem;
      color: var(--text-muted);
      font-family: monospace;
    }

    .card-sample-preview {
      width: 100%;
      height: 240px;
      border-radius: 10px;
      object-fit: cover;
      border: 1px solid var(--border-gold);
    }

    .spec-box {
      background: rgba(0, 0, 0, 0.25);
      border-left: 3px solid var(--accent-gold);
      padding: 0.65rem 0.85rem;
      border-radius: 0 8px 8px 0;
      font-size: 0.84rem;
      color: #e5e7eb;
      line-height: 1.45;
    }

    .spec-item { margin-bottom: 0.25rem; }
    .spec-item strong { color: var(--accent-gold); }

    .prompt-block {
      background: #0d0f15;
      border: 1px solid rgba(255, 255, 255, 0.08);
      border-radius: 12px;
      padding: 0.85rem;
      margin-top: auto;
    }

    .prompt-header {
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 0.5rem;
    }

    .prompt-label {
      font-size: 0.8rem;
      font-weight: 700;
      text-transform: uppercase;
      color: var(--accent-gold);
      letter-spacing: 0.05em;
    }

    .copy-btn {
      background: rgba(198, 160, 82, 0.15);
      border: 1px solid var(--border-gold);
      color: #fce7b0;
      font-size: 0.78rem;
      font-weight: 600;
      padding: 0.3rem 0.75rem;
      border-radius: 6px;
      cursor: pointer;
      transition: all 0.2s;
    }

    .copy-btn:hover {
      background: var(--border-gold);
      color: #0b0c10;
    }

    .prompt-text {
      font-size: 0.8rem;
      color: #d1d5db;
      line-height: 1.45;
      max-height: 120px;
      overflow-y: auto;
      font-family: monospace;
      padding-right: 0.4rem;
      word-break: break-word;
    }

    #toast {
      position: fixed;
      bottom: 2rem;
      right: 2rem;
      background: linear-gradient(135deg, #10b981 0%, #059669 100%);
      color: white;
      padding: 0.85rem 1.5rem;
      border-radius: 10px;
      font-size: 0.92rem;
      font-weight: 600;
      opacity: 0;
      transform: translateY(20px);
      pointer-events: none;
      transition: all 0.3s ease;
      z-index: 1000;
    }

    #toast.show {
      opacity: 1;
      transform: translateY(0);
    }

    footer {
      border-top: 1px solid rgba(255, 255, 255, 0.08);
      padding: 2.5rem 1.5rem;
      text-align: center;
      color: var(--text-muted);
      font-size: 0.9rem;
    }
  </style>
</head>
<body>

  <header>
    <div class="header-badge">✨ Master Prompt Specification v2 • Capture3.PNG Edition</div>
    <h1>Sensual Manhwa Tarot 78 Cards</h1>
    <p class="header-desc">
      Hệ thống Master Prompt 78 lá bài Tarot chuẩn hóa 100% theo kiến trúc từ phiên làm việc trước: cấu trúc 4 lớp chiều sâu, Layout TOP/MIDDLE/BOTTOM, Title Lock, Count Lock 5 lớp chống đếm sai, và 72 bộ thông số nhân vật nữ quyến rũ.
    </p>

    <div class="controls">
      <input type="text" id="searchInput" class="search-input" placeholder="Tìm kiếm theo tên lá bài (ví dụ: Fool, Magician, Star, Wands, Cups...)...">
      <div class="filter-pills">
        <button class="filter-btn active" data-filter="all">Tất cả (78)</button>
        <button class="filter-btn" data-filter="major">Bộ Ẩn Chính (22)</button>
        <button class="filter-btn" data-filter="wands">Bộ Gậy 🔥 (14)</button>
        <button class="filter-btn" data-filter="cups">Bộ Cốc 💧 (14)</button>
        <button class="filter-btn" data-filter="swords">Bộ Kiếm ⚔️ (14)</button>
        <button class="filter-btn" data-filter="pentacles">Bộ Tiền 🪙 (14)</button>
      </div>
    </div>
  </header>

  <main>
    <div class="stats-bar">
      <span id="displayCount">Hiển thị: 78 / 78 lá bài</span>
      <span>Nhấp "Copy Master Prompt" để sử dụng ngay</span>
    </div>

    <div class="cards-grid" id="cardsGrid"></div>
  </main>

  <div id="toast">
    <span id="toastMsg">✓ Đã sao chép Master Prompt vào bộ nhớ tạm!</span>
  </div>

  <footer>
    <p>Master Prompt Specification v2 • Kế thừa kiến trúc chuẩn từ <code>tarot-new</code> và <code>tarot-card</code></p>
  </footer>

  <script>
    const cardsData = """ + json.dumps(cards_data['cards'], ensure_ascii=False) + """;

    const cardsGrid = document.getElementById('cardsGrid');
    const searchInput = document.getElementById('searchInput');
    const filterBtns = document.querySelectorAll('.filter-btn');
    const displayCount = document.getElementById('displayCount');
    const toast = document.getElementById('toast');
    const toastMsg = document.getElementById('toastMsg');

    let currentFilter = 'all';
    let currentSearch = '';

    function showToast(msg) {
      toastMsg.innerText = msg;
      toast.classList.add('show');
      setTimeout(() => { toast.classList.remove('show'); }, 2500);
    }

    function copyText(text, title) {
      navigator.clipboard.writeText(text).then(() => {
        showToast(`Đã sao chép Master Prompt lá "${title}"!`);
      }).catch(err => {
        const textarea = document.createElement('textarea');
        textarea.value = text;
        document.body.appendChild(textarea);
        textarea.select();
        document.execCommand('copy');
        document.body.removeChild(textarea);
        showToast(`Đã sao chép Master Prompt lá "${title}"!`);
      });
    }

    function renderCards() {
      const filtered = cardsData.filter(card => {
        const matchesFilter = currentFilter === 'all' || card.group === currentFilter;
        const matchesSearch = currentSearch === '' || 
          card.title.toLowerCase().includes(currentSearch.toLowerCase()) ||
          card.slug.toLowerCase().includes(currentSearch.toLowerCase()) ||
          card.n.toLowerCase().includes(currentSearch.toLowerCase()) ||
          card.scene.toLowerCase().includes(currentSearch.toLowerCase());
        return matchesFilter && matchesSearch;
      });

      displayCount.innerText = `Hiển thị: ${filtered.length} / 78 lá bài`;

      cardsGrid.innerHTML = filtered.map(card => `
        <div class="tarot-card-item">
          <div class="card-top">
            <div class="card-number-badge">${card.n}</div>
            <div class="card-title-group">
              <h2 class="card-name-en">${card.title}</h2>
              <div class="card-slug"><code>${card.slug}</code> • Emblem: ${card.emblem}</div>
            </div>
          </div>

          ${card.sample_img ? `<img src="${card.sample_img}" class="card-sample-preview" alt="${card.title}">` : ''}

          <div class="spec-box">
            <div class="spec-item"><strong>Scene:</strong> ${card.scene}</div>
            ${card.age !== 'N/A' ? `
              <div class="spec-item"><strong>Tuổi & Vóc dáng:</strong> ${card.age} • ${card.build}</div>
              <div class="spec-item"><strong>Tóc & Mắt:</strong> ${card.hair} • ${card.eyes}</div>
              <div class="spec-item"><strong>Da & Nét riêng:</strong> ${card.skin} • ${card.signature}</div>
            ` : ''}
            <div class="spec-item"><strong>Count Lock:</strong> ${card.count_lock.split('\\n')[0]}</div>
          </div>

          <div class="prompt-block">
            <div class="prompt-header">
              <span class="prompt-label">📜 Master Prompt (Chuẩn v2)</span>
              <button class="copy-btn" onclick="copyText(${JSON.stringify(card.master_prompt)}, '${card.title}')">📋 Copy</button>
            </div>
            <div class="prompt-text">${card.master_prompt}</div>
          </div>
        </div>
      `).join('');
    }

    filterBtns.forEach(btn => {
      btn.addEventListener('click', () => {
        filterBtns.forEach(b => b.classList.remove('active'));
        btn.classList.add('active');
        currentFilter = btn.getAttribute('data-filter');
        renderCards();
      });
    });

    searchInput.addEventListener('input', (e) => {
      currentSearch = e.target.value.trim();
      renderCards();
    });

    renderCards();
  </script>
</body>
</html>
"""

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html_template)

with open('tarot_viewer.html', 'w', encoding='utf-8') as f:
    f.write(html_template)

print("Updated index.html and tarot_viewer.html successfully!")
