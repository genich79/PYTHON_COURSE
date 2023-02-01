# Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).

import os
os.system('cls')

n = int(input("Ведите номер четверти: "))
if n == 1:
    print("x > 0 and y > 0")
elif n == 2:
    print("x < 0 and y > 0")
elif n == 3:
    print("x < 0 and y < 0")
else:
    print("x > 0 and y < 0")