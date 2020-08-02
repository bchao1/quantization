import sys
sys.path.append('..')
from median_cut.main import median_cut
import numpy as np 
from PIL import Image

def floyd_steinberg_dither(img, quantized_img):
    h, w, _ = img.shape
    error = img - quantized_img
    dithered_img = np.zeros(img.shape)
    for y in range(h):
        for x in range(w):
            e = error[y, x, :]
            dithered_img[y, x, :] = quantized_img[y, x, :]
            dithered_img[y, min(x+1, w-1), :] += 7 * e / 16
            dithered_img[min(y+1, h-1), max(x-1, 0), :] += 3 * e / 16
            dithered_img[min(y+1, h-1), x, :] += 5 * e / 16
            dithered_img[min(y+1, h-1), min(x+1, w-1), :] += 1 * e / 16
    return dithered_img.astype(np.uint8)

infile = '../../data/town.png'
img = np.array(Image.open(infile).convert('RGB'))
q_img, _ = median_cut(img, 5)
d_img = floyd_steinberg_dither(img, q_img)
Image.fromarray(d_img).save('test.png')

