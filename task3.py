# Дан файл вывести сумму всех чисел в файле. Цифры могут быть не целыми и отрицательными
from Read_Write_File import read_file as rf
from Read_Write_File import error_file
from Regular_pattern import pattern_numbers as pn

name_file_read_numbers = "./numbers.txt"
try:
    list_numbers = rf(name_file_read_numbers)
except FileNotFoundError:
    error_file(name_file_read_numbers)
else:
    numb = [pn(i) for i in list_numbers]
    clear_list_numbers = [float(j.lstrip('.')) for i in numb for j in i if j]
    print(sum(clear_list_numbers))
