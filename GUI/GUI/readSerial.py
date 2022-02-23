import serial
import time

# Update based on the value the Arduino IDE indicates
serialConn = "/dev/cu.usbmodem143201"

startTime = time.time()

while time.time() - startTime < 5: # continue for 5 secconds
    value = serialConn.readline.decode() # get the value written to the serial moniitor
    
    if value: # check if there's a new value
        print(value)

