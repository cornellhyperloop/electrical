from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from widgets import *  # Custom widgets (assumed to be defined elsewhere)
from constants import *  # Constant values like NUM_PLOTS, PLOT_INCREMENTS
import pyqtgraph as pg  # A library for fast and efficient graphing

"""
Body Represents the initial UI for the GUI
The main feature is a graph that for now plots meaningless data
but is meant to plot the thermistor data

Other features in UI are a widgets for velocity and acceleration

Relevant Widgets:
-Proximity Sensor
-Speed
-Accelerometer
-Speedometer
"""

# Body class inherits from QWidget, which will represent the main interface
class Body(QWidget):
    def __init__(self, *args, **kwargs):
        super(Body, self).__init__()  # Initialize the QWidget parent class
        
        # Set dimensions for the widget
        self.width = args[0]  # Passed in as the first argument
        self.height = args[1]  # Passed in as the second argument
        
        # QHBoxLayout: Horizontal box layout for arranging child widgets
        hbox = QHBoxLayout(self)
        
        # Load the CSS file for styling the widget
        sshFile = "utils/body.css"
        with open(sshFile, "r") as fh:
            qstr = str(fh.read())

        # Main layout containers (QSplitter allows resizing between child widgets)
        home = QSplitter(Qt.Vertical)  # Vertical splitter for top-bottom sections
        home_footer = QSplitter(Qt.Horizontal)  # Horizontal splitter for bottom sections
        bottom_left = QSplitter(Qt.Vertical)  # Vertical splitter for left-bottom section
        vel_acc = QSplitter(Qt.Horizontal)  # Horizontal splitter for velocity and acceleration widgets
        
        # Speedometer and Accelerometer widgets
        speedometer = Speedometer()  # Custom Speedometer widget (defined elsewhere)
        accelerometer = Accelerometer()  # Custom Accelerometer widget (defined elsewhere)
        
        # Add widgets to the velocity-acceleration section
        vel_acc.addWidget(speedometer)
        vel_acc.addWidget(accelerometer)

        # Speed widget, added below the velocity-acceleration widgets
        speed = Speed()  # Custom Speed widget (defined elsewhere)
        bottom_left.addWidget(vel_acc)
        bottom_left.addWidget(speed)

        # Temporary graph setup using pyqtgraph
        self.temporary_graph = pg.PlotWidget()  # Create a plot widget using pyqtgraph
        hour = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  # Sample x-axis data
        temperature = [30, 32, 34, 32, 33, 31, 29, 32, 35, 45]  # Sample y-axis data
        self.temporary_graph.resize(int(self.width), int(self.height / 4))  # Resize the graph

        # PlotButtons manages control buttons for interacting with plots
        self.plot_buttons = PlotButtons(self.temporary_graph)

        # Data for six different plots
        self.x_data = [[], [], [], [], [], []]  # X-axis data for each plot
        self.y_data = [[], [], [], [], [], []]  # Y-axis data for each plot
        
        # Tracking indices and current plot values (x, y) for each plot
        self.current_plot_indices = [0, 0, 0, 0, 0, 0]
        self.current_plot_values = [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]
        
        self.currentPlotIndex = 0  # Index of the current plot (default: 0)
        self.currentPlotName = "Accelerometer"  # Name of the current plot

        # Proximity sensor widget added to the right of the bottom section
        prox_sensors = ProximitySensor()

        # Organizing bottom widgets
        home_footer.addWidget(bottom_left)  # Add bottom-left section (vel_acc + speed)
        home_footer.addWidget(prox_sensors)  # Add proximity sensor widget to footer

        # Main visual graph container
        vgraph = QSplitter(Qt.Horizontal)  # Another horizontal splitter for more graph flexibility
        vgraph.setSizes([2, 2])  # Setting initial size ratios

        # Adding widgets to the main layout
        home.addWidget(self.temporary_graph)  # Add the plot graph widget to the top
        home.addWidget(self.plot_buttons)  # Add plot buttons below the graph
        home.addWidget(home_footer)  # Add the footer (vel_acc + prox sensor)
        home.setSizes([350, 5, 45])  # Adjust relative sizes of sections

        # Add the home layout to the main widget layout
        hbox.addWidget(home)
        self.setLayout(hbox)
        self.setStyleSheet(qstr)  # Apply the loaded CSS for styling

        # Set up a QTimer to regularly call the update method
        self.timer = QTimer(self, timeout=self.update)
        self.timer.start(1000)  # Timer set to call update() every second
        self.x = 0  # X-axis value for live data simulation
        self.y = 0  # Y-axis value for live data simulation

    def update(self):
        """
        Update method that is called every second by the timer

        Has functinoality for updating the graph when we need to 
        rescale axis, reset plot, change plot, or just update w/ new data
        """
        current_plot = self.plot_buttons.getCurrentPlot()  # Get the current plot index
        pen = pg.mkPen(width=10)  # Create a pen for drawing the plot lines
        
        # If rescaling axes is needed, adjust the axes ranges
        if self.plot_buttons.getRescaleAxesFlag():
            self.plot_buttons.setRescaleAxesFlag(False)
            x_axes = self.plot_buttons.getXAxesLimits()
            y_axes = self.plot_buttons.getYAxesLimits()
            self.temporary_graph.setXRange(x_axes[0], x_axes[1])  # Set X-axis range
            self.temporary_graph.setYRange(y_axes[0], y_axes[1])  # Set Y-axis range

        # If plot needs to be reset, clear data and start from scratch
        if self.plot_buttons.getPlotResetFlag():
            self.current_plot_values[current_plot][0] = 0  # Reset X-value
            self.current_plot_values[current_plot][1] = 0  # Reset Y-value
            self.current_plot_indices[current_plot] = 0  # Reset index
            self.x_data[current_plot] = [0]  # Clear X-data
            self.y_data[current_plot] = [0]  # Clear Y-data
            self.plot_buttons.setPlotResetFlag(False)

        # If a plot has changed, switch to the new plot and plot its data
        elif self.plot_buttons.getChangedPlot():
            self.currentPlotIndex = self.plot_buttons.getCurrentPlot()  # Update current plot index
            self.currentPlotName = self.plot_buttons.getCurrentPlotName()  # Get plot name
            
            self.temporary_graph.clear()  # Clear the current plot
            
            # Plot all existing data points for the new plot
            for i in range(len(self.x_data[current_plot])):
                self.temporary_graph.plot([self.x_data[current_plot][i]], 
                                          [self.y_data[current_plot][i]],
                                          pen=pen, symbol='x', symbolSize=30)
            self.plot_buttons.setChangedPlot(False)  # Reset flag

        else:
            # Most of the time control ends up here
            # Update and plot new data points for all plots
            for i in range(NUM_PLOTS):
                self.x_data[i].append(self.current_plot_values[i][0])  # Update X-data
                self.y_data[i].append(self.current_plot_values[i][1])  # Update Y-data
                self.current_plot_values[i][0] += PLOT_INCREMENTS[i]  # Increment X-value
                self.current_plot_values[i][1] += PLOT_INCREMENTS[i]  # Increment Y-value
            
            # Get the current data point index
            currentIndex = self.current_plot_indices[current_plot]
            
            # Plot the current data point
            self.temporary_graph.plot([self.x_data[current_plot][currentIndex]], 
                                      [self.y_data[current_plot][currentIndex]],
                                      pen=pen, symbol='x', symbolSize=30)

            # Update index for the next data point
            self.current_plot_indices[current_plot] += 1

    # Return widget dimensions
    def dimensions(self):
        return self.width, self.height
