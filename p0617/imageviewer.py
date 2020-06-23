import cv2
import numpy
import os

def view(num):
    filename = file_list[num].split('.')
    fileinput = path + '\\' + file_list[num]
    img = cv2.imread(fileinput, cv2.IMREAD_COLOR)
    img = cv2.resize(img, dsize=(640, 480), interpolation=cv2.INTER_AREA)
    cv2.imshow(filename[0], img)

def capture():
    capture = cv2.VideoCapture(0)
    ret,frame = capture.read()
    cv2.imshow('a', frame)
    fm.append(frame)
    cv2.waitKey(0)

def imgsave():
    filename2 = input("filename? :")
    cv2.imwrite(f'C:\\Users\\jin\\Desktop\\playdata\\video\\p0617\\img\\{filename2}.png', fm[0])
    cv2.waitKey(0)

if __name__ == "__main__":
    num = 0
    fm = []
    path = "C:\\Users\\jin\\Desktop\\playdata\\video\\p0617\\img"
    file_list = os.listdir(path)
    if len(file_list) == 0:
        print("이미지 파일이 없습니다.")
    else:
        print("파일 갯수: ", len(file_list))
        view(num)
        cmd = cv2.waitKey(0)
        while True: 
            if cmd & 0xFF == "q":    
                if num >= 1:
                    num = num - 1
                    view(num)
            elif cmd & 0xFF == "n":
                if num == len(file_list)-1:
                    print("마지막 이미지 입니다.")
                else:
                    num = num + 1
                    view(num)
            elif cmd & 0xFF == "c":
                capture()
            elif cmd & 0xFF == "s":
                if len(fm) == 0:
                    print('저장할 사진이 없습니다.')
                else:
                    imgsave()
                    frame = 0
            elif cmd & 0xFF == "q":
                exit()
    cv2.destroyAllWindows()