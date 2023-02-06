# Дана последовательность из N целых чисел и число
# K. Необходимо сдвинуть всю последовательность
# (сдвиг - циклический) на K элементов вправо, K –
# положительное число.
# Input: [1, 2, 3, 4, 5] k = 3
# Output: [4, 5, 1, 2, 3]
# Примечание: Пользователь может вводить значения
# списка или список задан изначально.

# my_list = [1, 2, 3, 4, 5]
# k = int(input('Num: '))

from random import randint

n = int(input('Введите длину списка: '))
# my_list = []
# for i in range(n):
#     my_list[i] = random.randint(1, 100)

my_list = [randint(1, 100) for i in range(n)]
print(my_list)

k = int(input('Num: '))
# while k > 0:
#     my_list.append(my_list[0])
#     my_list.remove(my_list[0])
#     k -=1
for i in range(k):
    my_list.append(my_list[0])
    my_list.remove(my_list[0])
print(my_list)


# your_list = [int(input('type_element: ')) for i in range(int(input('type_amount')))]
# k = int(input('type K: ')) % len(your_list)
# print(your_list)
# k_list = your_list[k:] + your_list[:k]
# print(k_list)