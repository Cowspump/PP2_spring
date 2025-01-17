"""
There are three numeric types in Python:

int
float
complex

"""


x = 1    # int
y = 2.8  # float
z = 1j   # complex

print(type(x), type(y), type(z))

#Float, or "floating point number" is a number,
#positive or negative, containing one or more decimals.

x = 1.10
y = 1.0
z = -35.59

print(type(x))
print(type(y))
print(type(z))

#Float can also be scientific numbers with an "e"
#to indicate the power of 10.

min_number = 35e3
number = 12E4
print(min_number, number)


#Complex numbers are written with a "j" as the imaginary part:

complex_num = 3+5j

print(complex_num)

#You can convert from one type to another with
#the int(), float(), and complex() methods:

c = 3.50
d = int(c)
print(d, type(d)) #output: 3, int

#Python does not have a random() function to
#make a random number, but Python has a built-in module called random that can be used to make random numbers:


import random

print(random.randrange(1, 10))
#random num from 1-9