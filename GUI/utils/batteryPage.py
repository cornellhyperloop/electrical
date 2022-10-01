from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from widgets import *


class BatteryPage(QWidget):
    def __init__(self, *args, **kwargs):
        super(BatteryPage, self).__init__()

        # 5 different cells
        # for each cell: voltage, temperature, and current_temp 
        # at the top: display average for volt, temp, and current_temp

        
