# 4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад.
# А также класс «Оргтехника», который будет базовым для классов-наследников.
# Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс). В базовом классе определить параметры,
# общие для приведенных типов. В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.
#  5. Разработать методы, отвечающие за приём оргтехники на склад и передачу
# в определенное подразделение компании. Для хранения данных о наименовании и количестве единиц оргтехники,
# а также других данных, можно использовать любую подходящую структуру, например словарь.
class Warehouse:
    def __init__(self, name):
        self.name = name
        self._data = dict()

    def recept_unit(self, device):
        """
        :param device: получаем девайс - экземпляр класса Printer, Scanner или  Duplicator
        записываем в self._data девайс
        :return: 1 если успешно, None если нет
        """
        if not device:
            print('Нечего добавлять. Девайс пустой')
            return
        if self._data.get(device.serial_number):
            print(f'Будет перезаписано устройство с серийным номером {device.serial_number}')

        if (list(self._data.keys())).count(device.type) == 0:
            self._data.setdefault(device.type, {})
        self._data[device.type].update({device.serial_number: device})
        return 1

    def delivery_unit(self, device_type):
        """
        :param device_type: при вызове указываем какой тип устройства хотим получить
        :return: возвращает экземпляр девайса либо строку с сообщением и удаляет из словаря
        """

        if (list(self._data.keys())).count(device_type) != 0:

            if len(self._data[device_type]) != 0:
                return self._data[device_type].popitem()
            else:
                return f'Нет девайсов в категории {device_type}'
        else:
            return f'Нет категории {device_type}'

    def __str__(self):
        """ Представление данных на складе:
                Категория: Printer
                Printer, S/n:1101, Вес: 10кг,Марка: HP, Модель: 1010
                Printer, S/n:1103, Вес: 3кг,Марка: HP, Модель: 118

                Категория: Scanner
                S/n:1102, Вес: 3кг,Марка: HP, Модель: 588
                S/n:1104, Вес: 5кг,Марка: HP, Модель: 212
                S/n:1105, Вес: 1кг,Марка: HP, Модель: 512
        """
        res = f'{str(self.name)}\n'
        for key in self._data:
            res += f'Категория: {key}\n'
            for sn in self._data[key]:
                res += self._data[key][sn].__str__() + '\n'
            res += '\n'

        return res


class OfficeAutomation:
    def __init__(self, serial_number, weight, brand, model):
        self.serial_number = serial_number
        self.weigh = weight
        self.brand = brand
        self.model = model

    def __str__(self):
        return f'S/n:{self.serial_number}, Масса: {self.weigh}кг,Марка: {self.brand}, Модель: {self.model}'


class Printer(OfficeAutomation):
    def __init__(self, serial_number, weight, brand, model, is_color):
        super().__init__(serial_number, weight, brand, model)
        self.is_color = is_color
        self.type = 'Printer'

    def __str__(self):
        return f'{self.type}, S/n:{self.serial_number}, Масса: {self.weigh}кг,' \
               f'Марка: {self.brand}, Модель: {self.model}, Цветной: {self.is_color}'


class Scanner(OfficeAutomation):
    def __init__(self, serial_number, weight, brand, model, resolution):
        super().__init__(serial_number, weight, brand, model)
        self.resolution = resolution
        self.type = 'Scanner'


class Duplicator(OfficeAutomation):
    def __init__(self, serial_number, weight, brand, model, paper_format):
        super().__init__(serial_number, weight, brand, model)
        self.paper_format = paper_format
        self.type = 'Duplicator'


def main():
    wh = Warehouse('WHOFFICE1')
    pr1 = Printer(1101, 10, 'HP', '1010', False)
    sc1 = Scanner(1102, 3, 'HP', '588', 540)
    wh.recept_unit(pr1)
    wh.recept_unit(sc1)

    wh.recept_unit(Printer(1103, 3, 'HP', '118', True))
    wh.recept_unit(Scanner(1104, 5, 'HP', '212', 1540))
    wh.recept_unit(Scanner(1105, 1, 'HP', '512', 1200))
    print(wh)

    print(wh.delivery_unit('Prinxter'))
    print(pr1)
    print(*wh.delivery_unit('Printer'))
    print(wh.delivery_unit('Printer'))
    print(wh.delivery_unit('Printer'))

if __name__ == '__main__':
    main()
