import matplotlib.pyplot as plt
import numpy as np
from skimage.color import rgb2gray
from skimage.exposure import histogram
from skimage.io import imshow

# r = float(input('input R parameter: '))
r = 0.2125
# g = float(input('input G parameter: '))
g = 0.7154
# b = float(input('input B parameter: '))
b = 0.0721


original = plt.imread('lab1/cowboi.jpg')
grayscale = np.dot(original, [r, g, b])
# grayscale = rgb2gray(original)
grayscale = grayscale.astype(np.uint8)
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
hist_res, bin_res = histogram(grayscale)
plt.plot(bin_res, hist_res, color='black', linestyle='-', linewidth=1)

fig.tight_layout()
plt.show()
