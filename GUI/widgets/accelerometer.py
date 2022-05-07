from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

import constants


class Accelerometer(QWidget):
    def __init__(self, parent=None):
        super(Accelerometer, self).__init__(parent)
        self.initUI()

    def initUI(self):
        self.dial = QDial(self)
        # dial.setGeometry(100, 100, 100, 100)
        self.dial.setMinimum(0)
        self.dial.setMaximum(100)
        self.dial.setValue(constants.ACCELERATION)
        if constants.ACCELERATION > constants.ACCELERATION_THRESHOLD:
            self.dial.setStyleSheet("background-color : red")
        else:
            self.dial.setStyleSheet("background-color : green")
        # label = QLabel(self)
        # label.setText("Current Velocity: " +
        #               str(constants.CURRENT_VELOCITY) + " m/s")
        # label.setGeometry(220, 125, 200, 60)
        # label.setWordWrap(True)

        vbox = QVBoxLayout()

        vbox.addWidget(self.dial)
        # vbox.addWidget(label)
        self.setLayout(vbox)
        self.timer = QTimer(self, timeout=self.update)
        self.timer.start(1000)

    def update(self):
        constants.ACCELERATION = self.dial.value()
        if self.dial.value() > constants.ACCELERATION_THRESHOLD:
            self.dial.setStyleSheet("background-color : red")
        else:
            self.dial.setStyleSheet("background-color : green")
