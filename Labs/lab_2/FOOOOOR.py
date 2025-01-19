#Python For Loops

#A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).

#With the for loop we can execute a set of statements, once for each item in a list, tuple, set etc.


uni = ['KBTU', 'SDU', 'AITU']

for i in uni:
    if i == 'KBTU':
        print('GOAT universirty: ', i)
    else:
        print(i)


#Looping Through a String

stroka = 'it was such a BORING lab...'

for i in stroka:
    print(i, end=" ")
print()


'''
The range() Function
To loop through a set of code a specified number of times, we can use the range() function,
The range() function returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and ends at a specified number.
'''


for i in range(10):
    print(i, end=" ")

print()


cur = [i for i in range(1,52+1)]

print(len(cur))

'''
Else in For Loop
The else keyword in a for loop specifies a block of code to be executed when the loop is finished:

'''

for x in range(6):
  print(x)
else:
  print("i'm so pointless..")


#he else block will NOT be executed if the loop is stopped by a break statement.




#Nested Loops aka MATRIX

for i in range(1,10):
    for j in range(1,10):
        print(i * j, end="\t")
    print()

#output will be:

'''
1	2	3	4	5	6	7	8	9	
2	4	6	8	10	12	14	16	18	
3	6	9	12	15	18	21	24	27	
4	8	12	16	20	24	28	32	36	
5	10	15	20	25	30	35	40	45	
6	12	18	24	30	36	42	48	54	
7	14	21	28	35	42	49	56	63	
8	16	24	32	40	48	56	64	72	
9	18	27	36	45	54	63	72	81
'''


