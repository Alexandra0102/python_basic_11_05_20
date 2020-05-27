'''Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и наличие лекционных,
практических и лабораторных занятий по этому предмету и их количество.
Важно, чтобы для каждого предмета не обязательно были все типы занятий.
Сформировать словарь, содержащий название предмета и общее количество занятий по нему. Вывести словарь на экран.
Примеры строк файла: Информатика:   100(л)   50(пр)   20(лаб).
                                        Физика:   30(л)   —   10(лаб)
                                        Физкультура:   —   30(пр)   —
Пример словаря: {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}
'''


f_obj = open("les5_6_hw.txt", "r", encoding='UTF-8')
try:
    print(f_obj)
    content = f_obj.read()
 #   print(content)
except IOError:
    print('Ошибка')

dict = {}
dict_list = []
with open("les5_6_hw.txt", 'r', encoding='UTF-8') as file:
    for line in file:
        dict_list = line.split()
        print(dict_list)

        if dict_list[1] != '-':
            a_1 = dict_list[1].index('(')
            hours_1 = int(dict_list[1][:a_1])
        else: hours_1 = 0
        if dict_list[2] != '-':
            a_2 = dict_list[2].index('(')
            hours_2 = int(dict_list[2][:a_2])
        else: hours_2 = 0
        if dict_list[3] != '-':
            a_3 = dict_list[3].index('(')
            hours_3 = int(dict_list[3][:a_3])
        else: hours_3 = 0
 #       print(hours_1 + hours_2 + hours_3)
        dict.update({dict_list[0]: hours_1 + hours_2 + hours_3})
print(dict)