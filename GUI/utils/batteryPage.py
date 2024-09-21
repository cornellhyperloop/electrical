from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from widgets import *  # Assuming 'Battery' widget is defined in widgets module
from PyQt5.QtGui import *
import pyqtgraph as pg

"""
BatteryPage class represents a page in the GUI that displays multiple Battery widgets.
Each Battery widget displays information about the status of individual batteries.
This layout organizes multiple Battery widgets vertically using QVBoxLayout.
"""
class BatteryPage(QWidget):
    """
    Initializes the BatteryPage class by creating a vertical layout and adding 
    six Battery widgets to it. Each widget is labeled and managed individually.
    """
    def __init__(self, *args, **kwargs):
        super(BatteryPage, self).__init__()  # Initialize the QWidget parent class
        
        """
        Create a vertical box layout to arrange Battery widgets vertically.
        QVBoxLayout arranges child widgets in a vertical stack.
        """
        hbox = QVBoxLayout(self)  # Vertical layout for Battery widgets
        
        """
        Iterate from 1 to 6 and create a Battery widget for each iteration. 
        The Battery widget's ID is passed to differentiate between batteries.
        Add each Battery widget to the vertical layout.
        """
        for i in range(1, 7):
            hbox.addWidget(Battery(i))  # Add Battery widget with an ID (1 to 6)

        """
        Set the layout for the BatteryPage widget to be the vertical layout (hbox) 
        containing the Battery widgets.
        """
        self.setLayout(hbox)  # Apply layout to the current widget (BatteryPage)
