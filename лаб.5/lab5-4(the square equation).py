from math import sqrt
"""The square equation of common type is given: ax^2+bx+c, where a isn't 0."""


def factor(a, b, c):
    d = (b**2) - (4 * a * c)  # Calculate the discriminant
    if d < 0:
        print("Количество корней: 0")  # If d < 0, then the equation hasn't roots.
    if d == 0:
        print("Количество корней: 1")
        x1 = (-1 * b) / (2 * a)  # If d = 0, then the equation has a 1 root.
        print("{:.5f}".format(x1))
    if d > 0:
        print("Количество корней: 2")  # If d > 0 , then the equation has a 2 roots.
        x1 = (-b - sqrt(d)) / (2 * a)
        x2 = (-b + sqrt(d)) / (2 * a)
        print("{:.5f}".format(x1))
        print("{:.5f}".format(x2))


# Float numbers are entering from keyboard(factors of the square equation).
factor(float(input("Введите коэффициент при x^2, неравный 0")),
       float(input("Введите коэффициент при x^2, неравный 0")),
       float(input('Введите коэффициент при x^2, неравный 0')))
