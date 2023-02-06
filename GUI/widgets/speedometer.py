from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

import constants


class Speedometer(QWidget):
    def __init__(self, parent=None):
        super(Speedometer, self).__init__(parent)
        self.initUI()

    def initUI(self):
        self.dial = QDial(self)
<<<<<<< HEAD
        # dial.setGeometry(100, 100, 100, 100)
=======
>>>>>>> 088593597150e78bab5f05267d052282c28f0e0b
        self.dial.setMinimum(0)
        self.dial.setMaximum(100)
        self.dial.setValue(constants.CURRENT_VELOCITY)
        if constants.CURRENT_VELOCITY > constants.VELOCITY_THRESHOLD:
            self.dial.setStyleSheet("background-color : yellow")
        else:
            self.dial.setStyleSheet("background-color : lime green")
<<<<<<< HEAD
        # label = QLabel(self)
        # label.setText("Current Velocity: " +
        #               str(constants.CURRENT_VELOCITY) + " m/s")
        # label.setGeometry(220, 125, 200, 60)
        # label.setWordWrap(True)
=======
>>>>>>> 088593597150e78bab5f05267d052282c28f0e0b

        vbox = QVBoxLayout()

        vbox.addWidget(self.dial)
<<<<<<< HEAD
        # vbox.addWidget(label)
=======
>>>>>>> 088593597150e78bab5f05267d052282c28f0e0b
        self.setLayout(vbox)
        self.timer = QTimer(self, timeout=self.update)
        self.timer.start(1000)

    def update(self):
        constants.CURRENT_VELOCITY = self.dial.value()
        if self.dial.value() > constants.ACCELERATION_THRESHOLD:
            self.dial.setStyleSheet("background-color : red")
        else:
            self.dial.setStyleSheet("background-color : green")
