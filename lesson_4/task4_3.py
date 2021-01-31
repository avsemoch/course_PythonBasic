#3. Для чисел в пределах от 20 до 240 найти числа, кратные 20 или 21. Необходимо решить задание в одну строку.
#Подсказка: использовать функцию range() и генератор


#первый вариант решение через списки
print([elem for elem in [elem for elem in range(20, 240)] if elem % 20 == 0 or elem % 21 == 0])


#второй вариант решение через filterfalse
from itertools import filterfalse
print(list(filterfalse(lambda elem: elem % 20 and elem % 21, range(20, 240))))
