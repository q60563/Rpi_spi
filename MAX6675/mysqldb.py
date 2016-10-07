import MySQLdb

db = MySQLdb.connect(host="192.168.0.22", user="user",passwd="test",db="temp")

cursor = db.cursor()

cursor.execute("INSERT INTO st_Logs(float_Ktype1,float_Ktype2,float_Ktype3,float_Ktype4,float_Ktype5,float_Ktype6,float_Ktype7,float_Ktype8,float_Ktype9,float_Ktype10) VALUES(%d,%d,%d,%d,%d,%d,%d,%d,%d,%d)"%(10,9,8,7,6,5,4,3,2,1))

db.commit()
cursor.execute("SELECT * FROM st_Logs")
result = cursor.fetchall()
for rs in result:
	print rs

