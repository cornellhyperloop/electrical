from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import pyqtgraph as pg


from constants import ACCELERATION


class AccelerationGraph(QWidget):

    def __init__(self, parent=None):
        super(AccelerationGraph, self).__init__(parent)
        self.x = 0
        self.y = 0
        self.layout = QGridLayout()
        self.graphWidget = pg.PlotWidget()

        xs = []
        ys = []

        self.graphWidget.setBackground((224, 224, 224))
        pen = pg.mkPen(width=10)

        self.layout.addWidget(self.graphWidget)
        self.setLayout(self.layout)
        self.timer = QTimer(self, timeout=self.update)
        self.timer.start(1000)

    def update(self):
        self.x += 1
        self.y += 1
        pen = pg.mkPen(width=10)
        self.graphWidget.plot([self.x], [ACCELERATION],
                              pen=pen, symbol='x', symbolSize=30)
