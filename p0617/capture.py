import cv2
import numpy

capture = cv2.VideoCapture(0)
ret,frame = capture.read()

#print(frame.shape)
c = cv2.imshow('c', frame)
cv2.imwrite('c.png', frame)
cv2.waitKey(0)
cv2.destroyAllWindows()