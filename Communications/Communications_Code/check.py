import serial
import time

# make sure the 'COM#' is set according the Windows Device Manager
ser = serial.Serial('COM4', 9600, timeout=1)
time.sleep(2)

for i in range(50):
    line = ser.readline()   # read a byte
    if line:
        string = line.decode().strip()  # convert the byte string to a unicode string
        # num = int(string)  # convert the unicode string to an int
        print(string)

ser.close()
