from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from widgets import *


class MainWindow(QWidget):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__()

        # Insert change here
        self.setWindowTitle("Hyperloop GUI")
        sshFile = "test.css"
        with open(sshFile, "r") as fh:
            qstr = str(fh.read())

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

        splitter3 = QSplitter(Qt.Horizontal)
        speed = Speed()
        speed.setStyleSheet(qstr)
        # speed.setStyleSheet("color: red;"
        #                     "background-color: #87CEFA;"
        #                     "border-style: dashed;"
        #                     "border-width: 3px;"
        #                     "border-color: red")
        splitter3.addWidget(speed)
        speedometer = Speedometer()
        splitter3.addWidget(speedometer)
        accelerometer = Accelerometer()
        splitter3.addWidget(accelerometer)
        # splitter3.setSizes([1])

        vgraph = QSplitter(Qt.Horizontal)
        ###

        graph = TempGraph()
        vgraph.addWidget(graph)
        vgraph.setSizes([2, 2])

        splitter4 = QSplitter(Qt.Vertical)
        splitter4.addWidget(splitter1)
        splitter4.addWidget(splitter2)
        splitter4.addWidget(splitter3)
        splitter4.addWidget(vgraph)
        splitter4.setSizes([50, 50, 300])

        hbox.addWidget(splitter4)
        self.setLayout(hbox)
        QApplication.setStyle(QStyleFactory.create('Cleanlooks'))

        self.setGeometry(300, 300, 1000, 600)

        help = HelpPopup()
        splitter1.addWidget(help)
        splitter1.setSizes([2, 2, 1, 50])

        timer = Timer()
        splitter1.addWidget(timer)
        splitter1.setSizes([200, 600, 200, 200])
