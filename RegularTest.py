# -*-coding=utf-8-*-
import re
import urllib2
import HTMLParser





req = urllib2.Request('https://habrahabr.ru/')
response = urllib2.urlopen(req)
data = response.read()

print ('<article class=\"post post_preview\">(.*?)<\\article>')
var = re.findall(r'<article class=\"post post_preview\">(.*?)</article>', data, re.DOTALL)

for text in var:
    UserPublic = re.findall(r'<span class=\"user-info__nickname user-info__nickname_small\">(.*?)</span>', text, re.DOTALL)[0]
    Tittle = re.findall(r'class=\"post__title_link\">(.*?)</a>', text, re.DOTALL)[0]
    temp =re.findall(r'<h2 class=\"post__title\">(.*?)</h2>', text, re.DOTALL)[0]
    url = re.findall(r'<a href=\"(.*?)\" class', temp, re.DOTALL)[0]


    print ('{0}\n{1}\n{2}\n'.format(UserPublic,Tittle,url))


