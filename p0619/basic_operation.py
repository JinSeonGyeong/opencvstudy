import cv2

img1 = cv2.imread('C:\\Users\\jin\\Desktop\\playdata\\video\\img\\star.jpg')
img2 = cv2.imread('C:\\Users\\jin\\Desktop\\playdata\\video\\img\\basketball.jpg')

w,h,c = img1.shape
print(w,h,c)

img2[100:100+w, 100:100+h] = img1

cv2.imshow('img', img2)
cv2.waitKey(0)
cv2.destroyAllWindows()