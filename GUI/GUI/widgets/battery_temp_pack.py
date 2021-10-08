from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import pyqtgraph as pg


from constants import BATTERY_AVG_TEMP


class TempGraph(QWidget):

    def __init__(self, parent=None):
        super(TempGraph, self).__init__(parent)
        self.x = 0
        self.y = 0

        # doesn't do anything right now
        self.select = QComboBox()
        self.select.addItem("1")
        self.select.addItem("2")
        self.select.addItem("3")

        self.menu = QSplitter(Qt.Horizontal)
        self.label = QLabel()
        self.label.setText("Battery: ")
        self.menu.addWidget(self.label)
        self.menu.addWidget(self.select)

        self.outerlayout = QVBoxLayout()
        self.outerlayout.addWidget(self.menu)
        self.graph_layout = QGridLayout()
        self.graphWidget = pg.PlotWidget()

        xs = []
        ys = []

        self.graphWidget.setBackground((224, 224, 224))
        pen = pg.mkPen(width=10)

        self.graph_layout.addWidget(self.graphWidget)
        self.outerlayout.addLayout(self.graph_layout)
        self.setLayout(self.outerlayout)
        self.timer = QTimer(self, timeout=self.update)
        self.timer.start(1000)

    def update(self):
        self.x += 1
        self.y += 1
        pen = pg.mkPen(width=10)
        self.graphWidget.plot([self.x], [BATTERY_AVG_TEMP],
                              pen=pen, symbol='x', symbolSize=30)