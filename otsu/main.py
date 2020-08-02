import numpy as np 
import collections
from PIL import Image
import matplotlib.pyplot as plt

def otsu(infile):
    I = np.array(Image.open(infile).convert('L'))  # color intensity

    pixels, counts = np.unique(I.ravel(), return_counts = True)  # count pixel value occurences

    hist = np.zeros(256)
    hist[pixels] = counts  # color histogram

    total_pixels = I.size  # number of pixels in the image
    total_pixels_weighted = np.dot(np.arange(256), hist)  # sum of pixel values weighted by their occurence

    w0 = 0  # w1 = total_pixels_weighted - w0
    w0_sum = 0
    max_sigma = -np.inf
    thresh = 0

    for p, cnt in enumerate(hist):
        w1 = total_pixels - w0
        if w0 > 0 and w1 > 0:
            w1_sum = total_pixels_weighted - w0_sum
            mu0 = w0_sum / w0 
            mu1 = w1_sum / w1
            new_sigma = w0 * w1 * ((mu0 - mu1)**2)
            if new_sigma > max_sigma:
                thresh = p
                max_sigma = new_sigma
        w0 += cnt
        w0_sum += (p * cnt)


    mask_ostu = (I > thresh).astype(np.int)
    B_otsu = (255 * mask_ostu).astype(np.uint8)

    return B_otsu



