import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('C:\\Users\\jin\\Desktop\\playdata\\video\\p0623\\img\\image.jpg')
pts1 = np.float32([[2820,2644],[2956,2372],[2156,2176],[2317,1909]])
pts2 = np.float32([[10,10],[10,1000],[1000,10],[1000,1000]])
# 이름표 뽑아내기
M = cv2.getPerspectiveTransform(pts1, pts2)
dst = cv2.warpPerspective(img, M, (1200,1200))
mid_result = cv2.resize(dst, dsize=(0,0), fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA)

# 이름 정확도 올리기
canny = cv2.Canny(mid_result, 89, 90)
ret, thresh = cv2.threshold(canny, 127, 255, 0)
c, h = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

result = cv2.drawContours(mid_result, c, -1, (0,255,0), 3)

plt.subplot(121),plt.imshow(mid_result),plt.title('mid_result')
plt.subplot(122),plt.imshow(result),plt.title('result')
plt.show()