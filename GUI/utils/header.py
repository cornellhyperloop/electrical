from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from widgets import *


class Header(QWidget):
    def __init__(self, *args, **kwargs):
        super(Header, self).__init__()
        hbox = QHBoxLayout(self)
        sshFile = "utils/header.css"
        with open(sshFile, "r") as fh:
            qstr = str(fh.read())

        splitter1 = QSplitter(Qt.Horizontal)

        quit = Quit()
        splitter1.addWidget(quit)

        fsm = FSM()

        emergency_button = EmergencyButton(fsm)
        splitter1.addWidget(emergency_button)
        splitter1.setSizes([2, 2])

        splitter1.addWidget(fsm)
        splitter1.setSizes([1, 1])

        help = HelpPopup()
        splitter1.addWidget(help)
        splitter1.setSizes([2, 2, 1, 50])

        timer = Timer()
        splitter1.addWidget(timer)
        splitter1.setSizes([200, 600, 200, 200])

        splitter2 = QSplitter(Qt.Horizontal)
        battery = Battery()
        battery.setStyleSheet(qstr)
        splitter2.addWidget(battery)
        proximitySensor = ProximitySensor()
        proximitySensor.setStyleSheet(qstr)
        splitter2.addWidget(proximitySensor)
        vibrationSensor = VibrationSensor()
        vibrationSensor.setStyleSheet(qstr)
        splitter2.addWidget(vibrationSensor)
        pressureSensor = PressureSensor()
        pressureSensor.setStyleSheet(qstr)
        splitter2.addWidget(pressureSensor)
        fsm = FSM()
        ldrf = LongDistanceRangefinder()
        splitter2.addWidget(ldrf)
        splitter2.setSizes([2, 2, 1, 50])

        splitter3 = QSplitter(Qt.Vertical)
        splitter3.addWidget(splitter1)
        splitter3.addWidget(splitter2)
        splitter3.setSizes([50, 100])

        hbox.addWidget(splitter3)
        self.setStyleSheet(qstr)
