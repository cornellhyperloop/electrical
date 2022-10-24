from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

from constants import BATTERY_MAXIMUM_TEMP, BATTERY_CURRENT_TEMP, BATTERY_1, BATTERY_2, BATTERY_3, BATTERY_4, BATTERY_5, BATTERY_6, BATTERY_7, BATTERY_8


class Battery(QWidget):
    def __init__(self, parent=None):
        super(Battery, self).__init__(parent)
        self.initUI()

    def initUI(self):
        battery = QLabel(self)
        temperature = QLabel(self)
        maxtemp = QLabel(self)
        avgtemp = QLabel(self)

        battery.setText("Battery")
        battery.setAlignment(Qt.AlignCenter)
        battery.setStyleSheet("font-weight: bold; background-color : #2B26c1")

        temperature.setText("Current: " + str(BATTERY_CURRENT_TEMP) + " °C")
        temperature.setStyleSheet("background-color : #2B26c1")
        temperature.setAlignment(Qt.AlignCenter)

        maxtemp.setText("Max: " + str(BATTERY_MAXIMUM_TEMP) + " °C")
        maxtemp.setStyleSheet("background-color : #2B26c1")
        maxtemp.setAlignment(Qt.AlignCenter)

        avg = (BATTERY_1 + BATTERY_2 + BATTERY_3 + BATTERY_4 +
               BATTERY_5 + BATTERY_6 + BATTERY_7 + BATTERY_8) / 8
        avgtemp.setText("Average: " + str(avg) + " °C")
        avgtemp.setStyleSheet("background-color : #2B26c1")
        avgtemp.setAlignment(Qt.AlignCenter)

        vbox = QVBoxLayout()

        vbox.addWidget(battery)
        vbox.addWidget(maxtemp)
        vbox.addWidget(temperature)
        vbox.addWidget(avgtemp)

        self.setLayout(vbox)
#this is a comment
