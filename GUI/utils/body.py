from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from widgets import *
import pyqtgraph as pg
from widgets.cooling_systems import *


class Body(QWidget):
    def __init__(self, *args, **kwargs):
        super(Body, self).__init__()
        hbox = QHBoxLayout(self)

        sshFile = "utils/body.css"
        with open(sshFile, "r") as fh:
            qstr = str(fh.read())

        home = QSplitter(Qt.Vertical)

        home_footer = QSplitter(Qt.Horizontal)
        bottom_left = QSplitter(Qt.Vertical)
        vel_acc = QSplitter(Qt.Horizontal)

        speedometer = Speedometer()
        accelerometer = Accelerometer()
        vel_acc.addWidget(speedometer)
        vel_acc.addWidget(accelerometer)

        speed = Speed()
        bottom_left.addWidget(vel_acc)
        bottom_left.addWidget(speed)

        prox_sensors = ProximitySensor()
        battery = Battery()
        cool_systems = CoolingSystem()
        home_footer.addWidget(bottom_left)
        home_footer.addWidget(prox_sensors)
        home_footer.addWidget(battery)
        home_footer.addWidget(cool_systems)

        # hbox.addWidget(splitter3)

        vgraph = QSplitter(Qt.Horizontal)
        ###

        #graph = TempGraph()
        # vgraph.addWidget(graph)
        vgraph.setSizes([2, 2])

        # hbox.addWidget(vgraph)
        # self.setLayout(hbox)

        # temporary graph, i dont have arduino
        self.temporary = pg.PlotWidget()
        hour = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        temperature = [30, 32, 34, 32, 33, 31, 29, 32, 35, 45]
        #temporary.plot(hour, temperature)

        home.addWidget(self.temporary)
        home.addWidget(home_footer)
        home.setSizes([300, 50])

        hbox.addWidget(home)
        self.setLayout(hbox)
        self.setStyleSheet(qstr)

        self.timer = QTimer(self, timeout=self.update)
        self.timer.start(1000)
        self.x = 0
        self.y = 0
    
    def update(self):
        self.x += 1
        self.y += 1

        pen = pg.mkPen(width=10)
        self.temporary.plot([self.x], [self.y],
                            pen=pen, symbol='x', symbolSize=30)
