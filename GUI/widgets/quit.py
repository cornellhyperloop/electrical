from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import QSize
import sys


class Quit(QWidget):

    def __init__(self, *args, parent=None):
        super(Quit, self).__init__(parent)
        self.width = args[0] / 10
        self.height = args[1] / 30
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Quit")
        self.push = QPushButton(self)
        self.push.setText("Quit")
        self.push.setFont(QFont('AnyStyle', 18))
        self.push.setStyleSheet(
            "background-color : red; border-radius: 5px; font-family: Helvetica; font-size: 14px; border: 3px solid black")
        self.push.clicked.connect(self.pushedQuit)
        self.push.resize(self.width, self.height)

    def pushedQuit(self):
        sys.exit()

    def sizeHint(self):
        return QSize(self.width, self.height)
