class Animal(object):
    pass


class Manmal(Animal):
    pass


class Bird(Animal):
    pass


class RunnableMixIn(object):
    pass


class FlyableMixIn(object):
    pass


class CarnivorousMixIn(object):
    pass


class HerbiivoresMixIn(object):
    pass


class Dog(Manmal, RunnableMixIn, CarnivorousMixIn):
    pass


class Bat(Manmal, FlyableMixIn, CarnivorousMixIn):
    pass


class Parrot(Bird, FlyableMixIn, CarnivorousMixIn):
    pass


class Ostrich(Bird, RunnableMixIn, HerbiivoresMixIn):
    pass
