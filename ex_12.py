# Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.

import random

N = int(input("Введите N: "))
k = 1

while 2**k < N:
    print(k, end=", ")
    k += 1
