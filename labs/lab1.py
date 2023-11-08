import math


def task1():
    x = 1
    y = 8
    a = (math.sin(x) ** 2) + (math.cos(y) ** 2) + (math.log(math.e ** x + math.e ** (-y)))
    b = (math.log(math.sqrt(abs(x - 1)))) - (pow(5, 1 / abs(5)))
    print("Ответ:")
    print('a =', a)
    print('b =', b)


def task2():
    a = 1
    b = -2
    x = float(input('x = '))
    y = (math.sqrt(x + a)) + ((x ** 2 + b) / x)
    print('f(x) =', y)


def task3():
    x = float(input('x = '))
    y =math.sin(math.sqrt(x)) + math.cos(math.sqrt(x))
    print('f(x) =', y)


def task4():
    h = 5
    a = 4
    c = (a ** 2) # Площадь основания
    x = c + (4 * (0.5 * a) * h)
    y = (1 / 3) * c * h
    print("Площадь поверхности пирамиды", x)
    print("Объем пирамиды", y)


def task5():
    r = 68
    a = 37
    x = (math.sqrt(3) / 4) * a ** 2 #Площадь треугольника
    s = 4 * math.pi * r ** 2 #Площадь сферы
    y = math.floor(x / s)
    print("Max колличество шаров в треугольнике",y)


def task6():
    a = 18
    b = 9
    c = 13
    x = (a + b + c) / 2 #Полупериметр
    y = (x * (x - a) * (x - b) * (x - c)) ** 0.5 #Площадь
    def h_(n):
        h_(n) = (2 * y) / (n)
        result = h_(n)
        return result
    h_(a)
    h_(b)
    h_(c)
    h = h_(a) * h_(b) * h_(c)
    print("Произведение высот", h)


def task7():
    a * x + b = 0
    a = float(input(42))
    b = float(input(100))

    if (a == 0 and b == 0):
        print("Бесконечное количество решений.")
    if (a == 0 and b != 0):
        print("Решений нет.")
    if (a != 0):
        print(b / a))
