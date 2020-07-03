import sys
import cv2
import numpy as np
import os
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtGui import *

main_ui = uic.loadUiType('C:\\Users\\jin\\Desktop\\playdata\\video\\p0701_miniproject\\ui_file\\main.ui')[0]

class OptionWindow(QMainWindow):
    def __init__(self, parent):
        super(OptionWindow, self).__init__(parent) 
        uic.loadUi('C:\\Users\\jin\\Desktop\\playdata\\video\\p0701_miniproject\\ui_file\\image.ui', self)
        #self.pushButton.clicked.connect(self.previous)
        #self.pushButton_2.clicked.connect(self.next) 
        #self.initImage()
        self.show()
    
    def initImage(self):
        file_list = os.listdir(path)
        if len(file_list) == 0:
            QMessageBox.about(self.centralWidget, '알림', '사진이 없습니다.')
        else:
            filename = file_list[num].split('.')
            fileinput = path + '\\' + file_list[num]
            self.lbl = QLabel(self)
            self.lbl.resize(640, 480)
            pixmap = QPixmap(fileinput)
            self.lbl.setPixmap(QPixmap(pixmap))

    #def previous(self):


'''class OptionWindow2(QMainWindow):
    def __init__(self, parent):
        super(OptionWindow2, self).__init__(parent) 
        uic.loadUi('C:\\Users\\jin\\Desktop\\playdata\\video\\p0619\\ui_file\\list2.ui', self)

        self.show()'''

class MainWindow(QMainWindow, main_ui):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.cam = cv2.VideoCapture(0)

        self.pushButton.clicked.connect(self.capture)
        self.pushButton_2.clicked.connect(self.video_capture)
        self.pushButton_3.clicked.connect(self.image)

    def capture(self):
        if self.cam.isOpened() == False:
            QMessageBox.about(self.centralwidget, '알림', '카메라가 켜져있지 않습니다.')

        else:
            ret, frame = self.cam.read()
            frame = cv2.flip(frame, 1)
            c = cv2.imshow('c', frame)
            cv2.waitKey(0)
            cv2.destroyAllWindows()

    def video_capture(self):
        if self.cam.isOpened() == False:
            QMessageBox.about(self.centralwidget, '알림', '카메라가 켜져있지 않습니다.')

        width = self.cam.get(cv2.CAP_PROP_FRAME_WIDTH)
        height = self.cam.get(cv2.CAP_PROP_FRAME_HEIGHT)
        encode_param = [int(cv2.IMWRITE_JPEG_QUALITY), 90]
        cv2.namedWindow('CAM_Window')
        cv2.resizeWindow('CAM_Window', 640, 480)
        
        while True:
            ret, frame = self.cam.read()
            if ret:
                # 이미지 반전, 0:상하, 1:좌우
                frame = cv2.flip(frame, 1)
                cv2.imshow('CAM_Window', frame)
                if cv2.waitKey(1) >= 0:
                    break
            else:
                break
        cv2.destroyAllWindows()

    def image(self):
        OptionWindow(self)
            
if __name__ =="__main__":
    num = 0
    path = "C:\\Users\\jin\\Desktop\\playdata\\video\\p0701_miniproject\\capture_file"
    app = QApplication(sys.argv)
    main_dialog = MainWindow()
    main_dialog.show()
    app.exec_()

    