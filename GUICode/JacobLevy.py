import numpy as np
import pyqtgraph as pg
from pyqtgraph.Qt import QtCore, QtGui

#Simple plot
data = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
pg.plot(data, title="Simple graph of data fitting x^2", )

#bargraph
win = pg.plot()
win.setWindowTitle('Example BarGraphItem')

x = np.arange(1,6)
y1 = np.log10(x)
y2 = np.log10(x+1)
y3 = np.log10(x+2)

bg1 = pg.BarGraphItem(x=x, height=y1, width=0.3, brush='r')
bg2 = pg.BarGraphItem(x=x+0.33, height=y2, width=0.3, brush='g')
bg3 = pg.BarGraphItem(x=x+0.66, height=y3, width=0.3, brush='b')

win.addItem(bg1)
win.addItem(bg2)
win.addItem(bg3)

if __name__ == '__main__':
    import sys
    if sys.flags.interactive != 1 or not hasattr(QtCore, 'PYQT_VERSION'):
        pg.QtGui.QApplication.exec_()
