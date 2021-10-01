from math import sqrt
a = float(input("Введите ребро икосаэдра"))
r = (a*(3 + sqrt(5))) / (4 * sqrt(3))
print("Радиус сферы, вписанной в икосаэдр =", r)
