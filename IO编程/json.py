import json

d=dict(name='bob',age=20,score=88)
j=json.dumps(d)
print(j)

j_str='{"name": "bob", "age": 20, "score": 88}'
di=json.loads(j_str)
print(di)


class Student(object):
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score

def student2dict(std):
    return {
        'name': std.name,
        'age': std.age,
        'score': std.score
    }

def dict2student(d):
    return Student(d['name'], d['age'], d['score'])

s=Student('bob',20,88)
print(s)
print(json.dumps(s,default=student2dict))
print(json.dumps(s,default=lambda obj:obj.__dict__))

print(json.loads(j_str, object_hook=dict2student))