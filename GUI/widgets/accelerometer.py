from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

import constants


class Accelerometer(QWidget):
    def __init__(self, parent=None):
        """
        Initializes the Accelerometer widget.

        Parameters:
            parent (QWidget): The parent widget for this accelerometer display.
        """
        super(Accelerometer, self).__init__(parent)
        self.initUI()  # Call the method to set up the UI

    def initUI(self):
        """
        Sets up the user interface for the Accelerometer widget.

        This method creates a QDial to visually represent the current acceleration. 
        The dial is initialized with a minimum and maximum value, and its initial 
        value is set based on the current acceleration constant. The dial's 
        background color is also set based on whether the acceleration exceeds a 
        predefined threshold. A vertical layout is created to hold the dial, 
        and a timer is set to update the display every second.
        """
        self.dial = QDial(self)  # Create a dial for acceleration display
        self.dial.setMinimum(0)  # Set minimum value of the dial
        self.dial.setMaximum(100)  # Set maximum value of the dial
        self.dial.setValue(constants.ACCELERATION)  # Set initial value of the dial
        
        # Change the background color based on the acceleration threshold
        if constants.ACCELERATION > constants.ACCELERATION_THRESHOLD:
            self.dial.setStyleSheet("background-color : red")
        else:
            self.dial.setStyleSheet("background-color : green")

        vbox = QVBoxLayout()  # Create a vertical box layout for the dial

        vbox.addWidget(self.dial)  # Add the dial to the layout
        self.setLayout(vbox)  # Set the layout for this widget
        
        # Set up a QTimer to regularly call the update method
        self.timer = QTimer(self, timeout=self.update)
        self.timer.start(1000)  # Timer set to call update() every second

    def update(self):
        """
        Updates the accelerometer dial based on the current value.

        This method retrieves the current value from the dial and updates the 
        acceleration constant. It also adjusts the dial's background color based 
        on whether the current value exceeds the predefined acceleration threshold.
        """
        constants.ACCELERATION = self.dial.value()  # Update the constant with the current dial value
        
        # Change the background color based on the acceleration threshold
        if self.dial.value() > constants.ACCELERATION_THRESHOLD:
            self.dial.setStyleSheet("background-color : red")
        else:
            self.dial.setStyleSheet("background-color : green")
