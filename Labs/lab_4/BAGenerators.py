#first

def up_to_n(n):
    for num in range(1,n+1):
        yield num ** 2

if __name__ == "__main__":

    N = int(input("Enter your N: "))

    print("squares of nums 1 - N: ")
    print(list(up_to_n(N)), '\n')

#second

def only_evens(n):

    for num in range(1,n+1):
        if num % 2 == 0:
            yield  num

if __name__ == "__main__":

    N = int(input("Enter last N: "))
    evens = [i for i in only_evens(N)]

    print(f"only even nums between 1 and N: {evens}",'\n')


#third

def div_by_tf(n):

    for num in range(0, n+1):
        if num % 4 == 0 and num % 3 == 0:
            yield num


if __name__ == "__main__":

    N = int(input("Enter your N: "))

    divisbles = [i for i in div_by_tf(N)]

    print(f"nums such that divides by three and four: {divisbles}", '\n')



#four

def squares(a,b):

    for num in range(a,b+1):
        yield num ** 2

if __name__ == "__main__":

    print("squares using square generator such that apply a and b arguments")
    for i in squares(1,10):
        print(i, end=" ")
    print('\n')

#five

def from_n_to_0(n):

    for num in range(n,-1,-1):
        yield num

if __name__ == "__main__":

    print("Nums from N to 0 using 'from_n_to_0(n)' generator")
    for i in from_n_to_0(10):
        print(i, end=" ")
    print("Thats all.")






