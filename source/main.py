import json
import os
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt, QPointF, QLineF, QPoint
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton, QToolTip, QDesktopWidget, \
    QGraphicsEllipseItem, QGraphicsItem, QGraphicsScene, QLineEdit, QInputDialog, QFormLayout, QFrame, QLabel, QDialog, \
    QGraphicsLineItem, QGraphicsPathItem, QGraphicsItemGroup
from PyQt5.QtGui import QFont, QPen, QPainter
from urllib import request

from pymongo import MongoClient

from source.UserInterface.userInterface import Ui_MainWindow
from source.dataStorage.dataUtils import add_to_db


class mywindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(mywindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.setMouseTracking(True)

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

    """ 
   connecting database
   """
    path = "/tmp/dbdata"
    try:
        os.mkdir(path)
    except OSError:
        print("Directory was not created (it is Ok if folder dbdata was created earlier)")
    else:
        print("Directory was created successfully")
    os.system("mongod --dbpath /tmp/dbdata")
    client = MongoClient()

    """
    creating database "my_database" and collection "trees"
    """
    db = client.my_database
    trees = db.trees
    add_to_db(db, trees) # третий параметр - json
    sys.exit(app.exec_())