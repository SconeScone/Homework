import rec_sqr  # Импорт собственного модуля
file = open('input.txt', 'r')
num_list = list(map(int, file.readline().split()))
file.close()
if len(num_list) == 1:  # Если длина списка равна 1, то вызвать функцию, которая печатает квадрат
    a = int(num_list[0])
    rec_sqr.print_sqr(a)  # Вызов соответствующей функции из модуля
elif len(num_list) == 2:  # Если длина списка равна 2, то вызвать функцию, которая печатает прямоугольник
    a = int(num_list[0])
    b = int(num_list[1])
    rec_sqr.print_rec(a, b)  # Вызов соответствующей функции из модуля
