'''Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных.
Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
Подсказка: постарайтесь по возможности реализовать в проекте «Склад оргтехники» максимум возможностей,
изученных на уроках по ООП.
'''

class Warehous:
    def __init__(self, category_name):
        self.category_name = category_name

class OfficeEquipment(Warehous):
    def __init__(self, model, price, quantity):
        self.model = model
        self.price = price
        self.quantity = quantity

class Printer(OfficeEquipment):
    def __init__(self, print_type):
            self.print_type = print_type

class Scanner(OfficeEquipment):
    def __init__(self, speed):
            self.speed = speed

class Xerox(OfficeEquipment):
    def __init__(self, colour):
            self.colour = colour

    @staticmethod
    def isQuantity(quantity):
        return quantity == int()