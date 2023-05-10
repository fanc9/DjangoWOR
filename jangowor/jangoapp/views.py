from django.shortcuts import render
from django.http import HttpResponse
import MySQLdb
import cursor

# Create your views here.
def san (self):

    conn = MySQLdb.connect(host='127.0.0.1',database='san_db',user='root',password='Python@150')
    cursor=conn.cursor()



    cursor.execute('select * from em1')
    
    rows=cursor.fetchall()
    print('total num of rows:',cursor.rowcount)
    for row in rows:
        ENO=row[0]
        ENAME=row[1]
        return HttpResponse('%-6d %-15s'%(ENO,ENAME))
    cursor.close()
    conn.close()
