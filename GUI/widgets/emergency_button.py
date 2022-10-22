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
        self.setWindowTitle("Click button")
        self.push = QPushButton(self)
        #self.push.resize(200, 100)
        self.push.setText("Emergency Break")
        self.push.setFont(QFont('AnyStyle', 18))
        self.push.clicked.connect(self.pushedEmergency)
        #self.push.resize(400, 200)
        #self.push.move(0, 50)

        self.push.setStyleSheet(
            "background-color : red; border-radius: 5px; font-family: Helvetica; font-size: 14px; border: 3px solid black")
        self.push.resize(int(self.width), int(self.height))
        # sshFile = "test.css"
        # with open(sshFile, "r") as fh:
        #     self.push.setStyleSheet(fh.read())

    def msgButtonClick(self, i):
        print("Button clicked is:", i.text())

    def pushedEmergency(self):
        # self.msgBox = QMessageBox()
        # self.msgBox.setIcon(QMessageBox.Information)
        # self.msgBox.setText("Do you want to terminate program?")
        # self.msgBox.setWindowTitle("Emergency Button Pushed!")
        # self.msgBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        # self.msgBox.buttonClicked.connect(self.msgButtonClick)

        # returnValue = self.msgBox.exec()
        # if returnValue == QMessageBox.Ok:
        #     print('OK clicked')
        #     sys.exit()
        # else:
        #     print("Action cancelled")

        self.fsm.fsm.setState('Emergency')

    def sizeHint(self):
        return QSize(int(self.width), int(self.height))
