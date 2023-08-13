#  Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону 
# (т.е. не меньше заданного минимума и не больше заданного максимума)

import random

list_1 = [random.randint(0, 100) for _ in range(10)]
user_range = {"min": 15, "max": 50}
print(list_1)
print([index for index in range(len(list_1)) if list_1[index] <= user_range["max"] and list_1[index] >= user_range["min"]])