# coding:utf-8

# # print('请输入第一个数字')
# n1=input('请输入第一个数字')
# # print('请输入第二个数字')
# n2=input('请输入第二个数字')
# print('之和为：',n1+n2)

# a = 100
# if (a > 1):
#     print(1)
# else:
#     print(11)

# print('I\'m \nok.')

# a='ABC'
# b=a
# a='XYZ'
# print(b)

# print(10/3)
# print(9/3)
# print(10//3)
# import math
# print(math.pi)

# n = 123
# f = 456.789
# s1 = 'Hello, world'
# s2 = 'Hello, \'Adam\''
# s3 = r'Hello, "Bart"'
# s4 = r'''Hello,
# Lisa!'''
# s5=r'''ss"ss"dfsafd
# ssssdfsafd
# '''
# print(s3)
# print(s4)
# print(s5)

# # 对于单个字符的编码，Python提供了ord()函数获取字符的整数表示，chr()函数把编码转换为对应的字符
# print(ord('S'))
# print(ord('强'))
# print(chr(66))

# # s
# print('ABC'.encode('ascii'))
# print('强哥'.encode('utf-8'))

# # print(b'\xe5\xbc\xba\xe5\x93\xa5'.decode('utf-8'))
# # len()函数计算的是str的字符数，如果换成bytes，len()函数就计算字节数：
# print(len('qiang'))
# print(len('qiang1'.encode('ascii')))
# print(len('强'.encode('utf-8')))

# # 占位符
# print('%d-%d'%(3,1))
# import math
# print('pi:%f'% math.pi)

# # list

# mylist=['1','B','DDD']
# # print(mylist)
# # print(mylist[-1])
# mylist.reverse()
# print(mylist)

# #脚标
# for i,v in enumerate(mylist):
#     print(i,v)

# #tuple元组
# # mytuple=(1,2,3)
# mytuple = (1, '1')
# print(mytuple)

# height=float(input('输入身高：'))
# weight=float(input('输入体重：'))
# import math
# bmi=weight/math.pow(height,2)
# print(bmi)

# sum = 0
# for x in range(101):
#     sum = sum + x
# print(sum)

# sum = 0
# num = 1
# while num <= 100:
#     sum += num
#     num += 1
# print(sum)

#zidian dic

# dic={'a':1,'b':2}
# for item in dic:
#     print(dic[item])
# print(dic.get('aa',-1))

# for k,v in dic.items():
#     print(k,v)

# dic={}
# dic['a']=(1,2,3)
# print(dic['a'][1])
# dic['a']=[1,2,(23,3)]
# print(dic['a'][2])

# help(dict)

# #16进制
# print(hex(255))

# #函数
# def my_abs(num):
#     if not isinstance(num,(int,float)): #知识点
#         raise TypeError('只能输入整型和浮点型')
#     if (num > 0):
#         return num
#     else:
#         return -num

# print(my_abs('ww'))

# def jisuan(*num):
#     sum = 0
#     for n in num:
#         sum = sum + n
#     return sum

# print(jisuan(1,2,3,4))
# nums=[1,2,3,4,5]
# print(jisuan(*nums))

# def person(name,**other):
#     print('name:%s,other:%s'%(name,other))
# person('qiang',a='1',b='2')

# def person(name,*args,age,fm='f'):
#     print(name,age,fm)

# person('qiang',age=1,fm='m')
# person('qiang',age=1)

# #递归
# #阶乘例子
# def jiecheng(n):
#     if (n < 1):
#         return 0
#     if (n == 1):
#         return 1
#     return n * jiecheng(n - 1)

# print(jiecheng(0))
# print(jiecheng(2))
# print(jiecheng(4))

#切片
# mylist=list(range(100))
# # print(mylist[::2])
# # print(mylist[0:10])
# print(mylist[-1:])

# mystr=' ABCD '
# print(mystr[1:6])
# print(mystr.strip())

# #查找最大最小值
# def findMinAndMax(mylist):
#     minnum=None
#     maxnum=minnum
#     if(len(mylist)>0):
#         minnum=mylist[0]
#         maxnum=minnum
#     for v in mylist:
#         if(v>maxnum):
#             maxnum=v
#         if(v<minnum):
#             minnum=v
#     return (minnum,maxnum)
# mylist=[1]
# print(findMinAndMax(mylist))

# sqlist = [n * n for n in range(1, 10) if n % 2 == 0]
# print(sqlist)

# import os
# print([d for d in os.listdir('.')])

# L = ['Hello', 'World', 18, 'Apple', None]
# print([str(n).lower() for n in L])
# print([n.lower() for n in L if isinstance(n,str)])

# #map
# def cheng(x):
#     return x * x

# print(list(map(cheng, [1, 2, 3])))

# #reduce
# def add(x, y):
#     return x + y
# from functools import reduce
# reducedome=reduce(add,[1,2,3,4])
# print(reducedome)

# #把字符串'123456'转换成浮点数123456
# dic = {
#     '0': 0,
#     '1': 1,
#     '2': 2,
#     '3': 3,
#     '4': 4,
#     '5': 5,
#     '6': 6,
#     '7': 7,
#     '8': 8,
#     '9': 9,
#     '.': -1
# }

# def str2int(str):
#     def fn(x, y):
#         return x * 10 + y

#     def strnum(strnum):
#         return dic[strnum]

#     from functools import reduce
#     return reduce(fn, map(strnum, str))

# print(str2int('123123'))

# #把字符串'123.456'转换成浮点数123.456
# def str2folat(str):
#     nums = map(lambda n: dic[n], str)
#     point = 0

#     def fn(x, y):
#         nonlocal point
#         if (y == -1):
#             point = 1
#             return x
#         if (point == 0):
#             return x * 10 + y
#         else:
#             point = point * 10
#             return x + y / point

#     from functools import reduce
#     return reduce(fn, nums, 0.0)

# print(str2folat('.123123'))

# #sorted
# L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
# def mysort(tuple1,tuple2):
#     return tuple1[1]>tuple2[2]
# from operator import itemgetter
# print(sorted(L,key=itemgetter(1)))
# print(sorted(L,key=lambda n:n[1]))

#lambda
# print(list(filter(lambda x: x % 2 == 1, range(1, 21))))

# #装饰模式

# import functools


# def log(fun):
#     @functools.wraps(fun)
#     def wrapper(*arg, **kw):
#         print(fun.__name__)
#         return fun(*arg, **kw)
#     return wrapper


# def logtext(text):
#     def zhuangshi(fun):
#         @functools.wraps(fun)
#         def wrapper(*arg, **kw):
#             print(text, fun.__name__)
#             return fun(*arg, **kw)
#         return wrapper
#     return zhuangshi


# @logtext('hhhh')
# def nowadd():
#     print(2)


# nowadd()

# #访问机制
# import fangwen
# print(fangwen.add(1,2,3))
# print(fangwen._add(1,2))

import sys 
print(sys.path)

