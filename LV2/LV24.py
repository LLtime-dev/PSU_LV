import numpy as np
import matplotlib.pyplot as plt

size = 50
rows = 4
cols = 5

B = np.zeros((size, size), dtype=np.uint8)
W = np.ones((size, size), dtype=np.uint8) * 255
rowA = np.hstack((B, W) * ((cols+1)//2))[:, :cols*size]
rowB = np.hstack((W, B) * ((cols+1)//2))[:, :cols*size]
img = np.vstack((rowA, rowB) * ((rows+1)//2))[:rows*size, :]

plt.imshow(img, cmap='gray', vmin=0, vmax=255)
plt.show()
