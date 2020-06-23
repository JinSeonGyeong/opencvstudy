import cv2
import numpy as numpy

img = cv2.imread('C:\\Users\\jin\\Desktop\\playdata\\video\\p0623\\img\\logo.png')

height, width = img.shape[:2]

shrink = cv2.resize(img, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA)

zoom1 = cv2.resize(img, (width*2, height*2), interpolation=cv2.INTER_CUBIC)

zoom2 = cv2.resize(img, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)

cv2.imshow('Original', img)
cv2.imshow('Shrink', shrink)
cv2.imshow('Zoom1', zoom1)
cv2.imshow('Zoom2', zoom2)

cv2.waitKey(0)
cv2.destroyAllWindows()