#'hello' is the same as "hello".

print("Hello")
print('Hello')


#You can use quotes inside a string, as
#long as they don't match the quotes surrounding the string:

print("It's alright")
print("He is called 'Johnny'")
print('He is called "Johnny"')


#str to a var

var = "KBTU"
print(var)


a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)


#Strings are Arrays

some_str = "Hello, World!"
print(some_str[0]) #H


for x in "KBTU":
  print(x)

print(len(some_str))

#To check if a certain phrase
#or character is present in a string, we can use the keyword in.


check = "I'm really in Love with Makpal"

if 'really' in check:
    print("Its there !")
else:
    print("bruh")

print('Ali' not in check) #True


#slicing

sum = 'abcd'

print(sum[1:3])

#Modify Strings

a = "abc"
print(a.upper())

b = "ABC"
print(b.lower())

c = "    ali, alikhan"
print(c.strip())
c = c.strip()

print(c.replace("ali,", "makpal"))


print(c.split(','))


#concatenate

a = "hello"
b = "world"
c = a +b

print(a +" " +  b, c)

#f str

age = 2077

print(f"my age is {age}")

price = 50.2

print(f"the toys price is {price:.3f}")


#Escape Characters

print("check"+ '\n'+ "hello")

print("a" + '\t' + 'c')


#String Methods

#Note: All string methods return new values.
#They do not change the original string.

#find() count() endswith() isdigit() isupper() replace()....

a = "abcd"

print(a.find("a")) #0