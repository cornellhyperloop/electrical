from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import QSize
import sys
import constants as cons


class HelpPopup(QWidget):
    def __init__(self, *args, parent=None):
        super(HelpPopup, self).__init__(parent)
        self.width = args[0] / 10
        self.height = args[1] / 30
        self.initUI()

    def initUI(self):
        widFile = cons.WIDGETS
        with open(widFile, "r") as fh:
            qstr = str(fh.read())
        
        self.setWindowTitle("Click button")
        self.push = QPushButton(self)
        self.push.setText("Help")
        self.push.setFont(QFont('AnyStyle', 18))
        self.push.setStyleSheet(qstr)
        self.push.clicked.connect(self.pushedHelp)
        self.push.resize(int(self.width), int(self.height))

    def pushedHelp(self):
        self.msgBox = QMessageBox()
        self.msgBox.setWindowTitle("Tutorial on using GUI")
        self.msgBox.setText(
            "Click on the various buttons in order to receive more information about them. On the top you may visualize the design of the pod with the visualizer button, get battery information, check the temperature graphs, and view the state of the pod from the FSM page. On the bottom you may edit the graph of the data, being live plotted.")
        self.msgBox.setIcon(QMessageBox.Information)
        x = self.msgBox.exec()

    def sizeHint(self):
        return QSize(int(self.width), int(self.height))
