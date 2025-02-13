from math import *

def deg_to_rad():
    deg = float(input("Input degree: "))
    print(f'Output radians {radians(deg):.6f}')


def trapezoid_area():
    h = float(input("Height: "))
    a = float(input("Base, first value: "))
    b = float(input("Base, second value: "))

    res = (1/2) * (a + b) * h
    print(f'Area = {res:.2f}')

def polyg_area():
    n = int(input('Input number of sides: '))
    length = float(input('Input the length of a side: '))

    apothem = length / (2 * tan(pi/n))

    result = (n * length * apothem) / 2

    print(f'The area of the polygon is {result:.2f}')

def parallelogram_area():
    length = float(input("Length of base: "))
    height = float(input("Height of parallelogram: "))
    result = length * height
    print(f"Area = {result:.2f}")


if __name__ == "__main__":

    deg_to_rad()
    trapezoid_area()
    polyg_area()
    parallelogram_area()

