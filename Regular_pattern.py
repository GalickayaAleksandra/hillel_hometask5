import re


def pattern_dates(text):
    pattern = '\d{2}-\d{2}-\d{4}'
    full_dates = re.findall(pattern, text)
    return full_dates


def pattern_years(text):
    pattern = '[1-9]{1}\d{3}'
    years = re.findall(pattern, text)
    return years


def pattern_numbers(text):
    pattern = '[-+]?\d*\.\d+|[-+]?\d+'
    numbers = re.findall(pattern, text)
    return numbers


def pattern_negative_numbers(text):
    pattern = '[-]\d*\.\d+|[-]\d+'
    numbers = re.findall(pattern, text)
    return numbers


def pattern_proper_names(text):
    pattern = '[А - Я][а - я]*'
    names = re.findall(pattern, text)
    return names
