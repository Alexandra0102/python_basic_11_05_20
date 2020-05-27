'''Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.
'''

def func():
    while True:
        try:
            a = int(input('Введите число a'))
            b = int(input('Введите число b'))
            result = b / a
            print(result)
            break
        except ValueError as error:
            print(error)
            print('тут код обработки ошибки')
        except ZeroDivisionError:
            print('Деление на 0. Повторите ввод')
    return result
print(func())


