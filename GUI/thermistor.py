import serial
arduino = serial.Serial("/dev/cu.usbmodem143301")

list = []
line = arduino.readline().decode()
while line:
   list.append(line)
   print(line)
   line = arduino.readline().decode()


arduino.close()
