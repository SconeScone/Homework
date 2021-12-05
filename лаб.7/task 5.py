def count_num(line):
    """
    Данная функция подсчитывает количество цифр в символьной строке.
    :param line: str, символьная строка, которая заканчивается '.'.
    :return: Возвращает количество цифр в заданной строке.
    """
    if line[0] == '.':
        return 0
    else:
        if line[0] in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
            return 1 + count_num(line[1:])
        else:
            return count_num(line[1:])


f = open('input.txt', 'r', -1, 'utf-8')
cur_line = f.readline()
f.close()
if cur_line[-1] == '.':
    print(count_num(cur_line))
else:
    print('Строка символов не заканчивается точкой')
