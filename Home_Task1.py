# Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.

# Пример:

# - 6 -> да
# - 7 -> да
# - 1 -> нет

import os
os.system('cls')

n = int(input("Введите день недели от 1 до 7: "))
    
if (n == 6):
    print(f'{n} -> да, день является выходным!')
elif (n == 7):
    print(f'{n} -> да, день является выходным!')
else:
    print(f'{n} -> нет, день является рабочим!')