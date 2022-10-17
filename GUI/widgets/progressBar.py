from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys
import time
import constants as cons


class ProgressBar(QWidget):
    def __init__(self, parent=None):
        super(ProgressBar, self).__init__(parent)
        self.initUI()

    def initUI(self):
        self.pBar= QProgressBar(self, minimum=0, maximum=100)
        self.pBar.setFont(QFont('Arial', 20))   
        self.pBar.setFixedWidth(250)
        self.count = 0
        self.start = True
        self.label = QLabel("Progress: ", self)
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setFont(QFont('AnyStyle', 15))
        self.label.setFixedWidth(75)
        self.label.setStyleSheet(cons.LABEL_STYLE_SHEET)
        self.show()
        self.pBar.show()

