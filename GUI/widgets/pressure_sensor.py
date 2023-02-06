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
<<<<<<< HEAD
        absolute.setStyleSheet("background-color : #2B26c1")
=======
        absolute.setStyleSheet(
            "font-family: Helvetica; font-size: 14px; background-color : #2B26c1")
>>>>>>> 088593597150e78bab5f05267d052282c28f0e0b
        absolute.setAlignment(Qt.AlignCenter)

        relative.setText("Relative Pressure: " +
                         str(constants.RELATIVE_PRESSURE) + " inHg")
<<<<<<< HEAD
        relative.setStyleSheet("background-color : #2B26c1")
        relative.setAlignment(Qt.AlignCenter)

        altitude.setText("Altitude: " + str(constants.ALTITUDE) + " ft")
        altitude.setStyleSheet("background-color : #2B26c1")
=======
        relative.setStyleSheet(
            "font-family: Helvetica; font-size: 14px; background-color : #2B26c1")
        relative.setAlignment(Qt.AlignCenter)

        altitude.setText("Altitude: " + str(constants.ALTITUDE) + " ft")
        altitude.setStyleSheet(
            "font-family: Helvetica; font-size: 14px; background-color : #2B26c1")
>>>>>>> 088593597150e78bab5f05267d052282c28f0e0b
        altitude.setAlignment(Qt.AlignCenter)

        vbox = QVBoxLayout()

        vbox.addWidget(absolute)
        vbox.addWidget(relative)
        vbox.addWidget(altitude)

        self.setLayout(vbox)
