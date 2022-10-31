from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import pandas as pd


class PlotButtons(QWidget):
    def __init__(self, plot):
        super(PlotButtons, self).__init__(None)
        self.plot = plot
        self.plot_reset = False
        self.initUI()
        self.downloaded = False

    def initUI(self):

        hbox = QHBoxLayout()

        # Reset plot button
        self.reset_plot_button = QPushButton(self)
        self.reset_plot_button.setText("Reset Plot")
        self.reset_plot_button.setStyleSheet(
            "font-family: Helvetica; font-size: 14px; background-color : #2B26c1")
        self.reset_plot_button.clicked.connect(self.resetPlot)

        self.example_button = QPushButton(self)
        self.example_button.setText("Example Button")
        self.example_button.setStyleSheet(
            "font-family: Helvetica; font-size: 14px; background-color : #2B26c1")

        self.downloadButton = QPushButton(self)
        self.downloadButton.setText("Download Data")
        self.downloadButton.setStyleSheet(
            "font-family: Helvetica; font-size: 14px; background-color : #2B26c1")
        self.downloadButton.clicked.connect(self.downloadData)

        hbox.addWidget(self.reset_plot_button)
        hbox.addWidget(self.example_button)
        hbox.addWidget(self.downloadButton)
        self.setLayout(hbox)

    def downloadData(self):
        self.plot.getPlotItem().writeCsv("Data.csv")

    def resetPlot(self):
        self.plot.clear()
        self.plot_reset = True

    def setPlotResetFlag(self, flag):
        self.plot_reset = flag

    def getPlotResetFlag(self):
        return self.plot_reset
