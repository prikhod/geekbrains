# Пользователь вводит целое положительное число. Найдите самую большую цифру в числе. Для решения используйте цикл
# while и арифметические операции.


string_number = input('Введите целое положительное число: ')
i = 0
max_digit = 0

while i < len(string_number):
    if int(string_number[i]) > max_digit:
        max_digit = int(string_number[i])
    i += 1

print('Максимальная цифра в числе: ', max_digit)
