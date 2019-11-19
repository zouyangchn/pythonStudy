from types import MethodType


class Student(object):
    pass


def set_score(self, score):
    self.score = score


Student.set_score = set_score

s = Student()
s.name = 'bob'
print(s.name)


def set_age(self, age):
    self.age = age


s.set_age = MethodType(set_age, s)
s.set_age(25)
print(s.age)

s2 = Student()
# s2.set_age(23)

s.set_score(100)
print(s.score)


class Students(object):
    __slots__ = ('name', 'age')


ss = Students()
ss.name = 'lily'
ss.age = 12


# ss.score=87

class GraduateStudent(Students):
    pass


gs = GraduateStudent()

gs.score = 34
