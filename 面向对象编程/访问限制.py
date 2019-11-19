class Student(object):
    def __init__(self, name, score):
        self.__name = name
        self.__score = score

    def print_score(self):
        print('%s :%s' % (self.__name, self.__score))

    def get_name(self):
        return self.__name

    def get_score(self):
        return self.__score

    def set_name(self, name):
        self.__name = name

    def set_score(self, score):
        self.__score = score


lily = Student('lily', 98)
lily.print_score()
lily.__name = '123'
lily.print_score()
print(lily.__name)
print(lily.get_name())
print(lily.get_score())
lily.set_name('tom')
lily.print_score()
lily.set_score(69)
lily.print_score()
print(lily._Student__name)
lily._Student__name = 'lily'
lily.print_score()


class Peaple(object):
    def __init__(self, name, gender):
        self.name = name
        self.__gender = gender

    def get_gender(self):
        return self.__gender

    def set_gender(self, str):
        if str == 'male':
            self.__gender = str
        if str == 'female':
            self.__gender = str
        else:
            raise ValueError('bad gender')


bart = Peaple('bart', 'male')
if bart.get_gender() != 'male':
    print('测试失败!')
else:
    bart.set_gender('female')
    if bart.get_gender() != 'female':
        print('测试失败!')
    else:
        print('测试成功!')
