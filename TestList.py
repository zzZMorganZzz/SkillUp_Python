import psycopg2
import pprint
import sys

conn_string = "dbname=root user=krypton password=2JZ-gte@@"
conn = psycopg2.connect(conn_string)

cursor = conn.cursor()
# cursor.execute('SELECT maker, model, type FROM public.product')
# record = cursor.fetchall()


# for row in record:
#    print(row)
# pprint.pprint (record)
print("INSERT INTO product(maker, model, type) VALUES (\'{}\', \'{}\', \'{}\')".format('123', '123', 'PC'))
cursor.execute("INSERT INTO product(maker, model, type) VALUES (\'{}\', \'{}\', \'{}\')".format('0000000', '123', 'PC'))
conn.commit()
