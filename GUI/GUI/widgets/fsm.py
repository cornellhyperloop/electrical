from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import constants


class FSM(QWidget):
    def __init__(self, parent=None):
        super(FSM, self).__init__(parent)
        self.initUI()

    def initUI(self):
        state = QLabel(self)

        state.setText("Current State: " + constants.CURRENT_STATE)
        state.setAlignment(Qt.AlignCenter)
        state.setStyleSheet("background-color : rgb(143,255,91)")

        vbox = QVBoxLayout()

        vbox.addWidget(state)

        self.setLayout(vbox)
