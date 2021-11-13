from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *



class Thermistor(QWidget):
    def __init__(self, parent=None):
        super(Thermistor, self).__init__(parent)
        self.initUI()

    def initUI(self):
        avgtemp = QLabel(self)
        with open('temp.txt') as f:
            lines = f.readlines()

        temp = []
        for t in lines:
            temp.append(float(t))
        temp = round(sum(temp) / len(temp), 3)
        avgtemp.setText("Avg temp: " + str(temp))

        vbox = QVBoxLayout()
        vbox.addWidget(avgtemp)
        self.setLayout(vbox)