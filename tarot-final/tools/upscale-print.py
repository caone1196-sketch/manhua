#!/usr/bin/env python3
"""
upscale-print.py — AI upscale pipeline cho bản in Tarot (locked 3:4, 3072x4096 @300DPI)

Quy trình:
  1. LapSRN x4 AI (chia tile 2x3, overlap 32px chống seam) -> gấp 4 độ phân giải thật
  2. ImageMagick resize chính xác kích thước in + sharpen + gắn metadata 300 DPI

Yêu cầu:
  pip install opencv-contrib-python-headless
  (nếu pip bị chặn PEP 668: thêm --break-system-packages)

Model .pb nằm cạnh script trong ./models/ (LapSRN_x4.pb từ github.com/fannymonori/TF-LapSRN)

Dùng:
  python3 upscale-print.py INPUT.png OUTPUT.png [--width 3072] [--height 4096] [--sharp 0x0.8+1.5+0.003]
"""
import sys, os, argparse, subprocess
import cv2, numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
MODEL = os.path.join(HERE, "models", "LapSRN_x4.pb")

def lapsrn_x4(img):
    """Upscale 4x bằng LapSRN, chia tile để không tràn RAM."""
    H, W = img.shape[:2]
    S, ov = 4, 32
    cols, rows = (2 if W > 600 else 1), (3 if H > 1000 else 2)
    sr = cv2.dnn_superres.DnnSuperResImpl_create()
    sr.readModel(MODEL); sr.setModel("lapsrn", S)
    out = np.zeros((H*S, W*S, 3), np.uint8)
    tw, th = (W + cols - 1)//cols, (H + rows - 1)//rows
    for r in range(rows):
        for c in range(cols):
            ex0, ex1 = c*tw, ((c+1)*tw if c < cols-1 else W)
            ey0, ey1 = r*th, ((r+1)*th if r < rows-1 else H)
            px0, px1 = max(0, ex0-ov), min(W, ex1+ov)
            py0, py1 = max(0, ey0-ov), min(H, ey1+ov)
            up = sr.upsample(img[py0:py1, px0:px1])
            t, b = (ey0-py0)*S, (py1-ey1)*S
            l, ri = (ex0-px0)*S, (px1-ex1)*S
            out[ey0*S:ey1*S, ex0*S:ex1*S] = up[t:up.shape[0]-b, l:up.shape[1]-ri]
    return out

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("input"); ap.add_argument("output")
    ap.add_argument("--width", type=int, default=3072)
    ap.add_argument("--height", type=int, default=4096)
    ap.add_argument("--sharp", default="0x0.8+1.5+0.003",
                    help="unsharp kích thước in: 0x0.8+1.5+0.003 = max chi tiết; 0x0.6+0.9+0.005 = mịn sạch")
    a = ap.parse_args()
    img = cv2.imread(a.input)
    assert img is not None, f"Đọc được file? {a.input}"
    print(f"[1/3] AI upscale x4 (LapSRN) từ {img.shape[1]}x{img.shape[0]} ...")
    up = lapsrn_x4(img)
    tmp = a.output + ".tmp.png"
    cv2.imwrite(tmp, up)
    print(f"[2/3] Resize in {a.width}x{a.height} + sharpen {a.sharp} + 300DPI ...")
    subprocess.run(["convert", tmp, "-resize", f"{a.width}x{a.height}!",
                    "-unsharp", a.sharp, "-units", "PixelsPerInch",
                    "-density", "300", a.output], check=True)
    os.remove(tmp)
    print(f"[3/3] Xong -> {a.output}")

if __name__ == "__main__":
    main()
