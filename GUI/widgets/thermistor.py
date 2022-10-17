from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import pyqtgraph as pg
import serial


class Thermistor(QWidget):
    def __init__(self, parent=None):
        super(Thermistor, self).__init__(parent)
        self.initUI()
        self.arduino = serial.Serial("/dev/cu.usbmodem143201")
        self.x = 0
        self.y = 0
        self.layout = QGridLayout()
        self.graphWidget = pg.PlotWidget()

        self.graphWidget.setBackground((224, 224, 224))
        pen = pg.mkPen(width=10)
        # self.graphWidget.plot(second, temperature, pen=pen,
        #   symbol='x', symbolSize=30)
        self.layout.addWidget(self.graphWidget)
        self.setLayout(self.layout)
        self.timer = QTimer(self, timeout=self.update)
        self.timer.start(1000)

    def initUI(self):
        self.temp = QLabel(self)

        vbox = QVBoxLayout()
        vbox.addWidget(self.temp)
        self.temp.setStyleSheet("background-color : #2B26c1")
        self.setLayout(vbox)

    def update(self):
        self.x += 1
        line = self.arduino.readline().decode()
        if line:
            self.y = int(line)

        pen = pg.mkPen(width=10)
        self.graphWidget.plot([self.x], [self.y],
                              pen=pen, symbol='x', symbolSize=30)
