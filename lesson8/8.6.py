# Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число», реализуйте перегрузку
# методов сложения и умножения комплексных чисел. Проверьте работу проекта, создав экземпляры класса (комплексные
# числа) и выполнив сложение и умножение созданных экземпляров. Проверьте корректность полученного результата.

class Complex:
    def __init__(self, re, im):
        self._re = re
        self._im = im

    def __add__(self, other):
        return Complex(self._re + other._re, self._im + other._im)

    def __mul__(self, other):
        return Complex(self._re * other._re -  self._im * other._im, self._re * other._im + self._im * other._re)

    def __str__(self):
        return f'({self._re}+{self._im}j)'


if __name__ == '__main__':

    d = 1+4j
    c = 4+5j
    print(d + c)
    print(c * d)

    d1 = Complex(1, 4)
    c1 = Complex(4, 5)

    print(c1 + d1)
    print(c1 * d1)

"""Результат
                (5+9j)
                (-16+21j)
                (5+9j)
                (-16+21j)
"""