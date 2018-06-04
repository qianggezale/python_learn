# -*- utf-8 -*-

import datetime
import os
import sys

kuozhanming = ('.txt')
myspantime = 60  #默认60秒


def deleteOutOfDateFile(abspath):
    for f in os.listdir(abspath):
        f_join = os.path.join(abspath, f)
        if (os.path.isfile(f_join)):
            koutext = os.path.splitext(f)[1]
            if (koutext and (koutext in kuozhanming)):
                '''判断时间'''
                mtime = datetime.datetime.fromtimestamp(
                    os.path.getmtime(f_join)).strftime('%Y-%m-%d %H:%M:%S')
                # spantime = datetime.now() - datetime.strptime(mtime, '%Y-%m-%d %H:%M:%S')
                filetme = datetime.datetime.strptime(mtime, '%Y-%m-%d %H:%M:%S')
                settime = datetime.datetime.now() - datetime.timedelta(
                    seconds=myspantime)
                if (filetme < settime):
                    removeFile(f_join)
                else:
                    print(f, filetme, settime)
            else:
                removeFile(f_join)
        if (os.path.isdir(f_join)):
            if (not os.listdir(f_join)):
                os.rmdir(f_join)
            else:
                deleteOutOfDateFile(f_join)


def removeFile(path):
    if (os.path.splitext(path)[1] != '.py'):
        # os.remove(path)
        print(1)


def emptyDir(abspath):
    if (os.path.isdir(abspath)):
        for d in os.listdir(abspath):
            temppath = os.path.join(abspath, d)
            emptyDir(temppath)
        if (not os.listdir(abspath)):
            os.rmdir(abspath)


if (__name__ == '__main__'):
    try:
        if (len(sys.argv) == 2):
            myspantime = int(sys.argv[1])
            deleteOutOfDateFile('.')
            emptyDir('.')
        else:
            print('请输入一个时间参数(单位秒)')
    except Exception as e:
        print('出现错误：' + e)
