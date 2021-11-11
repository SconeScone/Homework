"""
МНОЖЕСТВО в Python -  это структура данных, содержащая не повторяющиеся элементы в случайном порядке.
"""
a = set()  # Создание пустого множества
a.add(1)  # Добавление элемента в множество
a.add(2)
a.add(1)
print(a)  # Объясните результат
#  Результат: выводит только уникальные элементы, добавленные в множество. Вывод: {1, 2}

b = set("hello")  # Преобразование строки в множество
print(b)  # Объясните результат
#  Результат: вывод только уникальных букв в строке. Вывод: {'o', 'l', 'h', 'e'}

"""
Множества удобно использовать для удаления повторяющихся элементов из списка
"""

a = ['aa', 'ab', 'aa', 'ba']
print(set(a))

"""
Множества поддерживают стандартные операции других структур данных - len, in, clear и т.п. 
"""

# Вставьте пропущенную строку, чтобы оператор print выводил True

b = ['aa', 'ab', 'aa', 'ba']
b = set(b)
print(len(b) == 3)

"""
Помимо базовых операций, множества в Python поддерживают операции математических множеств (объединение(union),
пересечение(intersection))
"""

a = {1, 2, 3, 4}
a = set(a)
# Создание множества
b = {3, 4, 5, 6}
b = set(b)
c = a.union(b)  # Объединение множества
print(c)

# Вставьте пропущенное действие, чтобы в консоль вывелось пересечение множеств a и b

d = a.intersection(b)
print(d)
print(len(set(a)))
print(1 in set(a))
print(d.clear())
