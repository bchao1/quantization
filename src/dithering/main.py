import sys
sys.path.append('..')
from median_cut.main import median_cut
import numpy as np 
from PIL import Image

def floyd_steinberg_dither(img, palette):
    h, w, _ = img.shape
    img = img.copy().astype(np.float64)
    print(palette.shape)
    for y in range(h):
        for x in range(w):
            old = img[y, x, :]
            new = palette[np.argmin(np.sum((palette - old)**2, axis=1))]
            err = old - new
            img[y, x, :] = new
            img[y, min(x+1, w-1), :] += 7 * err / 16
            img[min(y+1, h-1), max(x-1, 0), :] += 3 * err / 16
            img[min(y+1, h-1), x, :] += 5 * err / 16
            img[min(y+1, h-1), min(x+1, w-1), :] += 1 * err / 16
    img = img.astype(np.uint8)
    return img


if __name__ == "__main__":
    infile = '../../data/town.png'
    img = np.array(Image.open(infile).convert('RGB'))

    _ , palette = median_cut(img, 6)
    palette = np.stack(palette)
    d_img = floyd_steinberg_dither(img, palette)
    Image.fromarray(d_img).save('../../results/dither.png')

