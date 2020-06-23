import cv2

src = cv2.imread("C:\\Users\\jin\\Desktop\\playdata\\video\\p0618\\img\\dad.jpg", cv2.IMREAD_COLOR)

dst = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)

cv2.imshow("src", src)
cv2.imshow("dst", dst)
cv2.waitKey(0)
cv2.destroyAllWindows()