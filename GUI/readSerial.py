import serial
import time

# Update based on the value the Arduino IDE indicates
serialConn = "/dev/cu.usbmodem1401"
ser= serial.Serial(serialConn)

startTime = time.time()

while time.time() - startTime < 1: # continue for 5 secconds
    value = ser.readline().decode() # get the value written to the serial moniitor
    
    if value: # check if there's a new value
        print(value)
