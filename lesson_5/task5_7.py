# 7. Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме:
# название, форма собственности, выручка, издержки.
# Пример строки файла: firm_1 ООО 10000 5000.
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
# Если фирма получила убытки, в расчет средней прибыли ее не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями,
# а также словарь со средней прибылью. Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
# Пример json-объекта:
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
# Подсказка: использовать менеджеры контекста.

import json


with open('file for task5_7.txt', 'r', encoding='utf-8') as file:
    content = file.readlines()
    print(content)
    print('-----')

firm_count = len(content)
print(f'Количесвто фирм: {firm_count} ')

i = 0
sum_profit = 0
firm_profit = {}

while i < firm_count:
    list_firm = content[i].split()
    profit = int(list_firm[2]) - int(list_firm[3])
    if profit > 0:
        sum_profit = sum_profit + profit
    firm_profit[list_firm[0]] = profit
    i += 1

average_profit = {"average_profit": int(sum_profit / firm_count)}
firms = [firm_profit, average_profit]
print(firms)


with open("file json for task5_7.json", "w") as write_json:
    json.dump(firms, write_json)

