import spidev
import os
import time
import RPi.GPIO as GPIO

spi = spidev.SpiDev()
spi.open(0,0)

GPIO.setmode(GPIO.BOARD)
GPIO.setup(37,GPIO.OUT)
GPIO.output(37,True)

while True:
	GPIO.output(37,False)
	adc = spi.xfer2([1,(8)<<4,0])
	data = ((adc[1]&3)<<8) + adc[2]
	print data
	volts = (data*3.3)/float(1023)
	volts = round(volts,4)
	print volts
	temp = volts*100
	temp = round(temp,2)
	print temp
	time.sleep(1)
	GPIO.output(37,True)
