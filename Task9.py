# По данному целому неотрицательному n вычислите
# значение n!. N! = 1 * 2 * 3 * … * N (произведение всех
# чисел от 1 до N) 0! = 1 Решить задачу используя цикл
# while
# Input: 5
# Output: 120 

import os
os.system('cls')

# n = int(input('Введите целое не отрицательное число: '))
# result = 1
# i = 1

# while i <= n:
    
#     result = result * i
#     i = i + 1

# print(result)



n = int(input('Введите целое не отрицательное число: '))
while n < 0:
    print('Введены не верные данные')
    n = int(input('Введите целое не отрицательное число: '))

def factorial_number(number):
  factorial = 1
  i = 1
  # while i <= n:
  #   factorial*= i
  #   i+=1
  for i in range(1, n + 1):
    factorial*= i
  return factorial

factorial_n = factorial_number(n)
print(factorial_n)










# Console.Clear();
# Console.Write("Введите число: ");
# int n = Convert.ToInt32(Console.ReadLine()); 
#   int result = 1;
#   for (int i = 1; i <= n; i++)  
#     result = result * i;
#     Console.Write($"{result} ");