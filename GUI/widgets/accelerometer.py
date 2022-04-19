from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

import constants


class Accelerometer(QWidget):
    def __init__(self, parent=None):
        super(Accelerometer, self).__init__(parent)
        self.initUI()

    def initUI(self):
        dial = QDial(self)
        # dial.setGeometry(100, 100, 100, 100)
        dial.setMinimum(0)
        dial.setMaximum(100)
        dial.setValue(constants.ACCELERATION)
        if constants.ACCELERATION > constants.ACCELERATION_THRESHOLD:
            dial.setStyleSheet("background-color : red")
        else:
            dial.setStyleSheet("background-color : green")
        # label = QLabel(self)
        # label.setText("Current Velocity: " +
        #               str(constants.CURRENT_VELOCITY) + " m/s")
        # label.setGeometry(220, 125, 200, 60)
        # label.setWordWrap(True)

        vbox = QVBoxLayout()

        vbox.addWidget(dial)
        # vbox.addWidget(label)
        self.setLayout(vbox)