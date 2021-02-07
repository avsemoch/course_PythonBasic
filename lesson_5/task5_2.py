#2. Создать текстовый файл (не программно),
# сохранить в нем несколько строк, выполнить подсчет количества строк,
# количества слов в каждой строке


my_file1 = open('file for task5_2.txt', 'r', encoding='utf-8')
content = my_file1.readlines()
lines = len(content)
print(f'Количество строк - {lines}')
my_file1.close()
print('----')

my_file2 = open('file for task5_2.txt', 'r', encoding='utf-8')

i = 0
while i < lines:
    line = my_file2.readline()
    one_line = line.split()
    print(f'Кол-во слов в {i + 1} строке: {len(one_line)} --- {line} ')
    i += 1

my_file2.close()