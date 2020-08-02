# color-quantization
> Color quantization zoo.

## Otsu's method - binarization
[Otsu's method](https://en.wikipedia.org/wiki/Otsu%27s_method) is an algorithm for color binarization.

|Colored|Otsu's method|Median threshold|
|--|--|--|
|![img](./data/town.png)|![img](./results/otsu/otsu.png)|![img](./results/otsu/median.png)|

## Median cut algorithm - quantization
[Median cut](https://en.wikipedia.org/wiki/Median_cut) is an algorithm for color quantization of images into 2<sup>n</sup> colors.

|Original|2 color|
|--|--|
|![img](./data/town.png)|![img](./results/median_cut/q_2.png)|
|4 color|8 color|
|![img](./results/median_cut/q_4.png)|![img](./results/median_cut/q_8.png)|
|16 color|32 color|
|![img](./results/median_cut/q_16.png)|![img](./results/median_cut/q_32.png)|
|64 color|128 color|
|![img](./results/median_cut/q_64.png)|![img](./results/median_cut/q_128.png)|

