from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import QSize
from .fsm import FSM
import sys


class EmergencyButton(QWidget):
    def __init__(self, fsm, *args, parent=None):
        """
        Initializes the EmergencyButton widget.

        Parameters:
            fsm (FSM): The finite state machine instance to interact with.
            args (tuple): Additional arguments for width and height.
            parent (QWidget): The parent widget for this button.
        """
        super(EmergencyButton, self).__init__(parent)
        self.fsm = fsm  # Store the FSM instance for state management
        self.width = args[0] / 10  # Set the width based on passed arguments
        self.height = args[1] / 30  # Set the height based on passed arguments
        self.initUI()  # Call the method to set up the UI

    def initUI(self):
        """
        Sets up the user interface for the EmergencyButton widget.

        This method initializes the button with specific text, font, and styles. 
        It also connects the button's click event to the `pushedEmergency` method 
        to handle emergency state transitions. The button's size is set according 
        to the specified dimensions.
        """
        self.setWindowTitle("Click button")  # Set the window title
        self.push = QPushButton(self)  # Create the button
        self.push.setText("Emergency Break")  # Set button text
        self.push.setFont(QFont('AnyStyle', 18))  # Set button font size

        # Style the button with a red background and other visual properties
        self.push.setStyleSheet(
            "background-color : red; border-radius: 5px; font-family: Helvetica; font-size: 14px; border: 3px solid black")
        
        self.push.clicked.connect(self.pushedEmergency)  # Connect button click to emergency function
        self.push.resize(int(self.width), int(self.height))  # Set button size

    def msgButtonClick(self, i):
        """
        Prints the text of the clicked button.

        Parameters:
            i (QPushButton): The button that was clicked.
        """
        print("Button clicked is:", i.text())  # Print the text of the clicked button

    def pushedEmergency(self):
        """
        Handles the emergency button click event.

        This method changes the state of the FSM to 'Emergency' when the button 
        is clicked, indicating an emergency situation.
        """
        self.fsm.fsm.setState('Emergency')  # Change FSM state to 'Emergency'

    def sizeHint(self):
        """
        Provides the recommended size for the EmergencyButton widget.

        Returns:
            QSize: The recommended size based on the specified width and height.
        """
        return QSize(int(self.width), int(self.height))  # Return the size hint

