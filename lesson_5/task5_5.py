# 5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.

my_file = open('file for task5_5.txt', 'w', encoding='utf-8')
from_user = input('Введите набор чисел, разделенных пробелами: ')
content = my_file.write(f'{from_user}')
my_file.close()

with open('file for task5_5.txt', 'r', encoding='utf-8') as file:
    sum_content = sum(list(map(int, file.read().split())))

    print(sum_content)









