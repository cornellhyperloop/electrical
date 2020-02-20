#LEDscript

#include GPIO into namespace
import Adafruit_BBIO.GPIO as GPIO

#enable GPIO
GPIO.setup("P8_10", GPIO.OUT)
#turn on LED
GPIO.output("P8_10", GPIO.HIGH)
#turn off LED
GPIO.output("P8_10", GPIO.LOW)
