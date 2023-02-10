# Требуется найти в массиве A[1..N] самый близкий по
# величине элемент к заданному числу X. Пользователь в первой строке
# вводит натуральное число N – количество элементов в массиве. В
# последующих строках записаны N целых чисел Ai. Последняя строка
# содержит число X.

# 5
# 1 2 3 4 5
# 6
# -> 5

from random import randint

import os
os.system('cls')

n = int(input('Введите длину массива: '))

array = [randint(1, 10) for i in range(n)]
print(array)

X = int(input('Введите число X: '))

closest = array[0]
for i in range (0, len(array)):
    if abs(array[i] - X) < abs(closest - X):
        closest = array[i]
print(f'Cамый близкий по величине элемент к заданному числу X - является элемент: {closest}')


# N = int(input('Введите длину массива: '))
# X = int(input('Введите число для поиска ближайшего числа в массиве: '))

# my_list = [randint(1, 10) for i in range(N)]
# print(my_list)     
# my_list.append(X)
# print(my_list)     
# list.sort(my_list)     
# print(my_list)

# if X == my_list[0]:
#     print(my_list[1])
# else:
#     b = my_list.index(X)
#     b = b - 1
#     print(my_list[b])