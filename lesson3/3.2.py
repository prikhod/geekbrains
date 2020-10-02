# Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
# имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы.
# Реализовать вывод данных о пользователе одной строкой.


def person_profile(name='', surname='', birth='', city='', email='', phone='', print_info=False):
    summary_info = f'Имя: {name}, Фамилия: {surname}, Год рождения: ' \
                   f'{birth}, Город проживания: {city}, Email: {email}, Телефон: {phone}'
    if print_info:          # еще один аргумент - вызывать или нет печать из самой функции, по умолчанию выключена
        print(summary_info)

    return summary_info


def main():
    print(person_profile(surname='Иван', name='Иванов', birth='1961', city='Бобруйск',
                         email='ivan@ivanov.com', phone='+7979797999', print_info=False))


if __name__ == '__main__':
    main()
