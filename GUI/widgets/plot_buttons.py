from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import constants 



class PlotButtons(QWidget):
    def __init__(self, plot):
        super(PlotButtons, self).__init__(None)
        self.plot = plot
        self.plot_reset = False
        self.current_plot = 0
        self.plot_names = ['Plot 1', 'Plot 2']
        self.changed_plot = False
        self.rescale_axes = False
        self.initUI()
        self.downloaded = False

    def initUI(self):

        widFile = constants.WIDGETS
        with open(widFile, "r") as fh:
            qstr = str(fh.read())

        hbox = QHBoxLayout()

        # Reset plot button
        self.reset_plot_button = QPushButton(self)
        self.reset_plot_button.setText("Reset Plot")
        self.reset_plot_button.setStyleSheet(qstr)
        self.reset_plot_button.clicked.connect(self.resetPlot)

        self.export_button = QPushButton(self)
        self.export_button.setText("Export Graph")
        self.export_button.setStyleSheet(qstr)
        self.export_button.clicked.connect(self.exportGraph)
        
        self.downloadButton = QPushButton(self)
        self.downloadButton.setText("Download Data")
        self.downloadButton.setStyleSheet(qstr)
        self.downloadButton.clicked.connect(self.downloadData)
        

        self.plot_dropdown = QComboBox()
        self.plot_dropdown.setEditable(True)
        self.plot_dropdown.lineEdit().setAlignment(Qt.AlignCenter)
        self.plot_dropdown.lineEdit().setReadOnly(True)
        for plot_name in self.plot_names:
            self.plot_dropdown.addItem(plot_name)
        self.plot_dropdown.setStyleSheet(qstr)
        self.plot_dropdown.currentTextChanged.connect(self.plotDropdownChanged)

        # Add the widget for resizing the plot axes
        resize_input_widgets = QSplitter(Qt.Horizontal)
        row1 = QSplitter(Qt.Horizontal)
        row2 = QSplitter(Qt.Horizontal)
        row3 = QSplitter(Qt.Horizontal)

        self.textbox1 = QLineEdit(self)
        self.textbox1.setFixedSize(50, 20)
        self.textbox1.setStyleSheet(qstr)

        self.textbox2 = QLineEdit(self)
        self.textbox2.setFixedSize(50, 20)
        self.textbox2.setStyleSheet(qstr)

        self.textbox3 = QLineEdit(self)
        self.textbox3.setFixedSize(50, 20)
        self.textbox3.setStyleSheet(qstr)

        self.textbox4 = QLineEdit(self)
        self.textbox4.setFixedSize(50, 20)
        self.textbox4.setStyleSheet(qstr)

        self.rescale_axes_button = QPushButton(self)
        self.rescale_axes_button.setText("Rescale Axes")
        self.rescale_axes_button.setFixedSize(100, 20)
        
        self.rescale_axes_button.setStyleSheet(qstr)
        self.rescale_axes_button.clicked.connect(self.rescaleAxes)

        row1.addWidget(self.textbox1)
        row1.addWidget(self.textbox2)
        row2.addWidget(self.textbox3)
        row2.addWidget(self.textbox4)
        row3.addWidget(self.rescale_axes_button)

        resize_input_widgets.addWidget(row1)
        resize_input_widgets.addWidget(row2)
        resize_input_widgets.addWidget(row3)

        hbox.addWidget(self.reset_plot_button)
        hbox.addWidget(self.export_button)
        hbox.addWidget(self.downloadButton)
        hbox.addWidget(self.plot_dropdown)
        hbox.addWidget(resize_input_widgets)
        hbox.setAlignment(self.reset_plot_button, Qt.AlignTop)
        hbox.setAlignment(self.export_button, Qt.AlignTop)
        hbox.setAlignment(self.downloadButton, Qt.AlignTop)
        hbox.setAlignment(self.plot_dropdown, Qt.AlignTop)
        hbox.setAlignment(resize_input_widgets, Qt.AlignTop)

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

    def exportGraph(self):
        self.plot.getPlotItem().writeImage(constants.GRAPH_IMG_NAME)

    def plotDropdownChanged(self, dropdownValue):
        self.current_plot = self.plot_names.index(dropdownValue)
        self.changed_plot = True

    def getCurrentPlot(self):
        return self.current_plot

    def getChangedPlot(self):
        return self.changed_plot

    def setChangedPlot(self, newValue):
        self.changed_plot = newValue

    def rescaleAxes(self):
        self.x_min = int(self.textbox1.text())
        self.x_max = int(self.textbox2.text())
        self.y_min = int(self.textbox3.text())
        self.y_max = int(self.textbox4.text())
        self.rescale_axes = True

    def getRescaleAxesFlag(self):
        return self.rescale_axes

    def setRescaleAxesFlag(self, flag):
        self.rescale_axes = flag

    def getXAxesLimits(self):
        return [self.x_min, self.x_max]

    def getYAxesLimits(self):
        return [self.y_min, self.y_max]
