import cv2
import numpy as np
from matplotlib import pyplot as plt
from PIL import Image
from pytesseract import *

img = cv2.imread('C:\\Users\\jin\\Desktop\\playdata\\video\\p0624\\img\\car.jpg')
height, width, channel = img.shape
dst = img.copy()
#이미지 잘라내기
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
blur = cv2.bilateralFilter(gray, 9, 120, 30)
img_thresh = cv2.adaptiveThreshold(
    blur, 
    maxValue=255.0, 
    adaptiveMethod=cv2.ADAPTIVE_THRESH_GAUSSIAN_C, 
    thresholdType=cv2.THRESH_BINARY_INV, 
    blockSize=19, 
    C=9
)
contours, hierachy = cv2.findContours(img_thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

temp_result = np.zeros((height, width, channel), dtype=np.uint8)

cv2.drawContours(temp_result, contours=contours, contourIdx=-1, 
                 color=(255, 255, 255))

temp_result = np.zeros((height, width, channel), dtype=np.uint8)

contours_dict = []
for contour in contours:
    x, y, w, h = cv2.boundingRect(contour)
    cv2.rectangle(temp_result, pt1=(x, y), pt2=(x+w, y+h), 
                  color=(255, 255, 255), thickness=2)
     
    contours_dict.append({
        'contour': contour,
        'x': x,
        'y': y,
        'w': w,
        'h': h,
        'cx': x + (w / 2),
        'cy': y + (h / 2)
    })
#print(contours_dict)


#text = image_to_string(img_thresh, lang="kor")
#print(text)
titles = ['Original','Result', 'Blur', 'img_thresh']
images = [img, temp_result, blur, img_thresh]

for i in range(4):
    plt.subplot(1,4,i+1), plt.title(titles[i]), plt.imshow(images[i])
    plt.xticks([]), plt.yticks([])

plt.show()