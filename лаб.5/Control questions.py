# question 1
x = int(input("Введите число x "))
y = int(input("Введите число y "))
z = 0
if x > 0:
    if y > 0:
        z = 1
    else:
        z = 2
print(z)

# question 2
"""Пусть имеется оператор присваивания X=A or B and C, где переменные X, A, B, C имеют тип Boolean.
Напишите условный оператор, который эквивалентен данному
(например, оператору присваивания X=not A эквивалентен условный оператор if A : X=False else X=True)."""
a = bool(input('Ввведите 0 или 1'))
b = bool(input('Ввведите 0 или 1'))
c = bool(input('Ввведите 0 или 1'))
if a:
    x = True
elif b and c:
    x = True
print(x)

# question 3
"""Пусть имеется условный оператор if A : X=B else X=C, где переменные X, A, B, C имеют тип Boolean.
Напишите оператор присваивания, который эквивалентен данному."""
# x = not a and c or a and b

# question 5
print(123 // 10)
print(-123 // 10)
print(123 % 10)
print(-123 % 10)
