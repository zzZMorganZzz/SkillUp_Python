import urllib2
import json

pokemonListId = [1, 4, 7, 3, 90]  # max 802

for item in pokemonListId:
    req = urllib2.Request('http://pokeapi.co/api/v2/pokemon/{0}'.format(item), headers={'User-Agent': 'Mozilla/5.0'})
    response = urllib2.urlopen(req)
    obj = json.loads(response.read())
    print (obj['name'])
