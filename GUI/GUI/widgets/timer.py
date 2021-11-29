from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import QTimer, QTime, Qt
import sys


class Timer(QWidget):
    def __init__(self, parent=None):
        super(Timer, self).__init__(parent)
        self.initUI()

    def initUI(self):
        self.count = 0
        self.start = True
        self.label = QLabel("                      ", self)
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setFont(QFont('AnyStyle', 12))
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.showTime)
        self.timer.start(100)

    def showTime(self):
        self.count += 1
        text = f'Time: {self.count / 10} s'
	#text = '' + str(self.count / 10) + " s"
        self.label.setText(text)
