import numpy as np 
from PIL import Image

infile = '../data/town.png'
img = np.array(Image.open(infile).convert('RGB'))

img = img.reshape(-1, 3)
colors = 
print(img.shape)