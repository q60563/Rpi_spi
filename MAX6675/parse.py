import json
import httplib

connection = httplib.HTTPSConnection('api.parse.com', 443)
connection.connect()
connection.request('POST', '/1/classes/temp', json.dumps({
	"avg": 30,
	"ktype1": 10,
	"ktype2": 20,
	"ktype3": 30,
	"ktype4": 40,
	"ktype5": 50
	}),{
	"X-Parse-Application-Id": "rPX5jyZBXe7L01MDfAnqr6ALKVGJw4RsGh3DZVD6",
	"X-Parse-REST-API-Key": "w7xtwucJKJUHasA0dxLznlPb8Kz3hPzaQFBtBhuv",
	"Content-Type": "application/json"
	})
results = json.loads(connection.getresponse().read())
print results
