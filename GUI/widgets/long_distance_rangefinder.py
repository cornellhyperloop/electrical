from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import constants
import string


class LongDistanceRangefinder(QWidget):
    def __init__(self, parent=None):
        super(LongDistanceRangefinder, self).__init__(parent)
        self.initUI()

    def initUI(self):
        ldrf = QLabel(self)
        ldrf.setText("Distance: " + str(constants.DISTANCE))
        ldrf.setAlignment(Qt.AlignCenter)
<<<<<<< HEAD
        ldrf.setStyleSheet("background-color : #2B26c1")
=======
        ldrf.setStyleSheet(
            "font-family: Helvetica; font-size: 14px; background-color : #2B26c1")
>>>>>>> 088593597150e78bab5f05267d052282c28f0e0b
