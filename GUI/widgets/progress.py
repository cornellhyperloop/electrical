from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import QTimer, QTime, Qt, QSize
import sys


class Progress(QWidget):
    def __init__(self, *args, parent=None):
        super(Progress, self).__init__(parent)
        self.width = args[0] / 10
        self.height = args[1] / 30
        self.initUI()

    def initUI(self):
        self.pBar = QProgressBar(self)
        self.pBar.resize(int(self.width), int(self.height))

    def update(self):
        self.pBar.setValue(self.pBar.value() + 5)

    def sizeHint(self):
      return QSize(int(self.width), int(self.height))
