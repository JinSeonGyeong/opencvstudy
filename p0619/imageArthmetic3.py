import cv2

img1 = cv2.imread('./img/star.jpg')
img2 = cv2.imread('./img/me.jpg')

w,h,c = img1.shape
print(w,h,c)

roi = img2[100:100+w, 100:100+h]

img1_g = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)

ret, mask = cv2.threshold(img1_g, 230, 255, cv2.THRESH_BINARY)

mask_inv = cv2.bitwise_not(mask)

#img_s 별모양
img_s = cv2.bitwise_and(img1, img1, mask=mask_inv)
#img_b 나
img_b = cv2.bitwise_and(roi, roi, mask=mask)

dst = cv2.add(img_s, img_b)

img2[100:100+w, 100:100+h] = dst

cv2.imshow('img', img2)
cv2.waitKey(0)
cv2.destroyAllWindows()