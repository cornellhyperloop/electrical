from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

from constants import BATTERY, VOLTAGE, CURRENT


class Battery(QWidget):
    def __init__(self, battNum, parent=None):
        super(Battery, self).__init__(parent)
        self.initUI(battNum)

    def initUI(self, battNum):
        cssFile = "utils/body.css"
        with open(cssFile, "r") as fh:
            qstr = str(fh.read())
        
        battery = QLabel(self)
        temperature = QLabel(self)
        current = QLabel(self)
        voltage = QLabel(self)

        battery.setText("Cell " + str(battNum))
        battery.setAlignment(Qt.AlignCenter)
        battery.setStyleSheet(
            "font-family: Helvetica; font-size: 14px; background-color : #2B26c1;")

        if (battNum <= 5):
            temperature.setText(f"Temperature: {BATTERY[battNum-1]} °C")
            voltage.setText(f"Voltage: {VOLTAGE[battNum-1]} V")
            current.setText(f"Current: {CURRENT[battNum-1]} A")

        else:
            battery.setText("Averages ")
            avgTemp = (BATTERY[0] + BATTERY[1] +
                       BATTERY[2] + BATTERY[3] + BATTERY[4])/5
            temperature.setText(f"Average Temperature: {avgTemp} °C")
            avgVolt = (VOLTAGE[0] + VOLTAGE[1]+
                       VOLTAGE[2] + VOLTAGE[3] + VOLTAGE[4])/5
            voltage.setText(f"Average Voltage: {avgVolt} V")
            avgCurrent = (CURRENT[0] + CURRENT[1] +
                          CURRENT[2]+ CURRENT[3]+ CURRENT[4])/5
            current.setText(f"Average Current: {avgCurrent} A")

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
        self.setStyleSheet(qstr)
