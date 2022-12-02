from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import pyqtgraph as pg
import serial
import constants
import time


class Thermistor(QWidget):
    def __init__(self, parent=None):
        super(Thermistor, self).__init__(parent)
        self.initUI()
        self.arduino = serial.Serial(port="/dev/cu.usbmodem11101", baudrate = 9600, timeout=.1)
        self.x = 0
        self.y = 0
        self.layout = QGridLayout()
        self.graphWidget = pg.PlotWidget()

        self.graphWidget.setBackground((224, 224, 224))
        pen = pg.mkPen(width=10)
        self.layout.addWidget(self.graphWidget)
        self.setLayout(self.layout)
        self.timer = QTimer(self, timeout=self.update)
        self.timer.start(1000)

    def getPlotItem(self):
        return self.graphWidget.getPlotItem()

    def initUI(self):
        self.temp = QLabel(self)

        vbox = QVBoxLayout()
        vbox.addWidget(self.temp)
        self.temp.setStyleSheet("background-color : blue")
        self.setLayout(vbox)

    def update(self):
        self.x += 1
        line = self.arduino.readline().decode()
        if line:
           u = line.find(',')
           self.y = float(line[:u])
        # data = self.arduino.readline().decode()
        # if len(data)!=0:
        #     temp = float(data[data.index(':')+2:data.index(': ')+7])
        #     dist = float(data[data.rindex(':')+2:data.rindex('c')-1])
        #     d = [temp, dist]
        #     return d
        # return 0

        # if (data!=0): 
        #     pen = pg.mkPen(width=10)
        #     self.graphWidget.plot([time.time()-self.startTime], [data[0]],
        #                       pen=pen, symbol='x', symbolSize=30)
