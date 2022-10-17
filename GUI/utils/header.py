from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from widgets import *
from PyQt5.QtCore import QObject, pyqtSignal
import time
from widgets import progressBar
import constants as cons

class Header(QWidget):
    def __init__(self, w=1000, h=500, *args, **kwargs):
        super(Header, self).__init__()
        hbox = QHBoxLayout(self)
        sshFile = "utils/header.css"
        with open(sshFile, "r") as fh:
            qstr = str(fh.read())
        self.width = w * 1/2
        self.height = h / 6
        hbox.setContentsMargins(0, 0, 0, 0)
        head = QSplitter(Qt.Vertical)

        splitter1 = QSplitter(Qt.Horizontal)
        quit = Quit()
        splitter1.addWidget(quit)

        fsm = FSM()

        emergency_button = EmergencyButton(fsm)
        splitter1.addWidget(emergency_button)

        # splitter1.addWidget(fsm)
        # splitter1.setSizes([1, 1])

        timer = Timer()
        splitter1.addWidget(timer)
        help = HelpPopup()
        splitter1.addWidget(help)
        # splitter1.setStretchFactor(0, 1)
        # splitter1.setStretchFactor(1, 2.5)
        # splitter1.setStretchFactor(2, 2.5)
        # splitter1.setStretchFactor(3, 1)
        self.ratio = [1/12, 1/3, 5/12, 1/12]
        self.ratio = [int(x * self.width) for x in self.ratio]
        splitter1.setSizes(self.ratio)

        splitter2 = QSplitter(Qt.Horizontal)
        self.b1 = QPushButton("Home")
        self.b1.clicked.connect(lambda: self.navbar(self.b1))
        self.b2 = QPushButton("Visualizer")
        self.b2.clicked.connect(lambda: self.navbar(self.b2))
        self.b3 = QPushButton("Battery")
        self.b3.clicked.connect(lambda: self.navbar(self.b3))
        self.b4 = QPushButton("Temperature")
        self.b4.clicked.connect(lambda: self.navbar(self.b4))
        splitter2.addWidget(self.b1)
        splitter2.addWidget(self.b2)
        splitter2.addWidget(self.b3)
        splitter2.addWidget(self.b4)
        splitter2.addWidget(self.b4)
        splitter2.addWidget(self.b4)
        splitter2.addWidget(self.b4)

        # battery = Battery()
        # battery.setStyleSheet(qstr)
        # splitter2.addWidget(battery)
        # proximitySensor = ProximitySensor()
        # proximitySensor.setStyleSheet(qstr)
        # splitter2.addWidget(proximitySensor)
        # vibrationSensor = VibrationSensor()
        # vibrationSensor.setStyleSheet(qstr)
        # splitter2.addWidget(vibrationSensor)
        # pressureSensor = PressureSensor()
        # pressureSensor.setStyleSheet(qstr)
        # splitter2.addWidget(pressureSensor)
        # fsm = FSM()
        # ldrf = LongDistanceRangefinder()
        # splitter2.addWidget(ldrf)
        # splitter2.setSizes([2, 2, 1, 50])

        head.addWidget(splitter1)
        splitter3 = QSplitter(Qt.Vertical)
        splitter3.addWidget(splitter1)
        # splitter2.setSizes([int(0), int(self.height / 3)])
        splitter3.addWidget(splitter2)
        splitter3.setSizes([int(self.height / 3), int(self.height / 3)])

        hbox.addWidget(splitter3)
        self.setStyleSheet(qstr)

        
        splitter4= QSplitter(Qt.Horizontal)
        self.pBarContainer = progressBar.ProgressBar()
        splitter4.addWidget(self.pBarContainer.label)
        splitter4.addWidget(self.pBarContainer.pBar)                             # PROGRESS BAR
        splitter4.setSizes([self.height / 30, self.height / 30])

        hbox.addWidget(splitter4)

        self.timer = QTimer(self, timeout=self.update)
        self.timer.start(1000)

        #self.label = QLabel(self)
        #self.pixmap = QPixmap('images/hyperloop.png')
        #self.pixmap.setFixedWidth(200)
        #splitter5= QSplitter(Qt.Horizontal)
        #splitter5.addWidegt(self.pixmap)
        #hbox.addWidget(splitter5)
        #self.label.setPixmap(self.pixmap)
        #self.label.resize(self.pixmap.width(),self.pixmap.height())
        
        self.show()  

    def update(self):                                                  #PROGRESS BAR
        self.pBarContainer.pBar.setValue(self.pBarContainer.pBar.value()+5)

        if int(self.pBarContainer.pBar.value()) <50:
            self.pBarContainer.pBar.setStyleSheet(cons.PBAR_LOW_PROGRESS)
        elif int(self.pBarContainer.pBar.value())>50: 
            self.pBarContainer.pBar.setStyleSheet(cons.PBAR_MED_PROGRESS)
        elif int(self.pBarContainer.pBar.value())==100: 
            self.pBarContainer.pBar.setStyleSheet(cons.PBAR_HIGH_PROGRESS)
    

    def navbar(self, b):
        print("clicked button is ", b.text())
        buttons = [self.b1, self.b2, self.b3, self.b4]
        if buttons.index(b) > 2:
            return 0
        else:
            return buttons.index(b)
