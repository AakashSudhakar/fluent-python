#!python3

import numpy

# Basic NumPy playground
a = numpy.arange(12)
print(a)
print(type(a))

print(a.shape)
a.shape = 3, 4
print(a)

print(a[2])
print(a[2, 1])
print(a[:, 1])
print(a.transpose())
