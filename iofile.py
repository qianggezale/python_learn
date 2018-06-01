# -*- utf-8 -*-

# with open('README.md', 'r',encoding='utf-8') as f:
#     print(f.read())

# with open('README.md','w',encoding='utf-8') as f:
#     f.write('# python_learn\nLearn Python !')

# with open('README.md', 'r',encoding='utf-8') as f:
#     print(f.read())

# #StringIO BytesIO
# from io import StringIO
# f = StringIO()
# f.write('你好，强哥。\n谢谢！')
# print(f.getvalue())

# ff = StringIO('你好，强哥1\n谢谢1！')
# while True:
#     s = ff.readline()
#     if (s == ''):
#         break
#     print(s, end='')

# from io import BytesIO
# b = BytesIO('强哥'.encode('utf-8'))
# print(b.read())
# bb = BytesIO()
# bb.write(b'Hello World!')
# print(bb.getvalue())

from datetime import datetime

import os

pwd = os.path.abspath('.')

print('      Size     Last Modified  Name')
print('------------------------------------------------------------')

for f in os.listdir(pwd):
    fsize = os.path.getsize(f)
    mtime = datetime.fromtimestamp(
        os.path.getmtime(f)).strftime('%Y-%m-%d %H:%M:%S')
    flag = '/' if os.path.isdir(f) else ''
    print('%10d  %s  %s%s' % (fsize, mtime, f, flag))
