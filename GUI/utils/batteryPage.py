from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from widgets import *
from PyQt5.QtGui import *
import pyqtgraph as pg


class BatteryPage(QWidget):
    def __init__(self, *args, **kwargs):
        super(BatteryPage, self).__init__()

        hbox = QVBoxLayout(self)
        for i in range(1, 7):
            hbox.addWidget(Battery(i))

        self.setLayout(hbox)
