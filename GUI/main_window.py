from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from widgets import example1, example2
from utils.header import Header
from utils.left import Left
from utils.right import Right


class MainWindow(QWidget):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__()

        # Insert change here
        self.setWindowTitle("Hyperloop GUI")
        

        hbox = QHBoxLayout(self)

        # bottom = QFrame()
        # bottom.setFrameShape(QFrame.StyledPanel)

        header = Header()

        # Add example for multiple pages
        # self.switchPages = QComboBox()
        # self.switchPages.addItems(["Page 1", "Page 2"])
        # self.switchPages.activated.connect(self.changePages)
        # self.switchPages.setStyleSheet(
        #     "background-color : red; border-radius: 5px; font-weight: bold; border: 3px solid black")
       

        # self.page1 = example1.Example1()
        # self.page2 = example2.Example2()
        # self.stacked = QStackedLayout(self)
        
        # self.stacked.addWidget(self.page1)
        # self.stacked.addWidget(self.page2)

        left = Left()

        right = Right()

        splitter4 = QSplitter(Qt.Vertical)
        splitter4.addWidget(header)
        splitter4.addWidget(left)
        splitter4.addWidget(right)
        splitter4.setSizes([50, 50, 300])

        hbox.addWidget(splitter4)
        
        #hbox.addWidget(self.switchPages)
        #hbox.addLayout(self.stacked)

        self.setLayout(hbox)
        QApplication.setStyle(QStyleFactory.create('Cleanlooks'))
        self.setStyleSheet(" background-color: #494949;")

        self.setGeometry(300, 300, 1250, 900)
    
    #def changePages(self):
    #    self.stacked.setCurrentIndex(self.switchPages.currentIndex())
