from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class PlotButtons(QWidget):
    def __init__(self, plot):
        super(PlotButtons, self).__init__(None)
        self.plot = plot
        self.plot_reset = False
        self.initUI()

    def initUI(self):

        hbox = QHBoxLayout()

        # Reset plot button
        self.reset_plot_button = QPushButton(self)
        self.reset_plot_button.setText("Reset Plot")
        self.reset_plot_button.setStyleSheet("font-family: Helvetica; font-size: 14px; background-color : #2B26c1")
        self.reset_plot_button.clicked.connect(self.resetPlot)

        # Custom Data Point Button
        self.custom_point_button = QPushButton(self)
        self.custom_point_button.setText("Create Custom Data Point")
        self.custom_point_button.setStyleSheet("font-family: Helvetica; font-size: 14px; background-color : #2B26c1")
        self.custom_point_button.clicked.connect(self.createPoint)

        self.example_button = QPushButton(self)
        self.example_button.setText("Example Button")
        self.example_button.setStyleSheet("font-family: Helvetica; font-size: 14px; background-color : #2B26c1")

        hbox.addWidget(self.reset_plot_button)
        hbox.addWidget(self.custom_point_button)
        hbox.addWidget(self.example_button)
        self.setLayout(hbox)

    def resetPlot(self):
        self.plot.clear()
        self.plot_reset = True
    
    def setPlotResetFlag(self, flag):
        self.plot_reset = flag
    
    def getPlotResetFlag(self):
        return self.plot_reset

    def createPoint(self):
        x, ok = QInputDialog.getInt(None, 'Cutsom Coordinate', '<html style="font-size:12pt;">Enter x-coordinate:</html>')
        y, ok = QInputDialog.getInt(None, 'Custom Coordinate', '<html style="font-size:12pt;">Enter x-coordinate:</html>')
        if(ok):
            self.plot.plot([x],[y], pen=None, symbol='x', symbolSize = 30, symbolPen='g', symbolBrush=0.3, name='green')
        else:
            return None

      


    
    