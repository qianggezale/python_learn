# -*- utf-8 -*-

from datetime import datetime
import os
import sys

kuozhanming = ('.txt')
myspantime = 20  #默认20分钟


def deleteOutOfDateFile(abspath):
    for f in os.listdir(abspath):
        f_join = os.path.join(abspath, f)
        if (os.path.isdir(f_join)):
            if (not os.listdir(f_join)):
                os.rmdir(f_join)
            else:
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
    try:
        if (len(sys.argv) == 2):
            myspantime = int(sys.argv[1])
            deleteOutOfDateFile('.')
        else:
            print('请输入一个时间参数(单位分钟)')
    except Exception as e:
        print('出现错误：' + e)
