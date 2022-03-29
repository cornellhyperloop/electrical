from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from utils import stateMachine
import constants


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
        self.state.setStyleSheet("background-color : rgb(143,255,91)")

        vbox = QVBoxLayout()

        vbox.addWidget(self.state)

        self.setLayout(vbox)
    
    def changeState(self, newState):
        self.state.setText(f'Current State: {newState}')

