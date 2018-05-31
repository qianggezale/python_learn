# utf-8


class Student(object):
    def __init__(self, name):
        self.name = name

    def call(self):
        print(self.name)




if(__name__=='__main__'):
    qiang=Student('qiang')
    qiang.age=29
    print(qiang.age)
    chuang=Student('chuang')
    # print(chuang.age)
    qiang.call()
    chuang.call()