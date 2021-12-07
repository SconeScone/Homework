def greater(a, b):
    """
    Функция, которая находит наибольший общий делитель 2 чисел, при помощи алгоритма Евклида.
    :param a: int, натурально число, не превышающее 10^9.
    :param b: int, натурально число, не превышающее 10^9.
    :return: Возвращает НОД введенных чисел.
    """
    if b == 0:
        return a
    else:
        return greater(b, a % b)


print(greater(int(input('a')), (int(input('b')))))
