from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import QSize
import sys


class HelpPopup(QWidget):
    def __init__(self, *args, parent=None):
        super(HelpPopup, self).__init__(parent)
        self.width = args[0] / 10
        self.height = args[1] / 30
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Click button")
        self.push = QPushButton(self)
        self.push.setText("Help")
        self.push.setFont(QFont('AnyStyle', 18))
        self.push.setStyleSheet(
            "background-color : #2B26c1; border-radius: 5px; font-family: Helvetica; font-size: 14px; border: 3px #2B26c1")
        self.push.clicked.connect(self.pushedHelp)
        self.push.resize(int(self.width), int(self.height))
        #self.push.resize(400, 200)
        #self.push.move(0, 50)

    def pushedHelp(self):
        self.msgBox = QMessageBox()
        self.msgBox.setWindowTitle("Tutorial on using GUI")
        self.msgBox.setText(
            "Click on the various buttons in order to receive more information about them")
        self.msgBox.setIcon(QMessageBox.Information)
        x = self.msgBox.exec()

    def sizeHint(self):
        return QSize(int(self.width), int(self.height))
