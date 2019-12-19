# Дан файл с текстом, удалить из файла все отрицательные числа, числа могут быть не целыми

from Read_Write_File import read_file as rf
from Read_Write_File import add_file as af
from Regular_pattern import pattern_negative_numbers as pngn
from Read_Write_File import error_file

name_file_read_negative = "./numbers.txt"
name_file_write_without_negative = "./without_negative_numbers.txt"

try:
    list_negative_numbers = rf(name_file_read_negative)
except FileNotFoundError:
    error_file(name_file_read_negative)
else:
    sentence = [i.split(" ") for i in list_negative_numbers]
    for i in sentence:
        new_text = ""
        for j in i:
            if not pngn(j):
                new_text += j + " "
        af(name_file_write_without_negative, new_text)
