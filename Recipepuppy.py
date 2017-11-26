import urllib2
import json

productsList ='milk,eggs'

req = urllib2.Request('http://www.recipepuppy.com/api/?i={0}'.format(productsList))
response = urllib2.urlopen(req)
obj = json.loads(response.read())
for items in obj['results']:
    print (items['title'])
    print ('    '+items['thumbnail'])
    print ('    ' + items['href'])
    print ('    ' + items['ingredients'])
    print ('')


#print ('Current Position:{0},{1}'.format(currentPosition['latitude'], currentPosition['longitude']))
