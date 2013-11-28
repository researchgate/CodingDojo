import RPi.GPIO as GPIO ## Import GPIO library
import time

GPIO.setmode(GPIO.BOARD) ## Use board pin numbering
GPIO.setup(7, GPIO.OUT) ## Setup GPIO Pin 7 to OUT

for i in range(100):
	print "on"
	GPIO.output(7,True) ## Turn on GPIO pin 7
	time.sleep(0.05)
	print "off"
	GPIO.output(7,False)
	time.sleep(0.05)
