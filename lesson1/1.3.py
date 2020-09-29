# Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn. Например, пользователь ввёл число 2.
# Считаем 2 + 22 + 222 = 246.

double_count = 3
string_number = input('Введите число: ')
number = int(string_number) + int(string_number*2) + int(string_number*3)
print(number)

i = 0
number = 0

while i < double_count:
    i += 1
    number = number + int(string_number*i)
print(number)

number = 0
i = 0
for i in range(1, 4):
    number = number + int(string_number*i)
print(number)
