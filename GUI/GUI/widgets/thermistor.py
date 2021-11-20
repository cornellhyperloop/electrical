from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import serial


class Thermistor(QWidget):
    def __init__(self, parent=None):
        super(Thermistor, self).__init__(parent)
        self.initUI()
        #self.arduino = serial.Serial("/dev/cu.usbmodem143201")
        self.timer = QTimer(self, timeout=self.update)
        self.timer.start(1000)

    def initUI(self):
        self.temp = QLabel(self)

        vbox = QVBoxLayout()
        vbox.addWidget(self.temp)
        self.temp.setStyleSheet("background-color : rgb(143,255,91)")
        self.setLayout(vbox)

    def update(self):
	    pass
        #line = self.arduino.readline().decode()
        #if line:
        #    self.temp.setText(line)
