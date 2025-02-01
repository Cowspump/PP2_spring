#Python Classes 1-5

#1:
class OutLine:

    def __init__(self):

        self.line = ""

    def get_str(self):
        self.line = input("Enter a string: ")

    def prin_tstr(self):

        return self.line.upper()

jol = OutLine()

jol.get_str()

print("Upper str:", jol.prin_tstr())

#2:
class Shape:
    def __init__(self, shapet):
        self.shapet = shapet
        self.area = 0

    def cur_area(self):

        if self.shapet == "square":
            return f"Area of Square = {self.area}"
        elif self.shapet == "rectangle":
            return f"Area of Rectangle = {self.area}"


class Square(Shape):

    def __init__(self,length):
        super().__init__("square")
        self.length = length
        self.area += self.length ** 2


print()
print("Square Area length = 5")
sharshy = Square(5)
print(sharshy.cur_area())
print()


#3

class Rectangle(Shape):

    def __init__(self,length, width):
        super().__init__("rectangle")
        self.length = length
        self.width = width
        self.area += self.length * self.width


tiktt = Rectangle(6,10)

print("Area of Rectangle l = 6, w = 10")
print(tiktt.cur_area())
print()


#4

print("Another Two points problem...")
print()

class Point:


    def __init__(self, x,y):
        self.x = x
        self.y = y

    def show(self):
        return f"coordinates: x = {self.x}, y = {self.y}"

    def move(self):
        print("Choose how to change the coords:")
        print("x,y ->", end=": ")

        self.x, self.y = [int(i) for i in input().split(',')]

        print()
        print(f"Coords was successfully changed to {self.x}, {self.y}")
        print()

    def dist(self, point):

        q = (point.x - self.x) ** 2
        w = (point.y - self.y) ** 2

        e = (q + w) ** 0.5
        return f"Dist between two points equals to: {e}"


a = Point(0,0)
b = Point(1,1)

print()
print(a.show())
print(b.show())
print()

a.move()

print()
print(a.show())
print(b.show())
print()

print(a.dist(b))
print()

#5
print("KBTU BANK ?")
print()

class Account:

    owner = input("Your name: ")
    balance = 0

    def deposit(self,amount_of_money):
        Account.balance += amount_of_money
        print()
        print(f"{amount_of_money} was added to your balance.")
        print(f"Your current balance: {Account.balance}")

        print()

    def withdraw(self,amount_to_take):

        if amount_to_take <= Account.balance:
            print("Successfully !, good luck :D", f"{amount_to_take} was taken from your balance.")
            Account.balance -= amount_to_take
            print()
            print(f"Your current balance: {Account.balance}")
            print()
        else:
            print()
            print("Oops!, your current balance is less than you want to take !")
            print()
            print(f"Your current balance: {Account.balance}, but you want to take {amount_to_take}.")


kbtu = Account()

kbtu.deposit(5000)
kbtu.withdraw(2500)
kbtu.withdraw(5000)
print()


#6

print("i love prime numbers")

def is_prime(n):

    if n == 1 or n < 2: return False

    for i in range(2, (n//2)+1):
        if n % i == 0:
            return False
    return True

nums = [int(i) for i in range(50)]


ans = list(filter(lambda x: is_prime(x), nums))

print(ans)


