import urllib
import json

req = urllib.Request("http://api.open-notify.org/iss-now.json")
response = urllib.urlopen(req)

obj = json.loads(response.read())

print (obj['timestamp'])
print (obj['iss_position']['latitude'])