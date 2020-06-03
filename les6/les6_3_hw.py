'''Реализовать базовый класс Worker (работник), в котором определить атрибуты: name, surname, position (должность),
income (доход). Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы:
оклад и премия, например, {"wage": wage, "bonus": bonus}. Создать класс Position (должность) на базе класса Worker.
В классе Position реализовать методы получения полного имени сотрудника (get_full_name) и
дохода с учетом премии (get_total_income). Проверить работу примера на реальных данных (создать экземпляры класса
 Position, передать данные, проверить значения атрибутов, вызвать методы экземпляров).
'''
wage = 0
bonus = 0
class Worker():
    def __init__(self, name, surname, position, _incom):
        self.name = name
        self.surname = surname
        self.position = position
        self._incom = {"wage": wage,
                       "bonus": bonus}
class Position(Worker):
    def get_full_name(self, name, surname):
        print(f"Полное имя сотрудника {name, surname}")
    def get_total_income(self, name, surname, position, _incom):
        print(f"Доход с учетом премии сотрудника {name, surname, position, _incom}")
#a = Worker()
b = Position("Ivanov", "Ivan", "woker", 1000)
b.get_full_name("Ivanov", "Ivan")
b.get_total_income( "Ivanov", "Ivan", "woker", 1000)