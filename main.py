from turtledemo.chaos import f


def Zadacha1():
    # Задайте список из нескольких чисел. Напишите программу,
    # которая найдёт сумму элементов списка, стоящих на нечётной позиции.
    # Пример: - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

    list = [2, 3, 5, 9, 3, 5, 4, 8]
    sum = 0
    i = 1
    while i < len(list):
        sum = sum + list[i]
        i += 2
    print(sum)


def Zadacha2():
    # Напишите программу, которая найдёт произведение пар чисел списка.
    # Парой считаем первый и последний элемент, второй и предпоследний и т.д.
    # Пример: - [2, 3, 4, 5, 6] => [12, 15, 16];
    #         - [2, 3, 5, 6] => [12, 15]

    list = [2, 3, 5, 9, 5, 4, 8]
    i = 0
    while i < len(list) / 2:
        result = list[i] * list[(len(list) - 1) - i]
        i += 1
        print(result)


def Zadacha3():
    # Задайте список из вещественных чисел. Напишите программу,
    # которая найдёт разницу между максимальным и минимальным
    # значением дробной части элементов.
    # Пример: - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

    list = [2.8, 3.2, 5.5, 8.6, 1.2, 4.7]
    list.sort()
    print(list)
    result = list[len(list) - 1] - list[0]
    print("%.2f" % result)


def Zadacha4():


# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
#
# Пример:  - 45 -> 101101
#           - 3 -> 11
#           - 2 -> 10


    n = int(input('Введите число: '))
    b = ''

    while n > 0:
        b = str(n % 2) + b
        n = n // 2
    print('Число', n, 'в двоичной системе', b)


# Zadacha1()
# Zadacha2()
# Zadacha3()
Zadacha4()
