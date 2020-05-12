# PEP8
hello_str = "Hello World"
print(hello_str)

name = input('Ваше имя?\n')
age = input('Возраст?\n')

this_year = 2020

if age.isdigit():
    b_year = this_year - age

    print(b_year)
else:
    print('Неверный возраст')

