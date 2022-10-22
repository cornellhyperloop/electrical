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

        fsm = FSM()

        emergency_button = EmergencyButton(fsm, self.width, self.height)
        grid1.addWidget(emergency_button, 0, 4,
                        alignment=Qt.AlignCenter)

        self.pBar = Progress(self.width, self.height)
        grid1.addWidget(self.pBar, 0, 1, alignment=Qt.AlignCenter)

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
        grid2.addWidget(self.b1, 0, 0)
        grid2.addWidget(self.b2, 0, 1)
        grid2.addWidget(self.b3, 0, 2)
        grid2.addWidget(self.b4, 0, 3)

        vbox = QVBoxLayout(self)

        vbox.addLayout(grid1)
        vbox.addLayout(grid2)

        hbox.addLayout(vbox)
        self.setStyleSheet(qstr)

        splitter4 = QSplitter(Qt.Horizontal)
        self.pBarContainer = progressBar.ProgressBar()
        splitter4.addWidget(self.pBarContainer.label)
        # splitter4.addWidget(fsm)
        # PROGRESS BAR
        splitter4.addWidget(self.pBarContainer.pBar)
        splitter4.setSizes([int(self.height / 30), int(self.height / 30)])

        hbox.addWidget(splitter4)

        self.timer = QTimer(self, timeout=self.update)
        self.timer.start(1000)

        #self.label = QLabel(self)
        #self.pixmap = QPixmap('images/hyperloop.png')
        # self.pixmap.setFixedWidth(200)
        #splitter5= QSplitter(Qt.Horizontal)
        # splitter5.addWidegt(self.pixmap)
        # hbox.addWidget(splitter5)
        # self.label.setPixmap(self.pixmap)
        # self.label.resize(self.pixmap.width(),self.pixmap.height())

        self.show()

    def update(self):  # PROGRESS BAR
        self.pBarContainer.pBar.setValue(self.pBarContainer.pBar.value()+5)

        if int(self.pBarContainer.pBar.value()) < 50:
            self.pBarContainer.pBar.setStyleSheet(cons.PBAR_LOW_PROGRESS)
        elif int(self.pBarContainer.pBar.value()) > 50:
            self.pBarContainer.pBar.setStyleSheet(cons.PBAR_MED_PROGRESS)
        elif int(self.pBarContainer.pBar.value()) == 100:
            self.pBarContainer.pBar.setStyleSheet(cons.PBAR_HIGH_PROGRESS)

    def navbar(self, b):
        print("clicked button is ", b.text())
        buttons = [self.b1, self.b2, self.b3, self.b4]
        if buttons.index(b) > 2:
            return 0
        else:
            return buttons.index(b)
