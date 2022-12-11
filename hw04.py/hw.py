# 2. Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
#    "20" -> [2, 2, 5]

# n = int(input('natural number = '))
# a = []
# while not n % 2:
#         n = n/2
#         a.append(2)
# while not n % 3:
#         n = n/3
#         a.append(3)
# while not n % 5:
#         n = n/5
#         a.append(5)   
# while not n % 7:
#         n = n/7
#         a.append(7)
# print(a)

# 3. Задайте последовательность чисел. Напишите программу, которая выведет список 
#    неповторяющихся элементов исходной последовательности.
#    [1, 1, 2, 3, 4, 5, 5] -> [2, 3, 4]

# a = [1, 1, 2, 3, 4, 5, 5]
# b = []

# for j in range(0, len(a)):
#     c = 0
#     for i in range(0, len(a)):
#         if a[j] == a[i]:
#             c = c+1
#     if c == 1:
#         b.append(a[j])

# print(b)

# 4. Задана натуральная степень k. Сформировать случайным образом список коэффициентов
#    (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
#    Пример:
#    k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0



# k = 4

# while k > 0:
#     import random
#     x = random.randint(1, 50)
#     x = f'{x}X^{k} + '
#     data = open('/Users/nikitagaripov/Desktop/Python/HW/hw04.py/task4.txt', 'a')
#     data.writelines(x)
#     data.close()
#     k = k - 1

# import random
# x = random.randint(1, 50)
# x = f'{x}'
# data = open('/Users/nikitagaripov/Desktop/Python/HW/hw04.py/task4.txt', 'a')
# data.writelines(x)
# data.close()

# 5. Даны два файла, в каждом из которых находится запись многочлена.
#    Задача - сформировать файл, содержащий сумму многочленов.



Urovnenie_01 = '/Users/nikitagaripov/Desktop/Python/HW/hw04.py/task5_01.txt'
Urovnenie_02 = '/Users/nikitagaripov/Desktop/Python/HW/hw04.py/task5_02.txt'
Urovnenie_03 = '/Users/nikitagaripov/Desktop/Python/HW/hw04.py/task5_03.txt'
y = 10
while y > 0:
    with open (Urovnenie_01, 'r') as u1:
        numbers = u1.read()
        x_pos = -1
        for i in range(len(numbers)):
           if numbers[i] == 'x' and numbers[i+1] == '^' and numbers[i+2] == f'{y}':
            x_pos = i     
        if x_pos > 0:
            a = ''
            for i in range(0, x_pos):
               if numbers[i].isdigit():
                a = a + numbers[i]
               else:
                a = ''
        elif x_pos == 0:
            a = 1
        elif x_pos == -1:
            a = 0
        a = int(a)
    with open (Urovnenie_02, 'r') as u2:
        numbers = u2.read()
        x_pos = -1
        for i in range(len(numbers)):
            if numbers[i] == 'x' and numbers[i+1] == '^' and numbers[i+2] == f'{y}':
                x_pos = i     
        if x_pos > 0:
            b = ''
            for i in range(0, x_pos):
                if numbers[i].isdigit():
                    b = b + numbers[i]
                else:
                    b = ''
        elif x_pos == 0:
            b = 1
        elif x_pos == -1:
            b = 0
        b = int(b)
    c = a + b 
    if c > 0:
        with open (Urovnenie_03, 'a') as u3:
            u3.writelines(f'{c}x^{y} + ')
    y = y - 1

with open (Urovnenie_01, 'r') as u1:
    numbers = u1.read()
    for i in range(len(numbers)):
           if numbers[i] == '=':
            pos = i
    d = ''
    for i in range(0, pos - 1):
        if numbers[i].isdigit():
            d = d + numbers[i]
        else:
            d = ''
    d = int(d)
    print(d)

with open (Urovnenie_02, 'r') as u2:
    numbers = u2.read()
    for i in range(len(numbers)):
           if numbers[i] == '=':
            pos = i
    e = ''
    for i in range(0, pos - 1):
        if numbers[i].isdigit():
            e = e + numbers[i]
        else:
            e = ''
    e = int(e)
    print(e)
    
c = d + e 
with open (Urovnenie_03, 'a') as u3:
            u3.writelines(f'{c} = 0')








    

    # a = ''
    # for i in range(0, x_pos):
    #     if numbers[i].isdigit():
    #         a = a + numbers[i]
    #     else:
    #         a = ''
            
    # print(a)
# with open (Urovnenie_02, 'r') as u2:
#     numbers = u2.read()
#     for i in range(len(numbers)):
#         if numbers[i] == 'x':
#             x_pos = i
#     b = ''
#     for i in range(0, x_pos):
#         if numbers[i].isdigit():
#             b = b + numbers[i]
# b = int(b)
# x_1 = f'{a + b}x +'




# with open (Urovnenie_03, 'w') as u3:

#     u3.writelines(x_1)





