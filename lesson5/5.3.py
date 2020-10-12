# Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
# Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
# Выполнить подсчет средней величины дохода сотрудников.
from functools import reduce


def analize_employers(file_name):
    with open(file_name, 'r') as f_obj:
        num_employers = 0
        employers = {}
        for num_employers, str_employer in enumerate(f_obj, 1):
            employers.update({str_employer.split()[0]: float(str_employer.split()[1])})

        list_empl = list((item[0] for item in employers.items() if item[1] < 20000))
        print(f'Сотрудники, с зп меньше 20к:\n', '\n '.join(list_empl))
        sum_pay = reduce(lambda a, b: a + b, employers.values())
        print(f'Средняя зп сотрудников: {sum_pay / num_employers:.2f}')


if __name__ == '__main__':
    analize_employers('employers.txt')
