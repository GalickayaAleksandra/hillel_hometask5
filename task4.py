# Написать генератор геометрической прогрессии
import math


def create_geomet_generator(b0, q, n):
    for n in range(1, n + 1):
        yield b0 * math.pow(q, n - 1)


first_term_gprogres = int(input("Введите первый член геометрической прогресси b0= "))
denominator = int(input("Введите знаменатель геометрической прогрессии q= "))
numb_term = int(input("Какое колличество членов геометрической прогрессии необходимо ввести? n= "))
for i in create_geomet_generator(first_term_gprogres, denominator, numb_term):
    print(i)
