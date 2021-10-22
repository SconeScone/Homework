def money(sum):
    rub = sum // 100
    if (sum // 100) != 0:
        if (rub % 10) == 1:
            print(rub, 'рубль'.upper())
        elif (rub % 10) in [2, 3, 4]:
            print(rub, 'рубля'.upper())
        elif (rub % 10) in [5, 6, 7, 8, 9]:
            print(rub, 'рублей'.upper())
        elif (rub % 10) == 0:
            print(rub, 'рублей'.upper())
    else:
        pass
    kop = sum % 100
    if kop >= 5:
        if (kop % 10) == 1:
            print(kop, 'копейка'.upper())
        elif ((kop % 10) in [2, 3, 4]) and ((kop // 10) in [2, 3, 4, 5, 6, 7, 8, 9]):
            print(kop, 'копейки'.upper())
        else:
            print(kop, 'копеек'.upper())
    if (kop < 5) and (kop != 0):
        if (kop % 10) != 1:
            print(kop, 'копейки'.upper())
        else:
            print(kop, 'копейка'.upper())
    else:
        pass


money(int(input('Введите суммму покупки в копейках')))
