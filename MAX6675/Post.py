import RPi.GPIO as GPIO
import gettemp 
import MySQLdb

host = "192.168.0.22"
user = "user"
passwd = "test"
table = "temp"
#db = MySQLdb.connect(host=host,user=user,passwd=passwd,db=table)
#cursor = db.cursor()

try:
	all_device = [40, 38, 36, 32, 26]
	GPIO.setmode(GPIO.BOARD)
	for i in all_device:
        	GPIO.setup(i,GPIO.OUT)
        	GPIO.output(i,True)

	s = [0,0,0,0,0]

	while True:
		Temp =  gettemp.run()
		for i in range(0,len(all_device),+2):
			if (Temp[i]>30):
				GPIO.output(all_device[i],False)
				s[i] = 1
			else:
				GPIO.output(all_device[i],True)
				s[i] = 0
		for i in range(1,len(all_device),+2):
			if (Temp[i]<30):
				GPIO.output(all_device[i],False)
				s[i] = 1
			else:
				GPIO.output(all_device[i],True)
				s[i] = 0
		print "Sensing: " + str(Temp[:5])
		print "Control: " + str(Temp[5:])
		print "status:  " + str(s)
		print "---------------------------------------------------"
except KeyboardInterrupt:
	GPIO.cleanup()

	#for i in Temp:
	#	if i > 50:
	#		print "error"
	#		while True:
	#			pass
	
#	cursor.execute("insert into st_Logs(float_Ktype1,float_Ktype2,float_Ktype3,float_Ktype4,float_Ktype5,float_Ktype6,float_Ktype7,float_Ktype8,float_Ktype9,float_Ktype10)values(%d,%d,%d,%d,%d,%d,%d,%d,%d,%d)"%(Temp[0],Temp[1],Temp[2],Temp[3],Temp[4],Temp[5],Temp[6],Temp[7],Temp[8],Temp[9]))

#	cursor.execute("insert into st_Devices(int_device1_c,int_device2_c,int_device3_c,int_device1_h,int_device2_h) values (%d,%d,%d,%d,%d)"%(s[0],s[2],s[4],s[1],s[3]))

#	cursor.execute("update st_Devices set float_Ktype1=%d,float_Ktype2=%d,float_Ktype3=%d,float_Ktype4=%d,float_Ktype5=%d,float_Ktype6=%d,float_Ktype7=%d,float_Ktype8=%d,float_Ktype9=%d,float_Ktype10=%d"%(Temp[0],Temp[1],Temp[2],Temp[3],Temp[4],Temp[5],Temp[6],Temp[7],Temp[8],Temp[9]))

#	cursor.execute("update st_Devices set int_device1_c=%d,int_device2_c=%d,int_device3_c=%d,int_device1_h=%d,int_device2_h=%d"%(1,1,1,1,1))
	
#	db.commit()

		


