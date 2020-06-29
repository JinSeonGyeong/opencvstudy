#-*- coding:utf-8-*-
import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('C:\\Users\\jin\\Desktop\\playdata\\video\\img\\flower1.jpg')
hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

hist = cv2.calcHist([hsv],[0,1],None,[180,256],[0,180,0,256])

cv2.imshow('Hist',img)

plt.imshow(hist) #, interpolation='nearest')
plt.show()