import cv2
import sys

cascade_file = "C:\\Users\\jin\\Desktop\\playdata\\video\\opencv-master\\data\\haarcascades\\haarcascade_frontalface_default.xml"

cascade = cv2.CascadeClassifier(cascade_file)
me = cv2.imread("./img/me2.jpg")
crown = cv2.imread("./img/crown.jpg")
cw, ch, c = crown.shape
print(cw, ch, c)
face_list = cascade.detectMultiScale(me, scaleFactor=1.1, minNeighbors=1, minSize=(150, 150))

for face in face_list:
    x, y, w, h = face

roi = me[y-cw:y, x:x+ch]
crown_g = cv2.cvtColor(crown, cv2.COLOR_BGR2GRAY)
ret, mask = cv2.threshold(crown_g, 230, 255, cv2.THRESH_BINARY)
mask_inv = cv2.bitwise_not(mask)

crown_m = cv2.bitwise_and(crown, crown, mask=mask_inv)
me_m = cv2.bitwise_and(roi, roi, mask=mask)

dst = cv2.add(crown_m, me_m)

me[y-cw:y, x:x+ch] = dst

cv2.imshow('img', me)
cv2.waitKey(0)
cv2.destroyAllWindows()