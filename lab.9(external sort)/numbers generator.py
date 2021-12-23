from random import randint


def write_file():
    """
    A function, that generates random numbers and writes them to file.
    :return: None.
    """
    f = open('file1.txt', 'a')
    for i in range(55000):
        if i % 11000 == 0 and i != 0:
            f.write(str(randint(0, 1000)) + '\n')
        else:
            f.write(str(randint(0, 1000)) + ' ')
    f.close()


write_file()
