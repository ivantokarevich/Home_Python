# 1. Напишите программу, которая принимает на вход цифру, 
# обозначающую день недели, и проверяет, является ли этот день выходным.
# Пример:
# 6 -> да
# 7 -> да
# 1 -> нет

""" day = int(input('Введите номер дня недели: '))
if day > 7 or day < 1:
    print('Введите корректное значение: ')
elif day == 6 or day == 7:
     print("Сегодня выходный!")
else:
     print("Сегодня рабочий день!") """


# 2. Напишите программу, которая принимает на вход координаты точки (X и Y), 
# и выдаёт номер четверти плоскости, в которой находится эта точка 
# (или на какой оси она находится).
# Пример:
# x=34; y=-30 -> 4
# x=2; y=4-> 1
# x=-34; y=-30 -> 3

""" x = int(input('Введите координату x: '))
y = int(input('Введите координату y: '))
if x > 0 and y > 0:
    print('1')
if x < 0 and y > 0:
    print('2')
if x < 0 and y < 0:
    print('3')
if x > 0 and y < 0:
    print('4') """


# 3. Напишите программу, которая по заданному номеру четверти, 
# показывает диапазон возможных координат точек в этой четверти (x и y).

""" n = int(input('Введите номер четверти: '))
if n < 1 or n > 4:
    print('Введите число от 1 до 4')
elif n == 1:
    print('x > 0 and y > 0')
elif n == 2:
    print('x < 0 and y > 0')
elif n == 3:
    print('x < 0 and y < 0')
elif n == 4:
    print('x > 0 and y < 0') """


# 4. Напишите программу, которая принимает на вход координаты двух точек 
# и находит расстояние между ними в 2D пространстве.
# Пример:
# A (3,6); B (2,1) -> 5,09
# A (7,-5); B (1,-1) -> 7,21

""" print('Введите координаты точки А:')
x_A = float(input('X: '))
y_A = float(input('Y: '))
print("Введите координаты точки B:")
x_B = float(input('X: '))
y_B = float(input('Y: '))

from math import sqrt
print('Расстояние между A и B: ',round(sqrt((x_A - x_B)**2 + (y_A - y_B)**2), 2))  """


# Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.\
for x in range(2):
        for y in range(2):
            for z in range(2):
                print(not (x or y or z) == (not x and not y and not z))
                print(x, y, z)