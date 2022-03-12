from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from widgets import *


class Right(QWidget):
    def __init__(self, *args, **kwargs):
        super(Right, self).__init__()

        sshFile = "right.css"
        with open(sshFile, "r") as fh:
            qstr = str(fh.read())

        hbox = QHBoxLayout(self)

        vgraph = QSplitter(Qt.Horizontal)
        ###

        graph = TempGraph()
        vgraph.addWidget(graph)
        vgraph.setSizes([2, 2])

        hbox.addWidget(vgraph)
        self.setLayout(hbox)

        self.setStyleSheet(qstr)
