'''Реализовать проект расчета суммарного расхода ткани на производство одежды.
Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
К типам одежды в этом проекте относятся пальто и костюм. У этих типов одежды существуют параметры:
размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и H, соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5),
для костюма (2*H + 0.3). Проверить работу этих методов на реальных данных.
Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания:
реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.'''

from abc import ABC, abstractmethod

class MyAbstract(ABC):
    @abstractmethod
    def material_coat(self, coat: int) -> int:
        pass

    @abstractmethod
    def material_suit(self, suit: int) -> int:
        pass

class Clothers(MyAbstract):
    def __init__(self, coat, suit):
        self.V = int(coat)
        self.H = int(suit)

    @property
    def material_coat(self, **kwargs) -> int:
        a = self.V / 6.5 + 0.5
        return a

    def material_suit(self, **kwargs) -> int:
        b = (2 * self.H + 0.3)
        return b


#   def __add__(self, other):
#       return Clothers(self.coat + other.coat, self.suit + other.suit)

c = Clothers(44, 172)

print(round(c.material_coat, 2))
print(c.material_suit())
print(c.material_coat + c.material_suit())

# метод без @property и абстракции :)

class Clothers():
    def __init__(self, coat, suit):
        self.V = float(coat)
        self.H = float(suit)

    def material_coat(self):
        a = self.V / 6.5 + 0.5
        return a

    def material_suit(self):
        b = (2 * self.H + 0.3)
        return b

c = Clothers(44, 172)
a = c.material_coat()
b = c.material_suit()
print((round(a, 2)))
print(b)
