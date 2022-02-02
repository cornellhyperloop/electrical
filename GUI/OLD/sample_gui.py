#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  7 12:33:01 2019

@author: aneesh
"""

import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style

from matplotlib import rcParams
rcParams['axes.titlepad'] = 20 




style.use('fivethirtyeight')

fig = plt.figure()
fig.suptitle("Hyperloop Pod Sensors", fontsize=22)

#plt.title("Hyperloop Pod Sensors", y=1.05)
short_range = fig.add_subplot(241)
long_range = fig.add_subplot(242)
current = fig.add_subplot(243)
voltage = fig.add_subplot(244)
temperature = fig.add_subplot(245)
imu = fig.add_subplot(246)
reflective_strip = fig.add_subplot(247)
plt.subplots_adjust(hspace=.5, wspace=0.4)

  

def animate_short_range(i):
    graph_data = open('sample_data.txt','r').read()
    lines = graph_data.split('\n')
    xs = []
    ys = []
    for line in lines:
        if len(line) > 1:
            x, y = line.split(',')
            xs.append(float(x))
            ys.append(float(y))
    short_range.clear()
    short_range.set_title("Short Range", fontsize=15)
    short_range.set_xlabel("Time", fontsize=12)
    short_range.set_ylabel("Inches", fontsize=12)
    short_range.plot(xs, ys)
    
def animate_long_range(i):
    graph_data = open('sample_data.txt','r').read()
    lines = graph_data.split('\n')
    xs = []
    ys = []
    for line in lines:
        if len(line) > 1:
            x, y = line.split(',')
            xs.append(float(x))
            ys.append(float(y))
    long_range.clear()
    long_range.set_title("Long Range", fontsize=15)
    long_range.set_xlabel("Time", fontsize=12)
    long_range.set_ylabel("Inches", fontsize=12)
    long_range.plot(xs, ys)
    
def animate_current(i):
    graph_data = open('sample_data.txt','r').read()
    lines = graph_data.split('\n')
    xs = []
    ys = []
    for line in lines:
        if len(line) > 1:
            x, y = line.split(',')
            xs.append(float(x))
            ys.append(float(y))
    current.clear()
    current.set_title("Current", fontsize=15)
    current.set_xlabel("Time", fontsize=12)
    current.set_ylabel("Amperes", fontsize=12)
    current.plot(xs, ys)
    
def animate_voltage(i):
    graph_data = open('sample_data.txt','r').read()
    lines = graph_data.split('\n')
    xs = []
    ys = []
    for line in lines:
        if len(line) > 1:
            x, y = line.split(',')
            xs.append(float(x))
            ys.append(float(y))
    voltage.clear()
    voltage.set_title("Voltage", fontsize=15)
    voltage.set_xlabel("Time", fontsize=12)
    voltage.set_ylabel("Volts", fontsize=12)
    voltage.plot(xs, ys)
    
def animate_temperature(i):
    graph_data = open('sample_data.txt','r').read()
    lines = graph_data.split('\n')
    xs = []
    ys = []
    for line in lines:
        if len(line) > 1:
            x, y = line.split(',')
            xs.append(float(x))
            ys.append(float(y))
    temperature.clear()
    temperature.set_title("Temperature", fontsize=15)
    temperature.set_xlabel("Time", fontsize=12)
    temperature.set_ylabel("Degrees Farhenheit", fontsize=12)
    temperature.plot(xs, ys)

def animate_imu(i):
    graph_data = open('sample_data.txt','r').read()
    lines = graph_data.split('\n')
    xs = []
    ys = []
    for line in lines:
        if len(line) > 1:
            x, y = line.split(',')
            xs.append(float(x))
            ys.append(float(y))
    imu.clear()
    imu.set_title("IMU", fontsize=15)
    imu.set_xlabel("Time", fontsize=12)
    imu.set_ylabel("Acceleration", fontsize=12)
    imu.plot(xs, ys)
    
def animate_reflective_strip(i):
    graph_data = open('sample_data.txt','r').read()
    lines = graph_data.split('\n')
    xs = []
    ys = []
    for line in lines:
        if len(line) > 1:
            x, y = line.split(',')
            xs.append(float(x))
            ys.append(float(y))
    reflective_strip.clear()
    reflective_strip.set_title("Reflective Strip", fontsize=15)
    reflective_strip.set_xlabel("Time", fontsize=12)
    reflective_strip.set_ylabel("Light", fontsize=12)
    reflective_strip.plot(xs, ys)
    

    
    
short = animation.FuncAnimation(fig, animate_short_range, interval=1000)
long = animation.FuncAnimation(fig, animate_long_range, interval=1000)
current_graph = animation.FuncAnimation(fig, animate_current, interval=1000)
voltage_graph = animation.FuncAnimation(fig, animate_voltage, interval=1000)
temperature_graph = animation.FuncAnimation(fig, animate_temperature, interval=1000)
imu_graph = animation.FuncAnimation(fig, animate_imu, interval=1000)
reflective_graph = animation.FuncAnimation(fig, animate_reflective_strip, interval=1000)


plt.show()