from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from widgets import *


class Visualizer(QWidget):
    def __init__(self, *args, **kwargs):
        super(Visualizer, self).__init__()
        hbox = QHBoxLayout(self)
        #pod = Pod()
        #hbox.addWidget(pod)

        self.setLayout(hbox)
