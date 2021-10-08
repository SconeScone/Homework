diagram = {"Фамилия": [], "Имя": [], "Отчество": [], "Год рождения": [], "Заболевание": []}
for i in range(5):
    sur = input("Введите фамилию")
    name = input("Введите имя")
    pat = input("Введите отчество")
    year = input("Введите год рождения")
    illness = input("Введите заболевание")
    diagram["Фамилия"].append(sur)
    diagram["Имя"].append(name)
    diagram["Отчество"].append(pat)
    diagram["Год рождения"].append(year)
    diagram["Заболевание"].append(illness)
for key in diagram:
    print(key, diagram[key])
