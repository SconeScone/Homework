def print_rec(a, b):
    rec_list = [['*' for i in range(a)]] + [['*'] + [' ' for i in range(a - 2)] for i in range(b-2)] \
               + [['*' for i in range(a)]]
    for i in range(1, b - 1):
        rec_list[i].append('*')
    file = open('output.txt', 'a')
    for i in rec_list:
        for k in i:
            file.write(str(k) + '  ')
        file.write('\n')
    file.close()


def print_sqr(a):
    rec_list = [['*' for i in range(a)]] + [['*'] + [' ' for i in range(a - 2)] for i in range(a - 2)] \
               + [['*' for i in range(a)]]
    for i in range(1, a - 1):
        rec_list[i].append('*')
    file = open('output.txt', 'a')
    for i in rec_list:
        for k in i:
            file.write(str(k) + '  ')
        file.write('\n')
    file.close()
