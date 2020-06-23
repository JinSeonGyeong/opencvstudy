import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('C:\\Users\\jin\\Desktop\\playdata\\video\\p0623\\img\\dave.png')
canny = cv2.Canny(img,10,50)

laplacian = cv2.Laplacian(img,cv2.CV_16S)
sobelx = cv2.Sobel(img,cv2.CV_32F,1,0,ksize=3)
sobely = cv2.Sobel(img,cv2.CV_8U,0,1,ksize=3)

images = [img,laplacian, sobelx, sobely, canny]
titles = ['Origianl', 'Laplacian', 'Sobel X', 'Sobel Y','Canny']

for i in range(5):
    plt.subplot(2,3,i+1),plt.imshow(images[i]),plt.title([titles[i]])
    plt.xticks([]),plt.yticks([])

plt.show()