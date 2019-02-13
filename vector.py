import math

class Vector(object):
    _x = 0
    _y = 0

    def __init__(self, x, y):
        self._x = x
        self._y = y

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, x):
        self._x = x

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, y):
        self._y = y

    def __str__(self):
        return '({}, {})'.format(self._x, self._y)

    def __sub__(self, other):
        return Vector(self._x - other.x, self._y - other.y)

    def __add__(self, other):
        return Vector(self._x + other.x, self._y + other.y)

    def __iadd__(self, other):
        self._x += other.x
        self._y += other.y
        return self

    def get_normalized(self):
        length = self.get_length()
        if length > 0:
            x = self._x / length
            y = self._y / length
            return Vector(x, y)
        else:
            return Vector(0, 0)

    def get_length(self):
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def get_reversed(self):
        return Vector(-self._x, -self._y)

    @staticmethod
    def distance(start, end):
        vector = end - start
        return vector.get_length()