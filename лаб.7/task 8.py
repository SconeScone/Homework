def file():
    """
    Данная функция производит считывание данных из файла.
    :return: Возвращает список целых чисел.
    """
    f = open('input.txt', 'r')
    num = list(map(int, f.readline().split()))
    f.close()
    return num


num_list = file()


def order(num_list):
    """
    Данная функция выводит сначала отрицательные, а затем положительные числа в списке.
    :param num_list: list, список, который заканчивается 0.
    :return: Возвращает строку с числами, расположенными в нужном порядке.
    """
    if num_list[0] == 0:
        return ''
    else:
        if num_list[0] < 0:
            return str(num_list[0]) + ' ' + str(order(num_list[1:]))
        else:
            return str(order(num_list[1:])) + ' ' + str(num_list[0])


new_order = order(num_list)


f = open('output.txt', 'a')
f.write(new_order)
f.close()
