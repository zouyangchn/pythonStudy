class Student(object):

    def get_score(self):
        return self._score

    def set_score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be a integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0~100!')
        self._score = value

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be a integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0~100!')
        self._score = value

    @property
    def birth(self):
        return self._birth

    @birth.setter
    def birth(self, value):
        self._birth = value

    @property
    def age(self):
        return 2017 - self._birth


s = Student()
s.set_score(10)
# s.set_score('23')
print(s.get_score())
print(s.score)
s.score = 12
print(s.score)

s.birth = 1992
print(s.age)


class Screen(object):

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise ValueError('width must be a integer!')
        if value < 0:
            raise ValueError('width must be 大于0!')
        self._width = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise ValueError('height must be a integer!')
        if value < 0:
            raise ValueError('height must be 大于0!')
        self._height = value

    @property
    def resolution(self):
        return self._width * self._height


s = Screen()
s.width = 1024
s.height = 768
print(s.resolution)
