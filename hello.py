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

# #tuple元组
# # mytuple=(1,2,3)
# mytuple = (1, '1')
# print(mytuple)

# height=float(input('输入身高：'))
# weight=float(input('输入体重：'))
# import math
# bmi=weight/math.sqrt(height)
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

# dic={}
# dic['a']=(1,2,3)
# print(dic['a'][1])
# dic['a']=[1,2,(23,3)]
# print(dic['a'][2])

# help(dict)

# #16进制
# print(hex(255))


#函数
def my_abs(num):
    if (num > 0):
        return num
    else:
        return -num

print(my_abs(-22))


