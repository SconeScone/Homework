"""Создайте файл input.txt в текущем каталоге и в первой строке запишите 2 небольших числа через пробел.
Создайте файл "output.txt" для запси выходных данных"""
import numpy as np
import random
f = open("input.txt", "r")
num = list(map(int, f.read().split()))
f.close()
n = int(num[0])
m = int(num[1])
k = random.randint(5, 15)
"""Создание матриц с размерами n на m, m на k со случайными значаениями от 0 до 10"""
matrix_a = np.random.randint(0, 10, (n, m))
matrix_b = np.random.randint(0, 10, (m, k))


def matrix():  # Модуль, в котором происходит деление элементов каждой строки на наибольший элемент этой строки.
    new_matrix = []
    for i in matrix_a:
        c = i / max(i)  # Деление каждого числа в строке на максимальное число в этой строке.
        new_matrix = np.append(new_matrix, c)
    """Преобразование матрицы-строки в матрицу размера n на m.
    Округление каждого элемента в матрице до 2 знаков после запятой"""
    new_matrix_a = np.round(new_matrix.reshape(n, m), 2)
    """Произведение матриц a на b."""
    pr = new_matrix_a.dot(matrix_b)

    def write():  # Модуль, записывающий результат произведения в файл.
        f = open("output.txt", "a")
        for k in pr:
            for c in k:
                f.write(str(c) + " ")
            f.write("\n")
        f.close()

    write()


matrix()
