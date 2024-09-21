from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

import constants

# Mostly the same logic as Accelerometer

class Speedometer(QWidget):
    def __init__(self, parent=None):
        """
        Initializes the Speedometer widget.

        Parameters:
            parent (QWidget): The parent widget for this speedometer display.
        """
        super(Speedometer, self).__init__(parent)
        self.initUI()  # Call the method to set up the UI

    def initUI(self):
        """
        Sets up the user interface for the Speedometer widget.

        This method creates a QDial to visually represent the current velocity. 
        The dial is initialized with a minimum and maximum value, and its initial 
        value is set based on the current velocity constant. The dial's 
        background color is also set based on whether the velocity exceeds a 
        predefined threshold. A vertical layout is created to hold the dial, 
        and a timer is set to update the display every second.
        """
        self.dial = QDial(self)  # Create a dial for velocity display
        self.dial.setMinimum(0)  # Set minimum value of the dial
        self.dial.setMaximum(100)  # Set maximum value of the dial
        self.dial.setValue(constants.CURRENT_VELOCITY)  # Set initial value of the dial
        
        # Change the background color based on the velocity threshold
        if constants.CURRENT_VELOCITY > constants.VELOCITY_THRESHOLD:
            self.dial.setStyleSheet("background-color : yellow")
        else:
            self.dial.setStyleSheet("background-color : lime green")

        vbox = QVBoxLayout()  # Create a vertical box layout for the dial

        vbox.addWidget(self.dial)  # Add the dial to the layout
        self.setLayout(vbox)  # Set the layout for this widget
        
        # Set up a QTimer to regularly call the update method
        self.timer = QTimer(self, timeout=self.update)
        self.timer.start(1000)  # Timer set to call update() every second

    def update(self):
        """
        Updates the speedometer dial based on the current value.

        This method retrieves the current value from the dial and updates the 
        velocity constant. It also adjusts the dial's background color based 
        on whether the current value exceeds the predefined velocity threshold.
        """
        constants.CURRENT_VELOCITY = self.dial.value()  # Update the constant with the current dial value
        
        # Change the background color based on the velocity threshold
        if self.dial.value() > constants.VELOCITY_THRESHOLD:
            self.dial.setStyleSheet("background-color : yellow")
        else:
            self.dial.setStyleSheet("background-color : lime green")
