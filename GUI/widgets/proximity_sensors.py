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
<<<<<<< HEAD
        sensor1.setStyleSheet("background-color : #2B26c1")
=======
        sensor1.setStyleSheet(qstr)
>>>>>>> 088593597150e78bab5f05267d052282c28f0e0b

        sensor2.setText("Proximity Sensor 2: " +
                        constants.PROXIMITY_SENSOR_STATE2)
        sensor2.setAlignment(Qt.AlignCenter)
<<<<<<< HEAD
        sensor2.setStyleSheet("background-color : #2B26c1")
=======
        sensor2.setStyleSheet(qstr)
>>>>>>> 088593597150e78bab5f05267d052282c28f0e0b

        sensor3.setText("Proximity Sensor 3: " +
                        constants.PROXIMITY_SENSOR_STATE3)
        sensor3.setAlignment(Qt.AlignCenter)
<<<<<<< HEAD
        sensor3.setStyleSheet("background-color : #2B26c1")
=======
        sensor3.setStyleSheet(qstr)
>>>>>>> 088593597150e78bab5f05267d052282c28f0e0b

        sensor4.setText("Proximity Sensor 4: " +
                        constants.PROXIMITY_SENSOR_STATE4)
        sensor4.setAlignment(Qt.AlignCenter)
<<<<<<< HEAD
        sensor4.setStyleSheet("background-color : #2B26c1")
=======
        sensor4.setStyleSheet(qstr)
>>>>>>> 088593597150e78bab5f05267d052282c28f0e0b

        vbox = QVBoxLayout()

        vbox.addWidget(sensor1)
        vbox.addWidget(sensor2)
        vbox.addWidget(sensor3)
        vbox.addWidget(sensor4)

        self.setLayout(vbox)
