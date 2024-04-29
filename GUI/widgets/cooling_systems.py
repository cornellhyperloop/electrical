from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import constants
import sys

class CoolingSystem(QWidget):
    def __init__(self,parent = None):
        super(CoolingSystem,self).__init__(parent)
        self.initUI()

    def initUI(self):
        system1 = Qlabel(self)
        system2 = Qlabel(self)
        system3 = Qlabel(self)

        system1.setText("Cooling System 1: " +
                        constants.SYSTEM1_STATE)
        system1.setAlignment(Qt.AlignCenter)
        system1.setStyleSheet("background-color : #2B26c1")

        system2.setText("Cooling System 2: " +
                        constants.SYSTEM2_STATE)
        system2.setAlignment(Qt.AlignCenter)
        system2.setStyleSheet("background-color : #2B26c1")

        system3.setText("Cooling System 2: " +
                        constants.SYSTEM3_STATE)
        system3.setAlignment(Qt.AlignCenter)
        system3.setStyleSheet("background-color : #2B26c1")
        
        
        vbox = QVBoxLayout()
        vbox.addWidget(system1)
        vbox.addWidget(system2)
        vbox.addWidget(system3)

        self.setLayout(vbox)

