# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'crown.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

import cv2
import numpy as np
import os
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("faceApp")
        MainWindow.resize(200, 150)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 0, 0, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 1, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 200, 82))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.pushButton.clicked.connect(self.preview)
        self.pushButton_2.clicked.connect(self.face_crown)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "faceApp"))
        self.pushButton.setText(_translate("MainWindow", "촬영"))
        self.pushButton_2.setText(_translate("MainWindow", "왕관"))
  
    def preview(self):
        cam = cv2.VideoCapture(0)
        if cam.isOpened() == False:
            QMessageBox.about(self.centralwidget, '알림', '카메라가 켜져있지 않습니다.')

        width = cam.get(cv2.CAP_PROP_FRAME_WIDTH)
        height = cam.get(cv2.CAP_PROP_FRAME_HEIGHT)
        cv2.namedWindow('CAM_Window')
        cv2.resizeWindow('CAM_Window', 640, 400)
        
        while True:
            ret, frame = cam.read()
            frame_gs = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            face_list = cascade.detectMultiScale(frame, scaleFactor=1.1, minNeighbors=1, minSize=(150, 150))
            color = (0,0,255)
            if len(face_list) > 0:
                for face in face_list:
                    x, y, w, h = face
                cv2.rectangle(frame, (x, y), (x+w, y+h), color, thickness = 8)
                if ret:
                    # 이미지 반전, 0:상하, 1:좌우
                    frame = cv2.flip(frame, 1)
                    cv2.imshow('CAM_Window', frame)
                    if cv2.waitKey(1) &0xFF == 27:
                        break
                else:
                    break
            else:
                if ret:
                    # 이미지 반전, 0:상하, 1:좌우
                    frame = cv2.flip(frame, 1)
                    cv2.imshow('CAM_Window', frame)
                    if cv2.waitKey(1) &0xFF == 27:
                        break
                else:
                    break
        cv2.destroyAllWindows()

    def face_crown(self):
        cam = cv2.VideoCapture(0)
        if cam.isOpened() == False:
            QMessageBox.about(self.centralwidget, '알림', '카메라가 켜져있지 않습니다.')

        width = cam.get(cv2.CAP_PROP_FRAME_WIDTH)
        height = cam.get(cv2.CAP_PROP_FRAME_HEIGHT)
        cv2.namedWindow('CAM_Window')
        cv2.resizeWindow('CAM_Window', 640, 400)
        
        crown = cv2.imread("./img/crown.jpg")
        cw, ch, c = crown.shape
        while True:
            ret, frame = cam.read()
            frame_gs = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            face_list = cascade.detectMultiScale(frame, scaleFactor=1.1, minNeighbors=1, minSize=(150, 150))
            for face in face_list:
                x, y, w, h = face
            
            if len(face_list) > 0:
                roi = frame[y-cw:y, x:x+ch]
                crown_g = cv2.cvtColor(crown, cv2.COLOR_BGR2GRAY)
                ret, mask = cv2.threshold(crown_g, 230, 255, cv2.THRESH_BINARY)
                mask_inv = cv2.bitwise_not(mask)

                crown_m = cv2.bitwise_and(crown, crown, mask=mask_inv)
                frame_m = cv2.bitwise_and(roi, roi, mask=mask)

                dst = cv2.add(crown_m, frame_m)

                frame[y-cw:y, x:x+ch] = dst
                if ret:
                    # 이미지 반전, 0:상하, 1:좌우
                    frame = cv2.flip(frame, 1)
                    cv2.imshow('CAM_Window', frame)
                    if cv2.waitKey(1) &0xFF == 27:
                        break
                else:
                    break
            else:
                if ret:
                    # 이미지 반전, 0:상하, 1:좌우
                    frame = cv2.flip(frame, 1)
                    cv2.imshow('CAM_Window', frame)
                    if cv2.waitKey(1) &0xFF == 27:
                        break
                else:
                    break
        cv2.destroyAllWindows()

if __name__ == "__main__":
    import sys
    cascade_file = "C:\\Users\\jin\\Desktop\\playdata\\video\\opencv-master\\data\\haarcascades\\haarcascade_frontalface_default.xml"
    cascade = cv2.CascadeClassifier(cascade_file)
    frame = []
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
