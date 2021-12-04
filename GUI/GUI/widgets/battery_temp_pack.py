from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from widgets import *


class TempGraph(QWidget):

    def __init__(self, parent=None):
        super(TempGraph, self).__init__(parent)
        self.select = QComboBox()
        self.Stack = QStackedWidget(self)
        self.stack1 = Graph()
        self.stack2 = Graph()
        self.stack3 = Pod()

        self.Stack.addWidget(self.stack1)
        self.Stack.addWidget(self.stack2)
        self.Stack.addWidget(self.stack3)

        self.select.addItem("?? ")
        self.select.addItem("thermistor")
        self.select.addItem("visualization")

        self.menu = QSplitter(Qt.Horizontal)
        self.menu.addWidget(self.Stack)
        self.layout2 = QVBoxLayout()
        self.layout2.addWidget(self.menu)
        self.layout2.addWidget(self.select)

        self.setLayout(self.layout2)

        self.select.currentIndexChanged.connect(self.display)

    def display(self, i):
        self.Stack.setCurrentIndex(i)
