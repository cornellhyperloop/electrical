from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import constants


class ProximitySensor(QWidget):
    def __init__(self, parent=None):
        """
        Initializes the ProximitySensor widget.

        Parameters:
            parent (QWidget): The parent widget for this sensor.
        """
        super(ProximitySensor, self).__init__(parent)
        self.initUI()  # Call the method to set up the UI

    def initUI(self):
        """
        Sets up the user interface for the Proximity Sensor widget.

        This method creates four QLabel widgets, each representing a proximity sensor's state. 
        Each label is styled with a specific font and background color, and they are added 
        to a vertical layout.
        """
        sensor1 = QLabel(self)
        sensor2 = QLabel(self)
        sensor3 = QLabel(self)
        sensor4 = QLabel(self)

        sensor1.setText("Proximity Sensor 1: " +
                        constants.PROXIMITY_SENSOR_STATE1)
        sensor1.setAlignment(Qt.AlignCenter)
        sensor1.setStyleSheet(
            "font-family: Helvetica; font-size: 14px; background-color : #2B26c1")

        sensor2.setText("Proximity Sensor 2: " +
                        constants.PROXIMITY_SENSOR_STATE2)
        sensor2.setAlignment(Qt.AlignCenter)
        sensor2.setStyleSheet(
            "font-family: Helvetica; font-size: 14px; background-color : #2B26c1")

        sensor3.setText("Proximity Sensor 3: " +
                        constants.PROXIMITY_SENSOR_STATE3)
        sensor3.setAlignment(Qt.AlignCenter)
        sensor3.setStyleSheet(
            "font-family: Helvetica; font-size: 14px; background-color : #2B26c1")

        sensor4.setText("Proximity Sensor 4: " +
                        constants.PROXIMITY_SENSOR_STATE4)
        sensor4.setAlignment(Qt.AlignCenter)
        sensor4.setStyleSheet(
            "font-family: Helvetica; font-size: 14px; background-color : #2B26c1")

        vbox = QVBoxLayout()  # Create a vertical box layout

        # Add sensor labels to the vertical layout
        vbox.addWidget(sensor1)
        vbox.addWidget(sensor2)
        vbox.addWidget(sensor3)
        vbox.addWidget(sensor4)

        self.setLayout(vbox)  # Set the layout for this widget
