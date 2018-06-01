# -*- utf-8 -*-

from datetime import datetime
import os


def deleteOutOfDateFile(abspath):
    for f in os.listdir(abspath):
        f_join=os.path.join(abspath, f)
        if (os.path.isdir(f_join)):
            deleteOutOfDateFile(f_join)
        if (os.path.isfile(f_join)):
            '''判断时间'''
            mtime = datetime.fromtimestamp(
                os.path.getmtime(f_join)).strftime('%Y-%m-%d %H:%M:%S')
            print(f, mtime)

if (__name__ == '__main__'):
    deleteOutOfDateFile('.')

