from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from pyqtgraph import PlotWidget, plot
import pyqtgraph as pg


class Graph(QWidget):

    def __init__(self, parent=None):
        super(Graph, self).__init__(parent)
        self.x = 0
        self.y = 0
        self.layout = QGridLayout()
        self.graphWidget = pg.PlotWidget()
        # Sample data as array (neater demo)
        second = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        temperature = [30, 32, 34, 32, 33, 31, 29, 32, 35, 45]
        # Sample data from a txt file

        self.graphWidget.setBackground((224, 224, 224))
        # self.graphWidget.plot(second, temperature, pen=pen,
        #   symbol='x', symbolSize=30)
        self.layout.addWidget(self.graphWidget)
        self.setLayout(self.layout)
        self.timer = QTimer(self, timeout=self.update)
        self.timer.start(1000)

    def update(self):
        self.x += 1
        self.y += 1
        pen = pg.mkPen(width=10)
        self.graphWidget.plot([self.x], [self.y],
                              pen=pen, symbol='x', symbolSize=30)
