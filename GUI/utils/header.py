from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from widgets import *
from PyQt5.QtGui import *
import constants as cons
from widgets import progressBar

"""
Header represents the horizontal menu bar on the main Graph UI.
"""
class Header(QWidget):
    def __init__(self, w=1000, h=500, *args, **kwargs):
        super(Header, self).__init__()
        self.width = w
        self.height = h

        # Set up main layout for the Header widget
        hbox = QHBoxLayout(self)
        hbox.setContentsMargins(0, 0, 0, 0)

        # Load custom stylesheet for header
        sshFile = "utils/header.css"
        with open(sshFile, "r") as fh:
            stylesheet = fh.read()
        self.setStyleSheet(stylesheet)

        # Create and arrange the grid layout for buttons and widgets
        grid1 = QGridLayout(self)
        self.addHeaderButtons(grid1)

        grid2 = QGridLayout(self)
        self.addNavButtons(grid2)

        # Set up the vertical layout combining both grids
        vbox = QVBoxLayout(self)
        vbox.addLayout(grid1)
        vbox.addLayout(grid2)
        hbox.addLayout(vbox)

        # Set up the progress bar and logo display in the header
        self.setupProgressBarAndLogo(hbox)

        # Timer to trigger the progress bar updates
        self.timer = QTimer(self, timeout=self.update)
        self.timer.start(1000)

        self.show()

    def addHeaderButtons(self, grid):
        """
        Add header buttons for quit, timer, help, emergency, and FSM.
        """
        quit = Quit(self.width, self.height)
        grid.addWidget(quit, 0, 0, alignment=Qt.AlignCenter)

        timer = Timer(self.width, self.height)
        grid.addWidget(timer, 0, 2, alignment=Qt.AlignCenter)

        help_popup = HelpPopup(self.width, self.height)
        grid.addWidget(help_popup, 0, 3, alignment=Qt.AlignCenter)

        fsm = FSM()
        emergency_button = EmergencyButton(fsm, self.width, self.height)
        grid.addWidget(emergency_button, 0, 4, alignment=Qt.AlignCenter)

    def addNavButtons(self, grid):
        """
        Add navigation buttons (Home, Visualizer, Battery, Temperature, FSM).
        """
        self.b1 = self.createNavButton("Home", grid, 0, 0)
        self.b2 = self.createNavButton("Visualizer", grid, 0, 1)
        self.b3 = self.createNavButton("Battery", grid, 0, 2)
        self.b4 = self.createNavButton("Temperature", grid, 0, 3)
        self.b5 = self.createNavButton("FSM", grid, 0, 4)

    def createNavButton(self, name, layout, row, col):
        """
        Helper to create a QPushButton and add it to the layout.
        """
        btn = QPushButton(name)
        btn.clicked.connect(lambda: self.navbar(btn))
        btn.resize(self.width // 5, self.height // 20)
        layout.addWidget(btn, row, col)
        return btn

    def setupProgressBarAndLogo(self, hbox):
        """
        Set up the progress bar and logo in a horizontal splitter.
        """
        splitter = QSplitter(Qt.Horizontal)

        # Progress bar setup
        self.pBarContainer = progressBar.ProgressBar()
        splitter.addWidget(self.pBarContainer.label)
        splitter.addWidget(self.pBarContainer.pBar)
        splitter.setSizes([self.height // 30, self.height // 30])

        # Logo setup
        hyperloop_logo = QPixmap('state_icons/logo.png').scaled(200, 100)
        logo_label = QLabel()
        logo_label.setPixmap(hyperloop_logo)
        logo_label.setFixedSize(200, 100)
        logo_label.setStyleSheet("border: 1px grey;")
        splitter.addWidget(logo_label)

        # Add the splitter to the main layout
        hbox.addWidget(splitter)

    def update(self):
        """
        Update the progress bar and set styles according to progress levels.
        """
        self.pBarContainer.pBar.setValue(self.pBarContainer.pBar.value() + 5)
        progress = self.pBarContainer.pBar.value()

        if progress < 50:
            self.pBarContainer.pBar.setStyleSheet(cons.PBAR_LOW_PROGRESS)
        elif progress < 100:
            self.pBarContainer.pBar.setStyleSheet(cons.PBAR_MED_PROGRESS)
        else:
            self.pBarContainer.pBar.setStyleSheet(cons.PBAR_HIGH_PROGRESS)

    def navbar(self, button):
        """
        Handle navigation button clicks and return the index.
        Only the temperature page is not implemented (index 3).
        """
        buttons = [self.b1, self.b2, self.b3, self.b4, self.b5]
        index = buttons.index(button)

        if index == 3:  # Temperature page is not implemented
            return 0
        else:
            return index

