""" Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
В расчете необходимо использовать формулу: (выработка в часах * ставка в час) + премия.
Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.
"""

import argparse
from sys import argv

def calculate_reward(hours, pay_in_hour, bonus=0):
    """ Функция рассчитывает зарплату

        Аргументами принимает выработку, ставку и премию, возвращает сумму к выплате
    """
    if bonus:
        return hours * pay_in_hour + bonus
    else:
        return hours * pay_in_hour


def main():

    parser = argparse.ArgumentParser(description='reward calculate')
    parser.add_argument('-th', action="store", dest="hours", type=float, required=True)
    parser.add_argument('-pih', dest="payment_in_hour", type=float, required=True)
    parser.add_argument('-b', dest="bonus", type=float)
    args = parser.parse_args()
    print(calculate_reward(args.hours, args.payment_in_hour, args.bonus))


if __name__ == '__main__':
    main()
