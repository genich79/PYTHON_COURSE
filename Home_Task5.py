# Найдите сумму цифр трехзначного числа. 
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0)

# n = int(input("Введите трехзначное число: "))

# d1 = n % 10
# d2 = n % 100 // 10
# d3 = n // 100
 
# print("Сумма цифр числа:", d1 + d2 + d3)

import os
os.system('cls')

n = input("Введите трехзначное число: ")
 
a = int(n[0])
b = int(n[1])
c = int(n[2])
 
print("Сумма цифр числа:", a + b + c)