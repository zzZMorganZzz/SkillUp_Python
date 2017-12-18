# -*-coding=utf-8-*-
import psycopg2
import pprint
import sys

def GetData(query):
    conn_string = "dbname=Habrahabr user=krypton password=2JZ-gte@@"
    conn = psycopg2.connect(conn_string)
    cursor = conn.cursor()
    cursor.execute(query)
    record = cursor.fetchall()
    return  record

print (u'Все статьи с сылками')
for item in GetData("SELECT post_name, post_url FROM public.post"):
    print(u'{0}\n{1}'.format(item[0].decode('utf-8'),item[1]))
print ('\n\n')

print (u'Все статьи с авторами')
for item in GetData("SELECT post_name, post_url,autor_name FROM public.post inner join public.autor on post.autor_guid=autor.autor_guid"):
    print(u'{0}\n{1}\n Автор:{2}'.format(item[0].decode('utf-8'),item[1],item[2]))
print ('\n\n')

