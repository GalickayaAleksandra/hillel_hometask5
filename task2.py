# Пользователь вводит год в формате - YYYY (1999) Определить, является ли год високосным
from calendar import monthrange
from Regular_pattern import pattern_years as py

MONTH = 2
year = input("Введите год в формате YYYY (1999): ")
input_validation = py(year)
if input_validation:
    year_definition = monthrange(int(input_validation[0]), MONTH)
    if year_definition[1] == 28:
        print("Не высокосный год")
    else:
        print("Высокосный год")
else:
    print("Некорректный формат даты")
