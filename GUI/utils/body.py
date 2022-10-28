from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from widgets import *
from constants import *
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
        self.temporary_graph = pg.PlotWidget()
        hour = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        temperature = [30, 32, 34, 32, 33, 31, 29, 32, 35, 45]
        self.temporary_graph.resize(int(self.width), int(self.height / 4))

        self.plot_buttons = PlotButtons(self.temporary_graph)
        plot_button_splitter.addWidget(self.plot_buttons)

        # Data for plots
        self.x_data = [[], []]
        self.y_data = [[], []]
        self.current_plot_indices = [0,0]
        self.current_plot_values = [[0,0], [0,0]] # x,y for each plot

        prox_sensors = ProximitySensor()
        home_footer.addWidget(bottom_left)
        home_footer.addWidget(prox_sensors)

        vgraph = QSplitter(Qt.Horizontal)
        vgraph.setSizes([2, 2])

        home.addWidget(self.temporary_graph)
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
        current_plot = self.plot_buttons.getCurrentPlot()
        pen = pg.mkPen(width=10)

        if (self.plot_buttons.getRescaleAxesFlag()):
            self.plot_buttons.setRescaleAxesFlag(False)
            x_axes = self.plot_buttons.getXAxesLimits()
            y_axes = self.plot_buttons.getYAxesLimits()
            self.temporary_graph.setXRange(x_axes[0],x_axes[1])
            self.temporary_graph.setYRange(y_axes[0],y_axes[1])

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
            self.temporary_graph.clear()

            # Plot all the data for the new plot
            for i in range(len(self.x_data[current_plot])):
                self.temporary_graph.plot([self.x_data[current_plot][i]], [self.y_data[current_plot][i]],
                                pen=pen, symbol='x', symbolSize=30)

            # Reset the changed plot flag
            self.plot_buttons.setChangedPlot(False)
    
        else:
            # Updated variables for the next data
            for i in range(NUM_PLOTS):
                self.x_data[i].append(self.current_plot_values[i][0])
                self.y_data[i].append(self.current_plot_values[i][1])
                self.current_plot_values[i][0] += PLOT_INCREMENTS[i]
                self.current_plot_values[i][1] += PLOT_INCREMENTS[i]

            # Get the current index
            currentIndex = self.current_plot_indices[current_plot]

            # Plot the current data point
            self.temporary_graph.plot([self.x_data[current_plot][currentIndex]], [self.y_data[current_plot][currentIndex]],
                                pen=pen, symbol='x', symbolSize=30)
            
            # Update the indices for the next datapoint
            self.current_plot_indices[0] += 1
            self.current_plot_indices[1] += 1
            


