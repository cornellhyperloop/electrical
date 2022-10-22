"""
A script for reading thermistor readings from the serial monitor, processing
them, and saving them to a file that will be read by the GUI.
"""

import serial
import json
import datetime
import time

serialPort = "/dev/cu.usbmodem141401"

serialConn = serial.Serial(serialPort)

#### Save all the values in a json
temp_in_fahrenheit = {}
start = datetime.now()

while (true):
    data = serialConn.readline().decode()
    now = datetime.now()
    change = now-start
    durations = change.total_seconds()
    temp_in_fahrenheit[float(durations)] = float(data)
    time.sleep(1)

result = json.dumps(temp_in_fahrenheit)

with open('thermistorReadings.json', 'w') as f:
    f.write(result)
    print("JSON file is created successfully")

# JSON module documentation: https://docs.python.org/3/library/json.html

serialConn.close()
