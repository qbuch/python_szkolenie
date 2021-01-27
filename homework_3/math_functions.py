# Napisz program obliczający pola powierzchni poszczególnych figur:\
#     a.kwadratb.prostokątc.kołod.trójkąte.trapez

def area_of_square(a):
    return a**2


def area_of_rectangle(a,b):
    return a*b


def area_of_circle(radius, pi=3.1415):
    return pi * (radius**2)


def area_of_triangle(length, height):
    return int((triangle_a * triangle_b)/2)


def area_of_trapezoid(a,b,h):
    return int((a+b)/2 * h)

#Geometric area calculator

print('Available operations:')
print('1. Area of square')
print('2. Area of rectangle')
print('3. Area of circle')
print('4. Area of triangle')
print('5. Area of trapezoid')

while True:
    user_input = input("Enter number of chosen operation: ")

    if int(user_input) < 1 and int(user_input) > 5:
        print('Please, choose correct number.')

    elif user_input == '1':
        side_square = float(input('Enter the length of side of square: '))
        print('Area of square is ',float(area_of_square(side_square)))

    elif user_input == '2':
        side_a = float(input('Enter the length of side a of rectangle: '))
        side_b = float(input('Enter the length of side b of rectangle: '))
        print('Area of rectangle is ', float(area_of_rectangle(side_a,side_b)))

    elif user_input == '3':
        radius = float(input('Enter the radius of circle: '))
        print('Area of circle is ', float(area_of_circle(radius)))

    elif user_input == '4':
        triangle_a = float(input('Enter the length of side a of triangle: '))
        triangle_b = float(input('Enter the length of side b of triangle: '))
        print('Area of triangle is ', float(area_of_triangle(triangle_a, triangle_b)))

    elif user_input == '5':
        side_a = float(input('Enter the length of side a of trapezoid: '))
        side_b = float(input('Enter the length of side b of trapezoid: '))
        height = float(input('Enter the height of trapezoid: '))
        print('Area of trapezoid is ', float(area_of_trapezoid(side_a, side_b, height)))


