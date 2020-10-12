# Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме:
# название, форма собственности, выручка, издержки.
# Пример строки файла: firm_1 ООО 10000 5000.
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
# Если фирма получила убытки, в расчет средней прибыли ее не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
# Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
# Пример json-объекта:
#
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
# Подсказка: использовать менеджеры контекста.

import json


def firm_analize(file_name):
    firm_list = []
    sum_profit = 0
    count_firm_in_average = 0
    with open(file_name, 'r') as f_obj:
        for string in f_obj:
            data = string.split()
            profit = int(data[2]) - int(data[3])
            firm_list.append({data[0]: profit})
            if profit > 0:
                count_firm_in_average += 1
                sum_profit += profit
    firm_list.append({'average_profit': sum_profit / count_firm_in_average})
    print(firm_list)
    with open("firm.json", "w") as write_f:
        json.dump(firm_list, write_f)


if __name__ == '__main__':
    firm_analize('5.7')
