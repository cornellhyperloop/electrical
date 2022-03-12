from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

import constants


class PressureSensor(QWidget):
    def __init__(self, parent=None):
        super(PressureSensor, self).__init__(parent)
        self.initUI()

    def initUI(self):
        absolute = QLabel(self)
        relative = QLabel(self)
        altitude = QLabel(self)

        absolute.setText("Absolute Pressure: " +
                         str(constants.ABSOLUTE_PRESSURE) + " inHg")
        absolute.setStyleSheet("background-color : rgb(143,255,91)")
        absolute.setAlignment(Qt.AlignCenter)

        relative.setText("Relative Pressure: " +
                         str(constants.RELATIVE_PRESSURE) + " inHg")
        relative.setStyleSheet("background-color : rgb(143,255,91)")
        relative.setAlignment(Qt.AlignCenter)

        altitude.setText("Altitude: " + str(constants.ALTITUDE) + " ft")
        altitude.setStyleSheet("background-color : rgb(143,255,91)")
        altitude.setAlignment(Qt.AlignCenter)

        vbox = QVBoxLayout()

        vbox.addWidget(absolute)
        vbox.addWidget(relative)
        vbox.addWidget(altitude)

        self.setLayout(vbox)
