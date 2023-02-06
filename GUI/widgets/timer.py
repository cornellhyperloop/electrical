from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import QTimer, QTime, Qt, QSize
import sys
import constants as cons


class Timer(QWidget):


    def __init__(self, *args, parent=None):
        super(Timer, self).__init__(parent)
        self.width = int(args[0] / 10)
        self.height = int(args[0] / 30)
        self.initUI()

    def initUI(self):
        widFile = cons.WIDGETS
        with open(widFile, "r") as fh:
            qstr = str(fh.read())

        self.count = 0
        self.start = True
        self.label = QLabel("         Time         ", self)
        self.label.setAlignment(Qt.AlignCenter)
<<<<<<< HEAD
        self.label.setFont(QFont('AnyStyle', 12))
        self.label.setStyleSheet("background-color: grey; color: black")
=======
        self.label.setStyleSheet(qstr)
        self.label.resize(int(self.width), int(self.height))
>>>>>>> 088593597150e78bab5f05267d052282c28f0e0b
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.showTime)
        self.timer.start(100)

    def showTime(self):
        self.count += 1
        text = f'Time: {self.count / 10} s'
<<<<<<< HEAD
        #text = '' + str(self.count / 10) + " s"
=======
>>>>>>> 088593597150e78bab5f05267d052282c28f0e0b
        self.label.setText(text)
        self.label.update()

    def sizeHint(self):
        return QSize(int(self.width), int(self.height))
