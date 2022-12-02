from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from widgets import *
from constants import *
import pyqtgraph as pg
import time
import serial


class Therm(QWidget):
    def __init__(self, *args, **kwargs):
        super(Therm, self).__init__()
        self.arduino = serial.Serial(port="/dev/cu.usbmodem11101", baudrate = 9600, timeout=.1)
        self.startTime = time.time()
        self.width = args[0]
        self.height = args[1]
        self.live_data = args[2]
        hbox = QHBoxLayout(self)

        sshFile = "utils/therm.css"
        with open(sshFile, "r") as fh:
            qstr = str(fh.read())

        # home = QSplitter(Qt.Vertical)
        home = QGridLayout(self)

        plot_button_grid = QGridLayout(self)
        home_footer = QGridLayout(self)
        bottom_left = QGridLayout(self)  # vertical
        vel_acc = QGridLayout(self)

        speedometer = Speedometer()
        accelerometer = Accelerometer()

        vel_acc.addWidget(speedometer, 0, 0)
        vel_acc.addWidget(accelerometer, 0, 1)

        speed = Speed()
        bottom_left.addLayout(vel_acc, 0, 0)
        bottom_left.addWidget(speed, 1, 0)

        # use live data, else dummy graph
        if self.live_data:
            self.graph = Thermistor()
        else:
            self.graph = pg.PlotWidget()
            hour = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
            temperature = [30, 32, 34, 32, 33, 31, 29, 32, 35, 45]
            self.graph.resize(int(self.width), int(self.height / 4))

        self.plot_buttons = PlotButtons(self.graph)
        plot_button_grid.addWidget(self.plot_buttons, 0, 0)

        # Data for plots
        self.x_data = [[], []]
        self.y_data = [[], []]
        self.current_plot_indices = [0, 0]
        self.current_plot_values = [[0, 0], [0, 0]]  # x,y for each plot

        prox_sensors = ProximitySensor()

        home_footer.addLayout(bottom_left, 0, 0)
        home_footer.addWidget(prox_sensors, 0, 1)

        vgraph = QSplitter(Qt.Horizontal)
        vgraph.setSizes([2, 2])

        home.addWidget(self.graph, 0, 0)
        home.addLayout(plot_button_grid, 1, 0)
        home.addLayout(home_footer, 2, 0)

        hbox.addLayout(home)
        self.setLayout(hbox)
        # body.css affects the thermistor graph
        # self.setStyleSheet(qstr)

        # use dummy update function
        if not self.live_data:
            self.timer = QTimer(self, timeout=self.update)
            self.timer.start(1000)
            self.x = 0
            self.y = 0

    def get_data(self):
        data = self.arduino.readline().decode()
        if len(data)!=0:
            temp = float(data[data.index(':')+2:data.index(': ')+7])
            dist = float(data[data.rindex(':')+2:data.rindex('c')-1])
            d = [temp, dist]
            return d
        return 0

    def update(self):
        current_plot = self.plot_buttons.getCurrentPlot()
        pen = pg.mkPen(width=10)

        if (self.plot_buttons.getRescaleAxesFlag()):
            self.plot_buttons.setRescaleAxesFlag(False)
            x_axes = self.plot_buttons.getXAxesLimits()
            y_axes = self.plot_buttons.getYAxesLimits()
            self.graph.setXRange(x_axes[0], x_axes[1])
            self.graph.setYRange(y_axes[0], y_axes[1])

        if (self.plot_buttons.getPlotResetFlag()):
            # Reset the current plot
            self.current_plot_values[current_plot][0] = 0
            self.current_plot_values[current_plot][1] = 0
            self.current_plot_indices[current_plot] = 0
            self.x_data[current_plot] = [0]
            self.y_data[current_plot] = [0]
            self.plot_buttons.setPlotResetFlag(False)

        elif (self.plot_buttons.getChangedPlot()):
            # Reset the plot
            self.graph.clear()

            # Plot all the data for the new plot
            for i in range(len(self.x_data[current_plot])):
                self.graph.plot([self.x_data[current_plot][i]], [self.y_data[current_plot][i]],
                                pen=pen, symbol='x', symbolSize=30)

            # Reset the changed plot flag
            self.plot_buttons.setChangedPlot(False)

        else:
            # Updated variables for the next data
            for i in range(NUM_PLOTS):
                data = self.get_data()
                if (data!=0):
                    self.x_data[i].append(time.time()-self.startTime)
                    self.y_data[i].append(data[1])
                    self.current_plot_values[i][0] += PLOT_INCREMENTS[i]
                    self.current_plot_values[i][1] += PLOT_INCREMENTS[i]

            # Get the current index
                    currentIndex = self.current_plot_indices[current_plot]

            # Plot the current data point
                    #self.graph.plot([time.time()-self.startTime], [data[1]],
                    #       pen=pen, symbol='x', symbolSize=30)

                    self.graph.plot([time.time()-self.startTime], [data[0]],
                            pen=pen, symbol='x', symbolSize=30)

            # Update the indices for the next datapoint
                    self.current_plot_indices[0] += 1
                    self.current_plot_indices[1] += 1

    def dimensions(self):
        return self.width, self.height
