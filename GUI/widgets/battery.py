from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

from constants import BATTERY, VOLTAGE, CURRENT


class Battery(QWidget):
    def __init__(self, battNum, parent=None):
        super(Battery, self).__init__(parent)
        self.initUI(battNum)

    def initUI(self, battNum):
        battery = QLabel(self)
        temperature = QLabel(self)
        current = QLabel(self)
        voltage = QLabel(self)

        battery.setText("Cell " + str(battNum))
        battery.setAlignment(Qt.AlignCenter)
<<<<<<< HEAD
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
=======
        battery.setStyleSheet(
            "font-family: Helvetica; font-size: 14px; background-color : #2B26c1")

        if (battNum <= 5):
            temperature.setText("Temperature: " + str(BATTERY[battNum-1]) + " °C")
            voltage.setText("Voltage: " + str(VOLTAGE[battNum-1]))
            current.setText("Current: " + str(CURRENT[battNum-1]))

        else:
            battery.setText("Averages ")
            avgTemp = (BATTERY[0] + BATTERY[1] +
                       BATTERY[2] + BATTERY[3] + BATTERY[4])/5
            temperature.setText("Average Temperature: " + str(avgTemp) + " °C")
            avgVolt = (VOLTAGE[0] + VOLTAGE[1]+
                       VOLTAGE[2] + VOLTAGE[3] + VOLTAGE[4])/5
            voltage.setText("Average Voltage: " + str(avgVolt))
            avgCurrent = (CURRENT[0] + CURRENT[1] +
                          CURRENT[2]+ CURRENT[3]+ CURRENT[4])/5
            current.setText("Average Current: " + str(avgCurrent))

        temperature.setAlignment(Qt.AlignCenter)
        current.setAlignment(Qt.AlignCenter)
        voltage.setAlignment(Qt.AlignCenter)

        temperature.setStyleSheet("background-color : #2B26c1")
        voltage.setStyleSheet("background-color : #2B26c1")
        current.setStyleSheet("background-color : #2B26c1")
>>>>>>> 088593597150e78bab5f05267d052282c28f0e0b

        vbox = QHBoxLayout()
        vbox2 = QVBoxLayout()

        vbox2.addWidget(voltage)
        vbox2.addWidget(temperature)
        vbox2.addWidget(current)
        vbox.addWidget(battery)

        vbox.addLayout(vbox2)

        self.setLayout(vbox)
