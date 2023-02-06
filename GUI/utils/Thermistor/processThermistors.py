"""
A script for reading thermistor readings from the serial monitor, processing 
them, and saving them to a file that will be read by the GUI.
"""

import serial
import json

serialPort = "" # update with your port

serialConn = serial.Serial(serialPort)

### Store the thermistor readings -----

thermistorValues = []

# Repeat as many times as needed
data = serialConn.readline().decode()
thermistorValues.append(data)


#### Save all the values in a json

# JSON module documentation: https://docs.python.org/3/library/json.html



serialConn.close()
