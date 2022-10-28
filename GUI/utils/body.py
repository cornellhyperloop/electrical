from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from widgets import *
import pyqtgraph as pg


class Body(QWidget):
    def __init__(self, *args, **kwargs):
        super(Body, self).__init__()
        self.width = args[0]
        self.height = args[1]
        hbox = QHBoxLayout(self)

        sshFile = "utils/body.css"
        with open(sshFile, "r") as fh:
            qstr = str(fh.read())

        home = QSplitter(Qt.Vertical)

        plot_button_splitter = QSplitter(Qt.Horizontal)
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

        # temporary graph
        self.temporary = pg.PlotWidget()
        hour = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        temperature = [30, 32, 34, 32, 33, 31, 29, 32, 35, 45]
        self.temporary.resize(int(self.width), int(self.height / 4))

        self.plot_buttons = PlotButtons(self.temporary)
        plot_button_splitter.addWidget(self.plot_buttons)

        prox_sensors = ProximitySensor()
        home_footer.addWidget(bottom_left)
        home_footer.addWidget(prox_sensors)

        vgraph = QSplitter(Qt.Horizontal)
        vgraph.setSizes([2, 2])

        home.addWidget(self.temporary)
        home.addWidget(plot_button_splitter)
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
        if (self.plot_buttons.getRescaleAxesFlag()):
            self.plot_buttons.setRescaleAxesFlag(False)
            x_axes = self.plot_buttons.getXAxesLimits()
            y_axes = self.plot_buttons.getYAxesLimits()
            self.temporary.setXRange(x_axes[0],x_axes[1])
            self.temporary.setYRange(y_axes[0],y_axes[1])

        if (self.plot_buttons.getPlotResetFlag()):
            self.x = 0
            self.y = 0
            self.plot_buttons.setPlotResetFlag(False)
        else:
            pen = pg.mkPen(width=10)
            self.temporary.plot([self.x], [self.y],
                                pen=pen, symbol='x', symbolSize=30)
            self.x += 1
            self.y += 1

