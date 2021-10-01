from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class Battery(QWidget):
    def __init__(self, parent=None):
        super(Battery, self).__init__(parent)
        self.initUI()

    def initUI(self):
        battery = QLabel(self)
        volts = QLabel(self)
        amps = QLabel(self)
        temperature = QLabel(self)
        maxtemp = QLabel(self)

        battery.setText("Battery")
        battery.setAlignment(Qt.AlignCenter)
        battery.setStyleSheet("font-weight: bold")

        volts.setText("?? Volts")
        volts.setStyleSheet("background-color : rgb(143,255,91)")
        volts.setAlignment(Qt.AlignCenter)

        amps.setText("?? Amps")
        amps.setStyleSheet("background-color : rgb(143,255,91)")
        amps.setAlignment(Qt.AlignCenter)

        temperature.setText("?? °C")
        temperature.setStyleSheet("background-color : rgb(143,255,91)")
        temperature.setAlignment(Qt.AlignCenter)

        maxtemp.setText("?? °C")
        maxtemp.setStyleSheet("background-color : rgb(143,255,91)")
        maxtemp.setAlignment(Qt.AlignCenter)

        vbox = QVBoxLayout()

        vbox.addWidget(battery)
        vbox.addWidget(volts)
        vbox.addWidget(amps)
        vbox.addWidget(maxtemp)
        vbox.addWidget(temperature)

        self.setLayout(vbox)