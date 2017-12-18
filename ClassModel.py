# coding=utf-8
import HTMLParser
import urllib2
import re
import uuid
import psycopg2


class PostHabrInfo:
    def __init__(self):
        self.url = None
        self.post_name = None
        self.guid = str(uuid.uuid4())

    def __str__(self):
        return u'\n{0}\n{1}\n'.format(self.post_name, self.url)


class Publisher:
    def __init__(self):
        self.Name = None
        self.guid = str(uuid.uuid4())

    def __str__(self):
        return u'\n{0}'.format(self.Name)


class Manager:
    def __init__(self):
        self.conn_string = "dbname=Habrahabr user=krypton password=2JZ-gte@@"
        self.conn = psycopg2.connect(self.conn_string)

    def GetPost(self, data):
        post = PostHabrInfo()
        publish = Publisher()
        publish.Name =re.findall(r'<span class=\"user-info__nickname user-info__nickname_small\">(.*?)</span>', data, re.DOTALL)[0]
        post.post_name = re.findall(r'class=\"post__title_link\">(.*?)</a>', data, re.DOTALL)[0]
        temp = re.findall(r'<h2 class=\"post__title\">(.*?)</h2>', data, re.DOTALL)[0]
        post.url = re.findall(r'<a href=\"(.*?)\" class', temp, re.DOTALL)[0]
        post.post_name = post.post_name.replace('\'','')


        return [post, publish]

    def GetPostListTheData(self, data):
        ResultList = []
        var = re.findall(r'<article class=\"post post_preview\">(.*?)</article>', data, re.DOTALL)
        for text in var:
            ResultList.append(self.GetPost(text))
        return ResultList

    def GetPostGetSite(self, address):
        req = urllib2.Request(address)
        response = urllib2.urlopen(req)
        data = response.read()
        return self.GetPostListTheData(data)

    def SavePosts(self, arrayData):
        cursor = self.conn.cursor()
        for item in arrayData:
            cursor.execute('SELECT autor_guid FROM public.autor where autor_name=\'{0}\''.format(item[1].Name))
            record = cursor.fetchall()
            if len(record)==0:
                cursor.execute("INSERT INTO public.autor(autor_guid, autor_name)VALUES(\'{0}\', \'{1}\')".format(item[1].guid,item[1].Name))
                self.conn.commit()
            else:
                item[1].guid = record[0][0]
            cursor.execute('SELECT post_guid FROM public.post where post_url=\'{0}\';'.format(item[0].url))
            record = cursor.fetchall()
            if len(record)==0:
                cursor.execute("INSERT INTO public.post(post_guid, post_name, post_url, autor_guid)"
                                "VALUES(\'{0}\', \'{1}\',\'{2}\',\'{3}\')".format(item[0].guid,item[0].post_name,item[0].url,item[1].guid))
                self.conn.commit()







var = Manager()
array =var.GetPostGetSite('https://habrahabr.ru/')
var.SavePosts(array)
