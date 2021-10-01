bigslo = {}
for i in range(2):
    keys = input("Введите номер призывника")
    sur = input("Введите фамилию")
    name = input("Введите имя")
    otc = input("Введите отчество")
    y = input("Введите год рождения")
    il = input("Введите заболевание")
    value = [sur, name, otc, y, il]
    slo = dict.fromkeys(keys, value)
    bigslo[keys] = value
print(bigslo)
