# Notepad

Начнём со списка требований которые должны были быть реализованы:
1. Хранить в памяти список людей двух типов
a. Сотрудники (фамилия (строка), имя (строка), год рождения (целое),
номер телефона (строка), менеджер (строка))
b. Менеджеры (фамилия (строка), имя (строка), год рождения (целое),
номер телефона (строка), название отдела (строка))
(Сделано, даже не коряво, но сотрудники должны разделяться знаком';')

2. Сохранять в файл / загружать из файла записи (автоматически, при запуске
программы и выходе из нее)
(Сделано)
3. Добавлять и удалять записи
(Не сделано)
4. Осуществлять поиск записей по фамилии, имени и номеру телефона
(Не сделано/ Наброски есть в файле 'Unused_func')
5. Сортировать записи по фамилии и году рождения
(Сделано)

Основные проблемы с которыми я стокнулся:
1. В течении почти 2 дней искал решение проблемы, при которой Pandas и CSV модули не могли вбить кириллицу в список (Ни одна из кодировок не помогла: cp1251, utf8, utf16(переводил но игнорировал пунктуацию делая разделение невозможным)
2. Причина по которой не смог реализовать проверку(наброски функции проверки опять же в файле) возраста в том, что вывод данной функции не позволял записать её в таблицу, так как выводил None
3. Я криворукий.
