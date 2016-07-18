# coding: utf-8
import sqlite3
import time
import os
import sys

if not os.path.isfile('/tmp/sub.db'):
    sys.exit()
filename = 'pa_' + time.strftime('%Y%m%d') + '.csv'

conn = sqlite3.connect('/tmp/sub.db')
cursor = conn.cursor()
cursor.execute('select * from submitted where status=?',('1',))
values = cursor.fetchall()
#print(values)
try:
    with open("/tmp/{}".format(filename),'w',encoding='gbk') as file:
        file.write('id,name,phone,birthday,sex,give,dc1,dc2,status, ,response\n')
        for x in values:
            file.write(','.join(str(i)for i in list(x)) + '\n')
except Exception as E:
    print(E)
cursor.close()
conn.commit()
conn.close()



