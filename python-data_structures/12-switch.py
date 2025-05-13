#!/usr/bin/python3
a = 89
b = 10
# using a temporary variable
temp = a
a = b
b = temp
print("a={:d} - b={:d}".format(a, b))
