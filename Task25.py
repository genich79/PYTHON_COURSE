# Напишите программу, которая принимает на вход
# строку, и отслеживает, сколько раз каждый символ
# уже встречался. Количество повторов добавляется к
# символам с помощью постфикса формата _n.

# Input: a a a b c a a d c d d
# Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2

# Для решения данной задачи используйте функцию
# .split()

# s = 'a a a b c a a d c d d'
# s = s.split()
# print(s)

# result_dic = {} #Словарь, в который будем класть счетчики какой символ сколько раз встречается
# new_s = [] #Новый список, в который будем класть по условию в задаче

# for i in s:
#     if i not in result_dic: #Если еще нет в словаре первый раз
#         new_s.append(i) # Кладем наш символ
#         result_dic[i] = result_dic.get(i, 0) + 1 #С помощью метода get возвращаем в словарь наш символ
#     else: #Если уже есть в словаре, значит пошли повторы
#         new_s.append(f'{i}_{result_dic[i]}') #Кладем значение с постфиксом и значение из словаря
#         result_dic[i] = result_dic.get(i, 0) + 1
# print(*new_s)


text = 'a a a b c a a d c d d'
text = text.split()
result = ''
d = {}
for i in range(len(text)):
    if text[i] not in d:
        d[text[i]] = 1
        result += f'{text[i]} '
    else:
        result += f'{text[i]}_{d[text[i]]} '
        d[text[i]] += 1

print(result)
print(d)