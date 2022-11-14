from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import QSize
from .fsm import FSM
import sys


class EmergencyButton(QWidget):
    def __init__(self, fsm, *args, parent=None):
        super(EmergencyButton, self).__init__(parent)
        self.fsm = fsm
        self.width = args[0] / 10
        self.height = args[1] / 30
        self.initUI()

    def initUI(self):
        sshFile = "widgets/redwidgets.css"
        with open(sshFile, "r") as fh:
            qstr = str(fh.read())

        self.setWindowTitle("Click button")
        self.push = QPushButton(self)
        self.push.setText("Emergency Break")
        self.push.setFont(QFont('AnyStyle', 18))
        self.push.clicked.connect(self.pushedEmergency)

        self.push.setStyleSheet(qstr)
        self.push.resize(int(self.width), int(self.height))

    def msgButtonClick(self, i):
        print("Button clicked is:", i.text())

    def pushedEmergency(self):
        self.fsm.fsm.setState('Emergency')

    def sizeHint(self):
        return QSize(int(self.width), int(self.height))
