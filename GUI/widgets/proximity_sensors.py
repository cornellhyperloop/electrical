from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import constants


class ProximitySensor(QWidget):
    def __init__(self, parent=None):
        super(ProximitySensor, self).__init__(parent)
        self.initUI()

    def initUI(self):
        widFile = constants.WIDGETS
        with open(widFile, "r") as fh:
            qstr = str(fh.read())

        sensor1 = QLabel(self)
        sensor2 = QLabel(self)
        sensor3 = QLabel(self)
        sensor4 = QLabel(self)

        sensor1.setText("Proximity Sensor 1: " +
                        constants.PROXIMITY_SENSOR_STATE1)
        sensor1.setAlignment(Qt.AlignCenter)
        sensor1.setStyleSheet(qstr)

        sensor2.setText("Proximity Sensor 2: " +
                        constants.PROXIMITY_SENSOR_STATE2)
        sensor2.setAlignment(Qt.AlignCenter)
        sensor2.setStyleSheet(qstr)

        sensor3.setText("Proximity Sensor 3: " +
                        constants.PROXIMITY_SENSOR_STATE3)
        sensor3.setAlignment(Qt.AlignCenter)
        sensor3.setStyleSheet(qstr)

        sensor4.setText("Proximity Sensor 4: " +
                        constants.PROXIMITY_SENSOR_STATE4)
        sensor4.setAlignment(Qt.AlignCenter)
        sensor4.setStyleSheet(qstr)

        vbox = QVBoxLayout()

        vbox.addWidget(sensor1)
        vbox.addWidget(sensor2)
        vbox.addWidget(sensor3)
        vbox.addWidget(sensor4)

        self.setLayout(vbox)
