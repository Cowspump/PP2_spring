#Python Operators

print(53+2) #52

"""
+	Addition	x + y	
-	Subtraction	x - y	
*	Multiplication	x * y	
/	Division	x / y	
%	Modulus	x % y	
**	Exponentiation	x ** y	
//	Floor division	x // y	
"""

print(5 // 2) # 2

'''
==	Equal	x == y	
!=	Not equal	x != y	
>	Greater than	x > y	
<	Less than	x < y	
>=	Greater than or equal to	x >= y	
<=	Less than or equal to	x <= y
'''

#Python Logical Operators

#and or not

print(True and False) #False
print(True or False) #True
print(not(True)) #False


#Python Identity Operators

x = 52
y = 52

print(x is y)
print(x is not y)

#Python Membership Operators


nums = [1,2,3,4,5,6,7,8,9]


target = 5

print(target in nums) #True
print(2007 not in nums) #True


#Python Bitwise Operators

'''
& 	AND	Sets each bit to 1 if both bits are 1	x & y	
|	OR	Sets each bit to 1 if one of two bits is 1	x | y	
^	XOR	Sets each bit to 1 if only one of two bits is 1	x ^ y	
~	NOT	Inverts all the bits	~x	
<<	Zero fill left shift	Shift left by pushing zeros in from the right and let the leftmost bits fall off	x << 2	
>>	Signed right shift	Shift right by pushing copies of the leftmost bit in from the left, and let the rightmost bits fall off	x >> 2
'''

#Operator Precedence
print((6 + 3) - (6 + 3)) #0
print((6+3) - 6+3) #6

'''
()	Parentheses	
**	Exponentiation	
+x  -x  ~x	Unary plus, unary minus, and bitwise NOT	
*  /  //  %	Multiplication, division, floor division, and modulus	
+  -	Addition and subtraction	
<<  >>	Bitwise left and right shifts	
&	Bitwise AND	
^	Bitwise XOR	
|	Bitwise OR	
==  !=  >  >=  <  <=  is  is not  in  not in 	Comparisons, identity, and membership operators	
not	Logical NOT	
and	AND	
or	OR
'''

'''
If two operators have the same precedence
, the expression is evaluated from left to right.
'''

