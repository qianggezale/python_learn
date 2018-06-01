# -*- utf-8 -*-

# with open('README.md', 'r',encoding='utf-8') as f:
#     print(f.read())

# with open('README.md','w',encoding='utf-8') as f:
#     f.write('# python_learn\nLearn Python !')

# with open('README.md', 'r',encoding='utf-8') as f:
#     print(f.read())

#StringIO BytesIO
from io import StringIO
f = StringIO()
f.write('你好，强哥。\n谢谢！')
print(f.getvalue())

ff = StringIO('你好，强哥1\n谢谢1！')
while True:
    s = ff.readline()
    if (s == ''):
        break
    print(s, end='')

from io import BytesIO
b = BytesIO('强哥'.encode('utf-8'))
print(b.read())
