from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

import constants


class Speed(QWidget):
    def __init__(self, parent=None):
        super(Speed, self).__init__(parent)
        self.initUI()

    def initUI(self):
<<<<<<< HEAD
=======
        widFile = constants.WIDGETS
        with open(widFile, "r") as fh:
            qstr = str(fh.read())

>>>>>>> 088593597150e78bab5f05267d052282c28f0e0b
        self.setObjectName("display")
        self.velocity = QLabel(self)
        self.acceleration = QLabel(self)

        self.velocity.setText("Current Velocity: " +
                              str(constants.CURRENT_VELOCITY) + " m/s")
<<<<<<< HEAD
        self.velocity.setStyleSheet("background-color : #2B26c1")
=======
        self.velocity.setStyleSheet(qstr)
>>>>>>> 088593597150e78bab5f05267d052282c28f0e0b
        self.velocity.setAlignment(Qt.AlignCenter)

        self.acceleration.setText("Current Acceleration: " +
                                  str(constants.ACCELERATION) + " m/s²")
<<<<<<< HEAD
        self.acceleration.setStyleSheet("background-color : #2B26c1")
=======
        self.acceleration.setStyleSheet(qstr)
>>>>>>> 088593597150e78bab5f05267d052282c28f0e0b
        self.acceleration.setAlignment(Qt.AlignCenter)

        hbox = QHBoxLayout()
        splitter = QSplitter(Qt.Horizontal)

        hbox.addWidget(self.velocity)
        hbox.addWidget(self.acceleration)

        self.setLayout(hbox)
        self.timer = QTimer(self, timeout=self.update)
        self.timer.start(1000)

    def update(self):
        self.velocity.setText("Current Velocity: " +
                              str(constants.CURRENT_VELOCITY) + " m/s")
        self.acceleration.setText(
            "Current Acceleration: " + str(constants.ACCELERATION) + " m/s")
