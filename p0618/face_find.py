import cv2
import sys

cascade_file = "C:\\Users\\jin\\Desktop\\playdata\\video\\opencv-master\\data\\haarcascades\\haarcascade_frontalface_default.xml"

image = cv2.imread("C:\\Users\\jin\\Desktop\\playdata\\video\\img\\me2.jpg")

image_gs = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

cascade = cv2.CascadeClassifier(cascade_file)
print(cascade)

face_list = cascade.detectMultiScale(image, scaleFactor=1.1, minNeighbors=1, minSize=(150, 150))

if len(face_list) > 0:
    print(face_list)
    color = (0,0,255)
    for face in face_list:
        x, y, w, h = face
        cv2.rectangle(image, (x, y), (x+w, y+h), color, thickness = 8)

    cv2.imshow('img', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("no face")