from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from widgets import *
from PyQt5.QtCore import QObject, pyqtSignal
import time
from widgets import progressBar


class Header(QWidget):
    def __init__(self, w=1000, h=500, *args, **kwargs):
        super(Header, self).__init__()
        hbox = QHBoxLayout(self)
        sshFile = "utils/header.css"
        with open(sshFile, "r") as fh:
            qstr = str(fh.read())
        self.width = w * 1/2
        self.height = h / 6

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
        self.ratio = [x * self.width for x in self.ratio]
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
        splitter3.addWidget(splitter2)
        splitter3.setSizes([self.height / 3, self.height / 3])

        hbox.addWidget(splitter3)
        self.setStyleSheet(qstr)

        
        splitter4= QSplitter(Qt.Horizontal)

        #self.pBar= QProgressBar(self)                                  PROGRESS BAR
        self.pBar = progressBar.ProgressBar()
        #pBar.setGeometry(0, 0, 10, 30)
        #pBar.setFixedWidth(250)
        #pBar.show()
        splitter4.addWidget(self.pBar.label)
        splitter4.addWidget(self.pBar.pBar)
        #self.pBar = QProgressBar(self, minimum=0, maximum=100)
        #self.pBar.setFont(QFont('Arial', 15))                               # PROGRESS BAR
        splitter4.setSizes([self.height / 30, self.height / 30])
        #self.pBar.setGeometry(0, 0, 10, 30)                           # PROGRESS BAR
        #self.pBar.resize(10,10)
        #self.pBar.setFixedWidth(250)
        #label = progressBar.label

        hbox.addWidget(splitter4)

        self.timer = QTimer(self, timeout=self.update)
        self.timer.start(1000)
       

    def update(self):                                                  #PROGRESS BAR
        self.pBar.pBar.setValue(self.pBar.pBar.value()+5)

        if int(self.pBar.pBar.value()) <50:
            self.pBar.pBar.setStyleSheet("QProgressBar::chunk "
                  "{"
                    "background-color: red;"
                  "}")
        elif int(self.pBar.pBar.value())>50: 
            self.pBar.pBar.setStyleSheet("QProgressBar::chunk "
                  "{"
                    "background-color: gold;"
                  "}")
        elif int(self.pBar.pBar.value())==100: 
            self.pBar.pBar.setStyleSheet("QProgressBar::chunk "
                  "{"
                    "background-color: green;"
                  "}")
    


    def navbar(self, b):
        print("clicked button is ", b.text())
        buttons = [self.b1, self.b2, self.b3, self.b4]
        if buttons.index(b) > 1:
            return 0
        else:
            return buttons.index(b)
