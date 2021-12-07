def fib(n):
    """
    Функция, которая находит n-е число Фибоначчи.
    :param n: int, целое неотрицательное число n (n <= 30).
    :return: Возвращает n-е число Фибоначчи.
    """
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


print(fib(int(input())))
