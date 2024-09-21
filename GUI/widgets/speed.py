from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

import constants


class Speed(QWidget):
    def __init__(self, parent=None):
        """
        Initializes the Speed widget.

        Parameters:
            parent (QWidget): The parent widget for this speed display.
        """
        super(Speed, self).__init__(parent)
        self.initUI()  # Call the method to set up the UI

    def initUI(self):
        """
        Sets up the user interface for the Speed widget.

        This method creates two QLabel widgets to display the current velocity and 
        acceleration. The labels are styled with a specific font and background color 
        and are added to a horizontal layout. A timer is also set up to update the 
        displayed values every second.
        """
        self.setObjectName("display")  # Set the object name for the widget
        self.velocity = QLabel(self)  # Create label for velocity display
        self.acceleration = QLabel(self)  # Create label for acceleration display

        self.velocity.setText("Current Velocity: " +
                              str(constants.CURRENT_VELOCITY) + " m/s")
        self.velocity.setStyleSheet(
            "font-family: Helvetica; font-size: 14px; background-color : #2B26c1")
        self.velocity.setAlignment(Qt.AlignCenter)  # Center the text

        self.acceleration.setText("Current Acceleration: " +
                                  str(constants.ACCELERATION) + " m/s²")
        self.acceleration.setStyleSheet(
            "font-family: Helvetica; font-size: 14px; background-color : #2B26c1")
        self.acceleration.setAlignment(Qt.AlignCenter)  # Center the text

        hbox = QHBoxLayout()  # Create a horizontal box layout
        splitter = QSplitter(Qt.Horizontal)  # Create a horizontal splitter (not used here)

        # Add velocity and acceleration labels to the horizontal layout
        hbox.addWidget(self.velocity)
        hbox.addWidget(self.acceleration)

        self.setLayout(hbox)  # Set the layout for this widget

        # Set up a QTimer to regularly call the update method
        self.timer = QTimer(self, timeout=self.update)
        self.timer.start(1000)  # Timer set to call update() every second

    def update(self):
        """
        Updates the displayed values for velocity and acceleration.

        This method retrieves the current values from constants and updates the 
        corresponding QLabel widgets to reflect the latest measurements.
        """
        self.velocity.setText("Current Velocity: " +
                              str(constants.CURRENT_VELOCITY) + " m/s")
        self.acceleration.setText(
            "Current Acceleration: " + str(constants.ACCELERATION) + " m/s²")
