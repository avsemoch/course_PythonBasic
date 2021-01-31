#1. Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
# В расчете необходимо использовать формулу: (выработка в часах * ставка в час) + премия.
# Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.

from sys import argv

script_name, first_param, second_param, third_param = argv
first_param = int(first_param)
second_param = int(second_param)
third_param = int (third_param)

def salary(h, s, p):
    return (h * s) + p

#print("Имя скрипта: ", script_name)
print("Параметр 1 - выработка в часах: ", first_param)
print("Параметр 2 - ставка в час: ", second_param)
print("Параметр 3 - премия: ", third_param)

print('------')

print('Заработная плата сотрудника: ', salary(first_param, second_param, third_param))