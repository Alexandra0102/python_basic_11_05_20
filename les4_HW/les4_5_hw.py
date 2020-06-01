'''Реализовать формирование списка, используя функцию range() и возможности генератора.
В список должны войти четные числа от 100 до 1000 (включая границы).
Необходимо получить результат вычисления произведения всех элементов списка.
Подсказка: использовать функцию reduce().'''

import random
from functools import reduce
from random import randint

for el in [randint(99, 1001) for i in range(30)]:
    if el % 2 == 0:
       print(el)

i = 0
my_list = [randint(99, 1000) for i in range(30)]
if i % 2 == 0:
        print(my_list)

result = reduce((lambda x, y: x * y), my_list)
print(result)

