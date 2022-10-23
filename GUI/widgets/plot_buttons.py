from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class PlotButtons(QWidget):
    def __init__(self, plot):
        super(PlotButtons, self).__init__(None)
        self.plot = plot
        self.plot_reset = False
        self.current_plot = 0
        self.plot_names = ['Plot 1', 'Plot 2']
        self.changed_plot = False
        self.initUI()

    def initUI(self):

        hbox = QHBoxLayout()

        # Reset plot button
        self.reset_plot_button = QPushButton(self)
        self.reset_plot_button.setText("Reset Plot")
        self.reset_plot_button.setStyleSheet("font-family: Helvetica; font-size: 14px; background-color : #2B26c1")
        self.reset_plot_button.clicked.connect(self.resetPlot)

        self.example_button = QPushButton(self)
        self.example_button.setText("Example Button")
        self.example_button.setStyleSheet("font-family: Helvetica; font-size: 14px; background-color : #2B26c1")

        self.plot_dropdown = QComboBox()
        self.plot_dropdown.setEditable(True)
        self.plot_dropdown.lineEdit().setAlignment(Qt.AlignCenter)
        self.plot_dropdown.lineEdit().setReadOnly(True)
        for plot_name in self.plot_names:
            self.plot_dropdown.addItem(plot_name)
        self.plot_dropdown.setStyleSheet("font-family: Helvetica; font-size: 14px; background-color : #2B26c1;")
        self.plot_dropdown.currentTextChanged.connect(self.plotDropdownChanged)
       
        hbox.addWidget(self.reset_plot_button)
        hbox.addWidget(self.example_button)
        hbox.addWidget(self.plot_dropdown)
        self.setLayout(hbox)

    def resetPlot(self):
        self.plot.clear()
        self.plot_reset = True
    
    def setPlotResetFlag(self, flag):
        self.plot_reset = flag
    
    def getPlotResetFlag(self):
        return self.plot_reset

    def plotDropdownChanged(self, dropdownValue):
        self.current_plot = self.plot_names.index(dropdownValue)
        self.changed_plot = True

    def getCurrentPlot(self):
        return self.current_plot

    def getChangedPlot(self):
        return self.changed_plot
    
    def setChangedPlot(self, newValue):
        self.changed_plot = newValue
