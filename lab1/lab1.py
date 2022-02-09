import matplotlib.pyplot as plt
import numpy as np

r = float(input('input R parameter: '))
g = float(input('input G parameter: '))
b = float(input('input B parameter: '))


original = plt.imread('lab1/cowboi.jpg')
grayscale = np.dot(original, [r, g, b])

plt.imsave('lab1/cowboi_polutone.jpg', grayscale)

fig, axes = plt.subplots(1, 2, figsize = (10, 5))
ax = axes.ravel()

ax[0].imshow(original)
ax[0].set_title("Original")
ax[1].imshow(grayscale)
ax[1].set_title("GrayscaleMine")

fig.tight_layout()
plt.show()
