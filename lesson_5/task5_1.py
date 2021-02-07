# 1. Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных свидетельствует пустая строка.

my_file = open('file for task5_1.txt', 'w', encoding='utf-8')
from_user = 0
while from_user != '':
    from_user = input('Введите данные. Для записи нажмите Enter. Для завершения введите пустую строку: ')
    content = my_file.writelines(f'{from_user}\n')
my_file.close()