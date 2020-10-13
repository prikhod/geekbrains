# Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
# А также методы: go, stop, turn(direction), которые должны сообщать,что машина поехала, остановилась, повернула (куда).
# Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
# Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
# Для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar)
# и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
# Выполните вызов методов и также покажите результат.
from random import randint


class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        self.speed = randint(20, 90)
        print(f'{self.name} поехал со скоростью :{self.speed}км/ч')

    def stop(self):
        self.speed = 0
        print(f'{self.name} остановился')

    def car_turn(self, direction):
        return f'{self.name} повернул {direction}'

    def show_speed(self):
        print('Скорость:', self.speed)


class TownCar(Car):

    def show_speed(self):
        if self.speed > 60:
            print(f'{self.name} превысил скорость')
        print('Скорость:', self.speed)


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print(f'{self.name} превысил скорость')
        print('Скорость:', self.speed)


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police=True)


if __name__ == '__main__':
    car1 = Car(30, 'red', 'Car1', False)
    car1.show_speed()
    car1.stop()
    car1.go()
    car1.show_speed()
    print(car1.car_turn('left'))

    car2 = WorkCar(30, 'red', 'Car2', False)
    car2.show_speed()
    car2.stop()
    car2.go()
    car2.show_speed()
    print(car2.car_turn('left'))
    print('is police?', car2.is_police)

    car3 = TownCar(30, 'red', 'Car3', False)
    car3.show_speed()
    car3.stop()
    car3.go()
    car3.show_speed()
    print(car3.car_turn('left'))

    car4 = PoliceCar(30, 'red', 'Car4', False)
    car4.show_speed()
    car4.stop()
    car4.go()
    car4.show_speed()
    print(car4.car_turn('left'))
    print('is police?', car4.is_police)
