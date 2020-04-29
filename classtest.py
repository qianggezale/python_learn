class AAA:
    _name = "主宰一切"

    def say(self):
        print("我叫：{0}".format(self._name))


class person(AAA):
    _name = ""
    _age = 0

    def __init__(self, name, age):
        self._name = name
        self._age = age
        AAA.__init__(self)

    def say(self):
        print("我叫：{0}，年龄：{1}".format(self._name, self._age))


class worker(person):
    _gongzuo = ""

    def __init__(self, name, age, gz):
        person.__init__(self, name, age)
        self._gongzuo = gz

    def say(self):
        print("我叫：{0}，年龄：{1}，工作是：{2}".format(
            self._name, self._age, self._gongzuo))


# wr = worker("老大哥", "40", "码农")
# wr.say()
# super(worker, wr).say()

class NumVar:
    __a = 0
    __b = 0

    def __init__(self, a, b):
        self.__a = a
        self.__b = b

    def __str__(self):
        return "ToString:{0}+{1}".format(self.__a, self.__b)

    def __add__(self, other):
        return NumVar(self.__a+other.__a, self.__b+other.__b)


nv = NumVar(1, 2)
print(nv)
nv1 = NumVar(1, 2)
print(nv+nv1)
