# Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
# В рамках класса реализовать два метода. Первый, с декоратором @classmethod,
# должен извлекать число, месяц, год и преобразовывать их тип к типу «Число».
# Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
# Проверить работу полученной структуры на реальных данных.

class Date:
    def __init__(self, date_string):
        self.date_string = date_string

    @classmethod
    def date_to_int(cls, date_string):
        day = 0
        month = 0
        year = 0
        date_list = date_string.split('-')
        try:
            day = int(date_list[0])
            month = int(date_list[1])
            year = int(date_list[2])
        except (IndexError, ValueError) as err:  # Ожидаем IndexError и ValueError
            print(err, 'Date is incorrect')
        if len(date_list) != 3:
            print('Date is incorrect')
            return -1, -1, -1
        else:
            return day, month, year

    @staticmethod
    def is_valid_date(*args):
        if 1 < args[0] < 31 and 1 < args[1] < 12 and 1 < args[2] < 3000:
            return True
        else:
            return False


def main():
    d = Date('01-01-1111')
    day, month, year = Date.date_to_int('01-03-0101')
    print('01-03-0101', Date.is_valid_date(day, month, year))

    print('01-0f3-0101', Date.is_valid_date(*Date.date_to_int('01-0f3-0101')))

    print('01-030101', Date.is_valid_date(*Date.date_to_int('01-030101')))


if __name__ == '__main__':
    main()
