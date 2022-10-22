from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from widgets import *
from PyQt5.QtGui import *
import pyqtgraph as pg


class BatteryPage(QWidget):
    def __init__(self, *args, **kwargs):
        super(BatteryPage, self).__init__()

        
        hbox = QVBoxLayout(self)

        battery1 = Battery(1)
        battery2 = Battery(2)
        battery3 = Battery(3)
        battery4 = Battery(4)
        battery5 = Battery(5)
        battery6 = Battery(6)

        hbox.addWidget(battery1)
        hbox.addWidget(battery2)
        hbox.addWidget(battery3)
        hbox.addWidget(battery4)
        hbox.addWidget(battery5)
        hbox.addWidget(battery6)


        self.setLayout(hbox)
