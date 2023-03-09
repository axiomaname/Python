"""Даны два неупорядоченных набора целых чисел (может быть, с повторениями). Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во элементов второго множества. Затем пользователь вводит сами элементы множеств."""
"""
def quic_sor(arr):
    if len(arr)<=1:
        return arr
    else:
        pivot=arr(0)
    less=[i for i in arr[1:] if i<=pivot]
    greater=[i for i in arr[1:]if i > pivot]
    return quic_sor(less)+[pivot]+quic_sor(greater)
list1=input("Введите элементы первого множества ").split()
list2=input("Введите элементы второго множества ").split()
listNew1=[]
listNew2=[]
listEnd=[]

for i in set(list1):
    listNew1.append(i)
listNew1=quic_sor(listNew1)
listNew2=quic_sor(listNew2)

for  i in range(len(listNew1)):
    for j in range(len(listNew2)):
        if listNew1[i] ==listNew2[j]:
            listEnd.append(listNew1[i])
print(listNew1)
print(listNew2)
print(quic_sor(listEnd))
"""

"""  В фермерском хозяйстве в Карелии выращивают чернику. Она растет на круглой грядке, причем кусты высажены только по окружности. Таким образом, у каждого куста есть ровно два соседних. Всего на грядке растет N кустов.
Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них выросло различное число ягод – на i-ом кусте выросло ai ягод.
В этом фермерском хозяйстве внедрена система автоматического сбора черники. Эта система состоит из управляющего модуля и нескольких собирающих модулей. Собирающий модуль за один заход, находясь непосредственно перед некоторым кустом, собирает ягоды с этого куста и с двух соседних с ним.
Напишите программу для нахождения максимального числа ягод, которое может собрать за один заход собирающий модуль, находясь перед некоторым кустом заданной во входном файле грядки."""

