""" Ключевое слово if используется для построения условного оператора,
который выполняет определенный код после проверки некоторого условия (логического выражения) на истинность.

Для определения вложенных блоков кода в Python используются отступы!
"""

name = "John"
age = 17

if name == "John" or age == 17:  # проверяем, зовут ли человека "John " или ему 17 лет
    # Если выполняется хотя бы одно условие, вывести следующие 2 строчки
    print("name is John")  # обратите внимание на отступы перед словом print
    print("John is 17 years old")

tasks = ['task1', 'task2']  # создаем список
if not tasks:  # or 'if tasks == []:'
    print('Tasks is empty')
else:
    print('Tasks is not empty')
""" Оператор else дополняет оператор if. 
Ключевое слово elif сокращенная запись "else if".  """

x = 28
if x < 0:
    print('x < 0')  # выполняется только если x < 0
elif x == 0:
    print('x is zero')  # если x < 0 не истина, то проверяется равенство x == 0
elif x == 1:
    print('x == 1')  # если x < 0 не истина и x == 0 не истина, проверяется равенство x == 1
else:
    print('non of the above is true')  # объясните в каком случае выполняется этот оператор?
"""This operator will be done if none of conditionals don't execute"""

name = "John"
# Выведите True если значение переменной name "John" и False в противном случае
if name == 'John':
    print(True)
else:
    print(False)
