# Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных.
# Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
# Подсказка: постарайтесь по возможности реализовать в проекте «Склад оргтехники» максимум возможностей,
# изученных на уроках по ООП.

from warehouse import Warehouse as WH, Printer as P, Scanner as S, Duplicator as D


class PrepareDevice(P, S, D):  # В наследовании нет необходимости, только для смысловой связи
    def __init__(self):
        pass

    @staticmethod
    def is_validate_device(serial_number, weight, brand, model):
        if \
                isinstance(serial_number, int) and\
                isinstance(weight, float) and\
                isinstance(brand, str) and\
                isinstance(model, str):
            return True

    @staticmethod
    def input_device():
        try:
            device_type = input('Введите тип устройста(str): ')
            serial_number = int(input('Введите серийный номер устройста(int): '))
            weight = float(input('Введите массу устройста(float): '))
            brand = input('Введите марку устройста(str): ')
            model = input('Введите модель устройста(str): ')

        except ValueError as err:
            print(err)
        else:
            if PrepareDevice.is_validate_device(serial_number, weight, brand, model):
                if device_type == 'Printer':
                    additional_option = input('Принтер цветной?(str): ')
                    p = P(serial_number, weight, brand, model, additional_option)
                    return p
                elif device_type == 'Scanner':
                    additional_option = input('Разрешение сканирования(str): ')
                    s = S(serial_number, weight, brand, model, additional_option)
                    return s
                elif device_type == 'Duplicator':
                    additional_option = input('Размер бумаги(str): ')
                    d = D(serial_number, weight, brand, model, additional_option)
                    return d
                else:
                    print('Нет такого типа устройств')


def main():
    stop = ''
    wh = WH('ValidatorTestWH')
    while stop != 'stop':
        p = PrepareDevice.input_device()
        wh.recept_unit(p)
        stop = input('Продолжить?')
    print(wh)
    '''
        ValidatorTestWH
        Категория: Printer
        Printer, S/n:143954, Масса: 6.0кг,Марка: HP, Модель: 1320, Цветной: no
        
        Категория: Scanner
        S/n:325425, Масса: 2.0кг,Марка: Canon, Модель: 324i
    у Printer своя реализация __str__(), у Scanner - наследованная
    '''


if __name__ == '__main__':
    main()
