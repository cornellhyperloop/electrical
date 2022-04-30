from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

import constants


class Speed(QWidget):
    def __init__(self, parent=None):
        super(Speed, self).__init__(parent)
        self.initUI()

    def initUI(self):
        self.setObjectName("display")
        velocity = QLabel(self)
        acceleration = QLabel(self)

        velocity.setText("Current Velocity: " +
                         str(constants.CURRENT_VELOCITY) + " m/s")
        velocity.setStyleSheet("background-color : rgb(143,255,91)")
        velocity.setAlignment(Qt.AlignCenter)

        acceleration.setText("Current Acceleration: " +
                             str(constants.ACCELERATION) + " m/s²")
        acceleration.setStyleSheet("background-color : rgb(143,255,91)")
        acceleration.setAlignment(Qt.AlignCenter)

        hbox = QHBoxLayout()
        splitter = QSplitter(Qt.Horizontal)

        hbox.addWidget(velocity)
        hbox.addWidget(acceleration)

        self.setLayout(hbox)
