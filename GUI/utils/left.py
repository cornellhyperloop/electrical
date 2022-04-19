from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from widgets import *


class Left(QWidget):
    def __init__(self, *args, **kwargs):
        super(Left, self).__init__()
        hbox = QHBoxLayout(self)

        sshFile = "utils/left.css"
        with open(sshFile, "r") as fh:
            qstr = str(fh.read())

        splitter3 = QSplitter(Qt.Horizontal)
        speed = Speed()
        splitter3.addWidget(speed)
        speedometer = Speedometer()
        splitter3.addWidget(speedometer)
        accelerometer = Accelerometer()
        splitter3.addWidget(accelerometer)
        hbox.addWidget(splitter3)

        self.setStyleSheet(qstr)
