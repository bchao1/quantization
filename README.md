# color-quantization
> Color quantization zoo.

This is a repository for exploring various color quantization methods. Algorithm implementations are in `src/`, with great help from `numpy`.

## Table of Contents
- Otsu's Method
- Median Cut
- Kmeans++
- Octree
- Floyd-Steinberg Dithering

## Otsu's method - binarization
[Otsu's method](https://en.wikipedia.org/wiki/Otsu%27s_method) is an algorithm for color binarization. See `src/otsu/`.

|Colored|Otsu's method|Median threshold|
|--|--|--|
|![img](./data/town.png)|![img](./results/otsu/otsu.png)|![img](./results/otsu/median.png)|

## Median cut - quantization
[Median cut](https://en.wikipedia.org/wiki/Median_cut) is an algorithm for color quantization of images into 2<sup>n</sup> colors. See `src/median_cut/`.

|Original|2 color|
|--|--|
|![img](./data/town.png)|![img](./results/median_cut/q_2.png)|
|4 color|8 color|
|![img](./results/median_cut/q_4.png)|![img](./results/median_cut/q_8.png)|
|16 color|32 color|
|![img](./results/median_cut/q_16.png)|![img](./results/median_cut/q_32.png)|
|64 color|128 color|
|![img](./results/median_cut/q_64.png)|![img](./results/median_cut/q_128.png)|

## K-means++ - quantization
[K-means++](https://en.wikipedia.org/wiki/K-means%2B%2B) is an improved K-means algorithm with better initialization. Initializing with sparser centroids (though more computationally expensive) can lead to faster convergence. Note that this algorithm can quantize an image to arbitrary number of colors. See `src/kmeans/`.

|Original|2 color|
|--|--|
|![img](./data/town.png)|![img](./results/kmeans/q_2.png)|
|3 color|5 color|
|![img](./results/kmeans/q_3.png)|![img](./results/kmeans/q_5.png)|
|10 color|20 color|
|![img](./results/kmeans/q_10.png)|![img](./results/kmeans/q_20.png)|
|50 color|100 color|
|![img](./results/kmeans/q_50.png)|![img](./results/kmeans/q_100.png)|

## Octree - quantization
[Octrees](https://en.wikipedia.org/wiki/Octree) are trees which each node has (at most) eight children. It is an effective data structure for partitioning 3-dimensional spaces. A great post on octree implementations (in JavaScript) for color quantization can be found [here](https://observablehq.com/@tmcw/octree-color-quantization).

## Floyd-Steinberg Dithering
[Dither](https://en.wikipedia.org/wiki/Dither) is an intentionally applied form of noise used to randomize quantization error, preventing large-scale patterns such as color banding in images. See `src/dithering/`.

|Original|64-colored|Dithered|
|--|--|--|
|![img](./data/town.png)|![img](results/median_cut/q_64.png)|![img](./results/dither.png)|