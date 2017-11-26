import urllib2
import json

req = urllib2.Request('http://api.open-notify.org/iss-now.json')
response = urllib2.urlopen(req)
obj = json.loads(response.read())
currentPosition = obj['iss_position']
print ('Current Position:{0},{1}'.format(currentPosition['latitude'], currentPosition['longitude']))

