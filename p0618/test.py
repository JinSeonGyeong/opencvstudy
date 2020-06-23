import cv2

CAM_ID = 0

cam = cv2.VideoCapture(CAM_ID)
if cam.isOpened() == False:
    print(f'Can`t open the CAM{CAM_ID}')
    exit()

width = cam.get(cv2.CAP_PROP_FRAME_WIDTH)
height = cam.get(cv2.CAP_PROP_FRAME_HEIGHT)

cv2.namedWindow('CAM_Window')
cv2.resizeWindow('CAM_Window', 1280, 720)

while(True):
    ret, frame = cam.read()
    cv2.imshow('CAM_Window', frame)

    if cv2.waitKey(1000) >= 0:
        break
cam.release()
cam.destroyWindow('CAM_Window')