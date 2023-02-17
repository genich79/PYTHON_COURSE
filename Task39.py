# Даны два массива чисел. Требуется вывести те элементы
# первого массива (в том порядке, в каком они идут в первом
# массиве), которых нет во втором массиве. Пользователь вводит
# число N - количество элементов в первом массиве, затем N
# чисел - элементы массива. Затем число M - количество
# элементов во втором массиве. Затем элементы второго массива

# Ввод:                                   Вывод:
# 7                                       3 3 2 12
# 3 1 3 4 2 4 12
# 6
# 4 15 43 1 15 1                          (каждое число вводится с новой строки)
# word = 'Python'
# for letter in word:
#     print(letter, end= '')

import os
os.system('cls')

from random import randint

n = int(input('Введите длину 1 - го массива: '))
m = int(input('Введите длину 2 - го массива: '))

n_list = [randint(1, 10) for _ in range(n)]
m_list = [randint(1, 10) for _ in range(m)]

result_list = []

print(*n_list)
print(*m_list)

for i in range(n):
    if n_list[i] not in m_list:
        result_list.append(n_list[i])

print(*result_list)


# list1 = [int(input(f'Введите {i + 1} - e число: ')) for i in range(int(input('Введите длину 1 - го массива: ')))]
# list2 = [int(input(f'Введите {j + 1} - e число: ')) for j in range(int(input('Введите длину 2 - го массива: ')))]

# new_list = [elem for elem in list1 if not(elem in list2)]
# print(new_list)