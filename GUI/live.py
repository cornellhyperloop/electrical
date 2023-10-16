'''live.py authors: Mihika, Zarif, Steven, Stefan
    Date: 11/28/22

    Summary: reads data from the lines of info sent
    from the arduino the serial monitor at the usb port
    found in the arduino IDE
'''

import serial 
import time

arduino = serial.Serial(port="/dev/cu.usbmodem141101", baudrate = 9600, timeout = 1)
def write_read():           #reads lines of data from serial monitor
    time.sleep(0.05)
    data = arduino.readline()
    return data

while True:                 #run infinitely, print data using write_read()
    value = write_read()
    print(value)

#next step is to make the data look pretty and do live plotting with it