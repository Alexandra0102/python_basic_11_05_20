'''Продолжить работу над первым заданием. Разработать методы, отвечающие за приём оргтехники на склад и
передачу в определенное подразделение компании. Для хранения данных о наименовании и количестве единиц оргтехники,
а также других данных, можно использовать любую подходящую структуру, например словарь.'''

class Warehous:
    def __init__(self, category_name):
        self.category_name = category_name

    def AcceptEquipment(self, **kwargs):
        self.category_name = kwargs.get('name', '')
        self.model = kwargs.get('model', '')
        self.price = kwargs.get('price', '')
        self.quantity = kwargs.get('quantity', '')
        self.print_type = kwargs.get('print_type', '')
        self.speed = kwargs.get('speed', '')
        self.colour = kwargs.get('colour', '')
        return f'Наименование принятой категории оргтехники {self.category_name}, \n ' \
               f'модели {self.model}, \n ' \
               f'цена {self.price}, \n' \
               f'количество {self.quantity},\n ' \
               f'имя печати для принтера {self.print_type},\n ' \
               f'скорость сканирования для сканера {self.speed}, \n' \
               f'цвет/не цвет печать для копира {self.colour}'

    def TransferEquipment(self, **kwargs):
        self.category_name = kwargs.get('name', '')
        self.model = kwargs.get('model', '')
        self.price = kwargs.get('price', '')
        self.quantity = kwargs.get('quantity', '')
        self.print_type = kwargs.get('print_type', '')
        self.speed = kwargs.get('speed', '')
        self.colour = kwargs.get('colour', '')
        return f'Наименование принятой категории оргтехники {self.category_name}, \n ' \
               f'модели {self.model}, \n ' \
               f'цена {self.price}, \n' \
               f'количество {self.quantity},\n ' \
               f'имя печати для принтера {self.print_type},\n ' \
               f'скорость сканирования для сканера {self.speed}, \n' \
               f'цвет/не цвет печать для копира {self.colour}'


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



a = Printer({''})
b = a.AcceptEquipment()
print(b)
