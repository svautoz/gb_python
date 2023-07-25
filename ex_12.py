# Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.

import random

S = int(input("Введите сумму чисел: "))
P = int(input("Введите произведение чисел: "))


60 = 50 + 10
500 = 50 * 10

side_1 = 0
side_2 = 0
for _ in range(0, n):
    side = random.randint(0, 1)
    print(side, end=' ')
    if side:
        side_1 += 1
    else:
        side_2 += 1
print(f'\nМинимальное кол-во переворотов монеток равна {side_1 if side_1 <= side_2 else side_2}')
