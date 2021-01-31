# 7. Реализовать генератор с помощью функции с ключевым словом yield, создающим очередное значение.
# При вызове функции должен создаваться объект-генератор.
# Функция должна вызываться следующим образом: for el in fact(n).
# Функция отвечает за получение факториала числа,
# а в цикле необходимо выводить только первые n чисел, начиная с 1! и до n!.
# Подсказка: факториал числа n — произведение чисел от 1 до n.
# Например, факториал четырёх 4! = 1 * 2 * 3 * 4 = 24.

n = int(input('Введите число: '))
def fact(n):

    while True:
        m = n
        n = n - 1
        if n != 0:
            yield m
        else:
            yield 1
            break

my_fact = []
for elem in fact(n):
    print(elem)
    my_fact.append(elem)


from functools import reduce

fact_value = reduce(lambda acc, x: acc * x, my_fact)
print(f'Факториал равен: {fact_value}')