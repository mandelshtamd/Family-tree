import sys
from PyQt5.QtWidgets import QWidget, QDesktopWidget, QApplication, QPushButton, QMainWindow
from PyQt5 import uic


class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("myDesign.ui", self)
        self.initUI()


    def initUI(self):
        self.resize(500, 500)
        self.center()

        self.setWindowTitle('Family tree')
        self.show()


    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)

        self.move(qr.topLeft())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())