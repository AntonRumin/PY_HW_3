# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

#*Пример:* 5    1 2 3 4 5    6 -> 5

print (' --- НАХОЖДЕНИЕ БЛИЖАЙШЕГО ЭЛЕМЕНТА --- ')

from random import randint

array = list()
length = int ( input ( 'Введите длину списка: '))
for i in range (length+1):
    array.append (randint(0, length+1))
print (array)

num = int ( input ('Введите число: '))
distance = array[0]
for element in array:
    if abs(num - element) < abs (num - distance):
        distance = element 


print (distance)


