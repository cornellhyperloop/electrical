import serial
import matplotlib.pyplot as plt
import numpy as np

from PyQt5 import QtWidgets, uic
from pyqtgraph import PlotWidget, plot
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QHBoxLayout, QGridLayout, QLabel, QTableWidget
import pyqtgraph as pg


import pyqtgraph as pg
import sys  # We need sys so that we can pass argv to QApplication
import os

# benson is doing some editingefjh3uwiof
plt.ion()
fig = plt.figure()
2fuh12oifhj1p

i=0
x1 = list()
x2 = list()
x3 = list()
x4 = list()

y1 = list()
y2 = list()
y3 = list()
y4 = list()

i = 0
ser1 = serial.Serial('COM8', 9600, timeout=0)
ser2 = serial.Serial('COM9', 9600, timeout=0)
ser3 = serial.Serial('COM10', 9600, timeout=0)
ser4 = serial.Serial('COM11', 9600, timeout=0)

ser1.close()
ser2.close()
ser3.close()
ser4.close()
ser1.open()
ser2.open()
ser3.open()
ser4.open()

while True:

    data1 = ser1.readline()
    data2 = ser2.readline()
    data3 = ser3.readline()
    data4 = ser4.readline()

    plt.subplot(411)
    plt.plot(i, float(data1.decode()))

    plt.subplot(412)
    plt.plot(i, float(data2.decode()))

    plt.subplot(413)
    plt.plot(i, float(data3.decode()))

    plt.subplot(414)
    plt.plot(i, float(data4.decode()))

    x1.append(i)
    y1.append(data1.decode())
    x2.append(i)
    y2.append(data2.decode())
    x3.append(i)
    y3.append(data3.decode())
    x4.append(i)
    y4.append(data4.decode())

    i += 1
    plt.show()
    plt.pause(0.0001)  # Note this correction
