# Пользователь вводит время в секундах. Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
# Используйте форматирование строк.


seconds = int(input('Введите время в секундах: '))
sec = seconds % 60
minutes = int(seconds / 60) % 60
hours = int(seconds / 3600)
print(f'Время в формате чч:мм:сс - {hours}:{minutes}:{sec}')
