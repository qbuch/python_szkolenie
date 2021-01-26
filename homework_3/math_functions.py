# Napisz program obliczający pola powierzchni poszczególnych figur:\
#     a.kwadratb.prostokątc.kołod.trójkąte.trapez

def area_of_square(a):
    print(a**2)


def area_of_rectangle(a,b):
    print(a*b)


def area_of_circle(radius, pi=3.1415):
    print(pi * (radius**2))


def area_of_triangle(length, height):
    print(int((length * height)/2))


def area_of_trapezoid(a,b,h):
    print(int((a+b)/2 * h))

