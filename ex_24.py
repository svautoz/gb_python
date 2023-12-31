# Задача 24: В фермерском хозяйстве в Карелии выращивают чернику. Она растёт на круглой грядке, причём кусты высажены только по окружности. Таким образом, у 
# каждого куста есть ровно два соседних. Всего на грядке растёт N кустов.
# Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них выросло различное число ягод — на i-ом кусте выросло ai ягод.
# В этом фермерском хозяйстве внедрена система автоматического сбора черники. Эта система состоит из управляющего модуля и нескольких собирающих модулей. 
# Собирающий модуль за один заход, находясь непосредственно перед некоторым кустом, собирает ягоды с этого куста и с двух соседних с ним.
# Напишите программу для нахождения максимального числа ягод, которое может собрать за один заход собирающий модуль, находясь перед некоторым кустом 
# заданной во входном файле грядки.

import random

N = int(input("Введите кол-во кустов на грядке: "))
yield_list = list()
for _ in range(N):
    yield_list.append(random.randint(50, 70))
print(yield_list)

#1 вариант
yield_list.insert(0, yield_list[len(yield_list) - 1])
yield_list.insert(len(yield_list), yield_list[1])
print(yield_list)
max_yield = 0
for i in range(N):
    berries_sum = yield_list[i] + yield_list[i + 1] + yield_list[i + 2]
    if max_yield < berries_sum:
        max_yield = berries_sum
print(max_yield)
#2 вариант
max_yield = 0
for i in range(N):
    berries_sum = yield_list[i] + yield_list[(i + 1) % N] + yield_list[(i + 2)% N]
    if max_yield < berries_sum:
        max_yield = berries_sum
print(max_yield)