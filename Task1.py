# За день машина проезжает n километров. Сколько
# дней нужно, чтобы проехать маршрут длиной m
# километров? При решении этой задачи нельзя
# пользоваться условной инструкцией if и циклами.
# Input:
# n = 700
# m = 750
# Output:
# 2

# n = int(input('Введите сколько километров в день проезжает машина: '))
# m = int(input('Введите расстояние маршрута в километрах: '))
# print(int((m / n + (m / n) % n)))


n = int(input('Введите сколько километров в день проезжает машина: '))
m = int(input('Введите расстояние маршрута в километрах: '))
def arg(n, m):
    return (m + n - 1)//n
res = arg(n, m)
print(res)