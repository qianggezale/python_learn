# utf-8

# class Student(object):
#     def __init__(self, name):
#         self.__name = name

#     def get_name(self):
#         return self.__name

#     def set_name(self, name):
#         self.__name = name

#     def call(self):
#         print(self.__name)

# if (__name__ == '__main__'):
#     qiang = Student('qiang')
#     # print(qiang._Student__name) #不同版本显示不同
#     print(qiang.get_name())
#     # print(qiang.age)
#     chuang = Student('chuang')
#     # print(chuang.age)
#     qiang.call()
#     chuang.call()


#对property的理解
class Student(object):
    @property
    def birth(self):
        return self._birth

    @birth.setter
    def birth(self, value):
        self._birth = value

    @property
    def age(self):
        return 2018 - self._birth


if (__name__ == '__main__'):
    s1 = Student()
    s1.birth = 1990
    # s1.age = 11
    print(s1.age)
