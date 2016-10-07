import RPi.GPIO as GPIO
#import getTemp
import max31855
try: 
	all_device = [40]
	GPIO.setmode(GPIO.BOARD)
	for i in all_device:
		GPIO.setup(i,GPIO.OUT)
		GPIO.output(i,True)

	s = [0,0,0,0,0]
	setting = float(raw_input("Setting: "))
	Ubound = setting + 0.5
	Lbound = setting - 0.5
	while True:
		#Temp = getTemp.run()
		Temp = max31855.run()
		for i in range(0,len(all_device),+2):
			if(Temp[i]=="open"):
				 s[i] = 0
			else:
				if(Temp[i]>Ubound):
					GPIO.output(all_device[i],False)
					s[i] = 1
				else:
					GPIO.output(all_device[i],True)
					s[i] = 0
		for i in range(1,len(all_device),+2):
			if(Temp[i]=="open"):
				s[i] = 0
			else:
				if(Temp[i]<Lbound):
					GPIO.output(all_device[i],False)
					s[i] = 1
				else:
					GPIO.output(all_device[i],True)
					s[i] = 0
		print "Sensing: " + str(Temp[:5])
		print "Control: " + str(Temp[5:])
		print "status: " + str(s)
		print "------------------------------------------------------"
except KeyboardInterrupt:
	GPIO.cleanup()			


