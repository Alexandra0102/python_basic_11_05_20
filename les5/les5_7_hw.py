'''Создать вручную и заполнить несколькими строками текстовый файл,
в котором каждая строка должна содержать данные о фирме: название, форма собственности, выручка, издержки.
Пример строки файла: firm_1   ООО   10000   5000.
Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
Если фирма получила убытки, в расчет средней прибыли ее не включать.
Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями,
а также словарь со средней прибылью. Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
Итоговый список сохранить в виде json-объекта в соответствующий файл.
Пример json-объекта:
[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
Подсказка: использовать менеджер контекста.
'''

import json

dict_list = []
dict_list_2 = []
dict = {}
dict_1 = {}
with open("les5_7_hw.txt", 'r', encoding='UTF-8') as file:
    ave_profit = 0
    count = 0
    for line in file:

        dict_list = line.split()
        print(dict_list)

        profit = int(dict_list[2]) - int(dict_list[3])
        sales = int(dict_list[2])
        name = dict_list[0]
        dict.update({name: profit})
        print(dict)

        if profit >= 0:
            ave_profit += profit
            count += 1
dict_1.update({'средняя прибыль': ave_profit / count})
dict_list_2.append(dict)
dict_list_2.append(dict_1)
print(dict_list_2)

with open("my_file.json", "w") as write_f:
    json.dump(dict_list_2, write_f)