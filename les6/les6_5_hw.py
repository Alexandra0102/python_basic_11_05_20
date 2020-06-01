'''Реализовать класс Stationery (канцелярская принадлежность).
Определить в нем атрибут title (название) и метод draw (отрисовка). Метод выводит сообщение “Запуск отрисовки.”
Создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер).
В каждом из классов реализовать переопределение метода draw.
Для каждого из классов метод должен выводить уникальное сообщение.
Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.
'''

class Stationery():
    # атрибуты класса
    title = ""

    # методы класса
    def draw(self):
        print(f"Запуск отрисовки")

class Pen(Stationery):
    def draw(self):
        print(f"Это отрисовка ручкой")
class Pencil(Stationery):
    def draw(self):
        print(f"Это отрисовка карандашом")
class Handle(Stationery):
    def draw(self):
        print(f"Это отрисовка фломастером")

a = Pen()
b = Pencil()
c = Handle()
d = Stationery()
a.draw()
b.draw()
c.draw()
d.draw()




