
import RPi.GPIO as GPIO
import time

PIN = 12
GPIO.setmode(GPIO.BOARD)
GPIO.setup(PIN,GPIO.OUT)

GPIO.output(PIN,True)
time.sleep(1.0)
GPIO.output(PIN,False)
time.sleep(1.0)