# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'aboutUs.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt, QPointF
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton, QToolTip, QDesktopWidget, \
    QGraphicsEllipseItem, QGraphicsItem, QGraphicsScene, QLineEdit, QInputDialog, QFormLayout, QFrame, QLabel, QDialog, \
    QGraphicsLineItem, QGraphicsPathItem
from PyQt5.QtGui import QFont, QPen, QPainter
from urllib import request

class Ui_about_us(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1550, 884)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(0, 0, 1561, 331))
        font = QtGui.QFont()
        font.setFamily("Abyssinica SIL")
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.textEdit.setFont(font)
        self.textEdit.setStyleSheet("background-color: rgb(249, 249, 249);\n"
                                    "background-color: rgb(244, 244, 244);\n"
                                    "\n"
                                    "")
        self.textEdit.setObjectName("textEdit")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(310, 30, 151, 131))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("tree2.png"))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(-10, 310, 1591, 771))
        font = QtGui.QFont()
        font.setFamily("Khmer OS System")
        self.label_2.setFont(font)
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("фон3.png"))
        self.label_2.setObjectName("label_2")
        self.textEdit_3 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_3.setGeometry(QtCore.QRect(770, 340, 761, 441))
        self.textEdit_3.setStyleSheet("background-color: rgb(248, 248, 248);")
        self.textEdit_3.setObjectName("textEdit_3")
        self.textEdit_2 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_2.setGeometry(QtCore.QRect(20, 340, 701, 441))
        font = QtGui.QFont()
        font.setFamily("Abyssinica SIL")
        self.textEdit_2.setFont(font)
        self.textEdit_2.setStyleSheet("background-color: rgb(248, 248, 248);")
        self.textEdit_2.setObjectName("textEdit_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(80, 370, 91, 121))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("people7.png"))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(90, 480, 81, 81))
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap("genebook.png"))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(90, 590, 81, 61))
        self.label_5.setText("")
        self.label_5.setPixmap(QtGui.QPixmap("photo.png"))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(90, 670, 91, 91))
        self.label_6.setText("")
        self.label_6.setPixmap(QtGui.QPixmap("file.png"))
        self.label_6.setObjectName("label_6")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(780, 390, 111, 91))
        self.label_8.setText("")
        self.label_8.setPixmap(QtGui.QPixmap("free.png"))
        self.label_8.setObjectName("label_8")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(790, 490, 91, 91))
        self.label_10.setText("")
        self.label_10.setPixmap(QtGui.QPixmap("interface.png"))
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(800, 580, 91, 101))
        self.label_11.setText("")
        self.label_11.setPixmap(QtGui.QPixmap("bigdata.png"))
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(810, 690, 91, 81))
        self.label_12.setText("")
        self.label_12.setPixmap(QtGui.QPixmap("desktop.png"))
        self.label_12.setObjectName("label_12")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1550, 19))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.textEdit.setHtml(_translate("MainWindow",
                                         "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                         "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                         "p, li { white-space: pre-wrap; }\n"
                                         "</style></head><body style=\" font-family:\'Abyssinica SIL\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
                                         "<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
                                         "<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
                                         "<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:36pt; font-weight:600;\">Welcome to GeneTreetion!</span></p>\n"
                                         "<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
                                         "<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt; font-style:italic;\">Hello, everyone!We, Dmitry Mandelstam, Margarita Lashina and Anastasiia Isakova, students of St. Petersburg State University, are pleased to present you our universal desktop application for creating a family tree. As you know, each family has its own unique history, which is inextricably linked with the history of all mankind. However, the memories of the deeds of distant ancestors, just like their faces, eventually fade from our memory, not reaching the next generations. So, the family tree will help you solve this problem, as well as strengthen relationships between relatives. </span></p></body></html>"))
        self.textEdit_3.setHtml(_translate("MainWindow",
                                           "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                           "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                           "p, li { white-space: pre-wrap; }\n"
                                           "</style></head><body style=\" font-family:\'Sans Serif\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
                                           "<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
                                           "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Abyssinica SIL\'; font-size:22pt; font-weight:600; font-style:italic;\">Why GeneTreetion?</span></p>\n"
                                           "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Abyssinica SIL\'; font-size:22pt; font-weight:600; font-style:italic;\">                                                             </span></p>\n"
                                           "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Abyssinica SIL\'; font-size:18pt; font-style:italic;\">           Free access to all options</span></p>\n"
                                           "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Abyssinica SIL\'; font-size:18pt; font-style:italic;\"> </span></p>\n"
                                           "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Abyssinica SIL\'; font-size:18pt; font-style:italic;\"><br /></p>\n"
                                           "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Abyssinica SIL\'; font-size:18pt; font-style:italic;\">           User-friendly interface</span></p>\n"
                                           "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Abyssinica SIL\'; font-size:18pt; font-style:italic;\"><br /></p>\n"
                                           "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Abyssinica SIL\'; font-size:18pt; font-style:italic;\"><br /></p>\n"
                                           "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
                                           "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Abyssinica SIL\'; font-size:18pt; font-style:italic;\">           Modern technologies of data storage and processing</span></p>\n"
                                           "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Abyssinica SIL\'; font-size:18pt; font-style:italic;\"><br /></p>\n"
                                           "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Abyssinica SIL\'; font-size:18pt; font-style:italic;\"><br /></p>\n"
                                           "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Abyssinica SIL\'; font-size:18pt; font-style:italic;\">           Install application on your computer and use it offline</span></p>\n"
                                           "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Abyssinica SIL\'; font-size:18pt; font-style:italic;\"><br /></p></body></html>"))
        self.textEdit_2.setHtml(_translate("MainWindow",
                                           "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                           "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                           "p, li { white-space: pre-wrap; }\n"
                                           "</style></head><body style=\" font-family:\'Abyssinica SIL\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
                                           "<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
                                           "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:22pt; font-weight:600; font-style:italic;\">What can you do here?</span></p>\n"
                                           "<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:22pt; font-weight:600; font-style:italic;\"><br /></p>\n"
                                           "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:22pt; font-weight:600; font-style:italic;\">            </span><span style=\" font-size:18pt; font-style:italic;\">Create your own family tree</span></p>\n"
                                           "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt; font-style:italic;\"> </span></p>\n"
                                           "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:18pt; font-style:italic;\"><br /></p>\n"
                                           "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt; font-style:italic;\">               Add full information about each relative</span></p>\n"
                                           "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:18pt; font-style:italic;\"><br /></p>\n"
                                           "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:18pt; font-style:italic;\"><br /></p>\n"
                                           "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt; font-style:italic;\">               Don\'t forget about people\'s photo</span></p>\n"
                                           "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:18pt; font-style:italic;\"><br /></p>\n"
                                           "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:18pt; font-style:italic;\"><br /></p>\n"
                                           "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt; font-style:italic;\">               Save family tree to your computer</span></p>\n"
                                           "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:18pt; font-style:italic;\"><br /></p>\n"
                                           "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:18pt; font-style:italic;\"><br /></p>\n"
                                           "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt; font-style:italic;\">              </span></p></body></html>"))


class Ui_MainWindow(object):
    def OpenWindow(self):
        self.aboutUs = AboutUsWindow()
        self.aboutUs.show()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(1585, 861)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 1585, 861))
        font = QtGui.QFont()
        font.setFamily("Noto Sans Mono CJK TC Bold")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)

        self.graphicsView = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView.setStyleSheet("background-image: url(./фон4.png)")
        self.graphicsView.setGeometry(QtCore.QRect(0, 0, 1585, 861))
        self.graphicsView.setObjectName("graphicsView")
        self.QGraphicsScene = QGraphicsScene()

        self.label.setFont(font)
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("./фон4.png"))
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(0, 0, 271, 51))
        font = QtGui.QFont()
        font.setFamily("Serif")
        font.setPointSize(14)
        font.setItalic(True)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color: rgb(18, 18, 18);\n"
"color: rgb(255, 255, 255);")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(240, 0, 111, 51))
        font = QtGui.QFont()
        font.setFamily("Noto Sans Mono CJK TC Bold")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("background-color: rgb(48, 48, 48);\n"
"color: rgb(255, 255, 255);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(349, 0, 171, 51))
        font = QtGui.QFont()
        font.setFamily("Noto Sans Mono CJK TC Bold")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("background-color: rgb(48, 48, 48);\n"
"color: rgb(255, 255, 255);")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(510, 0, 121, 51))
        self.pushButton_4.clicked.connect(self.OpenWindow)
        font = QtGui.QFont()
        font.setFamily("Noto Sans Mono CJK TC Bold")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setStyleSheet("background-color: rgb(48, 48, 48);\n"
"color: rgb(255, 255, 255);")
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(620, 0, 661, 51))
        self.pushButton_5.setStyleSheet("background-color: rgb(48, 48, 48);\n"
"color: rgb(255, 255, 255);")
        self.pushButton_5.setText("")
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(1270, 0, 321, 51))
        font = QtGui.QFont()
        font.setFamily("Noto Sans Mono CJK TC Bold")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setStyleSheet("background-color: rgb(48, 48, 48);\n"
"color: rgb(255, 255, 255);")
        self.pushButton_6.setObjectName("pushButton_6")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 0, 61, 51))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("icontree.png"))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(1330, 10, 31, 31))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("./leave1.png"))
        self.label_3.setObjectName("label_3")
        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_7.setGeometry(QtCore.QRect(1070, 70, 131, 41))
        font = QtGui.QFont()
        font.setFamily("Noto Sans Mono CJK TC Bold")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_7.setFont(font)
        self.pushButton_7.setStyleSheet("background-color: rgb(48, 48, 48);\n"
"color: rgb(255, 255, 255);")
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_8 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_8.setGeometry(QtCore.QRect(1170, 70, 131, 41))
        font = QtGui.QFont()
        font.setFamily("Noto Sans Mono CJK TC Bold")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_8.setFont(font)
        self.pushButton_8.setStyleSheet("background-color: rgb(48, 48, 48);\n"
"color: rgb(255, 255, 255);")
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_9 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_9.setGeometry(QtCore.QRect(1290, 70, 141, 41))
        font = QtGui.QFont()
        font.setFamily("Noto Sans Mono CJK TC Bold")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_9.setFont(font)
        self.pushButton_9.setStyleSheet("background-color: rgb(48, 48, 48);\n"
"color: rgb(255, 255, 255);")
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_10 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_10.setGeometry(QtCore.QRect(1410, 70, 181, 41))
        font = QtGui.QFont()
        font.setFamily("Noto Sans Mono CJK TC Bold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_10.setFont(font)
        self.pushButton_10.setStyleSheet("background-color: rgb(48, 48, 48);\n"
"color: rgb(255, 255, 255);")
        self.pushButton_10.setObjectName("pushButton_10")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(1410, 70, 31, 41))
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap("./treesearch.PNG"))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(1290, 70, 31, 31))
        self.label_5.setText("")
        self.label_5.setPixmap(QtGui.QPixmap("./cross.png"))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(1180, 70, 31, 31))
        self.label_6.setText("")
        self.label_6.setPixmap(QtGui.QPixmap("./save.png"))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(1070, 70, 41, 31))
        self.label_7.setText("")
        self.label_7.setPixmap(QtGui.QPixmap("./share.PNG"))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(690, 300, 151, 151))
        self.label_8.setText("")
        self.label_8.setPixmap(QtGui.QPixmap("user2.png"))
        self.label_8.setObjectName("label_8")

        self.pushButton_11 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_11.setGeometry(QtCore.QRect(810, 300, 31, 31))

        self.pushButton_11.setObjectName("pushButton_11")
        self.pushButton_12 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_12.setGeometry(QtCore.QRect(690, 300, 31, 31))
        self.pushButton_12.setObjectName("pushButton_12")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1184, 19))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.addPerson = QtWidgets.QPushButton(self.centralwidget)
        self.addPerson.setGeometry(QtCore.QRect(810, 300, 31, 31))
        self.addPerson.clicked.connect(self.toAddPerson)
        self.addPerson.setEnabled(True)
        self.addPerson.setObjectName("addPerson")

        self.deletePerson = QtWidgets.QPushButton(self.centralwidget)
        self.deletePerson.setGeometry(QtCore.QRect(690, 300, 31, 31))
        self.deletePerson.setObjectName("deletePerson")
        self.deletePerson.clicked.connect(self.toDeletePerson)
        self.deletePerson.setEnabled(True)

        self.nodesMap = []

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1184, 19))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

    def toAddPerson(self):
        scene = self.QGraphicsScene
        blackPen = QPen(Qt.black)
        blackPen.setWidth(3)
        circle = QGraphicsEllipseItem(10, 10, 100, 100)
        circle.setFlag(QGraphicsItem.ItemIsMovable)

        device = AddDevice()
        circle.name = device.nameEdit.text()
        circle.surname = device.surnameEdit.text()
        circle.birth = device.birthEdit.text()
        circle.death = device.deathEdit.text()
        circle.mom = device.momEdit.text()
        circle.dad = device.dadEdit.text()
        circle.spouse = device.spouseEdit.text()
        circle.photo = device.imageLabel.pixmap()
        self.nodesMap.append(circle)

        circle.setFlag(QGraphicsItem.isUnderMouse(circle))
        scene.addItem(circle)
        self.graphicsView.setScene(scene)
        # self.rerender()

    def toDeletePerson(self):
        scene = self.QGraphicsScene
        nameToDelete, ok = QInputDialog.getText(self, 'Delete person', 'Who you want to delete?:')
        print(nameToDelete)
        for node in self.nodesMap:
            if (node.name == nameToDelete):
                scene.removeItem(node)
        self.graphicsView.setScene(scene)

    def rerender(self):
        scene = self.QGraphicsScene
        for firstNode in self.nodesMap:
            for secondNode in self.nodesMap:
                line = QGraphicsLineItem(QtCore.QLineF(firstNode.pos(), secondNode.pos()))
                line.setFlag(QGraphicsLineItem.ItemIsMovable)
                scene.addItem(line)
        self.graphicsView.setScene(scene)



    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "GeneTreetion"))
        self.pushButton_2.setText(_translate("MainWindow", "My trees"))
        self.pushButton_2.setToolTip('Click <b>here</b> to start a new project or continue the old one')
        QToolTip.setFont(QFont('PurisaBold', 13))

        self.pushButton_3.setText(_translate("MainWindow", "Language"))
        self.pushButton_3.setToolTip('Click <b>here</b> to select language')
        QToolTip.setFont(QFont('PurisaBold', 13))
        self.pushButton_4.setText(_translate("MainWindow", "About us"))
        self.pushButton_4.setToolTip('Click <b>here</b> if you want to get more information about the app')
        QToolTip.setFont(QFont('PurisaBold', 13))
        self.pushButton_6.setText(_translate("MainWindow", "Project name"))
        self.pushButton_7.setText(_translate("MainWindow", "Share"))
        self.pushButton_7.setToolTip('Click <b>here</b> to share your family tree with others')
        QToolTip.setFont(QFont('PurisaBold', 13))

        self.pushButton_8.setText(_translate("MainWindow", "Save"))
        self.pushButton_8.setToolTip('Click <b>here</b> to save project on your computer')
        QToolTip.setFont(QFont('PurisaBold', 13))

        self.pushButton_9.setText(_translate("MainWindow", "Delete"))
        self.pushButton_9.setToolTip('Click <b>here</b> to delete current project')
        QToolTip.setFont(QFont('PurisaBold', 13))
        self.pushButton_10.setText(_translate("MainWindow", "Tree search"))
        self.pushButton_10.setToolTip('Click <b>here</b> to quickly find the information you need in the tree')
        QToolTip.setFont(QFont('PurisaBold', 13))
        self.addPerson.setText(_translate("MainWindow", "+"))
        self.deletePerson.setText(_translate("MainWindow", "-"))


class mywindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(mywindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.retranslateUi(self)
        self.center()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())


class AddDevice(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        self.setWindowTitle("Person's information")
        self.setFixedSize(440, 500)

        self.nameLabel = QLabel("Name")
        self.nameEdit = QLineEdit()

        self.surnameLabel = QLabel("Surname")
        self.surnameEdit = QLineEdit()

        self.birthLabel = QLabel("Date of birth")
        self.birthEdit = QLineEdit()

        self.deathLabel = QLabel("Date of death")
        self.deathEdit = QLineEdit()

        self.momLabel = QLabel("Mother")
        self.momEdit = QLineEdit()

        self.dadLabel = QLabel("Father")
        self.dadEdit = QLineEdit()

        self.spouseLabel = QLabel("Spouse")
        self.spouseEdit = QLineEdit()

        self.urlEdit = QLineEdit()
        self.pathEdit = QLineEdit()


        self.imageLabel = QLabel("No image")
        self.imageLabel.setScaledContents(True)
        self.imageLabel.setFixedSize(150, 150)



        self.loadInternetButton = QPushButton("Photo from Internet")
        self.loadInternetButton.clicked.connect(self.loadFromInternet)
        self.loadInternetButton.setFixedSize(160, 25)

        self.loadComputerButton = QPushButton("Photo from Computer")
        self.loadComputerButton.clicked.connect(self.loadFromComputer)


        self.okButton = QPushButton()
        self.okButton.setText("OK")
        self.okButton.clicked.connect(self.add)

        frame = QFrame(self)

        formLayout = QFormLayout(frame)
        formLayout.addRow(self.imageLabel, self.imageLabel)
        formLayout.addRow(self.nameLabel, self.nameEdit)
        formLayout.addRow(self.surnameLabel, self.surnameEdit)
        formLayout.addRow(self.birthLabel, self.birthEdit)
        formLayout.addRow(self.deathLabel, self.deathEdit)
        formLayout.addRow(self.momLabel, self.momEdit)
        formLayout.addRow(self.dadLabel, self.dadEdit)
        formLayout.addRow(self.spouseLabel, self.spouseEdit)
        formLayout.addRow(self.loadInternetButton, self.urlEdit)
        formLayout.addRow(self.loadComputerButton, self.pathEdit)
        formLayout.addRow(self.okButton, self.okButton)

        self.exec_()

    def loadFromInternet(self):
        data = request.urlopen(self.urlEdit.text()).read()
        pixmap = QtGui.QPixmap()
        pixmap.loadFromData(data)
        self.imageLabel.setPixmap(pixmap)

    def loadFromComputer(self):
        hl = self.pathEdit.text()
        self.imageLabel.setPixmap(QtGui.QPixmap(hl))



    def add(self):
        name = self.nameEdit.text()
        surname = self.surnameEdit.text()
        birth = self.birthEdit.text()
        death = self.deathEdit.text()
        mom = self.momEdit.text()
        dad = self.dadEdit.text()
        spouse = self.spouseEdit.text()
        photo = self.imageLabel.pixmap()
        if (name != ""):
            self.close()





class AboutUsWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(AboutUsWindow, self).__init__()
        self.ui = Ui_about_us()
        self.ui.setupUi(self)
        self.ui.retranslateUi(self)
        self.center()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())



if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    application = mywindow()
    application.show()

    sys.exit(app.exec_())