from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from pyqtgraph import PlotWidget, plot
import pyqtgraph as pg
import serial
import json

class Graph(QWidget):

    def __init__(self, parent=None):
        super(Graph, self).__init__(parent)
        self.x = 0
        self.y = 0
        self.layout = QGridLayout()
        self.graphWidget = pg.PlotWidget()

        self.graphWidget.setBackground((224, 224, 224))
        # self.graphWidget.plot(second, temperature, pen=pen,
        #   symbol='x', symbolSize=30)
        self.layout.addWidget(self.graphWidget)
        self.setLayout(self.layout)
        self.timer = QTimer(self, timeout=self.update)
        self.timer.start(1000)

        # Live thermistor plotting ---
        #self.arduino = serial.Serial('/dev/cu.usbmodem') # UPDATE WITH CORRECT PORT

    def update(self):
        self.x += 1
        # self.y += 1
        # pen = pg.mkPen(width=10)
        # self.graphWidget.plot([self.x], [self.y],
        #                     pen=pen, symbol='x', symbolSize=30)
        
        # Process live thermistor data ---
        data = json.loads(self.arduino.readline().decode()) # load data in the format defined by the JSON scheme
        
        # UPDATED BASED ON THE JSON SCHEME
        thermistorValue1 = data['Thermistor1']
        thermistorValue2 = data['Thermistor2']

        pen = pg.mkPen(width=10)
        self.graphWidget.plot([self.x], [thermistorValue1],
                            pen=pen, symbol='x', symbolSize=30)

