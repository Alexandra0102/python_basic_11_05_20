'''Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад.
А также класс «Оргтехника», который будет базовым для классов-наследников.
Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс). В базовом классе определить параметры,
общие для приведенных типов. В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники. '''


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
