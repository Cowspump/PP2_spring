#Python Tuples


pos_tuple = ((1,0), (2,0), (3,0))

#A tuple is a collection which is ordered and unchangeable.


#Tuple items are indexed, the first item has index [0], the second item has index [1] etc.


some_tuple = ('a','b','c')

print(some_tuple[0], some_tuple[1], some_tuple[2])

print(len(some_tuple))

thistuple = ("apple",)
print(type(thistuple))

#NOT a tuple
thistuple = ("apple")
print(type(thistuple))


#Tuple Items - Data Types
#Tuple items can be of any data type:

tuple1 = ("apple", "banana", "cherry")
tuple2 = (1, 5, 7, 9, 3)
tuple3 = (True, False, False)

#Access Tuple Items

coolTuple = (1,2,3,4,5)

for i in coolTuple:
    print(i)

print(coolTuple[0], coolTuple[-1])


print(coolTuple[2:-1])


#Tuples are unchangeable, or immutable as it also is called.

x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

print(x)

# Add tuple to a tuple

thistuple = ("apple", "banana", "cherry")
y = ("orange",)
thistuple += y

print(thistuple)

#Note: You cannot remove items in a tuple.

thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.remove("apple")
thistuple = tuple(y)


#Unpacking a tuple:

fruits = ("apple", "banana", "cherry")

(green, yellow, red) = fruits

print(green)
print(yellow)
print(red)


fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

(green, yellow, *red) = fruits

print(green, yellow, red)


fruits = ("apple", "mango", "papaya", "pineapple", "cherry")

(green, *tropic, red) = fruits

print(green)
print(tropic)
print(red)



#Loop Tuples


thistuple = ("apple", "banana", "cherry")
for x in thistuple:
  print(x, end=" ")
print()

for i in range(len(thistuple)):
    print(thistuple[i])


#Join Two Tuples


tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2
print(tuple3)


fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2

print(mytuple)


'''
count()	Returns the number of times a specified value occurs in a tuple
index()	Searches the tuple for a specified value and returns the position of where it was found
'''