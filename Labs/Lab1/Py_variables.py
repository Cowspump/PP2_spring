# Python has no command for declaring a variable.
# A variable is created the moment you
# first assign a value to it.


x = 52
y = "I LOVE KBTU!!!"
print(x)
print(y)


#Variables do not need to be declared with any particular type,
# and can even change type after they have been set.

x = 4       # x is of type int
x = "ICPC" # x is now of type str
print(x) #output: "ICPC"


#Casting

x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0

#GET THE TYPE

#You can get the data type of a variable with the type() function.

a = 52
b = "Tyler the creator"
c = 3.1415

print(type(a), type(b), type(c))

#output: <class 'int'> <class 'str'> <class 'float'>


#Single or Double Quotes?

x = "Ali"
# is the same as
x = 'Ali'

print(x)


# Case-Sensitive
# Variable names are case-sensitive.

a = 52
A = 'fifty two'

#A will not overwrite a


#Python - Variable Names
myvar = "KBTU"
my_var = "KBTU"
_my_var = "KBTU"
myVar = "KBTU"
MYVAR = "KBTU"
myvar2 = "KBTU"


#Illegal variable names:

# 2myvar = "John"
# my-var = "John"
# my var = "John"


#Camel Case
myVarExample = 5
#Pascal Case
MyVarExample = 4
#Snake Case
my_var_example = 3


#Many Values to Multiple Variables
"""
Python allows you to assign values to multiple variables in one line:
ExampleGet your own Python Server
"""
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

#And you can assign the same value to multiple variables in one line:
x = y = z = "KBTU"
print(x)
print(y)
print(z)


#Unpack a list:

fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)



# Output Variables

x = "Python is NOT MID"
print(x)

#In the print() function, you output multiple
#variables, separated by a comma:

x = "Python"
y = "is"
z = "NOT MID"
print(x, y, z)


#also you can use +

x = "Python"
y = "is"
z = "PEAK"
print(x + y + z) #output: PythonisPEAK



#In the print() function, when you try to combine a string and
#a number with the + operator, Python will give you an error:

x = 52
y = "bruh"
#print(x + y) #mistake

x = 1
y = 2
print(x+y) # output : 3

z = "hello"
print(x,y, z) #output: 1 2 hello



# Global Variables

x = "IM THE GLOBAL VARIABLE" #gloval var

def myfunc():
  print("x equals " + x)

myfunc()


x = "awesome" #gloval

def myfunc():
  x = "fantastic" #local
  print("Python is " + x)

myfunc()

print("Python is " + x)


#To change the value of a global variable inside a function,
# refer to the variable by using the global keyword:

x = "awesome"

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)


