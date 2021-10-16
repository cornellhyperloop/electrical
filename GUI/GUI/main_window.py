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

        quit = Quit()
        splitter1.addWidget(quit)
        emergency_button = EmergencyButton()
        splitter1.addWidget(emergency_button)
        splitter1.setSizes([2, 2])

        splitter2 = QSplitter(Qt.Horizontal)
        battery = Battery()
        splitter2.addWidget(battery)
        proximitySensor = ProximitySensor()
        splitter2.addWidget(proximitySensor)
        fsm = FSM()
        splitter2.addWidget(fsm)
        ldrf = LongDistanceRangefinder()
        splitter2.addWidget(ldrf)
        splitter2.setSizes([2, 2, 1, 50])

        vgraph = QSplitter(Qt.Horizontal)
        graph = TempGraph()
        vgraph.addWidget(graph)
        vgraph.setSizes([2, 2])

        splitter3 = QSplitter(Qt.Vertical)
        splitter3.addWidget(splitter1)
        splitter3.addWidget(splitter2)
        splitter3.addWidget(vgraph)
        splitter3.setSizes([50, 50, 300])

        hbox.addWidget(splitter3)

        self.setLayout(hbox)
        QApplication.setStyle(QStyleFactory.create('Cleanlooks'))

        self.setGeometry(300, 300, 1000, 600)
        
        help = HelpPopup()
        splitter1.addWidget(help)
        splitter1.setSizes([2, 2, 1 , 50])

        timer = Timer()
        splitter1.addWidget(timer)
        splitter1.setSizes([200, 600, 200 , 200])
