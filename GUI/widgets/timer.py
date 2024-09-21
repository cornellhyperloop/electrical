from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import QTimer, Qt, QSize
import sys


class Timer(QWidget):
    def __init__(self, *args, parent=None):
        """
        Initializes the Timer widget.

        Parameters:
            args (tuple): Additional arguments for width and height.
            parent (QWidget): The parent widget for this timer.
        """
        super(Timer, self).__init__(parent)  # Initialize the QWidget parent class
        self.width = int(args[0] / 10)  # Set the width based on passed arguments
        self.height = int(args[0] / 30)  # Set the height based on passed arguments
        self.initUI()  # Call the method to set up the user interface

    def initUI(self):
        """
        Sets up the user interface for the Timer widget.

        This method initializes the label for displaying the time and starts the timer
        that updates the label every 100 milliseconds.
        """
        self.count = 0  # Initialize the count for the timer
        self.start = True  # State variable to track if the timer is running
        
        # Create and style the label for displaying time
        self.label = QLabel("         Time         ", self)
        self.label.setAlignment(Qt.AlignCenter)  # Center the label text
        self.label.setStyleSheet(
            "font-family: Helvetica; font-size: 14px; background-color: #2B26c1; color: white; border: 1px grey")
        self.label.resize(int(self.width), int(self.height))  # Set label size
        
        # Initialize the timer and connect the timeout signal to the showTime method
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.showTime)  # Update the label on timeout
        self.timer.start(100)  # Start the timer with a 100 ms interval

    def showTime(self):
        """
        Updates the label to display the elapsed time.

        This method increments the count and updates the label text 
        to reflect the current time in seconds.
        """
        self.count += 1  # Increment the count
        text = f'Time: {self.count / 10} s'  # Calculate time in seconds
        self.label.setText(text)  # Update the label with the new time
        self.label.update()  # Refresh the label display

    def sizeHint(self):
        """
        Provides the recommended size for the Timer widget.

        Returns:
            QSize: The recommended size based on the specified width and height.
        """
        return QSize(int(self.width), int(self.height))  # Return the size hint
