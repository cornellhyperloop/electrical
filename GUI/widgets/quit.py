from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import QSize
import sys


class Quit(QWidget):
    def __init__(self, *args, parent=None):
        """
        Initializes the Quit widget.

        Parameters:
            args (tuple): Additional arguments for width and height.
            parent (QWidget): The parent widget for this quit confirmation popup.
        """
        super(Quit, self).__init__(parent)  # Initialize the QWidget parent class
        self.width = args[0] / 10  # Set the width based on passed arguments
        self.height = args[1] / 30  # Set the height based on passed arguments
        self.initUI()  # Call the method to set up the user interface

    def initUI(self):
        """
        Sets up the user interface for the Quit widget.

        This method initializes the quit button with specific text, font, and styles.
        It connects the button's click event to the `pushedQuit` method to handle 
        the quit action.
        """
        self.setWindowTitle("Quit")  # Set the window title
        self.push = QPushButton(self)  # Create the quit button
        self.push.setText("Quit")  # Set button text
        self.push.setFont(QFont('AnyStyle', 18))  # Set button font size
        
        # Style the button with a red background color and other visual properties
        self.push.setStyleSheet(
            "background-color : red; border-radius: 5px; font-family: Helvetica; font-size: 14px; border: 3px solid black")
        
        self.push.clicked.connect(self.pushedQuit)  # Connect button click to quit function
        self.push.resize(int(self.width), int(self.height))  # Set button size

    def pushedQuit(self):
        """
        Exits the application when the quit button is clicked.

        This method calls sys.exit() to terminate the program.
        """
        sys.exit()  # Exit the application

    def sizeHint(self):
        """
        Provides the recommended size for the Quit widget.

        Returns:
            QSize: The recommended size based on the specified width and height.
        """
        return QSize(int(self.width), int(self.height))  # Return the size hint
