'''Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов
(не менее 10 строк). Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
Выполнить подсчет средней величины дохода сотрудников.
Пример файла:
Иванов 23543.12
Петров 13749.32
'''

f_obj = open("les5_4_hw.txt", "r", encoding='UTF-8')
try:
    print(f_obj)
    content = f_obj.read()
 #   print(content)
except IOError:
    print('Ошибка')

f_obj = open("les5_4_hw.txt", "r", encoding='UTF-8')
summ = []
while True:
    content = f_obj.readline()
   # print(content)
    if not content:
        break
    space = content.index(' ')
    lastName = content[:space]
    Salary = float(content[space:])
    if Salary >= 20000:
        print(lastName)

    summ.append(Salary)
print(sum(summ) / len(summ))

