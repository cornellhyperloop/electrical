from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

from constants import CURRENT_VELOCITY, ACCELERATION, PITCH, YAW, ROLL


class Motion(QWidget):
    def __init__(self, parent=None):
        super(Motion, self).__init__(parent)
        self.initUI()

    def initUI(self):
        velocity = QLabel(self)
        acceleration = QLabel(self)
        yaw = QLabel(self)
        pitch = QLabel(self)
        roll = QLabel(self)

        velocity.setText("V: " + str(CURRENT_VELOCITY))
        acceleration.setText("A: " + str(ACCELERATION))
        yaw.setText("Y: " + str(YAW))
        pitch.setText("P: " + str(PITCH))
        roll.setText("R: " + str(ROLL))

        vbox = QVBoxLayout()

        vbox.addWidget(velocity)
        vbox.addWidget(acceleration)
        vbox.addWidget(yaw)
        vbox.addWidget(pitch)
        vbox.addWidget(roll)

        self.setLayout(vbox)
