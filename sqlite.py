import sqlite3
import time
import os
conn = sqlite3.connect(r'c:\Users\zheng LM\Desktop\sub.db')
cursor = conn.cursor()
cursor.execute('select * from submitted where status=?',('1',))
values = cursor.fetchall()
filename = 'pa_' + time.strftime('%Y%m%d') + '.csv'
filedir = str(r'c:\Users\zheng LM\Desktop\')
fpath = os.path.join(filedir,filename)
print(fpath)
'''
try:
    with open("fpath",'w') as file:
        for x in values:
            file.write(','.join(str(i)for i in list(x)) + '\n')
finally:
    os.path.join(fdir,filename)
'''
