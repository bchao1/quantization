# color-quantization
> Color quantization zoo.

## Otsu's method - binarization
[Otsu's method](https://en.wikipedia.org/wiki/Otsu%27s_method) is an algorithm for color binarization. See `otsu/`.

|Colored|Otsu's method|Median threshold|
|--|--|--|
|![img](./data/town.png)|![img](./results/otsu/otsu.png)|![img](./results/otsu/median.png)|

## Median cut - quantization
[Median cut](https://en.wikipedia.org/wiki/Median_cut) is an algorithm for color quantization of images into 2<sup>n</sup> colors. See `median_cut/`.

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
[K-means++](https://en.wikipedia.org/wiki/K-means%2B%2B) is an improved K-means algorithm with better initialization. Initializing with sparser centroids (though more computationally expensive) can lead to faster convergence. See `kmeans/`.

|Original|2 color|
|--|--|
|![img](./data/town.png)|![img](./results/kmeans/q_2.png)|
|5 color|10 color|
|![img](./results/kmeans/q_5.png)|![img](./results/kmeans/q_10.png)|
|20 color|50 color|
|![img](./results/kmeans/q_20.png)|![img](./results/kmeans/q_50.png)|
|100 color||
|![img](./results/kmeans/q_100.png)||

## Octree - quantization