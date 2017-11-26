import urllib2
import json

req = urllib2.Request('http://api.football-data.org/v1/competitions/446')
response = urllib2.urlopen(req)
obj = json.loads(response.read())
print (obj['caption'])

print ('Teams list:')
isStop = False
req = urllib2.Request('http://api.football-data.org/v1/competitions/446/teams')
response = urllib2.urlopen(req)
obj = json.loads(response.read())

for items in obj['teams']:
    print ('    '+items['name'])



