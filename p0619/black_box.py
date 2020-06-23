import sys
import cv2
import numpy as np
import os
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtWidgets import QMessageBox

main_ui = uic.loadUiType('C:\\Users\\jin\\Desktop\\playdata\\video\\p0619\\ui_file\\blackbox.ui')[0]

class OptionWindow(QMainWindow):
    def __init__(self, parent):
        super(OptionWindow, self).__init__(parent) 
        uic.loadUi('C:\\Users\\jin\\Desktop\\playdata\\video\\p0619\\ui_file\\list.ui', self)

        self.show()

class OptionWindow2(QMainWindow):
    def __init__(self, parent):
        super(OptionWindow2, self).__init__(parent) 
        uic.loadUi('C:\\Users\\jin\\Desktop\\playdata\\video\\p0619\\ui_file\\list2.ui', self)

        self.show()

class MainWindow(QMainWindow, main_ui):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.pushButton.clicked.connect(self.clicked_option)
        self.pushButton_2.clicked.connect(self.clicked_option2)
        self.pushButton_3.clicked.connect(self.video_capture)

    def video_capture(self):
        cam = cv2.VideoCapture(0)
        if cam.isOpened() == False:
            QMessageBox.about(self.centralwidget, '알림', '카메라가 켜져있지 않습니다.')

        else:
            fourcc = cv2.VideoWriter_fourcc(*'DIVX')
            out = cv2.VideoWriter('output.avi', fourcc, 2500.0, (640,480))

            ret, frame = cam.read()

            if ret:
                # 이미지 반전, 0:상하, 1:좌우
                frame = cv2.flip(frame, 1)

                out.write(frame)

                cv2.imshow('frame', frame)

                if cv2.waitKey(0) & 0xFF == ord('q'):
                    break
            else:
                break

    def clicked_option(self):
        OptionWindow(self)

    def clicked_option2(self):
        OptionWindow2(self)

if __name__ =="__main__":
    app = QApplication(sys.argv)
    main_dialog = MainWindow()
    main_dialog.show()
    app.exec_()