import serial
import time
arduino = serial.Serial(port="/dev/cu.usbmodem11101", baudrate = 9600, timeout=.1)
def write_read():
    time.sleep(0.05)
    data = arduino.readline().decode()
    return data
while True:
    value = write_read()
    print(value)