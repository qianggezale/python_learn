# utf-8

import json

obj = dict(name='ming', age=20)
print(json.dumps(obj))


class St(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age


st1 = St('qiang', 20)
# print(st1)
stjson = json.dumps(st1, default=lambda obj: obj.__dict__)
print(stjson)
obj_st = json.loads(stjson, object_hook=lambda s: St(s['name'], s['age']))
print(obj_st)
