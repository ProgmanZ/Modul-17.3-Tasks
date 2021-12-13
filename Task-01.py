# Задача 1. Список чётных чисел

a = int(input('Введите начало диапазона: '))
b = int(input('Введите конец диапазона: '))

list_odd = [x for x in range(a, b + 1) if x % 2 == 0]

print(list_odd)
