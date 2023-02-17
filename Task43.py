# Дан список чисел. Посчитайте, сколько в нем пар
# элементов, равных друг другу. Считается, что любые
# два элемента, равные друг другу образуют одну пару,
# которую необходимо посчитать. Вводится список
# чисел. Все числа списка находятся на разных
# строках.


# Ввод:                   Вывод:
# 1 2 3 2 3               2

import os
os.system('cls')

# arr = list(int(input(f'Enter {i + 1} your num: ')) for i in range(int(input('Enter lengh array: '))))
# print(arr)
# arr.sort()
# print(arr)

# count = 0
# for i in range(1, len(arr)):
#     if arr[i] == arr[i - 1]:
#         count += 1
# print(count) 


arr = [1, 1, 1, 1, 1]
n = len(arr)
result = 0
for i in range(n - 1):
    for j in range(i + 1, n):
        if arr[i] == arr[j]:
            result += 1


print(f'{arr} \n')
print(f'Количество парных элементов списка = {result}')