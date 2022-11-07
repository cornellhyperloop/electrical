from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5 import QtGui
import sys
from widgets import *
from utils.header import Header
from utils.body import Body
from utils.visualizer import Visualizer
from utils.batteryPage import BatteryPage
from utils.FSM import FSM


class MainWindow(QWidget):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__()

        # Insert change here
        self.setWindowTitle("Hyperloop GUI")

        hbox = QHBoxLayout(self)

        width = 1250
        height = 900

        header = Header(w=int(width), h=int(height))
        header.b1.clicked.connect(
            lambda: self.renderPage(header.navbar(header.b1)))
        header.b2.clicked.connect(
            lambda: self.renderPage(header.navbar(header.b2)))
        header.b3.clicked.connect(
            lambda: self.renderPage(header.navbar(header.b3)))
        header.b4.clicked.connect(
            lambda: self.renderPage(header.navbar(header.b4)))
        header.b5.clicked.connect(
            lambda: self.renderPage(header.navbar(header.b5)))

        self.Stack = QStackedWidget(self)

        body = Body(int(width), int(height))
        visualizer = Visualizer()
        batteryPage = BatteryPage()
        fsm = FSM(width, height)

        self.Stack.addWidget(body)
        self.Stack.addWidget(visualizer)
        self.Stack.addWidget(batteryPage)
        # temperature page not implemented yet
        self.Stack.addWidget(Body(width, height))
        self.Stack.addWidget(fsm)

        splitter4 = QSplitter(Qt.Vertical)
        splitter4.addWidget(header)

        splitter4.addWidget(self.Stack)
        splitter4.setSizes([50, 350])

        hbox.addWidget(splitter4)

        self.setLayout(hbox)
        QApplication.setStyle(QStyleFactory.create('Cleanlooks'))
        self.setStyleSheet("background-color: #bebebe;")

        self.setGeometry(300, 300, width, height)

        self.showFullScreen()

    def renderPage(self, i):
        self.Stack.setCurrentIndex(i)
