class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def print_score(self):
        print('%s: %s' % (self.name, self.score))

    def get_grade(self):
        if self.score >= 90:
            return 'A'
        elif self.score >= 60:
            return 'B'
        else:
            return 'C'


bart = Student('bart same', 59)
print(bart)
print(Student)

bart.name = 'bart same'
print(bart.name)

lili = Student('lili tom', 98)
print(lili)
print(lili.name)
print(lili.score)
lili.print_score()
print(lili.get_grade())
