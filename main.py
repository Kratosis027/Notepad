import csv
import pandas as pd


manager_file = 'empl_base_managers.csv'
worker_file = 'empl_base_workers.csv'
EMPL_LIST = []


# choose next option for for the notepad to do, according the user choice
def user_input():
    note_action = input(f'Выберите нужное действие\nПоиск(П)/Сортировка(С)/Создание Списка(СП)\n')
    note_action = note_action.upper()
    if note_action == 'СОЗДАНИЕ СПИСКА' or note_action == 'СП':
        list_cr()
    if note_action == 'СОРТИРОВКА' or note_action == 'С':
        srt_list = input('В каком списке произовдим сортировку?\nМенеджеры(М)/Работники Отделов(О)\n')
        if srt_list.upper() == 'М' or srt_list.upper() == 'МЕНЕДЖЕРЫ':
            sort_file(manager_file)
        if srt_list.upper() == 'О' or srt_list.upper() == 'РАБОТНИКИ ОТДЕЛОВ':
            sort_file(worker_file)
    if note_action == 'ПОИСК' or note_action == 'П':
        print('Данная функция ещё не введена')
        user_input()
        # search_emp = input('Введите Фамилия, Имя или Номер телефона\n')
        # search_info(search_emp)
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
    if file_name == manager_file:
        position = 'Менеджер'
    else:
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
def sort_file(file):
    sort_opt = input('По каким критериями сортировать?\nФамилия/Год рождения:\n')
    sf = pd.read_csv(file, encoding='utf-8')
    sorted_list = sf.sort_values(sort_opt)
    print(sorted_list)


# decide what list should be created
def list_cr():
    ch_file = input('Выберите кого добавляем\nМендежер(М)/Работник отдела(О)\n')
    ch_file = ch_file.upper()
    try:
        if ch_file == 'О' or ch_file == 'РАБОТНИК ОТДЕЛА':
            emp_info = input('Введите данные работника: ')
            add_to_list(ass_ch(emp_info), worker_file)
        if ch_file == 'М' or ch_file == 'МЕНЕДЖЕР':
            emp_info = input('Введите данные работника: ')
            add_to_list(ass_ch(emp_info), manager_file)
    except IndexError:
        print('Данные введены не верным образом')
        list_cr()


# delete an inappropriate symbol of separation
def ass_ch(info):
    if info[-1] == ';':
        info = info[0:-1]
        return info
    else:
        return info


if __name__ == '__main__':
    read_file()
    user_input()


# Андреев,Андрей,1000,564897684,Менеджер;Олен,Сергей,1992,564897684,Менеджер;Гаара,Петр,1992,564897684,Менеджер;Псо,Анли,5643,6846163584,Отдел Продаж;
