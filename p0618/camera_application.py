import cv2
import numpy as np
import os
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("Camera_app")
        MainWindow.resize(300, 130)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 0, 0, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 1, 1, 1, 1)
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout.addWidget(self.pushButton_3, 2, 0, 1, 1)
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setObjectName("pushButton_5")
        self.gridLayout.addWidget(self.pushButton_5, 2, 1, 1, 1)
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setObjectName("pushButton_6")
        self.gridLayout.addWidget(self.pushButton_6, 2, 2, 1, 1)
        self.pushButton_8 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_8.setObjectName("pushButton_8")
        self.gridLayout.addWidget(self.pushButton_8, 1, 0, 1, 1) 
        self.pushButton_9 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_9.setObjectName("pushButton_9")
        self.gridLayout.addWidget(self.pushButton_9, 0, 1, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 0, 2, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 300, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    
        self.pushButton.clicked.connect(self.preview) #촬영모드
        self.pushButton_2.clicked.connect(self.black) #흑백촬영
        self.pushButton_3.clicked.connect(self.previousView) #이전사진
        self.pushButton_5.clicked.connect(self.nextView) #다음사진
        self.pushButton_6.clicked.connect(self.delete) #삭제
        self.pushButton_8.clicked.connect(self.capture) #사진찍기
        self.pushButton_9.clicked.connect(self.imgView) #사진보기

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Camera_app"))
        self.pushButton.setText(_translate("MainWindow", "촬영모드"))
        self.pushButton_2.setText(_translate("MainWindow", "흑백촬영"))
        self.pushButton_3.setText(_translate("MainWindow", "이전사진"))
        self.pushButton_5.setText(_translate("MainWindow", "다음사진"))
        self.pushButton_6.setText(_translate("MainWindow", "삭제"))        
        self.pushButton_8.setText(_translate("MainWindow", "사진찍기"))
        self.pushButton_9.setText(_translate("MainWindow", "사진보기"))     

    def preview(self):
        cam = cv2.VideoCapture(0)
        if cam.isOpened() == False:
            QMessageBox.about(self.centralwidget, '알림', '카메라가 켜져있지 않습니다.')

        width = cam.get(cv2.CAP_PROP_FRAME_WIDTH)
        height = cam.get(cv2.CAP_PROP_FRAME_HEIGHT)
        encode_param = [int(cv2.IMWRITE_JPEG_QUALITY), 90]
        cv2.namedWindow('CAM_Window')
        cv2.resizeWindow('CAM_Window', 640, 400)


        while True:
            ret, frame = cam.read()
            if ret:
                # 이미지 반전, 0:상하, 1:좌우
                frame = cv2.flip(frame, 1)
                cv2.imshow('CAM_Window', frame)
                if cv2.waitKey(1) >= 0:
                    break
            else:
                break
        cv2.destroyAllWindows()

    def saveEvent(self):
        filename = self.lineEdit.text()
        reply = QMessageBox.question(self.centralwidget, '알림', '저장하시겠습니까?', QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            cv2.imwrite(f'C:\\Users\\jin\\Desktop\\playdata\\video\\p0618\\img\\{filename}.png', fm.pop(0))
            self.lineEdit.clear()
            cv2.destroyAllWindows()
        else:
            self.lineEdit.clear()
            

    def capture(self):
        cap = cv2.VideoCapture(0)
        try:
            ret,frame = cap.read()
            frame = cv2.flip(frame, 1)
            cv2.imshow('image', frame)
            print("촬영")
            fm.append(frame)
            print("저장시작")
            self.saveEvent()                
        except cv2.error:
            QMessageBox.about(self.centralwidget, '알림', '카메라가 켜져있지 않습니다.')
        
    
    def imgView(self):
        cv2.destroyAllWindows()
        file_list = os.listdir(path)
        if len(file_list) == 0:
            QMessageBox.about(self.centralwidget, '알림', '사진이 없습니다.')
        else:
            filename = file_list[num].split('.')
            fileinput = path + '\\' + file_list[num]
            img = cv2.imread(fileinput, cv2.IMREAD_COLOR)
            img = cv2.resize(img, dsize=(640, 480), interpolation=cv2.INTER_AREA)
            cv2.imshow(filename[0], img)
           
    def previousView(self):
        cv2.destroyAllWindows()
        file_list = os.listdir(path)
        global num
        if num == 0:
            QMessageBox.about(self.centralwidget, '알림', '더 이상 이전 사진이 없습니다')
        else:
            num = num - 1
            filename = file_list[num].split('.')
            fileinput = path + '\\' + file_list[num]
            img = cv2.imread(fileinput, cv2.IMREAD_COLOR)
            img = cv2.resize(img, dsize=(640, 480), interpolation=cv2.INTER_AREA)
            cv2.imshow(filename[0], img)
            
    def nextView(self):
        cv2.destroyAllWindows()
        file_list = os.listdir(path)
        global num
        if num == len(file_list)-1:
            QMessageBox.about(self.centralwidget, '알림', '더 이상 다음 사진이 없습니다')
        else:
            num = num + 1
            filename = file_list[num].split('.')
            fileinput = path + '\\' + file_list[num]
            img = cv2.imread(fileinput, cv2.IMREAD_COLOR)
            img = cv2.resize(img, dsize=(640, 480), interpolation=cv2.INTER_AREA)
            cv2.imshow(filename[0], img)
    
    def black(self):
        cv2.destroyAllWindows()
        cap = cv2.VideoCapture(0)
        try:
            ret,frame = cap.read()
            frame = cv2.flip(frame, 1)       
            image_gs = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            cv2.imshow('image', image_gs)
            fm.append(image_gs)
            self.saveEvent() 
        except cv2.error:
            QMessageBox.about(self.centralwidget, '알림', '카메라가 켜져있지 않습니다.')
   
    def delete(self):
        file_list = os.listdir(path)
        delfile = path + '\\' + file_list[num]
        os.remove(delfile)
        QMessageBox.about(self.centralwidget, '알림', f'{file_list[num]} 파일이 삭제 되었습니다.')

if __name__ == "__main__":
    import sys
    fm = []
    num = 0
    path = "C:\\Users\\jin\\Desktop\\playdata\\video\\p0618\\img"
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
