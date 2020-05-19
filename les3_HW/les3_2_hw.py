'''Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
имя, фамилия, год рождения, город проживания, email, телефон.
Функция должна принимать параметры как именованные аргументы.
Реализовать вывод данных о пользователе одной строкой.
'''

def my_list(data_list, auto_inc):
    while True:
        user_value = input(f'{value[0]}\n')
        data_list.append(user_value)
        try:
            user_value = value[1](user_value)
        except ValueError as e:
            print(f"{e}\nНе верное значение анных")
            continue
        data_template[key] = user_value
        break
    auto_inc += 1
    print(data_list)
    print(data_template)

data_template = {
    'name': ('имя', str),
    'lastname': ('фамилия', str),
    'year': ('год рождения', int),
    'city': ('город проживания', str),
    'mail': ('email', str),
    'tel': ('телефон', str)
}
auto_inc = 1
data_list = []
next_enter = True

while next_enter:
    data_list.append(auto_inc)
    for key, value in data_template.items():
        my_list(data_list, auto_inc)

    while True:
        next_add = input("Добавить еще человека? Да/Нет\n")
        if next_add.lower() in ('да', 'нет'):
            next_enter = next_add.lower() == 'да'
            break
        else:
            print('Неверный ввод, повторите')






