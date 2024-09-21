from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from widgets import *  # Assuming 'Pod' is defined in widgets module, representing a 3D visualizer for the Hyperloop pod

"""
Visualizer class represents the user interface component that contains a 3D visualizer 
for the Hyperloop pod. 
"""
class Visualizer(QWidget):
    def __init__(self, *args, **kwargs):
        super(Visualizer, self).__init__()  # Initialize the QWidget parent class
        
        """
        Create a horizontal box layout (QHBoxLayout) to arrange child widgets horizontally.
        The layout will contain the 'Pod' widget, which is a 3D visualizer for the Hyperloop pod.
        """
        hbox = QHBoxLayout(self)  # Horizontal layout to hold the 3D visualizer (Pod)
        pod = Pod()  # Create an instance of the Pod widget (3D visualizer)
        
        hbox.addWidget(pod)  # Add the Pod widget to the horizontal layout
        self.setLayout(hbox)  # Apply the layout to the current widget (Visualizer)
