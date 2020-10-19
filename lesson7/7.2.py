# Реализовать проект расчета суммарного расхода ткани на производство одежды.
# Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
# К типам одежды в этом проекте относятся пальто и костюм. У этих типов одежды существуют параметры:
# размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и H, соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5),
# для костюма (2 * H + 0.3). Проверить работу этих методов на реальных данных.
# Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания:
# реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.


class Clothing:
    def __init__(self, name, param):
        self.name = name
        self.param = param

    @property
    def amount_textile(self):
        if self.name.lower() == 'пальто':
            return self.param/6.5 + 0.5
        elif self.name.lower() == 'костюм':
            return self.param*2 + 0.3


class ClothingAbstract:
    def __init__(self, name, param):
        self.name = name
        self.param = param

    def amount_textile(self):
        pass


class Coat(ClothingAbstract):
    @property
    def amount_textile(self):
        return self.param / 6.5 + 0.5


class Suit(ClothingAbstract):

    def calculate_textile(self):
        return self.param*2 + 0.3
    
    @property
    def amount_textile(self):
        return self.param*2 + 0.3


if __name__ == '__main__':
    dress1 = Clothing('Пальто', 52)
    dress2 = Clothing('Костюм', 152)
    print(dress1.amount_textile)
    print(dress2.amount_textile)

    dress3 = Suit('костюм', 152)
    dress4 = Coat('Пальто', 52)
    print(dress3.calculate_textile())
    print(dress3.amount_textile)

    print(dress4.amount_textile)
