#Python Dictionaries


my_dict = {0:'a', 1:'b', 2:'c'}

print(my_dict[2])


bad_dict = {
    404:"Error",
    404:"BRUH",
    111:"hello"
}

print(bad_dict[404])


#Length of dict
ex = {1:"a", 2:"b", 3:"c"}

print(len(ex))


#The values in dictionary items can be of any data type:
thisdict = {
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue"]
}


#The dict() Constructor

cool = dict(name = "John", age = 36, country = "Norway")
print(cool)

#Access Dictionary Items
my_dict = {0:'a', 1:'b', 2:'c'}
print(my_dict[0])

for i in my_dict.values():
    print(i)

#You can get a value by a key

print(my_dict.get(0))


K = my_dict.keys()
print(K)


X = my_dict.items()

print(X)

#o determine if a specified key is present in a dictionary use the in keyword:

if 0 in my_dict:
    print('KBTU')



#Change Dictionary Items

A = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
A["year"] = 2018

print(A)

#Add Dictionary Items

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["color"] = "red"
print(thisdict)


#Remove Dictionary Items

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.pop("model")
print(thisdict)

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.popitem()
print(thisdict)

#The clear() method empties the dictionary:



#Loop Dictionaries

B = {1:52, 2:53,3:54, 4:55}


for i in B:
    print(i, end=" ")

print()
for i in B.values():
    print(i,end=" ")
print()

for i in B.keys():
    print(i, end=" ")
print()

for i, j in B.items():
    print(i, j, end=" ")
print()


#Copy a Dictionary

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = thisdict.copy()
print(mydict)


thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = dict(thisdict)
print(mydict)


#Nested Dictionaries


myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}

print(myfamily["child2"]["name"])


for x, obj in myfamily.items():
  print(x)

  for y in obj:
    print(y + ':', obj[y])




'''
clear()	Removes all the elements from the dictionary
copy()	Returns a copy of the dictionary
fromkeys()	Returns a dictionary with the specified keys and value
get()	Returns the value of the specified key
items()	Returns a list containing a tuple for each key value pair
keys()	Returns a list containing the dictionary's keys
pop()	Removes the element with the specified key
popitem()	Removes the last inserted key-value pair
setdefault()	Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
update()	Updates the dictionary with the specified key-value pairs
values()	Returns a list of all the values in the dictionary
'''