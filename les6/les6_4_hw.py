'''Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police
(булево).  А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась,
повернула (куда). Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
Для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и 40 (WorkCar)
 должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
Выполните вызов методов и также покажите результат.
'''
class Car():
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f'Car goes')
    def stop(self):
        print('Car stops')
    def turn(self):
        print(f'Car turns')
    def show_speed(self):
        print(f"Car's speed")


class WorkCar(Car):
    def show_speed(self):
        if self.speed >= 40:
            print(f' {self.name} Ваша скорость выше допустимой')
        return self.speed
a = WorkCar(35, 'Black', 'KIA', True)
a.show_speed()
print(f'Good luck {a.name}  your speed is {a.speed}')

class TownCar(Car):
    def show_speed(self):
        if self.speed >= 60:
            print(f'{self.name} Ваша скорость выше допустимой')
        return self

b = TownCar(75, 'Red', 'BMW', False)
b.show_speed()
print(f'Good luck {b.name} your sdeed is {b.speed}')