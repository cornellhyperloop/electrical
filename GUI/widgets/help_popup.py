from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import sys


class HelpPopup(QWidget):
    def __init__(self, parent=None):
        super(HelpPopup, self).__init__(parent)
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Click button")
        self.push = QPushButton(self)
        self.push.setText("Help")
        self.push.setFont(QFont('AnyStyle', 18))
        self.push.setStyleSheet(
            "background-color : rgb(45, 121, 252); border-radius: 5px; font-weight: bold; border: 3px solid red")
        self.push.clicked.connect(self.pushedHelp)
        #self.push.resize(400, 200)
        #self.push.move(0, 50)

    def pushedHelp(self):
        self.msgBox = QMessageBox()
        self.msgBox.setWindowTitle("Tutorial on using GUI")
        self.msgBox.setText(
            "Click on the various buttons in order to receive more information about them")
        self.msgBox.setIcon(QMessageBox.Information)
        x = self.msgBox.exec()
