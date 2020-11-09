#!/usr/bin/env python

"""
Simple script to determine if there are major movements with the IMU 
based on the yaw, pitch, and roll.
"""

from vnpy import *
from joblib import load
import time
import algorithms
import funcs


def main():
    # Setup sensor
    s = VnSensor()
    s.connect("COM5", 115200) # change the connection parameter appropriately
    model = load('yprClassifier.joblib') # load classifier
    file = "data.txt"

    while(True):
        currYPR = s.read_yaw_pitch_roll()
        yaw = currYPR.x
        pitch = currYPR.y
        roll = currYPR.z
        time.sleep(0.5) # Delay 0.5 seconds

        # [accX, accY, accZ, angRateX, angRateY, angRateZ, magX, magY, magZ, temp, pressure, attQ]
        data = funcs.extraData(s)
        f = open(file, "a+")
        for val in data:
            f.write(str(val) + " ")
        
        problem = algorithms.algorithm2(s, yaw, pitch, roll)

        if (problem):
        # Do something
            print("Problem")
            f.write("Problem" + "\n")
        else:
            print("No problem")
            f.write("No problem" + "\n")

        f.close()


if __name__ == "__main__":
    main()