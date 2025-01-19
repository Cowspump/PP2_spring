#Set


myset = {"apple", "banana", "cherry"}


#Note: Set items are unchangeable, but you can remove items and add new items.

'''
Unordered means that the items in a set do not have a defined order.

Set items can appear in a different order every time you use them, and cannot be referred to by index or key.
'''


thisset = {"apple", "banana", "cherry", "apple"}

print(thisset) #"apple", "banana", "cherry"


thisset = {"apple", "banana", "cherry", True, 1, 2}

print(thisset)


#et Items - Data Types

set1 = {"apple", "banana", "cherry"}
set2 = {1, 5, 7, 9, 3}
set3 = {True, False, False}


set1 = {"abc", 34, True, 40, "male"}
print(set1)

#The set() Constructor

nums = [1,1,1,1,1,5,1,2]
x = set(nums)

print(set(nums))
print(x)

#Access Items

thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x)


thisset = {"apple", "banana", "cherry"}

print("banana" in thisset)
print("banana" not in thisset)


# Add Set Items


cur = set()
print(cur)

cur.add(5)
cur.add(5)
cur.add(2)
print(cur)

#Add Sets

thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}

thisset.update(tropical)

print(tropical)
print(thisset)


#Remove Set Items

setik = {1,2,3,4,5}

setik.remove(5)
print(setik)
#If the item to remove does not exist, remove() will raise an error.


setik.discard(2077)
#If the item to remove does not exist, discard() will NOT raise an error.

setik.pop()

print(setik)


setik.clear()
print(setik)


#Join Sets

set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)
print(set3)


set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}

myset = set1 | set2 | set3 |set4
print(myset)

#union can join a dif types



x = {"a", "b", "c"}
y = (1, 2, 3)

z = x.union(y)
print(z)




'''
add()	 	Adds an element to the set
clear()	 	Removes all the elements from the set
copy()	 	Returns a copy of the set
difference()	-	Returns a set containing the difference between two or more sets
difference_update()	-=	Removes the items in this set that are also included in another, specified set
discard()	 	Remove the specified item
intersection()	&	Returns a set, that is the intersection of two other sets
intersection_update()	&=	Removes the items in this set that are not present in other, specified set(s)
isdisjoint()	 	Returns whether two sets have a intersection or not
issubset()	<=	Returns whether another set contains this set or not
 	        <	Returns whether all items in this set is present in other, specified set(s)
issuperset()	>=	Returns whether this set contains another set or not
 	            >	Returns whether all items in other, specified set(s) is present in this set
pop()	 	Removes an element from the set
remove()	 	Removes the specified element
symmetric_difference()	^	Returns a set with the symmetric differences of two sets
symmetric_difference_update()	^=	Inserts the symmetric differences from this set and another
union()	|	Return a set containing the union of sets
update()	|=	Update the set with the union of this set and others
'''