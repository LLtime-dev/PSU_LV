import numpy as np
import matplotlib.pyplot as plt

img = plt.imread("tiger.png")

# a) 
img_bright = np.clip(img * 1.5, 0, 1)

# b) 
img_rotated = np.rot90(img, k=-1)

# c) 
img_flipped = np.flip(img, axis=1)

# d) 
img_resized = img[::10, ::10]

# e) 
img_quarter = np.zeros_like(img)
sirina = img.shape[1]
img_quarter[:, sirina//4:sirina//2] = img[:, sirina//4:sirina//2]


fig, axes = plt.subplots(1, 6, figsize=(18, 3))


images = [img, img_bright, img_rotated, img_flipped, img_resized, img_quarter]
titles = ["Original", "Posvijetljena", "Rotirana 90°", "Zrcaljena", "Smanjena rezolucija", "Druga četvrtina"]

for ax, image, title in zip(axes, images, titles):
    ax.imshow(image, cmap="gray")
    ax.set_title(title)
    ax.axis('off') 

plt.tight_layout()
plt.show()

