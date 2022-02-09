import matplotlib.pyplot as plt
import numpy as np
from skimage.exposure import histogram
from skimage.io import imshow

r = float(input('input R parameter: '))
g = float(input('input G parameter: '))
b = float(input('input B parameter: '))


original = plt.imread('lab1/cowboi.jpg')
grayscale = np.dot(original, [r, g, b])

plt.imsave('lab1/cowboi_polutone.jpg', grayscale)

fig = plt.figure()
fig.add_subplot(2,2,1)
imshow(original)
fig.add_subplot(2,2,2)
imshow(grayscale)
fig.add_subplot(2,2,3)
hist_red, bins_red = histogram(original[:, :, 2])
hist_green, bins_green = histogram(original[:, :, 1])
hist_blue, bins_blue = histogram(original[:, :, 0])
plt.plot(bins_green, hist_green, color='green', linestyle='-', linewidth=1)
plt.plot(bins_red, hist_red, color='red', linestyle='-', linewidth=1)
plt.plot(bins_blue, hist_blue, color='blue', linestyle='-', linewidth=1)
fig.add_subplot(2,2,4)
hist_red, bins_red = histogram(grayscale[:, 2])
hist_green, bins_green = histogram(grayscale[:, 1])
hist_blue, bins_blue = histogram(grayscale[:, 0])
plt.plot(bins_green, hist_green, color='green', linestyle='-', linewidth=1)
plt.plot(bins_red, hist_red, color='red', linestyle='-', linewidth=1)
plt.plot(bins_blue, hist_blue, color='blue', linestyle='-', linewidth=1)

fig.tight_layout()
plt.show()
