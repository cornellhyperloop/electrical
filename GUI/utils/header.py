from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from widgets import *
<<<<<<< HEAD
from PyQt5.QtCore import QObject, pyqtSignal
import time


class Header(QWidget):
    def __init__(self, w=1000, h=500, *args, **kwargs):
=======
from PyQt5.QtGui import *
from PyQt5.QtCore import QObject, pyqtSignal
import time
from widgets import progressBar
import constants as cons


class Header(QWidget):
    def __init__(self, fsm, w=1000, h=500, *args, **kwargs):
>>>>>>> 088593597150e78bab5f05267d052282c28f0e0b
        super(Header, self).__init__()
        hbox = QHBoxLayout(self)
        sshFile = "utils/header.css"
        with open(sshFile, "r") as fh:
            qstr = str(fh.read())
<<<<<<< HEAD
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

        self.pBar= QProgressBar(self)
        #self.pBar.setGeometry(0, 0, 10, 30)
        #self.pBar.resize(10,10)
        self.pBar.setFixedWidth(200)
        splitter4= QSplitter(Qt.Horizontal)
        splitter4.addWidget(self.pBar)
        #splitter4.setSizes([self.height / 30, self.height / 30])
        hbox.addWidget(splitter4)
        self.timer = QTimer(self, timeout=self.update)
        self.timer.start(1000)
       

    def update(self):
        self.pBar.setValue(self.pBar.value()+5)


    def navbar(self, b):
        print("clicked button is ", b.text())
        buttons = [self.b1, self.b2, self.b3, self.b4]
        if buttons.index(b) > 1:
=======
        self.width = w
        self.height = h
        hbox.setContentsMargins(0, 0, 0, 0)

        grid1 = QGridLayout(self)

        quit = Quit(w, h)
        grid1.addWidget(quit, 0, 0, alignment=Qt.AlignCenter)

        timer = Timer(self.width, self.height)
        grid1.addWidget(timer, 0, 2, alignment=Qt.AlignCenter)

        help = HelpPopup(int(self.width), int(self.height))
        grid1.addWidget(help, 0, 3, alignment=Qt.AlignCenter)

        emergency_button = EmergencyButton(fsm, self.width, self.height)
        grid1.addWidget(emergency_button, 0, 4,
                        alignment=Qt.AlignCenter)

        pBarSplitter = QSplitter(Qt.Vertical)
        self.pBarContainer = progressBar.ProgressBar()
        pBarSplitter.addWidget(self.pBarContainer.label)
        pBarSplitter.addWidget(self.pBarContainer.pBar)
        grid1.addWidget(pBarSplitter, 0,
                        1, alignment=Qt.AlignCenter)

        grid2 = QGridLayout(self)
        self.b1 = QPushButton("Home")
        self.b1.clicked.connect(lambda: self.navbar(self.b1))
        self.b1.resize(int(self.width / 5), int(self.height / 20))
        self.b2 = QPushButton("Visualizer")
        self.b2.clicked.connect(lambda: self.navbar(self.b2))
        self.b2.resize(int(self.width / 5), int(self.height / 20))
        self.b3 = QPushButton("Battery")
        self.b3.clicked.connect(lambda: self.navbar(self.b3))
        self.b3.resize(int(self.width / 5), int(self.height / 20))
        self.b4 = QPushButton("Temperature")
        self.b4.clicked.connect(lambda: self.navbar(self.b4))
        self.b4.resize(int(self.width / 5), int(self.height / 20))
        self.b5 = QPushButton("FSM")
        self.b5.clicked.connect(lambda: self.navbar(self.b5))
        self.b5.resize(int(self.width / 5), int(self.height / 20))
        grid2.addWidget(self.b1, 0, 0)
        grid2.addWidget(self.b2, 0, 1)
        grid2.addWidget(self.b3, 0, 2)
        grid2.addWidget(self.b4, 0, 3)
        grid2.addWidget(self.b5, 0, 4)

        vbox = QVBoxLayout(self)

        vbox.addLayout(grid1)
        vbox.addLayout(grid2)

        hbox.addLayout(vbox)
        self.setStyleSheet(qstr)

        hyperloop = QPixmap('state_icons/logo.png')
        hyperloop = hyperloop.scaled(200, 100)
        label = QLabel()
        label.setStyleSheet("border: 1px grey")
        label.setFixedWidth(200)
        label.setFixedHeight(100)
        label.setPixmap(hyperloop)

        splitter4 = QSplitter(Qt.Horizontal)
        splitter4.addWidget(label)

        hbox.addWidget(splitter4)

        self.timer = QTimer(self, timeout=self.update)
        self.timer.start(1000)

        self.show()

    def update(self):  # PROGRESS BAR
        progress_bar_value = int(self.pBarContainer.pBar.value())

        self.pBarContainer.pBar.setValue(progress_bar_value + 5)

        if (progress_bar_value < 50):
            self.pBarContainer.pBar.setStyleSheet(cons.PBAR_LOW_PROGRESS)
        elif (progress_bar_value > 99):
            self.pBarContainer.pBar.setStyleSheet(cons.PBAR_HIGH_PROGRESS)
        else:
            self.pBarContainer.pBar.setStyleSheet(cons.PBAR_MED_PROGRESS)
        

    def navbar(self, b):
        buttons = [self.b1, self.b2, self.b3, self.b4, self.b5]
        # only temperature page is not implemented
        if buttons.index(b) == 3:
>>>>>>> 088593597150e78bab5f05267d052282c28f0e0b
            return 0
        else:
            return buttons.index(b)
