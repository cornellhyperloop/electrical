from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from widgets import *
from utils.header import Header
from utils.left import Left
from utils.right import Right


class MainWindow(QWidget):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__()

        # Insert change here
        self.setWindowTitle("Hyperloop GUI")
        sshFile = "test.css"
        with open(sshFile, "r") as fh:
            qstr = str(fh.read())

        hbox = QHBoxLayout(self)

        # bottom = QFrame()
        # bottom.setFrameShape(QFrame.StyledPanel)

        header = Header()

        left = Left()

        right = Right()

        splitter4 = QSplitter(Qt.Vertical)
        splitter4.addWidget(header)
        splitter4.addWidget(left)
        splitter4.addWidget(right)
        splitter4.setSizes([50, 50, 300])

        hbox.addWidget(splitter4)
        self.setLayout(hbox)
        QApplication.setStyle(QStyleFactory.create('Cleanlooks'))

        self.setGeometry(300, 300, 1250, 900)
