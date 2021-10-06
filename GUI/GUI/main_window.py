from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

from widgets import *


class MainWindow(QWidget):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__()

        # Insert change here
        self.setWindowTitle("Hyperloop GUI")
        self.setStyleSheet("background-color : white")

        hbox = QHBoxLayout(self)

        # bottom = QFrame()
        # bottom.setFrameShape(QFrame.StyledPanel)

        splitter1 = QSplitter(Qt.Horizontal)
        #emergency_button = EmergencyButton()
        # splitter1.addWidget(emergency_button)
        #quit = Quit()
        # splitter1.addWidget(quit)
        #battery = Battery()
        # splitter1.addWidget(battery)
        # splitter1.setSizes([200])
        # hbox.addWidget(splitter1)
        #proximitySensor = ProximitySensor()
        # splitter1.addWidget(proximitySensor)
        # splitter1.setSizes([200])
        # hbox.addWidget(splitter1)
        fsm = FSM()
        splitter1.addWidget(fsm)
        splitter1.setSizes([200])
        hbox.addWidget(splitter1)

        self.setLayout(hbox)
        QApplication.setStyle(QStyleFactory.create('Cleanlooks'))

        self.setGeometry(300, 300, 450, 350)
