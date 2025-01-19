#Booleans represent one of two values: True or False.


print(52 == 25) #False
print("Ali" != 'makpal') #True
print(2077 > 5) #True


#Print a message based on whether the condition is True or False:

a = 200
b = 33

if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")


#Evaluate a string and a number:

print(bool(""), bool("Hello")) #False, True
print(bool(0), bool(2077)) #False, True

#Any list, tuple, set, and dictionary are True, except empty ones.
print(bool(['a', 'b','c']))

class myclass():
  def __len__(self):
    return 0

myobj = myclass()
print(bool(myobj))



def myFunction() :
  return True

if myFunction():
  print("YES!")
else:
  print("NO!")


#Python also has many built-in functions that return a boolean value,
#like the isinstance() function, which
#can be used to determine if an object is of a certain data type:

x = 200
print(isinstance(x, int))

