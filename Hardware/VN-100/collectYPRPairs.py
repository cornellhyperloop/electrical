#!/usr/bin/env python

"""
Simple script to collect pairs of yaw, pitch, and roll values from the IMU, 
and if there were major movements.
"""

from vnpy import *


def main():
    # Setup sensor
    s = VnSensor()
    s.connect("COM5", 115200) # change the connection parameter appropriately
    file = "test.txt" # filename

    # Setup IMU for the first reading then press enter
    x = input("Prepare for first reading (enter 'stop' to stop)")
    while ("stop" not in x.lower()):
        
        out1 = str(s.read_yaw_pitch_roll().x) + ", " + str(s.read_yaw_pitch_roll().y) + ", " + str(s.read_yaw_pitch_roll().z)

        # Setup IMU for the second reading then press enter
        y = input("Prepare for second reading")
        out2 = str(s.read_yaw_pitch_roll().x) + ", " + str(s.read_yaw_pitch_roll().y) + ", " + str(s.read_yaw_pitch_roll().z)

        z = input("Enter 0 if there was major movement, otherwise enter 1: ")
        while (z not in ["0", "1"]):
            z = input("Enter 0 if there was major movement, otherwise enter 1: ")

        f = open(file, "a+")
        output = out1 + ", " + out2 + ", " + z
        f.write(output + "\n")
        f.close()

        x = input("Prepare for first reading (enter stop to stop)")


if __name__ == "__main__":
    main()
