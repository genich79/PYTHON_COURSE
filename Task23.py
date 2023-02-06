# Задача №23. Общее обсуждение
# Дан массив, состоящий из целых чисел. Напишите
# программу, которая подсчитает количество
# элементов массива, больших предыдущего (элемента
# с предыдущим номером)
# Input: [0, -1, 5, 2, 3]
# Output: 2 (-1 < 5, 2 < 3)
# Примечание: Пользователь может вводить значения
# списка или список задан изначально.

# def count_lager_then_previous(arr):
#     count = 0
#     for i in range(1, len(arr)):
#         if arr[i] > arr[i - 1]:
#             count += 1
#     return count
# array = [0, -1, 5, 2, 3]
# print(count_lager_then_previous(array))


from random import randint

# my_list = [randint(-10, 10) for _ in range(randint(1, 10))]
# print(my_list)

# counter = 0
# for i in range(1, len(my_list)):
#     if my_list[i] > my_list[i - 1]:
#         counter += 1
# print(counter)

my_list = [randint(-10, 10) for _ in range(randint(1, 10))]
print(my_list)

new_list = [f'{my_list[i]} > {my_list[i - 1]}' for i in range(1, len(my_list)) if my_list[i] > my_list[i - 1]]
print(*new_list, sep='; ')
print(len(new_list))