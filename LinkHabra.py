# coding=utf-8

import HTMLParser
import urllib2

class MyHTMLParser(HTMLParser.HTMLParser):
    def __init__(self, site_name, *args, **kwargs):
        # список ссылок
        self.links = []
        # имя сайта
        self.site_name = site_name
        # вызываем __init__ родителя
        HTMLParser.HTMLParser.__init__(self)
        # при инициализации "скармливаем" парсеру содержимое страницы
        self.feed(self.read_site_content())

    def read_site_content(self):
         return str(urllib2.urlopen(urllib2.Request('https://habrahabr.ru/')).read()).decode('UTF-8')

    def handle_starttag(self, tag, attrs):
         # проверяем является ли тэг тэгом ссылки
         #if tag =='div':
             #print('{0} - {1}'.format(tag,attrs))
         if tag == 'article':
               print('{0} - {1}'.format(tag,attrs))







parcer = MyHTMLParser('https://habrahabr.ru/')



req = urllib2.Request('https://habrahabr.ru/')
response = urllib2.urlopen(req)

data = response.read()

parser = HTMLParser.HTMLParser()

parser.feed(data.decode('UTF-8'))


print(parser.get_starttag_text())





print ('Successfull')




