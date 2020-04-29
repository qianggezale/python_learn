import sys
import math
import keyword

# print(keyword.kwlist)

# str="wodege"

# print(str*2)
# print(str[1:-1])

# input("出入参数")

# print({hex(x * 2) for x in (1, 2, 7)})


def def_doc():
    '''函数文档'''
    print("ok")


def fnc_in(num, ins):
    if (num in ins):
        return True
    else:
        return False


def fnc_notin(num, ins):
    if (num not in ins):
        return True
    else:
        return False


def func_feibo():
    a, b = 0, 1
    for item in range(1, 10):
        print(b, end=",")
        a, b = b, a + b


def func_iter(varlist):
    it = iter(varlist)
    i = len(varlist)
    while (i > 0):
        print(next(it), end=",")
        i -= 1


# lambda
def sum(v1, v2, v3): return v1+v2+v3
# 1,2...9
# 1,2...9


def func_9x9():
    var1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    t_list = [str(x)+"*"+str(y)+"="+str(x*y) for x in var1 for y in var1]
    print(t_list)


if __name__ == "__main__":
    # def_doc()
    # print(def_doc.__doc__)
    # print(fnc_in(1,[1,2,3]))
    # print(fnc_in(5,[1,2,3]))
    # print(fnc_notin(1,[1,2,3]))
    # print(fnc_notin(5,[1,2,3]))
    # func_while()
    # func_iter([2, 1, 2, 64, 45, 53, 34, 546, 34, 5634, 6545])
    # print(sum(1, 2, 1))
    # func_9x9()
    # print(str(math.pi).zfill(30))
    # instr = input("输入：")
    # print("输入了："+instr)
    for i in sys.argv[1:]:
        print(i, end=",")
