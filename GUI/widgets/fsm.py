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
        #self.fsm.run()

    def initUI(self):
        self.state = QLabel(self)

        self.state.setText("Current State: " + constants.CURRENT_STATE)
        self.state.setAlignment(Qt.AlignCenter)
        self.state.setFont(QFont('AnyStyle', 12))
        self.state.setStyleSheet("background-color : #2B26c1")

        vbox = QVBoxLayout()

        vbox.addWidget(self.state)

        self.setLayout(vbox)

        # Automatically update the displayed FSM state frequently
        self.timerFSM = QTimer(self, timeout=self.updateStateText)
        self.timerFSM.start(100)

        # Use a timer to randomly change state for testing purposes
        self.timerFSMRand = QTimer(self, timeout=self.update)
        self.timerFSMRand.start(2000)
        
    def update(self):
        newState = self.fsm.allStates[random.randint(0, len(self.fsm.allStates) - 1)]
        self.fsm.setState(newState)

    def updateStateText(self):
        self.state.setText(f'Current State: {self.fsm.getState()}')

