'''Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
В расчете необходимо использовать формулу: (выработка в часах*ставка в час) + премия.
Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.'''

def my_func(hours, paymentHour, bonus):
    result = (hours * paymentHour) + bonus
    return result
print(my_func(2, 10, 25))


my_func2 = lambda a, b, c: a * b + c
print(my_func2(2, 10, 25))


