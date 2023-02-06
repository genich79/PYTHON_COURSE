# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

# Пример:

# - 6782 -> 23
# - 0,56 -> 11

# // Console.Clear();
# // Console.Write("Введите число: ");
# // string? n = Console.ReadLine();
# // int result = 0;
# // for (int i = 0; i < n.Length; i++)
# //     result = result + int.Parse(n[i].ToString());

# // Console.WriteLine(result);


import os
os.system('cls')

x = input('Введите число ')

def summa(x):                            
    if float(x) < 0:                            
        x = float(x) * (-1)
    
    number = 0
    for i in str(x):
        if i != '.':
            number += int(i)
    return number

   
print(f'Сумма чисел равна {summa(x)}')
