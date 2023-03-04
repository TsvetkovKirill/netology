# -*- coding: utf-8 -*-
documents = [
    {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
    {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
    {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
]

directories = {
    '1': ['2207 876234', '11-2'],
    '2': ['10006'],
    '3': []
}
def get_name():
    number = input('Введите номер документа ')
    for data in documents:
        if data.get("number") == number:
            return data.get('name')
    return 'Документ с таким номером отсутствует.'


def get_shelf():
    number = input('Введите номер документа ')
    for key in directories:
        if number in directories.get(key):
            return key
    return 'На полках нет документа с таким номером.'


def get_list(docs):
    for doc in docs:
        print(f'{doc.get("type")} {doc.get("number")} {doc.get("name")}')
    return

def add_doc():
    shelf_number = input('Введите номер полки, куда положить документ. ')
    if shelf_number not in directories:
        return 'Полки с таким номером нет'
    doc = {}
    for info in ('type', 'number', 'name'):
        doc[info] = input(f'{info}: ')
    documents.append(doc)
    directories.get(shelf_number).append(doc['number'])
    return 'Документ добавлен на полку'

# Функция add_doc немного не доработана. Во-первых, у вас отсутствует строка кода, которая добавит документ в каталог.
# Во-вторых, нельзя сохранять результат работы метода append в переменную, т.к. данный метод всегда возвращает None.
# Из строки кода, которая добавляет номер документа на полку, нужно удалить эту часть directories[shelf] =

# – add – команда, которая добавит новый документ в каталог и в перечень полок, спросив его номер, тип,
# имя владельца и номер полки, на котором он будет храниться.
# Корректно обработайте ситуацию, когда пользователь будет пытаться добавить документ на несуществующую полку.


while True:
    print('Допустимые команды: p, s, l, a')
    comand = input('Введите команду ')

    if comand == 'p':
        print(get_name())

    elif comand == 's':
        print(get_shelf())

    elif comand == 'l':
        get_list(documents)

    elif comand == 'a':
        print(add_doc())

