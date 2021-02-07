# 3. Создать текстовый файл (не программно),
# построчно записать фамилии сотрудников и величину их окладов.
# Определить, кто из сотрудников имеет оклад менее 20 тыс.,
# вывести фамилии этих сотрудников.
# Выполнить подсчет средней величины дохода сотрудников.

import functools

my_file = open('file for task5_3.txt', 'r', encoding='utf-8')
i = 0
sum_sal = []


print('Зарплата менее 20 тыс руб:')
while True:
    content = my_file.readline()

    if content == '':
        break
    else:
        empl = content.split()
        sal = int(empl[1])
        if sal < 20000:
            print(empl[0], sal)
            i += 1
            sum_sal.append(sal)
        else:
            i += 1
            sum_sal.append(sal)
print()
average_sal = functools.reduce(lambda acc, x: acc + x, sum_sal) / i
print(f'Средняя зарплата - {average_sal}')
my_file.close()