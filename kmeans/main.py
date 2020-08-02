import numpy as np 
from PIL import Image

def kmeans_plus_plus(img, K):
    img = img.copy()
    h, w, _ = img.shape
    img = img.reshape(-1, 3)  # h * w colors. One pixel is represented by an (R,G,B)

    # Find initial centroids of K-means (kmeans++)
    c0_idx = np.random.randint(img.shape[0])
    centroids = [img[c0_idx]]  # initial centroid
    for i in range(K - 1):
        print(i)
        D = np.max(np.stack([np.sum((img - c)**2, axis=1) for c in centroids]), axis=0)
        p = D / np.sum(D)
        c_idx = np.random.choice(img.shape[0], p = p)
        centroids.append(img[c_idx])

    # Perform K-means
    error = np.inf
    while error > 1:
        D = np.stack([np.sum((img - c)**2, axis=1) for c in centroids])
        group = np.argmin(D, axis=0)
        new_centroids = []
        for i in range(K):
            pixel_indices = np.argwhere(group == i).ravel()
            colors = img[pixel_indices]
            c = np.mean(colors, axis=0)
            new_centroids.append(c)
        print(error)
        error = np.mean([np.sqrt(np.sum((new_c - c)**2)) for new_c, c in zip(new_centroids, centroids)])
        centroids = new_centroids
    # Assign colors
    D = np.stack([np.sum((img - c)**2, axis=1) for c in centroids])
    centroids = np.stack(centroids)
    group = np.argmin(D, axis=0)
    img = centroids[group].reshape(h, w, -1).astype(np.uint8)
    return img

if __name__ == "__main__":
    infile = '../data/town.png'
    img = np.array(Image.open(infile).convert('RGB')).astype(np.int)

    for K in [100]:
        print(K)
        img_q = kmeans_plus_plus(img, K)
        Image.fromarray(img_q).save('../results/kmeans/q_{}.png'.format(K))




