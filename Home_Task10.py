# На столе лежат n монеток. Некоторые из них лежат вверх
# решкой, а некоторые – гербом. Определите минимальное число
# монеток, которые нужно перевернуть, чтобы все монетки были
# повернуты вверх одной и той же стороной. Выведите минимальное
# количество монет, которые нужно перевернуть

# 5 -> 1 0 1 1 0
# 2
import os
os.system('cls')

from random import randint

n = int(input('Введите количество монет: '))

coins = [randint(0, 1) for i in range(n)]

print(f'Случайный набор из {n} монет: ')
print(coins)

tails = [moneta for moneta in coins if moneta == 1]

turn_coins = len(tails) if len(tails) <= len(coins)//2 else len(coins) - len(tails)

print(f'Минимальное количество монет, которые нужно перевернуть: {turn_coins}')