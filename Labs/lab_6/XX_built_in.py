#Python builtin functions exercises
import  time

#task1


nums1 = [1, 2, 3, 4, 5]



def mult_list(l):

    return eval('*'.join(map(str, l)))

if __name__ == "__main__":
    print(mult_list(nums1))


somestr = "ABCabc"

def count_letters(s):

    capital = len([i for i in s if i.isupper()])
    small = len([i for i in s if i.islower()])

    return f"Capital letters: {capital}, Small letters: {small}"

if __name__ == "__main__":
    print(count_letters(somestr))


somestr2 = "aaabbaaa"

def palindrome(s):

    a = list(s)
    b = list(s)
    b.reverse()
    return a == b

if __name__ == "__main__":
    print(palindrome(somestr2))


def root_delay():

    from time import sleep

    num = int(input())
    sleeptime = int(input())

    sleep(sleeptime / 1000)


    print(f'Square root of {num} after {sleeptime} miliseconds is {num ** 0.5}')

if __name__ == "__main__":
    root_delay()


mytuple = (1, 2, 3, 4, 5)

def all_true(tp):

    return all(tp)

if __name__ == "__main__":
    print(all_true(mytuple))

