import json
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import serial
import constants

# DataReader can be instantiated with the GUI itself, and sensor widgets can
# take the DataReader.data_changed as a parameter & connect their updates to
# this QAction signal. One possibility:

# body.py:
# dataReader = DataReader()

# thermistor.py:
# dataReader.data_changed.connect(self.update)


class DataReader():
    def __init__(self, freq=1000):
        self.data = ""
        self.timer = QTimer(self, timeout=self.updateData)
        self.timer.start(freq)
        self.arduino = serial.Serial(constants.ARDUINO_SERIAL)
        self.data_changed = QAction()

    def updateData(self):
        line = self.arduino.readline().decode()
        if line:
            line = json.loads(line)
            self.data = line
            self.data_changed.trigger()

        QSlider.valueChanged
