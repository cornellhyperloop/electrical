from PyQt5 import QtWidgets, uic
from pyqtgraph import PlotWidget, plot
from PyQt5.QtWidgets import QMainWindow, QPushButton, QApplication, QWidget, QHBoxLayout, QGridLayout, QLabel, QTableWidget
import pyqtgraph as pg


import pyqtgraph as pg
import sys  # We need sys so that we can pass argv to QApplication
import os


class MainWindow(QWidget):

    def __init__(self):
        QWidget.__init__(self)
        self.times_pressed = 0
        self.topLayout = QHBoxLayout()

        self.mainLayout = QGridLayout()
        self.mainLayout.addLayout(self.topLayout, 0, 0, 1, 2)

        # self.setCentralWidget(self.mainLayout)

        self.mainLayout.addWidget(QPushButton('STATE'), 0, 0)
        self.mainLayout.addWidget(QPushButton('ESTOP'), 0, 1)

        # IMU
        self.imuLayout = QGridLayout()
        self.imuLayout.addWidget(QLabel('IMU'), 0, 0)
        self.imuLayout.addWidget(QTableWidget(2, 2), 1, 0)
        self.mainLayout.addLayout(self.imuLayout, 1, 0)

        # Long Distance Sensor

        self.ldsLayout = QGridLayout()
        self.ldsLayout.addWidget(QLabel('Long Distance Sensor'), 0, 0)
        self.ldsLayout.addWidget(QTableWidget(2, 2), 1, 0)
        self.mainLayout.addLayout(self.ldsLayout, 1, 1)

        # mainLayout.addWidget(QLabel('Long Distance Sensor'), 1, 1)

        self.psLayout = QGridLayout()
        self.psLayout.addWidget(QLabel('Pressure Sensor'), 0, 0)
        self.psLayout.addWidget(QTableWidget(2, 2), 1, 0)
        self.mainLayout.addLayout(self.psLayout, 2, 0)

        # mainLayout.addWidget(QLabel('Pressure Sensor'), 2, 0)

        self.pesLayout = QGridLayout()
        self.pesLayout.addWidget(QLabel('Photo Electric Sensor'), 0, 0)
        self.pesLayout.addWidget(QTableWidget(2, 2), 1, 0)
        self.mainLayout.addLayout(self.pesLayout, 2, 1)

        # mainLayout.addWidget(QLabel('Photo Electric Sensor'), 2, 1)

        self.reLayout = QGridLayout()
        self.reLayout.addWidget(QLabel('Rotary Encoders'), 0, 0)
        self.reLayout.addWidget(QTableWidget(2, 2), 1, 0)
        self.mainLayout.addLayout(self.reLayout, 3, 0, 1, 2)

        self.button_label = QLabel()
        self.button_label.setText("Times pressed: " + str(self.times_pressed))

        self.reLayout.addWidget(self.button_label, 3, 0)

        self.button = QPushButton('Example button')
        self.reLayout.addWidget(self.button, 2, 0)
        self.button.clicked.connect(self.button_press)

        # graph_layout = pg.GraphicsLayout()
        # graphics_window = pg.GraphicsLayoutWidget()
        # graphics_window.setCentralWidget(graph_layout)

        self.data = [1, 6, 3, 7]
        self.graph_window = pg.PlotWidget()
        self.graph_window.plot(self.data)

        self.reLayout.addWidget(self.graph_window, 4, 0)
        # plt = graph_layout.addPlot(row=2, col=2)
        # plot(data)
        # plt.PlotItem(plot([1, 2, 3]))
        # graph_layout.plot
        # mainLayout.addWidget(QLabel('Rotary Encoders'), 3, 0, 1, 2)

        self.setLayout(self.mainLayout)

    def button_press(self):
        self.times_pressed += 1
        self.button_label.setText(
            "Times pressed: " + str(self.times_pressed))


app = QApplication(sys.argv)
win = MainWindow()
win.show()
sys.exit(app.exec_())
