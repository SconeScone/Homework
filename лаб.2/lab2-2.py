# Целые числа и числа с плавающей точкой являются одними из самых распространенных в языке Python

number = 9

print(type(number))  # Вывод типа переменной number

float_number = int(9.0)
print(float_number)
# Создайте ещё несколько переменных разных типов и осуществите вывод их типов
s_tip = "Медведь"
b_tip = False
f_tip = 56.23
print("Медведь - ", type(s_tip), " ", "False - ", type(b_tip), " ", "56.23 - ", type(f_tip))


# Существует множество функций, позволяющих изменять тип переменных.
print(str(f_tip))
print(str(b_tip))
print(int(f_tip))
print(int(b_tip))
print(bool(s_tip))
print(bool(f_tip))
print(bool(b_tip))
#  нельзя преобразовать тип string к float
print(float(b_tip))
#  нельзя преобразовать тип string к int
print(float(9))
# Изучите такие функции как int(), float(), str() и последовательно примените их к переменным, созданным ранее.
