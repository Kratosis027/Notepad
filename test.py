import csv
import pandas as pd


manager_file = 'empl_base_managers.csv'
worker_file = 'empl_base_workers.csv'
EMPL_LIST = []


# choose next option for for the notepad to do, according the user choice
def user_input():
    note_action = input(f'Выберите нужное вам действие\nПоиск(П)/Сортировка(С)/Создание Списка(СП)\n')
    note_action = note_action.upper()
    if note_action == 'СОЗДАНИЕ СПИСКА' or note_action == 'СП':
        ch_file = input('Выберите кого добавляем\nМендежер(М)/Работник отдела(О)\n')
        ch_file = ch_file.upper()
        if ch_file == 'О' or ch_file == 'РАБОТНИК ОТДЕЛА':
            file_name = worker_file
            emp_info = input('Введите данные работника: ')
            add_to_list(emp_info, file_name)
        if ch_file == 'М' or ch_file == 'МЕНЕДЖЕР':
            file_name = manager_file
            emp_info = input('Введите данные работника: ')
            add_to_list(emp_info, file_name)
    if note_action == 'СОРТИРОВКА' or note_action == 'С':
        print(sort_file())
    if note_action == 'ПОИСК' or note_action == 'П':
        print('Данная функция ещё не введена')
        #search_emp = input('Введите Фамилия, Имя или Номер телефона\n')
        #search_info(search_emp)
    else:
        user_input()


# add a list of employees to the list
def add_to_list(number_persons, file_name):
    persons = number_persons
    if len(persons.split(';')) > 1:
        add_list = persons.split(';')
        for i in add_list:
            employee_info(i, file_name)
        print(f'Все работники теперь полностью зарегестрированы')
    else:
        employee_info(persons, file_name)
    read_file()


# divide one position in the list into name,surname,birth date,phone number and position
def employee_info(info, file_name):
    one_person = info.split(',')
    name = one_person[1].strip(' ')
    surname = one_person[0].strip(' ')
    birth_date = one_person[2].strip(' ')
    phone_number = one_person[3].strip(' ')
    try:
        position = one_person[4].strip(' ')
    except IndexError:
        position = input(f'Введите должность {name} {surname}: ')
    EMPL_LIST.append({
        'Фамилия': f'{name}',
        'Имя': f'{surname}',
        'Год рождения': f'{birth_date}',
        'Номер телефона': f'{phone_number}',
        'Должность': f'{position}'
        })
    save_file(EMPL_LIST, file_name)


# save the file in notepad's folder
def save_file(emp_list, file):
    with open(file, 'w', encoding='UTF-8', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Фамилия', 'Имя', 'Год рождения', 'Номер телефона', 'Должность'])
        for position in emp_list:
            writer.writerow([position['Имя'], position['Фамилия'], position['Год рождения'], position['Номер телефона'], position['Должность']])


# read the content of the file
def read_file():
    try:
        rfm = pd.read_csv(manager_file, encoding='utf-8')
        print(rfm)
    except FileNotFoundError:
        print("Файл со списком менеджеров ещё не создан")
    try:
        rfe = pd.read_csv(worker_file, encoding='utf-8')
        print(rfe)
    except FileNotFoundError:
        print("Файл со списком работников ещё не создан")


# sort the content of the file
def sort_file():
    sort_opt = input('По каким критериями сортировать?\nФамилия/Год рождения:\n')
    sf = pd.read_csv(manager_file, encoding='utf-8')
    sorted_list = sf.sort_values(sort_opt)
    return sorted_list




read_file()
user_input()


# Андреев,Андрей,1000,564897684,Менеджер;Олен,Сергей,1992,564897684,Менеджер;Гаара,Петр,1992,564897684,Менеджер;
# Псо,Анли,5643,6846163584,Отдел Продаж;
