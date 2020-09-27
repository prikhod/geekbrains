# Запросите у пользователя значения выручки и издержек фирмы. Определите, с каким финансовым результатом работает фирма
# (прибыль — выручка больше издержек, или убыток — издержки больше выручки). Выведите соответствующее сообщение.
# Если фирма отработала с прибылью, вычислите рентабельность выручки (соотношение прибыли к выручке).
# Далее запросите численность сотрудников фирмы и определите прибыль фирмы в расчете на одного сотрудника.

proceeds = int(input('Введите сумму выручки: '))
costs = int(input('Введите сумму издержек: '))

if proceeds > costs:
    print('Фирма работает с прибылью')
    print('Рентабельность составляет: ', (proceeds - costs)/proceeds)
    count_employee = int(input('Введите численность сотрудников фирмы: '))
    print('Прибыль на одного сотрудника составляет: ', (proceeds - costs) / count_employee)
else:
    print('Фирма работает с убытком')