from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from widgets import *

class Example1(QWidget):
    def __init__(self, parent=None):
        super(Example1, self).__init__(parent)
        # self.button = QPushButton(self)
        # self.button.setText('Button 1')
        # self.button.setFont(QFont('AnyStyle', 18))
        # self.button.setStyleSheet(
        #     "background-color : red; border-radius: 5px; font-weight: bold; border: 3px solid black")
        
        hbox = QHBoxLayout(self)
        sshFile = "utils/header.css"
        with open(sshFile, "r") as fh:
            qstr = str(fh.read())

            splitter2 = QSplitter(Qt.Horizontal)
            vibrationSensor = VibrationSensor()
            vibrationSensor.setStyleSheet(qstr)
            splitter2.addWidget(vibrationSensor)
            pressureSensor = PressureSensor()
            pressureSensor.setStyleSheet(qstr)
            splitter2.addWidget(pressureSensor)
            ldrf = LongDistanceRangefinder()
            splitter2.addWidget(ldrf)

            fsm = FSM()     
            splitter2.setSizes([10, 10, 60])

            hbox.addWidget(splitter2)
            self.setStyleSheet(qstr)

        fh.close()
