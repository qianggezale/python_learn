# -*- utf-8 -*-

from datetime import datetime
import os
kuozhanming = ('.txt')
myspantime = 20  #分钟


def deleteOutOfDateFile(abspath):
    for f in os.listdir(abspath):
        f_join = os.path.join(abspath, f)
        if (os.path.isdir(f_join)):
            deleteOutOfDateFile(f_join)
        if (os.path.isfile(f_join)):
            koutext = os.path.splitext(f)[1]
            if (koutext and (koutext in kuozhanming)):
                '''判断时间'''
                mtime = datetime.fromtimestamp(
                    os.path.getmtime(f_join)).strftime('%Y-%m-%d %H:%M:%S')
                spantime = datetime.now() - datetime.strptime(
                    mtime, '%Y-%m-%d %H:%M:%S')
                spanint = spantime.seconds / 60
                if (spanint > myspantime):
                    os.remove(f_join)
                    # print(f, mtime, spantime)
                else:
                    print(f, mtime, spanint)


if (__name__ == '__main__'):
    deleteOutOfDateFile('.')
