import numpy as np 
from PIL import Image
from main import median_cut


def make_palette(infile, d = 1):
    img = np.array(Image.open(infile).convert('RGB'))

    _, colors = median_cut(img, d)
    colors = [c.reshape(1, 1, 3) for c in colors]
    colors = [np.tile(c, (100, 100, 1)) for c in colors]
    palette = np.concatenate(colors, axis=1)
    return palette

if __name__ == '__main__':
    infile = '../data/town.png'
    palette = make_palette(infile, d=2)
    Image.fromarray(palette).save('palette.png')