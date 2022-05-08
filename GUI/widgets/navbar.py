from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from widgets import *

class NavBar(QWidget):
    def __init__(self, parent=None):
        super(NavBar, self).__init__(parent)
        hbox = QHBoxLayout(self)

        # Add example for multiple pages
        self.switchPages = QComboBox()
        self.switchPages.addItems(["Page 1", "Page 2"])
        self.switchPages.activated.connect(self.changePages)
        self.switchPages.setStyleSheet(
            "background-color : red; border-radius: 100px; font-weight: bold; border: 3px solid black; height: 60px; width: 70px")
       

        self.page1 = example1.Example1()
        self.page2 = example2.Example2()
        self.stacked = QStackedLayout(self)
        
        self.stacked.addWidget(self.page1)
        self.stacked.addWidget(self.page2)

        hbox.addWidget(self.switchPages)
        hbox.addLayout(self.stacked)

        self.setLayout(hbox)

    def changePages(self):
        self.stacked.setCurrentIndex(self.switchPages.currentIndex())
