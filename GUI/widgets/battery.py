from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

from constants import BATTERY_1, BATTERY_2, BATTERY_3, BATTERY_4, BATTERY_5, VOLTAGE_BATT_1, VOLTAGE_BATT_2, VOLTAGE_BATT_3, VOLTAGE_BATT_4, VOLTAGE_BATT_5, CURRENT_BATT_1, CURRENT_BATT_2, CURRENT_BATT_3, CURRENT_BATT_4, CURRENT_BATT_5


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
        battery.setStyleSheet("font-weight: bold; background-color : #2B26c1")
        
        if(battNum == 1):
            temperature.setText("Temperature: " + str(BATTERY_1) + " °C")
            voltage.setText("Voltage: " + str(VOLTAGE_BATT_1))
            current.setText("Current: " + str(CURRENT_BATT_1))
        elif(battNum == 2):
            temperature.setText("Temperature: " + str(BATTERY_2) + " °C")
            voltage.setText("Voltage: " + str(VOLTAGE_BATT_2))
            current.setText("Current: " + str(CURRENT_BATT_2))
        elif(battNum == 3):
            temperature.setText("Temperature: " + str(BATTERY_3) + " °C")
            voltage.setText("Voltage: " + str(VOLTAGE_BATT_3))
            current.setText("Current: " + str(CURRENT_BATT_3))
        elif(battNum == 4):
            temperature.setText("Temperature: " + str(BATTERY_4) + " °C")
            voltage.setText("Voltage: " + str(VOLTAGE_BATT_4))
            current.setText("Current: " + str(CURRENT_BATT_4))
        elif(battNum == 5):
            temperature.setText("Temperature: " + str(BATTERY_5) + " °C")
            voltage.setText("Voltage: " + str(VOLTAGE_BATT_5))
            current.setText("Current: " + str(CURRENT_BATT_5))
        else:
            battery.setText("Averages ")
            avgTemp = (BATTERY_1 + BATTERY_2 + BATTERY_3 + BATTERY_4 + BATTERY_5)/5
            temperature.setText("Average Temperature: " + str(avgTemp) + " °C")
            avgVolt = (VOLTAGE_BATT_1 + VOLTAGE_BATT_2 + VOLTAGE_BATT_3 + VOLTAGE_BATT_4 + VOLTAGE_BATT_5)/5
            voltage.setText("Average Voltage: " + str(avgVolt))
            avgCurrent = (CURRENT_BATT_1 + CURRENT_BATT_2 + CURRENT_BATT_3 + CURRENT_BATT_4 + CURRENT_BATT_5)/5
            current.setText("Average Current: " + str(avgCurrent))

        temperature.setAlignment(Qt.AlignCenter)
        current.setAlignment(Qt.AlignCenter)
        voltage.setAlignment(Qt.AlignCenter)

        temperature.setStyleSheet("background-color : #2B26c1")
        voltage.setStyleSheet("background-color : #2B26c1")
        current.setStyleSheet("background-color : #2B26c1")

        vbox = QHBoxLayout()
        vbox2 = QVBoxLayout()

        
        vbox2.addWidget(voltage)
        vbox2.addWidget(temperature)
        vbox2.addWidget(current)
        vbox.addWidget(battery)

        vbox.addLayout(vbox2)

        self.setLayout(vbox)
