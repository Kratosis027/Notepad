# def date_check(age, name, surname):
#    ags = age
#    try:
#        if int(ags) >= 2005 or int(ags) <= 1890:
#            ags = input(f'Введите год рождения {name} {surname} корректно: ')
#            date_check(ags, name, surname)
#       else:
#           return str(ags)
#    except ValueError:
#        ags = input(f'Введите год рождения {name} {surname} корректно: ')
#        date_check(ags, name, surname)


# search the info in the list
# def search_info(target):
#    excel_files = ['empl_base_managers.csv', 'empl_base_workers.csv']
#    for individual_excel_file in excel_files:
#        df = pd.read_csv(individual_excel_file)
#        programmers = df['Имя'].where(df['Имя'] == target).dropna()
#        print(programmers)
