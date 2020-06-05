'''Для чисел в пределах от 20 до 240 найти числа, кратные 20 или 21. Необходимо решить задание в одну строку.
Подсказка: использовать функцию range() и генератор.'''

import random
from random import randint

for el in [randint(20, 240) for i in range(30)]:
    if el % 20 == 0 or el % 21 == 0: print(el)

