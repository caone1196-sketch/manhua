import json

with open('tarot_cards_data.json', 'r', encoding='utf-8') as f:
    cards = json.load(f)

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
      padding: 3rem 1.5rem 2rem;
      text-align: center;
      border-bottom: 1px solid rgba(198, 160, 82, 0.2);
      background: linear-gradient(180deg, rgba(21, 24, 33, 0.9) 0%, rgba(11, 12, 16, 0.95) 100%);
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
      margin-bottom: 1rem;
      box-shadow: 0 0 15px var(--gold-glow);
    }

    h1 {
      font-family: var(--font-title);
      font-size: clamp(1.8rem, 4vw, 3rem);
      font-weight: 900;
      background: linear-gradient(135deg, #fff2c6 0%, #d4af37 50%, #aa7c11 100%);
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
      margin-bottom: 0.75rem;
      letter-spacing: 0.02em;
      text-shadow: 0 2px 20px rgba(212, 175, 55, 0.25);
    }

    .header-desc {
      color: var(--text-muted);
      max-width: 800px;
      margin: 0 auto 1.5rem;
      font-size: 1rem;
      line-height: 1.6;
    }

    /* Style Reference Showcase */
    .style-ref-container {
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 1.5rem;
      background: rgba(30, 35, 48, 0.6);
      border: 1px solid rgba(198, 160, 82, 0.3);
      border-radius: 16px;
      padding: 1rem 1.5rem;
      max-width: 800px;
      margin: 0 auto 1.5rem;
      box-shadow: 0 8px 30px rgba(0, 0, 0, 0.4);
    }

    .style-ref-img {
      width: 70px;
      height: 70px;
      border-radius: 12px;
      object-fit: cover;
      border: 2px solid var(--border-gold);
      box-shadow: 0 0 12px var(--gold-glow);
    }

    .style-ref-info {
      text-align: left;
      font-size: 0.9rem;
    }

    .style-ref-title {
      font-weight: 700;
      color: var(--accent-gold);
      margin-bottom: 0.25rem;
    }

    /* Controls & Filters */
    .controls {
      display: flex;
      flex-direction: column;
      align-items: center;
      gap: 1.25rem;
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
      padding: 0.85rem 1.25rem 0.85rem 2.8rem;
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
      gap: 0.6rem;
    }

    .filter-btn {
      background: rgba(30, 35, 48, 0.8);
      color: var(--text-muted);
      border: 1px solid rgba(255, 255, 255, 0.08);
      padding: 0.55rem 1.1rem;
      border-radius: 9999px;
      font-size: 0.88rem;
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
      margin: 2.5rem auto;
      padding: 0 1.5rem 5rem;
    }

    .stats-bar {
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 2rem;
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
      gap: 1.25rem;
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

    .tarot-card-item:hover::before {
      opacity: 1;
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

    .prompt-text::-webkit-scrollbar {
      width: 4px;
    }
    .prompt-text::-webkit-scrollbar-thumb {
      background: rgba(255, 255, 255, 0.2);
      border-radius: 4px;
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

    @media (max-width: 640px) {
      .cards-grid {
        grid-template-columns: 1fr;
      }
      .style-ref-container {
        flex-direction: column;
        text-align: center;
      }
      .style-ref-info {
        text-align: center;
      }
    }
  </style>
</head>
<body>

  <!-- Header -->
  <header>
    <div class="header-badge">✨ Nguồn cảm hứng Manhwa: Capture3.PNG</div>
    <h1>Bộ Prompts 78 Lá Bài Tarot Manhwa</h1>
    <p class="header-desc">
      Hệ thống Prompt AI đầy đủ 78 lá bài Tarot (22 Ẩn chính + 56 Ẩn phụ) được thiết kế riêng theo phong cách Manhwa Webtoon quyến rũ, nét vẽ sắc sảo, bắt sáng rực rỡ từ hình mẫu <code>Capture3.PNG</code>.
    </p>

    <!-- Style Reference Card -->
    <div class="style-ref-container">
      <img src="Capture3_cropped_portrait.png" alt="Capture3 Source Crop" class="style-ref-img" onerror="this.src='Capture3.PNG'">
      <div class="style-ref-info">
        <div class="style-ref-title">🎨 Phân tích DNA phong cách từ Capture3:</div>
        <div>Tóc vàng óng, mắt eyeliner quyến rũ, má hồng, trang phục đan dây/ren gợi cảm, bóng đổ mềm mại, ánh sáng viền (rim lighting) và khung viền hoàng kim.</div>
      </div>
    </div>

    <!-- Controls -->
    <div class="controls">
      <div class="search-box">
        <span class="search-icon">🔍</span>
        <input type="text" id="searchInput" class="search-input" placeholder="Tìm kiếm lá bài (ví dụ: The Fool, Át Cốc, Queen, Gậy, Tiền...)...">
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
        // Fallback
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

          <div class="card-meaning">
            <strong>Ý nghĩa:</strong> ${card.meaning}
          </div>

          <div class="card-concept">
            <strong>Tạo hình:</strong> ${card.concept}
          </div>

          <div class="prompt-section">
            <!-- Midjourney Box -->
            <div class="prompt-block">
              <div class="prompt-header">
                <span class="prompt-label label-mj">🚀 Midjourney Prompt</span>
                <button class="copy-btn" onclick="copyText(${JSON.stringify(card.prompt_mj)}, 'Midjourney')">📋 Copy</button>
              </div>
              <div class="prompt-text">${card.prompt_mj}</div>
            </div>

            <!-- Stable Diffusion Box -->
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

    // Filter clicks
    filterBtns.forEach(btn => {
      btn.addEventListener('click', () => {
        filterBtns.forEach(b => b.classList.remove('active'));
        btn.classList.add('active');
        currentFilter = btn.getAttribute('data-filter');
        renderCards();
      });
    });

    // Search input
    searchInput.addEventListener('input', (e) => {
      currentSearch = e.target.value.trim();
      renderCards();
    });

    // Initial render
    renderCards();
  </script>
</body>
</html>
"""

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html_template)

with open('tarot_viewer.html', 'w', encoding='utf-8') as f:
    f.write(html_template)

print("Generated index.html and tarot_viewer.html successfully!")
