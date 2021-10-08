from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

from constants import BATTERY_MAXIMUM_TEMP, BATTERY_CURRENT_TEMP

class Battery(QWidget):
    def __init__(self, parent=None):
        super(Battery, self).__init__(parent)
        self.initUI()

    def initUI(self):
        battery = QLabel(self)
        temperature = QLabel(self)
        maxtemp = QLabel(self)

        battery.setText("Battery")
        battery.setAlignment(Qt.AlignCenter)
        battery.setStyleSheet("font-weight: bold")

        temperature.setText("Current: " + str(BATTERY_CURRENT_TEMP) + " °C")
        temperature.setStyleSheet("background-color : rgb(143,255,91)")
        temperature.setAlignment(Qt.AlignCenter)

        maxtemp.setText("Max: " + str(BATTERY_MAXIMUM_TEMP) + " °C")
        maxtemp.setStyleSheet("background-color : rgb(143,255,91)")
        maxtemp.setAlignment(Qt.AlignCenter)

        vbox = QVBoxLayout()

        vbox.addWidget(battery)
        vbox.addWidget(maxtemp)
        vbox.addWidget(temperature)

        self.setLayout(vbox)