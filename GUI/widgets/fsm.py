from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from utils import stateMachine
import constants
import random


class FSM(QWidget):
    def __init__(self, parent=None):
        super(FSM, self).__init__(parent)
        self.initUI()
        self.fsm = stateMachine.FSM()
        # self.fsm.run()

    def initUI(self):
        self.state = QLabel(self)

        self.state.setText("Current State: " + constants.CURRENT_STATE)
        self.state.setAlignment(Qt.AlignCenter)
        self.im = QPixmap(constants.STATES[constants.CURRENT_STATE])
        self.im = self.im.scaled(
            50, 50, Qt.KeepAspectRatio, Qt.FastTransformation)
        self.label = QLabel()
        self.label.setPixmap(self.im)
        self.label.setFixedWidth(50)
        self.label.setFixedHeight(50)
        vbox = QVBoxLayout()

        vbox.addWidget(self.state)
        vbox.addWidget(self.label)

        self.setLayout(vbox)

        # Automatically update the displayed FSM state frequently
        self.timerFSM = QTimer(self, timeout=self.updateStateText)
        self.timerFSM.start(100)

        # Use a timer to randomly change state for testing purposes
        self.timerFSMRand = QTimer(self, timeout=self.update)
        self.timerFSMRand.start(2000)

    def update(self):
        newState = self.fsm.allStates[random.randint(
            0, len(self.fsm.allStates) - 1)]
        self.fsm.setState(newState)

    def updateStateText(self):
        self.state.setText(f'Current State: {self.fsm.getState()}')
