import cv2
import numpy as np
import random
from matplotlib import pyplot as plt

img = cv2.imread('C:\\Users\\jin\\Desktop\\playdata\\video\\p0624\\img\\imageHierarchy.jpg')

imgray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(imgray,125,255,0)

contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
contours2, hierarchy2 = cv2.findContours(thresh, cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)
contours3, hierarchy3 = cv2.findContours(thresh, cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
contours4, hierarchy4 = cv2.findContours(thresh, cv2.RETR_CCOMP,cv2.CHAIN_APPROX_SIMPLE)

for i in range(len(contours)):
    #각 Contour Line을 구분하기 위해서 Color Random생성
    b = random.randrange(1,255)
    g = random.randrange(1,255)
    r = random.randrange(1,255)

    cnt = contours[i]
    img = cv2.drawContours(img, [cnt], -1,(b,g,r), 2)

for i in range(len(contours2)):
    #각 Contour Line을 구분하기 위해서 Color Random생성
    b = random.randrange(1,255)
    g = random.randrange(1,255)
    r = random.randrange(1,255)

    cnt1 = contours2[i]
    img = cv2.drawContours(img, [cnt], -1,(b,g,r), 2)

for i in range(len(contours3)):
    #각 Contour Line을 구분하기 위해서 Color Random생성
    b = random.randrange(1,255)
    g = random.randrange(1,255)
    r = random.randrange(1,255)

    cnt2 = contours3[i]
    img = cv2.drawContours(img, [cnt], -1,(b,g,r), 2)

for i in range(len(contours4)):
    #각 Contour Line을 구분하기 위해서 Color Random생성
    b = random.randrange(1,255)
    g = random.randrange(1,255)
    r = random.randrange(1,255)

    cnt3 = contours4[i]
    img = cv2.drawContours(img, [cnt], -1,(b,g,r), 2)

titles = ['RETR_TREE', 'RETR_LIST', 'RETR_EXTERNAL', 'RETR_CCOMP']

for i in range(4):
    plt.subplot(2,2,i+1), plt.title(titles[i]), plt.imshow(img)
    plt.xticks([]), plt.yticks([])

plt.show()
