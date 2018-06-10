#!python3

from math import hypot

class Vector:
    """ General class structure for 2D vector representation. """

    def __init__(self, x=0, y=0):
        """ Special method for class initialization. """
        self.x = x
        self.y = y

    def __repr__(self):
        """ Special method to return customized string representation of object. """
        return "Vector({}, {})".format(self.x, self.y)

    def __abs__(self):
        """ Special method to return Euclidian distance between points. """
        return hypot(self.x, self.y)

    def __bool__(self):
        """ Special method to return magnitude of Euclidean distance between points. """
        return bool(abs(self))

    def __add__(self, other):
        """ Special method to allow for vector addition. """
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)

    def __mul__(self, scalar):
        """ Special method to allow for vector multiplication. """
        return Vector(self.x * scalar, self.y * scalar)