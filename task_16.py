# Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N]. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

# *Пример:*   5        1 2 3 4 5 3 -> 1

print (' ----ОПРЕДЕЛЕНИЕ ПОВТОРЕНИЙ ЧИСЛА В СПИСКЕ ----   ', "\n")

import random
num = int (input ( 'Введите число элементов списка: '))
print()

array = list()

for i in range (0, num + 1):
    array.append (random.randint (0, num + 1))
print (f'Список : {array}',"\n")

number = int ( input ('Введите искомое число: '))
k = 0

for element in array:
    if element == number: 
        k += 1
print ()
if k > 0: 
    print (f' Число {number} повторяется в списке {k} раз(a)')
else : 
    print (f' Число {number} не встречается в списке')
    
# m = array.count (number)
# print (m)

# for t in range (num+1):
# array.append (int(input ()))
# print (array)
