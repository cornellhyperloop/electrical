from PySide import QtGui, QtCore
import pyqtgraph as pg
import numpy as np
import threading
import time
import random

VIEWXRANGE = 20
VIEWYRANGE = 80
#operating limits for safe range
UPPERLIMIT = 150
LOWERLIMIT = 50

dataStreamX = [0]
dataStreamY = [100]
exceededLimitX = []
exceededLimitY = []

#SIMULATE DATA STREAM START
#PROGRAM IS NOT THREAD SAFE, FOR SIMULATING ACTUAL DATA ONLY, DO NOT BE SUPRISED IF THIS CRASHES
def dummyData():
    startTime = time.time()
    while True:
        dataStreamX.append( time.time()- startTime)
        dataStreamY.append( dataStreamY[-1] + random.randint(-10,10) )
        time.sleep( random.uniform(0.0,2.0) )

t = threading.Thread(target=dummyData)
t.start()
#SIMULATE DATA STREAM END

app = QtGui.QApplication([])

w = QtGui.QTabWidget()

#tab1 stuff
plot = pg.PlotWidget()
upperLine = pg.InfiniteLine(pos = UPPERLIMIT, angle=0, movable=False,pen=("#F00"))
lowerLine = pg.InfiniteLine(pos = LOWERLIMIT, angle=0, movable=False,pen=("#F00"))
plot.addItem(upperLine)
plot.addItem(lowerLine)
tab1 = QtGui.QWidget()
layout1 = QtGui.QGridLayout()
layout1.addWidget(plot, 0, 1, 3, 1)
tab1.setLayout(layout1)
curve = plot.plot(dataStreamX, dataStreamY, pen=("F3F"), symbol=None)
#ecurve is all points that exceeded limits of safe operating range
ecurve = plot.plot(exceededLimitX, exceededLimitY, pen=None, symbol='x')

#tab2 stuff
plot1 = pg.PlotWidget()
upperLine1 = pg.InfiniteLine(pos = UPPERLIMIT, angle=0, movable=False,pen=("#F00"))
lowerLine1 = pg.InfiniteLine(pos = LOWERLIMIT, angle=0, movable=False,pen=("#F00"))
ax = plot1.getAxis('bottom')
plot1.scene().removeItem(ax)
bg = pg.BarGraphItem(x=[0], height=[20], width=0.6, brush='g')
plot1.addItem(bg)
plot1.addItem(upperLine1)
plot1.addItem(lowerLine1)
tab2 = QtGui.QWidget()
layout2 = QtGui.QGridLayout()
layout2.addWidget(plot1, 0, 1)
tab2.setLayout(layout2)

#add tabs
w.addTab(tab1, "Dynamic line graph")
w.addTab(tab2, "Dynamic bar graph")

## Create a grid layout to manage the widgets size and position
layout = QtGui.QGridLayout()
w.setLayout(layout)


w.show()

global currIndex
currIndex = 0

def update():
    global currIndex
    #hacky way of adding special marks for exceeded limit values
    for i in range(currIndex,len(dataStreamX)):
        if dataStreamY[i] > UPPERLIMIT or dataStreamY[i] < LOWERLIMIT:
            exceededLimitX.append(dataStreamX[i])
            exceededLimitY.append(dataStreamY[i])
        currIndex+=1
    #update all data and scroll graph
    curve.setData(dataStreamX,dataStreamY)
    ecurve.setData(exceededLimitX,exceededLimitY)
    plot.setXRange(dataStreamX[-1]-VIEWXRANGE, dataStreamX[-1])
    plot.setYRange(dataStreamY[0]-VIEWYRANGE, dataStreamY[0]+VIEWYRANGE)

    #update bar graph height, change color if not in safe range
    bg.setOpts(height=dataStreamY[-1],brush='r' if dataStreamY[-1] > UPPERLIMIT or dataStreamY[-1] < LOWERLIMIT else 'g' );
    plot1.setYRange(dataStreamY[0]-VIEWYRANGE, dataStreamY[0]+VIEWYRANGE)
    
timer = QtCore.QTimer()
timer.timeout.connect(update)
timer.start(1000)


app.exec_()
