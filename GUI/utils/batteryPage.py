from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from widgets import *
from PyQt5.QtGui import *
import pyqtgraph as pg


class BatteryPage(QWidget):
    def __init__(self, *args, **kwargs):
        super(BatteryPage, self).__init__()

        
        hbox = QVBoxLayout(self)
        # lay2 = QVBoxLayout() 

        battery1 = Battery(1)
        battery2 = Battery(2)
        battery3 = Battery(3)
        battery4 = Battery(4)
        battery5 = Battery(5)
        battery6 = Battery(6)


        # lay2.addWidget(battery1)
        # lay2.addWidget(battery2)
        # lay2.addWidget(battery3)
        # lay2.addWidget(battery4)
        # lay2.addWidget(battery5)

        # for i in range (1, 6):
        #     battery = Battery(i)
        #     # battery.__init__(self, i)
        hbox.addWidget(battery1)
        hbox.addWidget(battery2)
        hbox.addWidget(battery3)
        hbox.addWidget(battery4)
        hbox.addWidget(battery5)
        hbox.addWidget(battery6)


        self.setLayout(hbox)


        # self.setLayout(hbox)
        # 5 different cells
        # for each cell: voltage, temperature, and current_temp 
        # at the top: display average for volt, temp, and current_temp

        
