# 1. Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.
# Пример:
# - 6 -> да
# - 7 -> да
# - 1 -> нет

print(" Type day of the week ")
day = int(input(('day-of-the-week:')))
print(day)
if 6<=day<=7 :
    print("yes")
elif 1<=day<=5:
    print("no")
else:
    print("error")

    
# 2. Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).
# Пример:
# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3

print("Type coordinates")
x = float(input(("x = ")))
y = float(input(("y = ")))
if (x == 0 or y == 0):
    print("you are out of quater")
elif (x > 0 and y > 0):
    print("1")
elif (x < 0 and y > 0):
    print("2")
elif (x < 0 and y < 0):
    print("3")
elif (x > 0 and y < 0):
    print("4")
else:
    print("WTF")
    
# 3. Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.
# Пример:
# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21

x1 = int(input("x1= "))
y1 = int(input("y1= "))
x2 = int(input("x2= "))
y2 = int(input("y2= "))

ac = (x1 - x2)**2
ab = (y1 - y2)**2
bc = (ab + ac)**0.5
print(f"distance = {bc} ")