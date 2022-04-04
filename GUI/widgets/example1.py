from PyQt5.QtWidgets import *
from PyQt5.QtGui import *


class Example1(QWidget):
    def __init__(self, parent=None):
        super(Example1, self).__init__(parent)
        self.button = QPushButton(self)
        self.button.setText('Button 1')
        self.button.setFont(QFont('AnyStyle', 18))
        self.button.setStyleSheet(
            "background-color : red; border-radius: 5px; font-weight: bold; border: 3px solid black")
       
