
"""
Text Type:	str
Numeric Types:	int, float, complex
Sequence Types:	list, tuple, range
Mapping Type:	dict
Set Types:	set, frozenset
Boolean Type:	bool
Binary Types:	bytes, bytearray, memoryview
None Type:	NoneType
"""


x = 2077
print(type(x)) #Print the data type of the variable x:

stroka = "KBTU"

y = 52 #int

z = 1j #complex
print(type(z))

pi = 3.1415 #float

print(type(pi))

my_dict = {1:"Mac", 2:"Windows", 3:"LINUX"}



#If you want to specify the data type,
#you can use the following constructor functions:

#str(), int(), float(), .... tuple(), range(), bool()...

R = range(5)
print(R) #output : (0,5)


bruh = list(("red", "group", "blue"))
print(bruh, type(bruh))