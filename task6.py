# Дан файл с текстом, вывести список который содержит все имена,
# все фамилии и все географические названия. Имена, Фамилии и Географические названии
# в простом формате, без дифисов.

from Read_Write_File import read_file as rf
from Read_Write_File import add_file as wf
from Read_Write_File import error_file
from Regular_pattern import pattern_proper_names as ppn


def cheekynew(line_text):
    if line_text != 0:
        return "\n"
    return ""


name_file_with_high_letters = "./text_with_high_letters.txt"
dict_proper_names = "./proper_names.txt"
try:
    list_with_high_letters = rf(name_file_with_high_letters)
except FileNotFoundError:
    error_file(name_file_with_high_letters)
else:
    sentences_form_file = [i.split(" ") for i in list_with_high_letters]
    list_for_proper_names = [k.split(" ") for j in sentences_form_file for k in j]
    proper_names = [j for i in list_for_proper_names for j in i if ppn(j)]
    print(proper_names)
    try:
        list_dict_proper_names = rf(dict_proper_names)
    except FileNotFoundError:
        error_file(dict_proper_names)
    else:
        clear_list_proper_names = list(map(str.strip, list_dict_proper_names))
        if clear_list_proper_names == []:
            line = 0
        else:
            line = 1
        true_proper_names = [i for i in proper_names if i in clear_list_proper_names]
        false_proper_names = [i for i in proper_names if i not in clear_list_proper_names]
        true_proper_names = list(dict.fromkeys(true_proper_names))
        false_proper_names = list(dict.fromkeys(false_proper_names))
        print(f"Эти имена точно являются именами собственными => {true_proper_names}")
        print(f"Этих имен нет в словаре собственных имён => {false_proper_names}")
        answear = input("Добавить новые имена в словарь? y/n: ")
        while answear != 'n':
            if answear == 'y':
                for i in false_proper_names:
                    answear = input(f"Добавить имя '{i}' в словарь? y/n: ")
                    if answear == 'y':
                        wf(dict_proper_names, cheekynew(line) + i)
