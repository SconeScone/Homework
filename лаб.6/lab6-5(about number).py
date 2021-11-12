"""Создайте файл input.txt в текущем каталоге
и в первой строке запишите 1 или несколько небольших чисел через пробел.
Создайте файл "output.txt" для запси выходных данных"""
import os


def file_here():  # This module checks, is file in the directory or not.
    files = os.listdir(r"C:\Users\User\PycharmProgect\Homework\лаб.6")
    print(len(files))

    def number():  # This module reads a number from the file and finds count of digits in this number.
        f = open("input.txt", "r")
        num = list(map(int, f.read().split()))
        f.close()
        length = len(str(num[0]))
        f = open("output.txt", "a", -1, "utf-8")
        f.write("Число:" + str(num[0]) + "\n")
        f.write("Количество цифр:" + str(length) + "\n")

        def sp():  # This module finds sum and product of digits in a number
            s = 0
            p = 1
            num_s = str(num[0])
            for i in range(len(num_s)):
                s = s + int(str(num_s[i]))
                p = p * int(str(num_s[i]))
            f.write("Сумма цифр:" + str(s) + "\n")
            f.write("Произведение цифр:" + str(p) + "\n")
            f.close()
        sp()
    if "input.txt" in files:  # If the file is in the directory, then call the function
        number()
    else:
        print("Файл с входными данными не обнаружен")


file_here()
