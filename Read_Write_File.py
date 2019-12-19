import pickle


def read_file(name_file):
    with open(name_file, 'r', encoding='utf-8') as fln:
        text = fln.readlines()
    return text


def error_file(name_file):
    print('Файл отсутствует в директории')
    fl = open(name_file, 'w', encoding='utf-8')
    fl.close()
    print("Файл успешно создан. Заполните его данными и перезапустите программу.")


def add_file(name_file, text):
    with open(name_file, 'w', encoding='utf-8') as fln:
        fln.writelines(text)
