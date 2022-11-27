# 1.Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример: - 0,56 -> 11

# text = input('enter number = ')
# text = text.replace(',', '' )
# text = list(text)
# # text = map(int, text)
# s = sum(text)
# print(s)

# 2.Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# Пример:
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

# n = int(input('enter n = '))
# for i in range(2, n):
#     m = 1
#     for j in range(2, i):
#         m *=j
#     print(m)

#     3.Задайте список из k чисел последовательности (1 + 1\k)^k и выведите на экран их сумму.

# k = int(input('enter k = '))
# list = []
# for i in range(1, k+1):
#     m = (1 + 1/i)**i
#     list.append(m)
# print(list)
# print(sum(list))

# 4.Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных пользователем через пробел позициях.

# k = int(input('enter k = '))
# list = []
# for i in range(-k, k+1):
#     print(i)
#     m = i
#     list.append(m)
# print(list)

# 5. Реализуйте алгоритм перемешивания списка.


# list = [1, 5, 6, 7]

# def mix(list):
#     x = len(list)
#     for j in range(0, x - 1):
#         n = list[j]
#         list[j]=list[j+1]
#         list [j+1] = n
#     print(list)

# # mix(list)


