import json

with open('tarot_cards_data.json', 'r', encoding='utf-8') as f:
    cards = json.load(f)

# Update the cards to reference the generated images for the 5 sample cards
sample_map = {
    "MA-01": "card_01_the_magician.png",
    "MA-02": "card_02_the_high_priestess.png",
    "MA-03": "card_03_the_empress.png",
    "MA-17": "card_04_the_star.png",
    "MA-15": "card_05_the_devil.png"
}

for c in cards:
    if c["id"] in sample_map:
        c["sample_img"] = sample_map[c["id"]]

with open('tarot_cards_data.json', 'w', encoding='utf-8') as f:
    json.dump(cards, f, ensure_ascii=False, indent=2)

html_template = """<!DOCTYPE html>
<html lang="vi">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>🔮 Manhwa Tarot Prompts Deck - 78 Lá Bài Tarot AI</title>
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
      --purple-glow: rgba(168, 85, 247, 0.3);
      --accent-purple: #a855f7;
      --accent-pink: #ec4899;
      --accent-gold: #fbbf24;
      --text-main: #f3f4f6;
      --text-muted: #9ca3af;
      --font-title: 'Cinzel', serif;
      --font-body: 'Plus Jakarta Sans', sans-serif;
    }

    * {
      box-sizing: border-box;
      margin: 0;
      padding: 0;
    }

    body {
      background-color: var(--bg-main);
      color: var(--text-main);
      font-family: var(--font-body);
      min-height: 100vh;
      background-image: 
        radial-gradient(circle at 15% 15%, rgba(168, 85, 247, 0.08) 0%, transparent 40%),
        radial-gradient(circle at 85% 85%, rgba(245, 158, 11, 0.06) 0%, transparent 40%),
        radial-gradient(circle at 50% 50%, rgba(236, 72, 153, 0.04) 0%, transparent 60%);
      background-attachment: fixed;
    }

    /* Header */
    header {
      padding: 2.5rem 1.5rem 1.75rem;
      text-align: center;
      border-bottom: 1px solid rgba(198, 160, 82, 0.2);
      background: linear-gradient(180deg, rgba(21, 24, 33, 0.92) 0%, rgba(11, 12, 16, 0.98) 100%);
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
      padding: 0.4rem 1.2rem;
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
      font-size: clamp(1.8rem, 4vw, 2.8rem);
      font-weight: 900;
      background: linear-gradient(135deg, #fff2c6 0%, #d4af37 50%, #aa7c11 100%);
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
      margin-bottom: 0.5rem;
      letter-spacing: 0.02em;
      text-shadow: 0 2px 20px rgba(212, 175, 55, 0.25);
    }

    .header-desc {
      color: var(--text-muted);
      max-width: 800px;
      margin: 0 auto 1.25rem;
      font-size: 0.95rem;
      line-height: 1.5;
    }

    /* Showcase Carousel of 5 generated sample cards */
    .showcase-section {
      max-width: 1300px;
      margin: 2rem auto;
      padding: 0 1.5rem;
    }

    .showcase-title {
      font-family: var(--font-title);
      font-size: 1.35rem;
      color: var(--accent-gold);
      text-align: center;
      margin-bottom: 1.25rem;
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 0.75rem;
    }

    .showcase-grid {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
      gap: 1.5rem;
      margin-bottom: 2.5rem;
    }

    .showcase-card {
      background: var(--bg-card);
      border: 2px solid rgba(198, 160, 82, 0.4);
      border-radius: 14px;
      overflow: hidden;
      box-shadow: 0 10px 25px rgba(0,0,0,0.6);
      transition: all 0.3s;
      display: flex;
      flex-direction: column;
    }

    .showcase-card:hover {
      transform: translateY(-8px) scale(1.02);
      border-color: var(--accent-gold);
      box-shadow: 0 15px 35px var(--gold-glow);
    }

    .showcase-img {
      width: 100%;
      height: 340px;
      object-fit: cover;
      display: block;
    }

    .showcase-caption {
      padding: 0.75rem 0.5rem;
      text-align: center;
      font-family: var(--font-title);
      font-size: 0.95rem;
      font-weight: 700;
      color: #fff;
      background: #11141c;
      border-top: 1px solid rgba(198, 160, 82, 0.2);
    }

    /* Controls & Filters */
    .controls {
      display: flex;
      flex-direction: column;
      align-items: center;
      gap: 1rem;
      max-width: 1200px;
      margin: 0 auto;
    }

    .search-box {
      width: 100%;
      max-width: 550px;
      position: relative;
    }

    .search-input {
      width: 100%;
      padding: 0.8rem 1.25rem 0.8rem 2.8rem;
      background: #1e2230;
      border: 1px solid rgba(198, 160, 82, 0.3);
      border-radius: 12px;
      color: white;
      font-size: 0.95rem;
      font-family: var(--font-body);
      outline: none;
      transition: all 0.3s;
    }

    .search-input:focus {
      border-color: var(--accent-gold);
      box-shadow: 0 0 15px var(--gold-glow);
      background: #232838;
    }

    .search-icon {
      position: absolute;
      left: 1rem;
      top: 50%;
      transform: translateY(-50%);
      color: var(--text-muted);
      pointer-events: none;
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
      padding: 0.5rem 1rem;
      border-radius: 9999px;
      font-size: 0.85rem;
      font-weight: 600;
      cursor: pointer;
      transition: all 0.2s;
      font-family: var(--font-body);
    }

    .filter-btn:hover {
      color: white;
      border-color: var(--border-gold);
      transform: translateY(-1px);
    }

    .filter-btn.active {
      background: linear-gradient(135deg, #c6a052 0%, #8b6b23 100%);
      color: #0b0c10;
      font-weight: 700;
      border-color: transparent;
      box-shadow: 0 4px 15px var(--gold-glow);
    }

    /* Main Container */
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
      padding-bottom: 0.75rem;
      border-bottom: 1px solid rgba(255, 255, 255, 0.06);
      font-size: 0.95rem;
      color: var(--text-muted);
    }

    .cards-grid {
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(360px, 1fr));
      gap: 2rem;
    }

    /* Tarot Card Design */
    .tarot-card-item {
      background: var(--bg-card);
      border: 1px solid rgba(198, 160, 82, 0.25);
      border-radius: 18px;
      padding: 1.5rem;
      display: flex;
      flex-direction: column;
      gap: 1.2rem;
      position: relative;
      overflow: hidden;
      transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
      box-shadow: 0 10px 25px rgba(0, 0, 0, 0.5);
    }

    .tarot-card-item::before {
      content: '';
      position: absolute;
      top: 0;
      left: 0;
      right: 0;
      height: 4px;
      background: linear-gradient(90deg, #c6a052, #a855f7, #ec4899);
      opacity: 0.7;
      transition: opacity 0.3s;
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

    .card-title-group {
      flex: 1;
    }

    .card-name-en {
      font-family: var(--font-title);
      font-size: 1.35rem;
      font-weight: 700;
      color: #fff;
      letter-spacing: 0.02em;
      margin-bottom: 0.2rem;
    }

    .card-name-vi {
      font-size: 0.95rem;
      color: #d1d5db;
      font-weight: 500;
    }

    .card-suit-tag {
      display: inline-block;
      font-size: 0.75rem;
      font-weight: 600;
      padding: 0.2rem 0.65rem;
      border-radius: 6px;
      text-transform: uppercase;
      letter-spacing: 0.04em;
      margin-top: 0.4rem;
    }

    .suit-Major { background: rgba(168, 85, 247, 0.2); color: #d8b4fe; border: 1px solid rgba(168, 85, 247, 0.4); }
    .suit-Wands { background: rgba(239, 68, 68, 0.2); color: #fca5a5; border: 1px solid rgba(239, 68, 68, 0.4); }
    .suit-Cups { background: rgba(59, 130, 246, 0.2); color: #93c5fd; border: 1px solid rgba(59, 130, 246, 0.4); }
    .suit-Swords { background: rgba(14, 165, 233, 0.2); color: #7dd3fc; border: 1px solid rgba(14, 165, 233, 0.4); }
    .suit-Pentacles { background: rgba(234, 179, 8, 0.2); color: #fde047; border: 1px solid rgba(234, 179, 8, 0.4); }

    .card-sample-preview {
      width: 100%;
      height: 240px;
      border-radius: 10px;
      object-fit: cover;
      border: 1px solid var(--border-gold);
      box-shadow: 0 4px 15px rgba(0,0,0,0.5);
    }

    .card-meaning {
      background: rgba(0, 0, 0, 0.25);
      border-left: 3px solid var(--accent-gold);
      padding: 0.65rem 0.85rem;
      border-radius: 0 8px 8px 0;
      font-size: 0.88rem;
      color: #e5e7eb;
      line-height: 1.45;
    }

    .card-concept {
      font-size: 0.88rem;
      color: #9ca3af;
      line-height: 1.5;
    }

    /* Prompt Boxes */
    .prompt-section {
      display: flex;
      flex-direction: column;
      gap: 0.85rem;
      margin-top: auto;
    }

    .prompt-block {
      background: #0d0f15;
      border: 1px solid rgba(255, 255, 255, 0.08);
      border-radius: 12px;
      padding: 0.85rem;
      position: relative;
    }

    .prompt-header {
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 0.5rem;
    }

    .prompt-label {
      font-size: 0.78rem;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.06em;
      display: flex;
      align-items: center;
      gap: 0.4rem;
    }

    .label-mj { color: #60a5fa; }
    .label-sd { color: #f472b6; }

    .copy-btn {
      background: rgba(255, 255, 255, 0.08);
      border: 1px solid rgba(255, 255, 255, 0.15);
      color: #e5e7eb;
      font-size: 0.75rem;
      font-weight: 600;
      padding: 0.25rem 0.65rem;
      border-radius: 6px;
      cursor: pointer;
      transition: all 0.2s;
      font-family: var(--font-body);
      display: flex;
      align-items: center;
      gap: 0.35rem;
    }

    .copy-btn:hover {
      background: var(--border-gold);
      color: #0b0c10;
      border-color: transparent;
      box-shadow: 0 0 10px var(--gold-glow);
    }

    .prompt-text {
      font-size: 0.82rem;
      color: #d1d5db;
      line-height: 1.45;
      max-height: 95px;
      overflow-y: auto;
      font-family: monospace;
      padding-right: 0.4rem;
      word-break: break-word;
    }

    /* Toast Notification */
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
      box-shadow: 0 10px 25px rgba(0, 0, 0, 0.5), 0 0 15px rgba(16, 185, 129, 0.4);
      display: flex;
      align-items: center;
      gap: 0.6rem;
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

    /* Footer */
    footer {
      border-top: 1px solid rgba(255, 255, 255, 0.08);
      padding: 2.5rem 1.5rem;
      text-align: center;
      color: var(--text-muted);
      font-size: 0.9rem;
      background: #090a0d;
    }
  </style>
</head>
<body>

  <!-- Header -->
  <header>
    <div class="header-badge">✨ Nguồn cảm hứng Manhwa: Capture3.PNG</div>
    <h1>Bộ Prompts 78 Lá Bài Tarot Manhwa</h1>
    <p class="header-desc">
      Hệ thống Prompt AI đầy đủ 78 lá bài Tarot (22 Ẩn chính + 56 Ẩn phụ) được tạo mẫu và thiết kế riêng theo phong cách Manhwa Webtoon quyến rũ, nét vẽ sắc sảo, bắt sáng rực rỡ từ hình mẫu <code>Capture3.PNG</code>.
    </p>

    <!-- Controls -->
    <div class="controls">
      <div class="search-box">
        <span class="search-icon">🔍</span>
        <input type="text" id="searchInput" class="search-input" placeholder="Tìm kiếm lá bài (ví dụ: The Magician, Priestess, Empress, Star, Devil, Cốc, Gậy...)...">
      </div>

      <div class="filter-pills">
        <button class="filter-btn active" data-filter="all">Tất cả (78)</button>
        <button class="filter-btn" data-filter="Major">Bộ Ẩn Chính (22)</button>
        <button class="filter-btn" data-filter="Wands">Bộ Gậy 🔥 (14)</button>
        <button class="filter-btn" data-filter="Cups">Bộ Cốc 💧 (14)</button>
        <button class="filter-btn" data-filter="Swords">Bộ Kiếm ⚔️ (14)</button>
        <button class="filter-btn" data-filter="Pentacles">Bộ Tiền 🪙 (14)</button>
      </div>
    </div>
  </header>

  <!-- Showcase section of 5 generated sample cards -->
  <section class="showcase-section">
    <div class="showcase-title">
      <span>🎴 5 LÁ BÀI MẪU ĐÃ RENDER HOÀN THIỆN</span>
    </div>
    <div class="showcase-grid">
      <div class="showcase-card">
        <img src="card_01_the_magician.png" alt="I. The Magician" class="showcase-img">
        <div class="showcase-caption">I. The Magician</div>
      </div>
      <div class="showcase-card">
        <img src="card_02_the_high_priestess.png" alt="II. The High Priestess" class="showcase-img">
        <div class="showcase-caption">II. The High Priestess</div>
      </div>
      <div class="showcase-card">
        <img src="card_03_the_empress.png" alt="III. The Empress" class="showcase-img">
        <div class="showcase-caption">III. The Empress</div>
      </div>
      <div class="showcase-card">
        <img src="card_04_the_star.png" alt="XVII. The Star" class="showcase-img">
        <div class="showcase-caption">XVII. The Star</div>
      </div>
      <div class="showcase-card">
        <img src="card_05_the_devil.png" alt="XV. The Devil" class="showcase-img">
        <div class="showcase-caption">XV. The Devil</div>
      </div>
    </div>
  </section>

  <!-- Main Content -->
  <main>
    <div class="stats-bar">
      <span id="displayCount">Hiển thị: 78 / 78 lá bài</span>
      <span>Tip: Nhấp "Copy" để lấy prompt dùng ngay cho Midjourney hoặc SD!</span>
    </div>

    <div class="cards-grid" id="cardsGrid">
      <!-- Cards will be populated by JS -->
    </div>
  </main>

  <!-- Toast -->
  <div id="toast">
    <span>✓</span>
    <span id="toastMsg">Đã sao chép prompt vào bộ nhớ tạm!</span>
  </div>

  <!-- Footer -->
  <footer>
    <p>Manhwa Tarot Prompt Engine • Thiết kế độc quyền dựa trên dữ liệu ảnh <code>Capture3.PNG</code></p>
  </footer>

  <script>
    const cardsData = """ + json.dumps(cards, ensure_ascii=False) + """;

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
      setTimeout(() => {
        toast.classList.remove('show');
      }, 2500);
    }

    function copyText(text, typeName) {
      navigator.clipboard.writeText(text).then(() => {
        showToast(`Đã sao chép prompt ${typeName}!`);
      }).catch(err => {
        const textarea = document.createElement('textarea');
        textarea.value = text;
        document.body.appendChild(textarea);
        textarea.select();
        document.execCommand('copy');
        document.body.removeChild(textarea);
        showToast(`Đã sao chép prompt ${typeName}!`);
      });
    }

    function renderCards() {
      const filtered = cardsData.filter(card => {
        const matchesFilter = currentFilter === 'all' || card.suit === currentFilter;
        const matchesSearch = currentSearch === '' || 
          card.name_en.toLowerCase().includes(currentSearch.toLowerCase()) ||
          card.name_vi.toLowerCase().includes(currentSearch.toLowerCase()) ||
          card.number.toLowerCase().includes(currentSearch.toLowerCase()) ||
          card.meaning.toLowerCase().includes(currentSearch.toLowerCase());
        return matchesFilter && matchesSearch;
      });

      displayCount.innerText = `Hiển thị: ${filtered.length} / 78 lá bài`;

      if (filtered.length === 0) {
        cardsGrid.innerHTML = `
          <div style="grid-column: 1/-1; text-align: center; padding: 4rem 1rem; color: #9ca3af;">
            <div style="font-size: 3rem; margin-bottom: 1rem;">🃏</div>
            <h3>Không tìm thấy lá bài phù hợp</h3>
            <p>Hãy thử tìm kiếm với từ khóa khác (ví dụ: Fool, Lovers, Cốc, Gậy, 10, King...)</p>
          </div>
        `;
        return;
      }

      cardsGrid.innerHTML = filtered.map(card => `
        <div class="tarot-card-item">
          <div class="card-top">
            <div class="card-number-badge">${card.number}</div>
            <div class="card-title-group">
              <h2 class="card-name-en">${card.name_en}</h2>
              <div class="card-name-vi">${card.name_vi}</div>
              <span class="card-suit-tag suit-${card.suit}">${card.suit === 'Major' ? 'Bộ Ẩn Chính' : 'Bộ ' + card.suit}</span>
            </div>
          </div>

          ${card.sample_img ? `<img src="${card.sample_img}" class="card-sample-preview" alt="${card.name_en}">` : ''}

          <div class="card-meaning">
            <strong>Ý nghĩa:</strong> ${card.meaning}
          </div>

          <div class="card-concept">
            <strong>Tạo hình:</strong> ${card.concept}
          </div>

          <div class="prompt-section">
            <div class="prompt-block">
              <div class="prompt-header">
                <span class="prompt-label label-mj">🚀 Midjourney Prompt</span>
                <button class="copy-btn" onclick="copyText(${JSON.stringify(card.prompt_mj)}, 'Midjourney')">📋 Copy</button>
              </div>
              <div class="prompt-text">${card.prompt_mj}</div>
            </div>

            <div class="prompt-block">
              <div class="prompt-header">
                <span class="prompt-label label-sd">🎨 Stable Diffusion / NovelAI</span>
                <button class="copy-btn" onclick="copyText(${JSON.stringify(card.prompt_sd)}, 'SD / NovelAI')">📋 Copy</button>
              </div>
              <div class="prompt-text">${card.prompt_sd}</div>
            </div>
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
