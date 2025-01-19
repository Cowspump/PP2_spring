mylist = ['Python', 'FastApi', 'C#', 'JS']

print(mylist)

#List items are ordered, changeable, and allow duplicate values.
#index starts with 0

#Length of list: len()


names = ['Alikhan', 'Makpal', 'Burik']

print(len(names)) #3



#List Items - Data Types
list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]


strangeList= ["abc", 34, True, 40, "male"]



#The list() Constructor
#It is also possible to use the list() constructor when creating a new list.

Doner = list(((1,2), (0,5), (1,2)))

print(Doner)

for i in Doner:
    print(type(i))


#Range of Indexes


thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])

# 2 included, 5 not

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[:4])

#from 0 to 3, 4 not included

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:])

#2 included


food= ['ham', 'horse','burger']

if 'horse' in food:
    print("Welcome to KZ")
else:
    print("Bruh")



# Change List Items

a = [1,2,3,4,5]

a[0] = 2077

print(a)

a.insert(0, 5252)
print(a)





b = ['a','b','c','d']

b.append('KBTU')

print(b)




thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)
print(tropical)

#Remove from List


thislist.remove("mango")
thislist.remove("pineapple")
thislist.remove("papaya")

print(thislist)


thislist.pop(0)
print(thislist)

del thislist[0]
print(thislist)


thislist.clear()
print(thislist) #[]



#Loop Through a List

ex = [1,2,3]

for i in ex:
    print(i, end=" ")

print()

top = ['tyler', 'kendrick', 'Kanye', 'Weekend']

for i in range(len(top)):
    print(top[i], end="\t")
print()

#Using a While Loop

i = 0
while i < len(top):
    print(top[i])
    i += 1


ans = [x for x in top]
print(ans)



#List Comprehension
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)


fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits if "a" in x]

print(newlist)


newlist = [x for x in range(10)]
print(newlist)


#Sort Lists
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)


thislist = [100, 50, 65, 82, 23]
thislist.sort()
print(thislist)



#To sort descending, use the keyword argument reverse = True:

thislist = [100, 50, 65, 82, 23]
thislist.sort(reverse = True)
print(thislist)


#Customize Sort Function

def myfunc(n):
  return abs(n - 50)

thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)
print(thislist)


#Copy Lists

thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)


thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
print(mylist)



thislist = ["apple", "banana", "cherry"]
mylist = thislist[:]
print(mylist)

#Join Lists

list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)


list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

list1.extend(list2)
print(list1)


#_______________________________
#List Methods

'''
append()	Adds an element at the end of the list
clear()	Removes all the elements from the list
copy()	Returns a copy of the list
count()	Returns the number of elements with the specified value
extend()	Add the elements of a list (or any iterable), to the end of the current list
index()	Returns the index of the first element with the specified value
insert()	Adds an element at the specified position
pop()	Removes the element at the specified position
remove()	Removes the item with the specified value
reverse()	Reverses the order of the list
sort()	Sorts the list
'''

