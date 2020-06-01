'''Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские.
Новый блок строк должен записываться в новый текстовый файл.
'''

numbers_Rus = {
    'one': 'один',
    'two': 'два',
    'three': 'три',
    'four': 'четыре',
}

f_obj = open("les5_41_hw.txt", "r", encoding='UTF-8')
try:
    print(f_obj)
    content = f_obj.read()
 #   print(content)
except IOError:
    print('Ошибка')

f_obj = open("les5_41_hw.txt", "r", encoding='UTF-8')
summ = []
f_obj_2 = open("les5_41NEW_hw.txt", "w", encoding='UTF-8')
Value_0 = []
Value_1 = []

while True:
    content = f_obj.readline()
#    print(content)
    if not content:
        break
    space = content.index(' ')
    numbers = content[:space]
    print(numbers)
    Value_1.append(content[space:])

    for (key, value) in numbers_Rus.items():
        if key == numbers:
            Value_0.append(value)
 #       f_obj_2.write(value)
for f,f1 in zip(Value_0, Value_1):
    f_obj_2.write(f + f1 + '\n')


