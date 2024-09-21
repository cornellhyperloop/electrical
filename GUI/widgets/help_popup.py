from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import QSize
import sys


class HelpPopup(QWidget):
    def __init__(self, *args, parent=None):
        """
        Initializes the HelpPopup widget.

        Parameters:
            args (tuple): Additional arguments for width and height.
            parent (QWidget): The parent widget for this help popup.
        """
        super(HelpPopup, self).__init__(parent)
        self.width = args[0] / 10  # Set the width based on passed arguments
        self.height = args[1] / 30  # Set the height based on passed arguments
        self.initUI()  # Call the method to set up the UI

    def initUI(self):
        """
        Sets up the user interface for the HelpPopup widget.

        This method initializes the help button with specific text, font, and styles.
        It connects the button's click event to the `pushedHelp` method to display 
        the help message.
        """
        self.setWindowTitle("Click button")  # Set the window title
        self.push = QPushButton(self)  # Create the help button
        self.push.setText("Help")  # Set button text
        self.push.setFont(QFont('AnyStyle', 18))  # Set button font size
        
        # Style the button with a custom background color and other visual properties
        self.push.setStyleSheet(
            "background-color : #2B26c1; border-radius: 5px; font-family: Helvetica; font-size: 14px; border: 3px #2B26c1")
        
        self.push.clicked.connect(self.pushedHelp)  # Connect button click to help function
        self.push.resize(int(self.width), int(self.height))  # Set button size

    def pushedHelp(self):
        """
        Displays a help message when the help button is clicked.

        This method creates a message box that provides information on how to use 
        the GUI, encouraging users to click on various buttons for more details.
        """
        self.msgBox = QMessageBox()  # Create a message box instance
        self.msgBox.setWindowTitle("Tutorial on using GUI")  # Set message box title
        self.msgBox.setText(
            "Click on the various buttons in order to receive more information about them")  # Set the message text
        self.msgBox.setIcon(QMessageBox.Information)  # Set the icon for the message box
        x = self.msgBox.exec()  # Execute the message box and wait for user response

    def sizeHint(self):
        """
        Provides the recommended size for the HelpPopup widget.

        Returns:
            QSize: The recommended size based on the specified width and height.
        """
        return QSize(int(self.width), int(self.height))  # Return the size hint
