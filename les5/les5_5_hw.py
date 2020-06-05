'''Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.'''

import random
from random import randint

i = 0
my_list = [randint(0, 100) for i in range(20)]


f_obj = open("les5_5_hw.txt", "w", encoding='UTF-8')
for i in my_list:
    f_obj.write(str(i) + ' ')
f_obj.close()

f_obj = open("les5_5_hw.txt", "r", encoding='UTF-8')
content = f_obj.read()
print(content)
my_list = content.split(' ')
print(my_list)

summ = 0
for i in my_list:
    if i != '':
        summ += int(i)
print(summ)
