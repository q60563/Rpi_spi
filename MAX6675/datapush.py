import time
import RPi.GPIO as GPIO
import json,httplib

sck = 23
cs = 35
so = 21
clod5 = 38
hot5 = 40
clod4 = 32
hot4 = 36

UpperLimit = 0
LowerLimit = 0
Temp29 = 0
Temp31 = 0
Temp33 = 0
Temp35 = 0
Temp37 = 0
Average = 0 
status1 = "STOP"
status2 = "STOP"
status3 = "STOP"
status4 = "STOP"
status5 = "STOP"

GPIO.setmode(GPIO.BOARD)
GPIO.setup(clod5,GPIO.OUT)
GPIO.setup(hot5,GPIO.OUT)
GPIO.setup(clod4,GPIO.OUT)
GPIO.setup(hot4,GPIO.OUT)

GPIO.output(clod5,False)
GPIO.output(hot5,False)
GPIO.output(clod4,False)
GPIO.output(hot4,False)

def GPIOSET():
	GPIO.setmode(GPIO.BOARD)
	GPIO.setup(sck,GPIO.OUT)
	GPIO.setup(cs,GPIO.OUT)
	GPIO.setup(so,GPIO.IN)

	GPIO.output(cs,True)
	
def getTemp(TC):
	TC = "0";
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
		#TC += GPIO.input(so) << (i-1)
		TC = TC + str(GPIO.input(so))
		GPIO.output(sck,False)
	
	GPIO.output(sck,True)
	open = GPIO.input(so)
	GPIO.output(sck,False)

	for i in range(2, 0, -1):
		GPIO.output(sck,True)
		time.sleep(0.001)
		GPIO.output(sck,False)

	GPIO.output(cs, True)
	return (float)(int(TC,2)*0.25)
	
def parse():
	connection = httplib.HTTPSConnection('api.parse.com', 443)
	connection.connect()
	connection.request('POST', '/1/classes/temp', json.dumps({
        	"avg": Average,
        	"ktype1": 0,
        	"ktype2": 0,
        	"ktype3": 0,
        	"ktype4": Temp35,
        	"ktype5": Temp37
        	}),{
        	#"X-Parse-Application-Id": "Xu1HHxBfS7J54hNaheTE0PXLIf0vuk2GJAVYR0vv",
        	#"X-Parse-REST-API-Key": "oi5Na1YKsj9QMci6palMnTnvx12CB11nPgsjAzZ7",

		"X-Parse-Application-Id": "rPX5jyZBXe7L01MDfAnqr6ALKVGJw4RsGh3DZVD6",
		"X-Parse-REST-API-Key": "w7xtwucJKJUHasA0dxLznlPb8Kz3hPzaQFBtBhuv",
        	"Content-Type": "application/json"
        	})
	#results = json.loads(connection.getresponse().read())
	#print results

def device():
	connection = httplib.HTTPSConnection('api.parse.com', 443)
	connection.connect()
	connection.request('POST', '/1/classes/device', json.dumps({
        	"avg": Average,
        	"drive1": status1,
		"drive2": status2,
        	"drive3": status3,
        	"drive4": status4,
        	"drive5": status5
        	}),{
        	#"X-Parse-Application-Id": "Xu1HHxBfS7J54hNaheTE0PXLIf0vuk2GJAVYR0vv",
        	#"X-Parse-REST-API-Key": "oi5Na1YKsj9QMci6palMnTnvx12CB11nPgsjAzZ7",

		"X-Parse-Application-Id": "rPX5jyZBXe7L01MDfAnqr6ALKVGJw4RsGh3DZVD6",
		"X-Parse-REST-API-Key": "w7xtwucJKJUHasA0dxLznlPb8Kz3hPzaQFBtBhuv",
        	"Content-Type": "application/json"
        	})

while True:
	if cs == 35:
		GPIOSET()
		Temp35 = getTemp(0.0)
		cs = 37
	elif cs == 37:
		GPIOSET()
		Temp37 = getTemp(0.0)
		cs = 35
	Average = (Temp35 + Temp37) / 2
	UpperLimit = Average + 0.5
	LowerLimit = Average - 0.5

	parse()
	device()

	print "Temperature: "
	print "T35: " + str(Temp35) + "    " +  "T37: " + str(Temp37)
	print "Average: " + str(Average)	
	
	if Temp35 != 0 and Temp37 !=0 and Average != 0:
		if Temp37 > UpperLimit:
			GPIO.output(clod5,True)
			GPIO.output(hot5,False)
			status5 = "CLOD"	
		elif Temp37 < LowerLimit:
			GPIO.output(clod5,False)
			GPIO.output(hot5,True)
			status5 = "HOT"
		else:			
			GPIO.output(clod5,False)
			GPIO.output(hot5,False)
			status5 = "STOP"
              
		if Temp35 > UpperLimit:
                        GPIO.output(clod4,True)
                        GPIO.output(hot4,False)
			status4 = "CLOD"
                elif Temp35 < LowerLimit:
                        GPIO.output(clod4,False)
                        GPIO.output(hot4,True)
			status4 = "HOT"
                else:
                        GPIO.output(clod4,False)
                        GPIO.output(hot4,False)
			status4 = "STOP"
	#time.sleep(0.2)
	

