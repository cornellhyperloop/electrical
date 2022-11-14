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
        sshFile = "widgets/redwidgets.css"
        with open(sshFile, "r") as fh:
            qstr = str(fh.read())
        
        self.setWindowTitle("Quit")
        self.push = QPushButton(self)
        self.push.setText("Quit")
        self.push.setFont(QFont('AnyStyle', 18))
        self.push.setStyleSheet(qstr)
        self.push.clicked.connect(self.pushedQuit)
        self.push.resize(int(self.width), int(self.height))


    def pushedQuit(self):
        sys.exit()

    def sizeHint(self):
        return QSize(int(self.width), int(self.height))
