import time
import RPi.GPIO as GPIO

sck = 23
all_cs =[37, 33, 31, 29, 15, 35, 13, 11, 18, 16]
so = 21
Temp = [0,0,0,0,0,0,0,0,0,0]
#all_device = [26, 32, 36, 38, 40]

GPIO.setmode(GPIO.BOARD)
GPIO.setup(sck,GPIO.OUT)
for i in all_cs:
	GPIO.setup(i,GPIO.OUT)
	GPIO.output(i,True)
GPIO.setup(so,GPIO.IN)
"""
for i in all_device:
	GPIO.setup(i,GPIO.OUT)
	GPIO.output(i,False)
"""

def getTemp(cs):
        TC = "0"
        GPIO.output(cs,False)
        time.sleep(0.002)
        GPIO.output(cs,True)
        time.sleep(0.22)

        GPIO.output(cs,False)
        GPIO.output(sck,True)
        time.sleep(0.001)
        GPIO.output(sck,False)

        for i in range(12, 0, -1):
                GPIO.output(sck,True)
                TC = TC + str(GPIO.input(so))
                GPIO.output(sck,False)

        GPIO.output(sck,True)
	open = 0
	GPIO.output(sck,False)

        for i in range(2, 0, -1):
                GPIO.output(sck,True)
                time.sleep(0.001)
		GPIO.output(sck,False)

        GPIO.output(cs, True)
        return (float)(int(TC,2)*0.25)
def run():
	for i in range(0, len(all_cs) ):
		try:
			Temp[i] = getTemp( int(all_cs[i]) )
		except IndentationError:
			Temp.append(0)
		#print "T" + str(all_cs[i]) +": " + str(Temp[i])
	return Temp
#print run()
