#4. Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.

def translate(eng):
    dict_numb = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
    for eng_nub, rus_nub in dict_numb. items():
        if eng_nub == eng:
            return rus_nub


def addToFile(lines):
    with open('file for task5_4 (итог).txt', 'a', encoding='utf-8') as file:
        new_line = file.write(f'{lines}\n')



with open('file for task5_4 (исходный).txt', 'r', encoding='utf-8') as file_1:
    while True:
        content = file_1.readline()

        if content == '':
            break

        else:
            my_content = content.split()
            numb_eng = my_content[0]
            numb_rus = translate(numb_eng)
            my_content[0] = numb_rus
            new_content = ' '.join(my_content)
            addToFile(new_content)
            print(new_content)



