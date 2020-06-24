from PIL import Image
from pytesseract import *
import cv2
import numpy as np

img = cv2.imread("C:\\Users\\jin\\Desktop\\playdata\\video\\p0624\\img\\hangul.jpg")
text = image_to_string(img, lang="kor", config='--psm 1 -c preserve_interword_spaces=1')
print(text)
cv2.imshow("result", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
