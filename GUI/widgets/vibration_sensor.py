from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import constants

class VibrationSensor(QWidget):
  def __init__(self, parent=None):
    super(VibrationSensor, self).__init__(parent)
    self.initUI()

  def initUI(self):
    sensor = QLabel(self)

    sensor.setText("Vibration Sensor: " + constants.VIBRATIONLEVEL)
    sensor.setAlignment(Qt.AlignCenter)
    sensor.setStyleSheet("background-color : rgb(143,255,91)")

    vbox = QVBoxLayout()

    vbox.addWidget(sensor)

    self.setLayout(vbox)