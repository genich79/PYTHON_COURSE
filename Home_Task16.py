# Даны два неупорядоченных набора целых чисел (может быть, с
# повторениями). Выдать без повторений в порядке возрастания все те числа, которые
# встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во
# элементов второго множества. Затем пользователь вводит сами элементы множеств.

# 11 6
# 2 4 6 8 10 12 10 8 6 4 2
# 3 6 9 12 15 18
# 6 12

import os
os.system('cls')

from random import randint

n = int(input('Введите количество элементов в первом множестве: '))
m = int(input('Введите количество элементов во втором множестве: '))

list_one = set([randint(1, 12) for _ in range(n)])
print(list_one)
list_two = set([randint(1, 12) for _ in range(m)])
print(list_two)

print('Пересекающиеся элементы: ')
print(sorted(list_one & list_two))
# print(f'{sorted(list_one.intersection(list_two))}')

# list_one = set ([randint(1, 12) for _ in range(int(input('Введите количество элементов в первом множестве: ')))])
# print(list_one)
# list_two = set ([randint(1, 10) for _ in range(int(input('Введите количество элементов во втором множестве: ')))])
# print(list_two)
# print('Пересекающиеся элементы: ')
# print(sorted(list_two & list_one))
