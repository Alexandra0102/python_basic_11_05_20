'''Представлен список чисел. Определить элементы списка, не имеющие повторений.
Сформировать итоговый массив чисел, соответствующих требованию.
Элементы вывести в порядке их следования в исходном списке.
Для выполнения задания обязательно использовать генератор.
Пример исходного списка: [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11].
Результат: [23, 1, 3, 10, 4, 11]
'''

import random
from random import randint

my_list = [randint(20, 50) for i in range(14)]
print(my_list)

for el in range(len(my_list) - 1):
    for i in range(el + 1, len(my_list)):
        if my_list[el] == my_list[i]:
            print(my_list[i])
new_list = []
print(new_list.append(my_list[el]))


