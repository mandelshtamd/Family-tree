from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import QLineF, Qt
from PyQt5.QtGui import QFont, QPen
from PyQt5.QtWidgets import QWidget, QToolTip, QGraphicsScene, QInputDialog, QGraphicsItem, \
    QGraphicsLineItem, QGraphicsItemGroup, QGraphicsEllipseItem

from source.UserInterface.aboutUsWindow import AboutUsWindow
from source.UserInterface.helpInterface import Help
from source.UserInterface.interfaceUtils import *


humans = {}

class Vertex():
    def __init__(self, name, surname, birth, death, mom, dad, photo, scene):
        self.circle = callbackEllipse(-40, -40, 80, 80)

        self.name = name
        self.circle.name = name
        self.surname = surname
        self.circle.surname = surname
        humans[name + " " + surname] = self
        self.birth = birth
        self.circle.birth = birth
        self.death = death
        self.circle.death = death
        self.circle.mom = mom
        self.circle.dad = dad
        self.photo = photo
        self.family = []
        self.edges = []

        self.scene = scene

        self.circle.setFlag(QGraphicsItem.isWidget(self.circle))
        self.circle.setFlag(QGraphicsItem.ItemIsMovable)
        self.circle.setToolTip(self.name + " " + self.surname)


        if mom != "" and mom in humans and mom != name + " " + surname:
            self.family.append(humans[mom])
            humans[mom].family.append(self)
            line = QGraphicsLineItem(QLineF(self.circle.pos(), humans[mom].circle.pos()))
            line.setFlag(QGraphicsLineItem.ItemIsMovable)
            self.scene.addItem(line)
            self.edges.append(line)
            humans[mom].edges.append(line)
            line.setParentItem(self.circle)


        if dad != "" and dad in humans and dad != name + " " + surname:
            self.family.append(humans[dad])
            humans[dad].family.append(self)
            line = QGraphicsLineItem(QLineF(self.circle.pos(), humans[dad].circle.pos()))
            line.setFlag(QGraphicsLineItem.ItemIsMovable)
            self.scene.addItem(line)
            self.edges.append(line)
            humans[dad].edges.append(line)

        self.scene.addItem(self.circle)


class Ui_MainWindow(QWidget):
    def OpenWindow(self):
        self.aboutUs = AboutUsWindow()
        self.aboutUs.show()


    def OpenWindow2(self):
        self.help = Help()
        self.help.show()


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
        self.graphicsView.setStyleSheet("background-image: url(images/фон4.png)")
        self.graphicsView.setGeometry(QtCore.QRect(0, 0, 1585, 861))
        self.graphicsView.setObjectName("graphicsView")
        self.QGraphicsScene = QGraphicsScene()

        self.label.setFont(font)
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("images/фон4.png"))
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
        self.pushButton_2.setGeometry(QtCore.QRect(250, 0, 181, 51))
        font = QtGui.QFont()
        font.setFamily("Noto Sans Mono CJK TC Bold")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("background-color: rgb(48, 48, 48);\n"
                                        "color: rgb(255, 255, 255);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.openFile)

        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(409, 0, 161, 51))
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
        self.pushButton_4.setGeometry(QtCore.QRect(640, 0, 151, 51))
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
        self.pushButton_5.setGeometry(QtCore.QRect(780, 0, 501, 51))
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
        self.label_2.setPixmap(QtGui.QPixmap("images/icontree.png"))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(1330, 10, 31, 31))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("images/leave1.png"))

        self.pushButton_8 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_8.setGeometry(QtCore.QRect(1140, 70, 131, 41))
        font = QtGui.QFont()
        font.setFamily("Noto Sans Mono CJK TC Bold")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_8.setFont(font)
        self.pushButton_8.setStyleSheet("background-color: rgb(48, 48, 48);\n"
                                        "color: rgb(255, 255, 255);")
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_8.clicked.connect(self.toAddPerson)
        self.pushButton_9 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_9.setGeometry(QtCore.QRect(1250, 70, 191, 41))
        font = QtGui.QFont()
        font.setFamily("Noto Sans Mono CJK TC Bold")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_9.setFont(font)
        self.pushButton_9.setStyleSheet("background-color: rgb(48, 48, 48);\n"
                                        "color: rgb(255, 255, 255);")
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_9.clicked.connect(self.toDeletePerson)

        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(1250, 70, 31, 31))
        self.label_5.setText("")
        self.label_5.setPixmap(QtGui.QPixmap("images/cross.png"))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(1130, 70, 31, 31))
        self.label_6.setText("")
        self.label_6.setPixmap(QtGui.QPixmap("images/plus1.png"))
        self.label_6.setObjectName("label_6")
        self.pushButton_11 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_11.setGeometry(QtCore.QRect(559, 0, 101, 51))
        font = QtGui.QFont()
        font.setFamily("Noto Sans Mono CJK TC Bold")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_11.setFont(font)
        self.pushButton_11.setStyleSheet("background-color: rgb(48, 48, 48);\n"
                                         "color: rgb(255, 255, 255);")
        self.pushButton_11.setObjectName("pushButton_11")
        self.pushButton_11.clicked.connect(self.OpenWindow2)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1184, 19))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1184, 19))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "GeneTreetion"))
        self.pushButton_2.setText(_translate("MainWindow", "Open project"))
        self.pushButton_2.setToolTip('Click <b>here</b> to change your old project')
        QToolTip.setFont(QFont('PurisaBold', 13))

        self.pushButton_3.setText(_translate("MainWindow", "Language"))
        self.pushButton_3.setToolTip('Click <b>here</b> to select language')
        QToolTip.setFont(QFont('PurisaBold', 13))
        self.pushButton_4.setText(_translate("MainWindow", "About us"))
        self.pushButton_4.setToolTip('Click <b>here</b> if you want to get more information about the app')
        QToolTip.setFont(QFont('PurisaBold', 13))
        self.pushButton_6.setText(_translate("MainWindow", "Project name"))
        self.pushButton_8.setText(_translate("MainWindow", "Add node"))
        self.pushButton_8.setToolTip('Click <b>here</b> to add node to your family tree')
        QToolTip.setFont(QFont('PurisaBold', 13))

        self.pushButton_9.setText(_translate("MainWindow", "Delete node"))
        self.pushButton_9.setToolTip('Click <b>here</b> to delete node from your family tree')
        QToolTip.setFont(QFont('PurisaBold', 13))


        self.pushButton_11.setText(_translate("MainWindow", "Help"))
        self.pushButton_11.setToolTip('Click <b>here</b> if you need some tips how to use GeneTreetion')
        QToolTip.setFont(QFont('PurisaBold', 13))

    def openFile(self):
        filename, ok = QInputDialog.getText(self, 'Open project', 'Enter project name')

    def toAddPerson(self):
        device = AddDevice()
        scene = self.QGraphicsScene

        name = device.nameEdit.text()
        surname = device.surnameEdit.text()
        birth = device.birthEdit.text()
        death = device.deathEdit.text()
        mom = device.momEdit.text()
        dad = device.dadEdit.text()
        #spouse = device.spouseEdit.text()
        photo = device.imageLabel.pixmap()

        vertex = Vertex(name, surname, birth, death, mom, dad, photo, scene)
        self.graphicsView.setScene(vertex.scene)
        blackPen = QPen(Qt.black)
        blackPen.setWidth(3)
        circle = QGraphicsEllipseItem(-20, -20, 40, 40)
        circle.setFlag(QGraphicsItem.ItemIsMovable)
        self.graphicsView.setScene(scene)
        self.update()


    def toDeletePerson(self):
        scene = self.QGraphicsScene
        nameToDelete, ok = QInputDialog.getText(self, 'Delete person', 'Who you want to delete?:')
        print(nameToDelete)
        if nameToDelete in humans:
            obj = humans[nameToDelete]
            for relatives in obj.family:
                relatives.family.remove(obj)
            for edge in obj.edges:
                obj.scene.removeItem(edge) #del edge
            obj.scene.removeItem(obj.circle)
            del obj
            del humans[nameToDelete]
        self.graphicsView.setScene(scene)



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
        #spouse = self.spouseEdit.text()
        photo = self.imageLabel.pixmap()
        if (name != ""):
            self.close()



class callbackEllipse(QGraphicsEllipseItem):
    def __init(self):

        super().__init__()

    def mouseDoubleClickEvent(self, event):
        self.dialog = Second(self)
        self.dialog.show()



class Second(QDialog):
    def __init__(self, cbEllipse):
        QDialog.__init__(self)
        self.setWindowTitle("Person's information")
        self.setFixedSize(280, 360)

        self.nameLabel = QLabel("Name: " + cbEllipse.name)
        self.surnameLabel = QLabel("Surname: " + cbEllipse.surname)
        self.birthLabel = QLabel("Date of birth: " + cbEllipse.birth)
        self.deathLabel = QLabel("Date of death: " + cbEllipse.death)
        self.momLabel = QLabel("Mother: " + cbEllipse.mom)
        self.dadLabel = QLabel("Father: " + cbEllipse.dad)


        self.imageLabel = QLabel("No image")
        self.imageLabel.setScaledContents(True)
        self.imageLabel.setFixedSize(150, 150)

        self.okButton = QPushButton()
        self.okButton.setText("OK")
        frame = QFrame(self)

        formLayout = QFormLayout(frame)
        formLayout.addRow(self.imageLabel, self.imageLabel)
        formLayout.addRow(self.nameLabel)
        formLayout.addRow(self.surnameLabel)
        formLayout.addRow(self.birthLabel)
        formLayout.addRow(self.deathLabel)
        formLayout.addRow(self.momLabel)
        formLayout.addRow(self.dadLabel)
        formLayout.addRow(self.okButton)

        self.exec_()