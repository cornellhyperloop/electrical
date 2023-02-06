from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import constants


class VibrationSensor(QWidget):
    def __init__(self, parent=None):
        super(VibrationSensor, self).__init__(parent)
        self.initUI()

    def initUI(self):
        sensor = QLabel(self)

<<<<<<< HEAD
    sensor.setText("Vibration Sensor: " + constants.VIBRATIONLEVEL)
    sensor.setAlignment(Qt.AlignCenter)
    sensor.setStyleSheet("background-color : #2B26c1")
=======
        sensor.setText("Vibration Sensor: " + constants.VIBRATIONLEVEL)
        sensor.setAlignment(Qt.AlignCenter)
        sensor.setStyleSheet(
            "font-family: Helvetica; font-size: 14px; background-color : #2B26c1")
>>>>>>> 088593597150e78bab5f05267d052282c28f0e0b

        vbox = QVBoxLayout()

        vbox.addWidget(sensor)

        self.setLayout(vbox)
