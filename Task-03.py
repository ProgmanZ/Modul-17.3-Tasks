# Задача 3. Отряды

import random

first = [random.randint(50, 80) for f in range(10)]
second = [random.randint(30, 60) for s in range(10)]

print('Урон первого отряда:', first)
print('Урон второго отряда:', second)

third = ['Выжил' if first[i] + second[i] < 100 else 'Погиб' for i in range(10)]
print('\nСостояние третьего отряда:', third)
