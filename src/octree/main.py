import numpy as np 
from PIL import Image
from octree import Octree

infile = '../../data/town.png'
img = np.array(Image.open(infile).convert('RGB'))

img = img.reshape(-1, 3)

octree = Octree()
for c in img:
    octree.insert(c)
    