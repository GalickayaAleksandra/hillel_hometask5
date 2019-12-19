# Дан файл с текстом, создать список из дат в тексте - даты в формате DD-MM-YYYY (02-03-1999)
from Read_Write_File import read_file as rf
from Read_Write_File import error_file
from Regular_pattern import pattern_dates as pd

name_file_read = "./data.txt"
try:
    text = rf(name_file_read)
except FileNotFoundError:
    error_file(name_file_read)
else:
    list_dates = [pd(i) for i in text]
    clear_list_dates = [j for i in list_dates for j in i if j]
    print(clear_list_dates)
