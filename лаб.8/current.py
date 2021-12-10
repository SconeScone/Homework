from prettytable import PrettyTable
from random import randint
from time import time
import sorts
from copy import deepcopy

table = PrettyTable()
table.field_names = ['Метод', 'Случайная', 'Отсортированная', 'Отсортированная в обратном порядке']  # Шапка таблицы.


def check(array):
    """
    Функция, которая проверяет, является ли массив отсортированным.
    :param array: list, массив чисел.
    :return: Возвращает True, если массив отсортирован, и False - в противнм случае.
    """
    for j in range(1, len(array)):
        if array[j - 1] > array[j]:
            return False
    return True


def hoare_time(array, n):
    """
    Функция, которая вычисляет время работы импортированной подпрограммы,
    выполняющей сортировку массива сортировкой Хоара.
    :param array: list, массив чисел.
    :param n: int, число элементов в массиве.
    :return: Возвращает время выполнения программы.
    """
    start_time = time()
    sorts.hoare(array, 0, n - 1)
    end_time = time()
    return end_time - start_time


def bubble_time(array, n):
    """
    Функция, которая вычисляет время работы импортированной подпрограммы,
    выполняющей пузырьковую сортировку массива.
    :param array: list, массив чисел.
    :param n: int, число элементов в массиве.
    :return: Возвращает время выполнения программы.
    """
    start_time = time()
    sorts.bubble(array, n)
    end_time = time()
    return end_time - start_time


def insert_time(array, n):
    """
    Функция, которая вычисляет время работы импортированной подпрограммы,
    выполняющей сортировку массива простыми вставками.
    :param array: list, массив чисел.
    :param n: int, число элементов в массиве.
    :return: Возвращает время выполнения программы.
    """
    start_time = time()
    sorts.insert(array, n)
    end_time = time()
    return end_time - start_time


def sort_time(array):
    """
    Функция, которая вычисляет время работы встроенной фнкции sort().
    :param array: list, массив чисел.
    :return: Возвращает время выполнения программы.
    """
    start_time = time()
    array.sort()
    end_time = time()
    return end_time - start_time


n = int(input('n'))
rand_seq = [randint(0, n)for i in range(n)]
sort_seq = [e for e in range(n)]
reverse_seq = [f for f in reversed(range(n))]
rand_seq_h = deepcopy(rand_seq)  # Копии созданныйх массивов.
sort_seq_h = deepcopy(sort_seq)
reverse_seq_h = deepcopy(reverse_seq)
rand_seq_i = deepcopy(rand_seq)
sort_seq_i = deepcopy(sort_seq)
reverse_seq_i = deepcopy(reverse_seq)
rand_seq_b = deepcopy(rand_seq)
sort_seq_b = deepcopy(sort_seq)
reverse_seq_b = deepcopy(reverse_seq)

if n <= 30:
    """Данное условие необходимо для проверки работоспособности разных методов сортировки.
    Проверяется на небольших значениях n."""
    print(check(rand_seq_h), check(sort_seq_h), check(reverse_seq_h))  # Проверка отсортированности исходных данных.
    print(check(sorts.hoare(rand_seq_h, 0, n - 1)),
          check(sorts.hoare(sort_seq_h, 0, n - 1)), check(sorts.hoare(reverse_seq_h, 0, n - 1)))

    print(check(rand_seq_i), check(sort_seq_i), check(reverse_seq_i))
    print(check(sorts.insert(rand_seq_i, n)),
          check(sorts.insert(sort_seq_i, n)), check(sorts.insert(reverse_seq_i, n)))

    print(check(rand_seq_b), check(sort_seq_b), check(reverse_seq_b))
    print(check(sorts.bubble(rand_seq_b, n)),
          check(sorts.bubble(sort_seq_b, n)), check(sorts.bubble(reverse_seq_b, n)))

if n > 5000:  # Для сравнения времени работы разных подпрограмм, используются большие значения n.
    table.add_row(['Сортировка Хоара', hoare_time(rand_seq_h, n),
                   hoare_time(sort_seq_h, n), hoare_time(reverse_seq_h, n)])
    table.add_row(['Сортировка простыми вставками', insert_time(rand_seq_i, n),
                   insert_time(sort_seq_i, n), insert_time(reverse_seq_i, n)])
    table.add_row(['Пузырьковая сортировка', bubble_time(rand_seq_b, n),
                   bubble_time(sort_seq_b, n), bubble_time(reverse_seq_b, n)])
    table.add_row(['Встроенная сортировка', sort_time(rand_seq), sort_time(sort_seq), sort_time(reverse_seq)])
    table.align = 'l'
    f = open('output.txt', 'w', -1, 'utf-8')
    f.write(table.get_string())
    f.write('\n')
    f.close()
