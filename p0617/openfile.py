import cv2
import numpy

fn = 'a.png'
img = cv2.imread(fn, cv2.IMREAD_COLOR)
#print(img.shape)
cv2.imshow('a', img)
cv2.waitKey(0)
cv2.destroyAllWindows()