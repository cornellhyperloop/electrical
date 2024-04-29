from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from widgets import *
from utils.header import Header
from utils.body import Body
from utils.visualizer import Visualizer


class MainWindow(QWidget):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__()

        # Insert change here
        self.setWindowTitle("Hyperloop GUI")

        hbox = QHBoxLayout(self)

        # bottom = QFrame()
        # bottom.setFrameShape(QFrame.StyledPanel)
        width = 1250
        height = 900

        header = Header(w=width, h=height)
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

        body = Body()
        visualizer = Visualizer()

        self.Stack.addWidget(body)
        self.Stack.addWidget(visualizer)

        splitter4 = QSplitter(Qt.Vertical)
        splitter4.addWidget(header)

        splitter4.addWidget(self.Stack)
        splitter4.setSizes([50, 350])

        hbox.addWidget(splitter4)

        self.setLayout(hbox)
        QApplication.setStyle(QStyleFactory.create('Cleanlooks'))
        self.setStyleSheet("background-color: #bebebe;")

        self.setGeometry(300, 300, width, height)

    def renderPage(self, i):
        self.Stack.setCurrentIndex(i)
