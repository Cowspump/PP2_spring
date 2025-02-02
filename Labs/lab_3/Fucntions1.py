#Python Function

#1
def convert(cur):

    grams = cur * 28.3495231

    return f"{cur} ounces equals to {grams} grams ~= {int(grams)}"


ounces = int(input("Enter a ounces: "))

print(convert(ounces), '\n')


#2

def convet_f_to_c(far):

    c =  (5 / 9) * (far - 32)

    return f"{far} Fahrenheit = {c} celsius."

F = int(input("Input a Fahrenheit degree to convert: "))
print(convet_f_to_c(F), '\n')
import random


#3

def solve(numheads, numlegs):

    x = abs(numlegs - (numheads * 4 )) //2
    y = numheads - x

    return f"{x} kfc and {y} bad bunny"

print(solve(35,94), '\n')

#4

def is_prime(num):

    if num <= 0 or num == 1: return False

    for i in range(2,int(num ** 0.5) +1):
        if num % i == 0:
            return False

    return True


def filter_prime(yournums):

    ans = []

    for i in yournums:
        if is_prime(i): ans.append(i)

    return ans

nums = [int(i) for i in range(20)]

print(filter_prime(nums), '\n')


#5 Permutations of string

def all_views(stroka, i = 0):

    if i == len(stroka):
        print("".join(stroka))

    for j in range(i, len(stroka)):

        perm = [char for char in stroka]
        perm[i],perm[j] = perm[j],perm[i]

        all_views(perm, i+1)


all_views("KBTU")
print()

#6

def rev(s):
    words = [word for word in s.split()]

    words.reverse()

    return words

print(rev("I'm in love with Makpal"), '\n')


#7

def has_33(nums):

    check = ""
    for i in nums:
        check += str(i)


    if '33' in check:
        return True
    else:
        return False

print(has_33([1, 3, 3]))
print(has_33([1, 3, 1, 3]))
print(has_33([3, 1, 3]), '\n')


#8


def spy_game(nums):
    check = []

    for i in nums:
        if i in [0,7]:
            check.append(i)

    if check == [0,0,7]:
        return True
    else:
        return False

print(spy_game([1,2,4,0,0,7,5]))
print(spy_game([1,0,2,4,0,5,7]))
print(spy_game([1,7,2,0,4,5,0]))


#9

def volume_of_sphere(r):

    cur = (4/3) * 3.1415 * r ** 3

    return f"Volume of Sphere with a {r} radius = {cur}\n"

print(volume_of_sphere(5))


#10

def uniq(nums):
    new = []

    for i in nums:
        if i not in new:
            new.append(i)


    return f"New version of list with only unique members: {new}"


print(uniq([1,1,1,1,1,1,2,2,2,2,2077,3,2077]), '\n')


#11


print("I solved 40 leetcode problems.... ", '\n')


def is_palindrome(stroka):

    check = [i for i in stroka if i not in [',', ' ','.']]

    if check == check[::-1]:
        return "Yes its a palindrome"
    else:
        return "No, its not a palindrome"

print(is_palindrome(input("Введите , какую строку вы хотите проверить: ")), '\n')


#12

def histogram(heigths):

    print(f"histogram for {heigths}:", '\n')

    for i in heigths:
        print('*' * i)
    print()


histogram([1,5,10])


#13

print("SQUID GAME: GUESS A NUMBER OR DIE !", '\n')


def game_for_life():
    tar = random.randint(1,21)

    print("Hello , Dear friend !")


    att = 0

    while True:
        print("Guess a number between 1-20: ")

        cur = input()

        if not cur.isdigit():
            print("ITS NOT EVEN A NUMBER!", '\n')
        elif int(cur) < tar:
            print("Too low", '\n')
            att +=1
        elif int(cur) > tar:
            att += 1
            print("Too high", '\n')
        elif int(cur) == tar:
            print("BANG, thank you for a game :D",'\n')

            print(f"total attempts: {att}")
            break


game_for_life()

