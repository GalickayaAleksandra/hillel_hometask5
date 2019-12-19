# программа перевода числа из арабских цифр в число из римских цифр
def transform_arab_to_roman_numeral(number):
    roman_value = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    roman_char = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
    res = ''
    for i in range(len(roman_value)):
        while number >= roman_value[i]:
            number -= roman_value[i]
            res += roman_char[i]
    return res


my_number = int(input("Enter your arab number: "))
roman_numeral = transform_arab_to_roman_numeral(my_number)
print('number', my_number, 'equal to: ', roman_numeral)


# программа обратного перевода
def transform_roman_to_arab(roman_number):
    roman_char = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    res = 0
    for i in range(0, len(roman_number)):
        if i == 0 or roman_char[roman_number[i]] <= roman_char[roman_number[i - 1]]:
            res += roman_char[roman_number[i]]
        else:
            res += roman_char[roman_number[i]] - 2 * roman_char[roman_number[i - 1]]
    return res


my_number = input("Enter your roman number(example: 'XX'): ")
arab_numeral = transform_roman_to_arab(my_number)
print('Roman numeral', my_number, 'equal to: ', arab_numeral)
