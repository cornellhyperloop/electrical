from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

import constants


class Speed(QWidget):
    def __init__(self, parent=None):
        super(Speed, self).__init__(parent)
        self.initUI()

    def initUI(self):
        sshFile = "widgets/widgets.css"
        with open(sshFile, "r") as fh:
            qstr = str(fh.read())

        self.setObjectName("display")
        self.velocity = QLabel(self)
        self.acceleration = QLabel(self)

        self.velocity.setText("Current Velocity: " +
                              str(constants.CURRENT_VELOCITY) + " m/s")
        self.velocity.setStyleSheet(qstr)
        self.velocity.setAlignment(Qt.AlignCenter)

        self.acceleration.setText("Current Acceleration: " +
                                  str(constants.ACCELERATION) + " m/s²")
        self.acceleration.setStyleSheet(qstr)
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
