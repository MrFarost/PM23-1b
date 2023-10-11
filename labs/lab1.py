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
    print('x =', y)


def task3():
    x = float(input('x = '))
    y =math.sin(math.sqrt(x)) + math.cos(math.sqrt(x))
    print('x =', y)


def task4():
    
