def bubble(array, n):
    """
    Функция, сортирующая элементы массива методом 'Пузырька'(самые маленькие элементы оказываются в начале)
    :param array: list, список(массив) из n случайных чисел.
    :param n: int, количество элементов в массиве.
    :return: Возвращает отсортированный список.
    """
    for i in range(n - 1):
        for j in range(n - 1, i, -1):
            k = j
            if array[k - 1] > array[k]:
                array[k - 1], array[k] = array[k], array[k - 1]
    return array


def insert(array, n):
    """
    Функция, сортирующая элементы массива с помощь метода "Сортировка простыми вставками".
    :param array: list, список(массив) из n случайных чисел.
    :param n: int, количество элементов в массиве.
    :return: Возвращает отсортированный список.
    """
    for i in range(1, n):
        k = i
        while k > 0 and array[k - 1] > array[k]:
            array[k - 1], array[k] = array[k], array[k - 1]
            k -= 1
    return array


def hoare(array, left, right):
    """
    Функция, кторая сортирует массив при помощи сортировки Хоара(быстрой сортировки).
    :param array: list, список(массив), содержащий n случайных элементов.
    :param left: int, левый индекс массива(первый)
    :param right: int, правый индекс массива(последний)
    :return: Возвращает массив, отсортированнй в порядке возрастания.
    """
    if left >= right:
        return
    i, j = left, right
    p = array[i + (j - i) // 2]

    while i <= j:
        while array[i] < p:
            i += 1
        while array[j] > p:
            j -= 1
        if i <= j:
            array[i], array[j] = array[j], array[i]
            i += 1
            j -= 1
    hoare(array, left, j)
    hoare(array, i, right)
    return array
