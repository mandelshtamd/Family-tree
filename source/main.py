import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt, QPointF
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton, QToolTip, QDesktopWidget, \
    QGraphicsEllipseItem, QGraphicsItem, QGraphicsScene, QLineEdit, QInputDialog, QFormLayout, QFrame, QLabel, QDialog, \
    QGraphicsLineItem, QGraphicsPathItem
from PyQt5.QtGui import QFont, QPen, QPainter


class Ui_MainWindow(QWidget):
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
        self.graphicsView.setGeometry(QtCore.QRect(-29, 110, 1630, 871))
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
        self.label_2.setGeometry(QtCore.QRect(10, 0, 51, 41))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("./icon3.png"))
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
        self.label_8.setPixmap(QtGui.QPixmap("./user2.png"))
        self.label_8.setObjectName("label_8")
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
        circle.name = device.iText.text()
        circle.bornYear = device.pText.text()
        circle.status = device.uText.text()
        circle.setToolTip(circle.name)
        self.nodesMap.append(circle)

        circle.setFlag(QGraphicsItem.isUnderMouse(circle))
        scene.addItem(circle)
        self.graphicsView.setScene(scene)
        #self.rerender()


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

    # def paintEvent(self, QPaintEvent):
    #     painter = QPainter()
    #     painter.begin(self)
    #     painter.setRenderHint(QPainter.Antialiasing)
    #     painter.setPen(QtCore.Qt.red)
    #     painter.setBrush(QtCore.Qt.white)
    #     painter.drawLine(0, 0, 200, 200)




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
        self.resize(400, 300)

        iLabel = QLabel("Name and surname")
        self.iText = QLineEdit()

        uLabel = QLabel("Year of born")
        self.uText = QLineEdit()

        pLabel = QLabel("Status")
        self.pText = QLineEdit()

        okButton = QPushButton()
        okButton.setText("OK")
        okButton.clicked.connect(self.add)

        frame = QFrame(self)

        formLayout = QFormLayout(frame)
        formLayout.addRow(iLabel, self.iText)
        formLayout.addRow(uLabel, self.uText)
        formLayout.addRow(pLabel, self.pText)
        formLayout.addRow(okButton, okButton)

        self.exec_()

    def add(self):
        name = self.iText.text()
        yearOfBorn = self.uText.text()
        status = self.pText.text()
        if (name != ""):
            self.close()





if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    application = mywindow()
    application.show()

    sys.exit(app.exec_())