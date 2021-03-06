import cv2
from matplotlib import pyplot as plt

img = cv2.imread('a.png', cv2.IMREAD_COLOR)

b, g, r = cv2.split(img)
img2 = cv2.merge([r,g,b])

plt.imshow(img2)
plt.xticks([])
plt.yticks([])
plt.show()