
# Top level file
# Run using a Python Version <= 3.6

import sys
import pyqtgraph as pg
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton


def printSomething():
    print(10)


def main():
    gui = QApplication(sys.argv)

    # w = QWidget()
    # w.resize(250, 150)
    # w.move(300, 300)
    # w.setWindowTitle('Hyperloop GUI')

    # btn = QPushButton('Button', w)
    # btn.clicked.connect(printSomething)
    # btn.resize(btn.sizeHint())
    # btn.move(50, 50)

    graphWidget = pg.PlotWidget()
    gui.setCentralWidget(graphWidget)
    
    hour = [1,2,3,4,5,6,7,8,9,10]
    temperature = [30,32,34,32,33,31,29,32,35,45]
    graphWidget.plot(hour, temperature)

    graphWidget.show()
    
    #w.show()
    
    sys.exit(gui.exec())




if __name__ == '__main__':
    main()