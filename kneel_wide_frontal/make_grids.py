#!/usr/bin/env python3
"""Build the GRID_*.png contact sheets in this folder.

Usage:  python3 make_grids.py
Missing source images are skipped (with a placeholder in their cell), so the
script can be re-run as new renders land.
"""
from PIL import Image, ImageDraw, ImageFont
import os

HERE = os.path.dirname(os.path.abspath(__file__))
FONT = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
FONT_SM = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"

BG = (14, 12, 24)
BAR = (26, 22, 44)
FG = (226, 222, 245)
ACCENT = (178, 160, 255)


def font(path, size):
    return ImageFont.truetype(path, size)


def build(name, title, cells, columns, col_headers=None, cell_w=None):
    """cells: list of (filename, caption)."""
    if cell_w is None:
        cell_w = {1: 620, 2: 560, 3: 470, 4: 420, 5: 380, 6: 340}.get(columns, 340)
    gap = 16
    cap_h = 46
    head_h = 54 if col_headers else 0
    title_h = 78
    pad = 18

    cell_h = int(cell_w * 1360 / 784)
    rows = (len(cells) + columns - 1) // columns
    W = pad * 2 + columns * cell_w + (columns - 1) * gap
    H = title_h + head_h + rows * (cell_h + cap_h + gap) - gap + pad * 2

    sheet = Image.new("RGB", (W, H), BG)
    d = ImageDraw.Draw(sheet)
    ft = font(FONT, 40)
    fh = font(FONT, 26)
    fc = font(FONT_SM, 24)

    d.text((pad, 20), title, font=ft, fill=ACCENT)

    if col_headers:
        for c, head in enumerate(col_headers):
            x = pad + c * (cell_w + gap)
            d.rectangle([x, title_h, x + cell_w, title_h + head_h - 10], fill=BAR)
            bb = d.textbbox((0, 0), head, font=fh)
            d.text((x + (cell_w - (bb[2] - bb[0])) // 2, title_h + 8), head, font=fh, fill=FG)

    for i, (fname, caption) in enumerate(cells):
        r, c = divmod(i, columns)
        x = pad + c * (cell_w + gap)
        y = title_h + head_h + r * (cell_h + cap_h + gap)
        src = os.path.join(HERE, fname)
        if os.path.exists(src):
            im = Image.open(src).convert("RGB")
            im = im.resize((cell_w, cell_h), Image.LANCZOS)
            sheet.paste(im, (x, y))
        else:
            d.rectangle([x, y, x + cell_w, y + cell_h], fill=(30, 26, 48), outline=(70, 62, 100))
            bb = d.textbbox((0, 0), "pending", font=fh)
            d.text((x + (cell_w - (bb[2] - bb[0])) // 2, y + cell_h // 2), "pending", font=fh, fill=(120, 112, 150))
        d.rectangle([x, y + cell_h, x + cell_w, y + cell_h + cap_h - 4], fill=BAR)
        d.text((x + 10, y + cell_h + 10), caption, font=fc, fill=FG)

    out = os.path.join(HERE, name)
    sheet.save(out)
    print(f"{name}: {sheet.size} <- {[c[0] for c in cells]}")


build(
    "GRID_W01_W05.png",
    "SERIES W — quỳ 2 gối dạng rộng · chính diện · 2 bình",
    [(f"W0{i}_{s}.png", f"W0{i}  {label}") for i, (s, label) in enumerate([
        ("arms_straight_up", "2 tay thẳng lên"),
        ("wrists_crossed", "chéo cổ tay X"),
        ("one_high_one_low", "1 cao 1 thấp"),
        ("hands_cupped", "rót vào tay khum"),
        ("arms_wide_T", "2 tay chữ T"),
    ], start=1)],
    columns=5,
)

build(
    "GRID_SENSE.png",
    "SERIES S — ướt + hở tối đa trong giới hạn lọc",
    [(f"S{i}_{s}.png", f"S{i}  {label}") for i, (s, label) in enumerate([
        ("open_back", "trần lưng"),
        ("offshoulder_slit", "hở vai + xẻ"),
        ("hair_curtain", "tóc màn"),
        ("eyes_open_camera", "mắt mở"),
        ("one_knee_up", "1 gối nhô"),
    ], start=1)],
    columns=5,
)

build(
    "GRID_FRAMELESS.png",
    "SERIES F — frameless + cổ trễ (4 thế chính)",
    [("F1b_frameless_lowneck_frontal.png", "F1b  1 cao 1 thấp"),
     ("F2_frameless_plunge_bowed.png", "F2  đầu cúi"),
     ("F3_frameless_plunge_wrists_x.png", "F3  cổ tay X"),
     ("F4b_frameless_lowneck_rising.png", "F4b  1 gối nhô")],
    columns=4,
)

build(
    "GRID_FRAMELESS_ALL.png",
    "SERIES F — toàn bộ 6 bản frameless",
    [("F1b_frameless_lowneck_frontal.png", "F1b  1 cao 1 thấp"),
     ("F1c_frameless_both_streams_on_body.png", "F1c  2 dòng trúng người"),
     ("F2_frameless_plunge_bowed.png", "F2  đầu cúi"),
     ("F3_frameless_plunge_wrists_x.png", "F3  cổ tay X"),
     ("F4b_frameless_lowneck_rising.png", "F4b  1 gối nhô"),
     ("F5_frameless_symmetric_mirror.png", "F5  đối xứng gương")],
    columns=6,
)

build(
    "GRID_SIZE_A_vs_C.png",
    "SIZE A (slender) vs SIZE C (softly curvy) — mọi thứ khác giữ nguyên",
    [("F5_frameless_symmetric_mirror.png", "A · đối xứng gương"),
     ("T1_C_build_symmetric.png", "C · đối xứng gương"),
     ("F1b_frameless_lowneck_frontal.png", "A · 1 cao 1 thấp"),
     ("T2_C_build_one_high_low.png", "C · 1 cao 1 thấp")],
    columns=2,
    col_headers=["SIZE A — slender / willowy", "SIZE C — softly curvy"],
    cell_w=560,
)
