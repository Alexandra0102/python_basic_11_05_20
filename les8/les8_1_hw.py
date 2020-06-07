'''Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата
«день-месяц-год». В рамках класса реализовать два метода. Первый, с декоратором @classmethod, должен
извлекать число, месяц, год и преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod,
должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
Проверить работу полученной структуры на реальных данных.'''

class Data:
    def __init__(self, day, month, year: str):
        self.day = day
        self.month = month
        self.year = year

    @classmethod
    def data_print(cls, day, month, year):
        day = int(day)
        month = int(month)
        year = int(year)
        return [day, month, year]

    @staticmethod
    def val_day(day, month, year):
        if day >= 1 and day <= 31:
            return day
        else:
            print("Error")
        if 1 >= month <= 12:
            return month
        else:
            print("Error")


a = Data('10', '12', '2010')
b = a.data_print('10', '12', '2010')
c = a.val_day(32,15,2010)
print(f'Дата {b}')
print(type(b[1]))
print(type(a))