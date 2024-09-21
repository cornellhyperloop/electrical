from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from widgets import *
from PyQt5.QtGui import *
import constants
from numpy import random
import numpy as np
import math

"""
FSM is the visualization UI for the Pod
"""

class FSM(QWidget):
    # Constructor to initialize the FSM (Finite State Machine) class
    def __init__(self, *args, **kwargs):
        super().__init__()
        # Coordinates and dimensions for the window
        self.left = 0
        self.top = 0
        self.width = args[0]
        self.height = args[1]
        # Initial state for the FSM
        self.currstate = constants.CURRENT_STATE
        # Call the initialization functions
        self.initUI()
        self.color()

    # Initialize the user interface
    def initUI(self):
        # Function to create and display a state with a corresponding image
        def create(state):
            # Load and scale the image for the state from constants
            im = QPixmap((constants.STATES[state]))
            im = im.scaled(100, 100, Qt.KeepAspectRatio, Qt.FastTransformation)
            
            # Create a label to display the state image
            label = QLabel()
            label.setPixmap(im)
            label.setFixedWidth(100)
            label.setFixedHeight(100)
            
            # Set stylesheet for the state label
            label.setStyleSheet("font-family: Helvetica; font-size: 14px; background-color : #2B26c1")
            label.setAutoFillBackground(True)
            return label

        # Function to create an arrow between two states to show transitions
        def arrow(start, end):
            # Get the positions of the start and end states
            startx, starty, endx, endy = start.pos().x(), start.pos().y(), end.pos().x(), end.pos().y()
            orig = ((startx + endx) / 2, (starty + endy) / 2)

            # Load the arrow image and adjust its size according to the distance between states
            arr = QPixmap(('state_icons/arrow.png'))
            length = np.sqrt((startx - endx) ** 2 + (starty - endy)**2)
            arr = arr.scaled(int(length - 110), 50)
            
            # Calculate the angle to rotate the arrow based on the positions
            if endx != orig[0] and endy != orig[1]:
                tan_theta = (endy - orig[1]) / (endx - orig[0])
                theta = math.degrees(np.arctan(tan_theta))
            elif endx == orig[0]:
                if endy > orig[1]:
                    theta = 90
                else:
                    theta = 270
            else:
                if endx > orig[0]:
                    theta = 0
                else:
                    theta = 180

            # Apply transformation to rotate the arrow image
            final = QTransform()
            final.rotate(theta)
            if (endy - orig[1]) > 0 and endx != orig[0]:
                final.rotate(180)
            if (endx > orig[0] and endy > orig[1]) or (endx < orig[0] and endy < orig[1]):
                final.rotate(180)
            arr = arr.transformed(final)

            # Create a label to hold the arrow image and position it correctly between the states
            label = QLabel()
            label.setPixmap(arr)
            label.setStyleSheet("background-color: transparent;")
            finalx, finaly = int((startx + endx - arr.size().width() + 100) / 2), int((starty + endy - arr.size().height() + 100) / 2)
            label.move(finalx, finaly)
            return label

        # Create the state labels using the 'create' function
        self.states = {i: create(i) for i in constants.STATES.keys()}

        # Create a grid layout to organize the states and arrows
        layout = QGridLayout()

        # Create a scene to position the states and arrows
        scene = QGraphicsScene(self.left, self.top, self.width * 1.07, self.height * 0.81)
        xi = int(self.height * 0.81 / 5)
        yi = int(self.width * 1.07 / 7)

        # Positioning states on the scene
        self.states["Stop"].move(2 * xi, 0*yi)
        scene.addWidget(self.states["Stop"])
        self.states["Crawl"].move(0 * xi, yi)
        scene.addWidget(self.states["Crawl"])
        self.states["Deceleration"].move(2 * xi, 2 * yi)
        scene.addWidget(self.states["Deceleration"])
        self.states["Emergency"].move(4 * xi, yi)
        scene.addWidget(self.states["Emergency"])
        self.states["Cruise"].move(4 * xi, 3 * yi)
        scene.addWidget(self.states["Cruise"])
        self.states["Verification"].move(6 * xi, 0*yi)
        scene.addWidget(self.states["Verification"])
        self.states["Pre-Acceleration"].move(6 * xi, 2 * yi)
        scene.addWidget(self.states["Pre-Acceleration"])
        self.states["Acceleration"].move(6 * xi, 3 * yi)
        scene.addWidget(self.states["Acceleration"])
        self.states["Overheating"].move(8 * xi, yi)
        scene.addWidget(self.states["Overheating"])
        self.states["Extreme Overheating"].move(8 * xi, 3 * yi)
        scene.addWidget(self.states["Extreme Overheating"])

        # Adding arrows to represent transitions between states
        scene.addWidget(arrow(self.states["Stop"], self.states["Crawl"]))
        scene.addWidget(arrow(self.states["Crawl"], self.states["Deceleration"]))
        scene.addWidget(arrow(self.states["Stop"], self.states["Crawl"]))
        scene.addWidget(arrow(self.states["Deceleration"], self.states["Stop"]))
        scene.addWidget(arrow(self.states["Verification"], self.states["Stop"]))
        scene.addWidget(arrow(self.states["Verification"], self.states["Pre-Acceleration"]))
        scene.addWidget(arrow(self.states["Verification"], self.states["Overheating"]))
        scene.addWidget(arrow(self.states["Pre-Acceleration"], self.states["Acceleration"]))
        scene.addWidget(arrow(self.states["Acceleration"], self.states["Cruise"]))
        scene.addWidget(arrow(self.states["Cruise"], self.states["Deceleration"]))
        scene.addWidget(arrow(self.states["Acceleration"], self.states["Deceleration"]))
        scene.addWidget(arrow(self.states["Overheating"], self.states["Extreme Overheating"]))

        # Create a QGraphicsView to display the scene with states and arrows
        view = QGraphicsView(scene)
        layout.addWidget(view)

        # Set the layout for the FSM widget
        self.setLayout(layout)

        # Timer to randomly change the current state every 2 seconds for testing
        self.timerFSMRand = QTimer(self, timeout=self.update)
        self.timerFSMRand.start(2000)

    def update(self):
        """
        Function to update the state randomly
        """
        self.undocolor()  # Undo the color change of the previous state
        self.currstate = random.choice(list(self.states.keys()))  # Pick a random state
        self.color()  # Highlight the new current state

    def color(self):
        """
        Function to highlight the current state with a different background color        
        """
        self.states[self.currstate].setStyleSheet("font-family: Helvetica; font-size: 14px; background-color : #8c88f8")
        self.states[self.currstate].update()

    def undocolor(self):
        """
        Function to revert the background color of the previous state
        """
        self.states[self.currstate].setStyleSheet("font-family: Helvetica; font-size: 14px; background-color : #2B26c1")
        self.states[self.currstate].update()
