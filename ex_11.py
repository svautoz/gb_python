# Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. Петя помогает Кате по математике. 
# Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. Для этого Петя делает две подсказки. 
# Он называет сумму этих чисел S и их произведение P. Помогите Кате отгадать задуманные Петей числа.

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