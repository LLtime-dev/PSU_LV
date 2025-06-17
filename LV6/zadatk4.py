import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from sklearn.cluster import KMeans


imageNew = mpimg.imread('C:/Users/student/Desktop/LV6_ciki/example_grayscale.png')


if len(imageNew.shape) == 2:  
    
    imageNew = np.stack([imageNew] * 3, axis=-1)


image_reshaped = imageNew.reshape((-1, 3))


k = 10  
kmeans = KMeans(n_clusters=k, n_init=1, random_state=42)
kmeans.fit(image_reshaped)


cluster_centers = kmeans.cluster_centers_.astype(int)


quantized_image = cluster_centers[kmeans.labels_].reshape(imageNew.shape)


plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
plt.imshow(imageNew)
plt.title("Original Image")

plt.subplot(1, 2, 2)
plt.imshow(quantized_image)
plt.title(f"Quantized Image (k={k})")

plt.show()


original_size = imageNew.size * imageNew.itemsize  # in bytes
quantized_size = k * image_reshaped.shape[0] * image_reshaped.itemsize  # in bytes
compression_ratio = original_size / quantized_size

print(f"Compression achieved with {k} clusters: {compression_ratio:.2f}x")