# 6. Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и
# наличие лекционных, практических и лабораторных занятий по этому предмету и их количество.
# Важно, чтобы для каждого предмета не обязательно были все типы занятий.
# Сформировать словарь, содержащий название предмета и общее количество занятий по нему.
# Вывести словарь на экран.
# Примеры строк файла:
# Информатика: 100(л) 50(пр) 20(лаб).
# Физика: 30(л) — 10(лаб)
# Физкультура: — 30(пр) —
#
# Пример словаря:
# {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}

def delNotNumb(line):
    i = 0
    numb = []
    while i < len(line):
        el = line[i]
        for elem in el:
            if elem == '0' or elem == '1' or elem == '2' or elem == '3' or elem == '4' or elem == '5' or elem == '6' or elem == '7' or elem == '8' or elem == '9':
                numb.append(elem)
        i += 1
        final_numb = ''.join(numb)
    return final_numb

def toSum(line):
    sum = 0
    for elem in line:
        if elem == '':
            continue
        else:
            elem = int(elem)
            sum = sum + elem

    return sum


subjects = {}
with open('file for task5_6.txt', 'r', encoding='utf-8') as file:
    while True:
        content = file.readline()
        print(content)

        if content == "":
            break
        else:
            lines = content.split(':')
            lines2 = lines[1].split()
            i = 0
            sum_my_numb = []
            while i < len(lines2):
                my_numb = delNotNumb(lines2[i])
                sum_my_numb.append(my_numb)
                i += 1
            summ = toSum(sum_my_numb)
            subjects[lines[0]] = summ
    print('_' * 50)
    print(subjects)


