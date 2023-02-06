from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import QSize
from .fsm import FSM
import sys
import constants as cons


class EmergencyButton(QWidget):
    def __init__(self, fsm, *args, parent=None):
        super(EmergencyButton, self).__init__(parent)
        self.fsm = fsm
        self.width = args[0] / 7
        self.height = args[1] / 30
        self.initUI()

    def initUI(self):
        widFile = cons.REDWIDGETS
        with open(widFile, "r") as fh:
            qstr = str(fh.read())

        self.setWindowTitle("Click button")
        self.push = QPushButton(self)
<<<<<<< HEAD
        #self.push.resize(200, 100)
        self.push.setText("Emergency Break")
        self.push.setFont(QFont('AnyStyle', 18))
        self.push.clicked.connect(self.pushedEmergency)
        #self.push.resize(400, 200)
        #self.push.move(0, 50)

        self.push.setStyleSheet(
            "background-color : red; border-radius: 5px; font-weight: bold; border: 3px solid black")
        # sshFile = "test.css"
        # with open(sshFile, "r") as fh:
        #     self.push.setStyleSheet(fh.read())
=======
        self.push.setText("Emergency Break")
        self.push.setFont(QFont('AnyStyle', 18))
        self.push.clicked.connect(self.pushedEmergency)

        self.push.setStyleSheet(qstr)
        self.push.resize(int(self.width), int(self.height))
>>>>>>> 088593597150e78bab5f05267d052282c28f0e0b

    def msgButtonClick(self, i):
        print("Button clicked is:", i.text())

    def pushedEmergency(self):
        self.fsm.setState('Emergency')

    def sizeHint(self):
        return QSize(int(self.width), int(self.height))
