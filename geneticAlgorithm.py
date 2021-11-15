import numpy as np
import re
import random
from random import randint
import matplotlib.pyplot as plt
# import salesmanGenerator

# Данные
# N = 10
# A = np.array([[0.00000000e+00, 5.87000000e+01, 1.13500000e+02, 9.75000000e+01, 2.11000000e+01, 9.26000000e+01,
#                8.17000000e+01, 7.06000000e+01, 5.47000000e+01, 8.85000000e+01],
#               [5.87000000e+01, 0.00000000e+00, 8.89000000e+01, 8.30000000e+01, 6.60000000e+01, 5.47000000e+01,
#                9.47000000e+01, 4.50000000e+01, 4.63000000e+01, 3.76000000e+01],
#               [1.13500000e+02, 8.89000000e+01, 0.00000000e+00, 2.07000000e+01, 1.01100000e+02, 3.68000000e+01,
#                6.23000000e+01, 4.64000000e+01, 5.89000000e+01, 6.15000000e+01],
#               [9.75000000e+01, 8.30000000e+01, 2.07000000e+01, 0.00000000e+00, 8.32000000e+01, 4.01000000e+01,
#                4.20000000e+01, 3.80000000e+01, 4.47000000e+01, 6.38000000e+01],
#               [2.11000000e+01, 6.60000000e+01, 1.01100000e+02, 8.32000000e+01, 0.00000000e+00, 8.66000000e+01,
#                6.18000000e+01, 6.33000000e+01, 4.51000000e+01, 8.83000000e+01],
#               [9.26000000e+01, 5.47000000e+01, 3.68000000e+01, 4.01000000e+01, 8.66000000e+01, 0.00000000e+00,
#                7.34000000e+01, 2.34000000e+01, 4.19000000e+01, 2.49000000e+01],
#               [8.17000000e+01, 9.47000000e+01, 6.23000000e+01, 4.20000000e+01, 6.18000000e+01, 7.34000000e+01,
#                0.00000000e+00, 5.77000000e+01, 4.85000000e+01, 9.15000000e+01],
#               [7.06000000e+01, 4.50000000e+01, 4.64000000e+01, 3.80000000e+01, 6.33000000e+01, 2.34000000e+01,
#                5.77000000e+01, 0.00000000e+00, 1.85000000e+01, 3.41000000e+01],
#               [5.47000000e+01, 4.63000000e+01, 5.89000000e+01, 4.47000000e+01, 4.51000000e+01, 4.19000000e+01,
#                4.85000000e+01, 1.85000000e+01, 0.00000000e+00, 4.92000000e+01],
#               [8.85000000e+01, 3.76000000e+01, 6.15000000e+01, 6.38000000e+01, 8.83000000e+01, 2.49000000e+01,
#                9.15000000e+01, 3.41000000e+01, 4.92000000e+01, 0.00000000e+00]])


# Матрица для 100 городов
N=100
A = np.loadtxt("100.txt").reshape(100, 100)
# print(A)

# TestData
Number = 7
Array = np.array([[0, 1, 2, 7, 6, 3, 1],
                  [1, 0, 1, 3, 6, 5, 3],
                  [2, 1, 0, 1, 3, 5, 6],
                  [7, 3, 1, 0, 1, 3, 6],
                  [6, 6, 3, 1, 0, 1, 4],
                  [3, 5, 5, 3, 1, 0, 1],
                  [1, 3, 6, 6, 4, 1, 0]])


# Задание 2
def convert_str_to_list(string):
    listnum = []
    for i in re.findall('[0-9][0-9]?', string):
        listnum.append(int(i))
    return listnum


def convert_list_to_str(lst):
    string = ''
    for i in range(len(lst)):
        if i != len(lst) - 1:
            string += str(lst[i]) + ' '
        else:
            string += str(lst[i])
    return string


# Функция полезности
def cost_function(a):
    num = convert_str_to_list(a)
    num.append(num[0])
    summa = 0
    for i in range(len(num)):
        try:
            summa += A[num[i] - 1][num[i + 1] - 1]
        except:
            break
    return summa


# Функция полезности для примера
def cost_fun(a):
    num = convert_str_to_list(a)
    num.append(num[0])
    summa = 0
    for i in range(len(num)):
        try:
            summa += Array[num[i] - 1][num[i + 1] - 1]
        except:
            break
    return summa


# path = "1 4 2 3 5 7 6"
# num = convert_str_to_list(path)
# print('__Функция полезности__')
# print('Стоимость пути', path, '=',  cost_fun(path), '\n')


# Функция мутации - Берем любой элемент списка и ставим его в любое место
def mutation(num):
    count = 0
    old_index = num.index(random.choice(num))
    num.insert(random.choice(num), num.pop(old_index))
    count = count + 1
    return num


# Функция динамической мутации
def mutation_d(num, itr):
    count = 0
    if itr > 0:
        mutation_count = round(num.__len__() / 2 ** itr)
        if mutation_count == 0:
            mutation_count = 1
        while count < mutation_count:
            old_index = num.index(random.choice(num))
            num.insert(random.choice(num), num.pop(old_index))
            count = count + 1
        # print(mutation_count)
    else:
        old_index = num.index(random.choice(num))
        num.insert(random.choice(num), num.pop(old_index))
    return num


# print('__Мутация__')
# print('Исходный путь', num)
# print('Мутировавший путь', mutation(num), '\n')


# Кроссинговер
def crossingover(path_x, path_y):
    num_x = convert_str_to_list(path_x)
    num_y = convert_str_to_list(path_y)
    newpath = []
    i = 0
    currentversh = 0
    while i < len(num_x):
        if (i + 1) % 2 == 1:
            if i == 0:
                firstelement = randint(0, len(num_x) - 2)
                newpath.append(num_x[firstelement])
                left = firstelement - 1
                right = firstelement + 1
                if firstelement < len(num_x) - 1:
                    leftsum = A[num_x[firstelement] - 1][num_x[firstelement - 1] - 1]
                    rightsum = A[num_x[firstelement] - 1][num_x[firstelement + 1] - 1]
                else:
                    leftsum = A[num_x[firstelement] - 1][num_x[firstelement - 1] - 1]
                    rightsum = A[num_x[firstelement] - 1][num_x[0]]
                if leftsum < rightsum:
                    newpath.append(num_x[left])
                else:
                    newpath.append(num_x[right])
                i += 1
            elif i == len(num_x) - 1:
                for j in range(len(num_x)):
                    if num_x[j] not in newpath:
                        newpath.append(num_x[j])
                i += 1
            else:
                elementindex = num_x.index(currentversh)
                for k in range(len(num_x)):
                    leftindx = (elementindex - (k + 1)) % len(num_x)
                    rightindx = (elementindex + (k + 1)) % len(num_x)
                    leftel = num_x[leftindx]
                    rightel = num_x[rightindx]
                    if (leftel not in newpath or rightel not in newpath):
                        break
                leftsum = A[currentversh - 1][leftel - 1]
                rightsum = A[currentversh - 1][rightel - 1]
                empty = 0
                if leftel in newpath:
                    empty = 1  # 1 если левый элемент уже есть
                if rightel in newpath:
                    empty = 2  # 2 если правый элемент уже есть

                if leftsum < rightsum and empty == 0:
                    newpath.append(num_x[leftindx])
                elif rightsum < leftsum and empty == 0:
                    newpath.append(num_x[rightindx])
                elif empty == 1:
                    newpath.append(num_x[rightindx])
                elif empty == 2:
                    newpath.append(num_x[leftindx])
                i += 1
        else:
            if i == len(num_y) - 1:
                for j in range(len(num_y)):
                    if num_y[j] not in newpath:
                        newpath.append(num_y[j])
                i += 1
            else:
                elementindex = num_y.index(currentversh)
                for k in range(len(num_y)):
                    leftindx = (elementindex - (k + 1)) % len(num_y)
                    rightindx = (elementindex + (k + 1)) % len(num_y)
                    leftel = num_y[leftindx]
                    rightel = num_y[rightindx]
                    if (leftel not in newpath or rightel not in newpath):
                        break
                leftsum = A[currentversh - 1][leftel - 1]
                rightsum = A[currentversh - 1][rightel - 1]
                empty = 0
                if leftel in newpath:
                    empty = 1  # 1 если левый элемент уже есть
                if rightel in newpath:
                    empty = 2  # 2 если правый элемент уже есть

                if leftsum < rightsum and empty == 0:
                    newpath.append(num_y[leftindx])
                elif rightsum < leftsum and empty == 0:
                    newpath.append(num_y[rightindx])
                elif empty == 1:
                    newpath.append(num_y[rightindx])
                elif empty == 2:
                    newpath.append(num_y[leftindx])
                i += 1
        currentversh = newpath[-1]
    return newpath


# Проверка функции кроссинговера
# x = "1 4 2 3 5 7 6"
# y = "6 3 5 4 2 1 7"
# print('__Кроссинговер__')
# print('Расстояние пути X', x, '=', cost_fun(x))
# print('Расстояние пути Y', y, '=', cost_fun(y))
# num_x = convert_str_to_list(x)
# num_y = convert_str_to_list(y)
# newpath = []
# i = 0
# currentversh = 0
# while i < len(num_x):
#     print(i + 1, '- й шаг')
#     # Выбор первого родителя
#     if (i + 1) % 2 == 1:
#         if i == 0:
#             # Случайным образом выбираем стартовую вершину в первом родителе
#             firstelement = randint(0, len(num_x) - 1)
#             # firstelement = 4
#             newpath.append(num_x[firstelement])
#             left = firstelement - 1
#             right = firstelement + 1
#             # Выбор одной из соседних вершин, лежащей ближе к текущей
#             if firstelement < len(num_x) - 1:
#                 leftsum = Array[num_x[firstelement] - 1][num_x[firstelement - 1] - 1]
#                 rightsum = Array[num_x[firstelement] - 1][num_x[firstelement + 1] - 1]
#             else:
#                 leftsum = Array[num_x[firstelement] - 1][num_x[firstelement - 1] - 1]
#                 rightsum = Array[num_x[firstelement] - 1][num_x[0]]
#             if leftsum < rightsum:
#                 newpath.append(num_x[left])
#             else:
#                 newpath.append(num_x[right])
#             i += 1
#         elif i == len(num_x) - 1:
#             for j in range(len(num_x)):
#                 if num_x[j] not in newpath:
#                     newpath.append(num_x[j])
#             i += 1
#         else:
#             elementindex = num_x.index(currentversh)
#             for k in range(len(num_x)):
#                 leftindx = (elementindex - (k + 1)) % len(num_x)
#                 rightindx = (elementindex + (k + 1)) % len(num_x)
#                 leftel = num_x[leftindx]
#                 rightel = num_x[rightindx]
#                 if (leftel not in newpath or rightel not in newpath):
#                     break
#             leftsum = Array[currentversh - 1][leftel - 1]
#             rightsum = Array[currentversh - 1][rightel - 1]
#             print('Текущий родитель', num_x)
#             print("Текущая вершина", currentversh)
#             print("Элемент слева", leftel, "Сумма слева", leftsum)
#             print("Элемент справа", rightel, "Сумма справа", rightsum)
#             empty = 0
#             if leftel in newpath:
#                 empty = 1  # 1 если левый элемент уже есть
#             if rightel in newpath:
#                 empty = 2  # 2 если правый элемент уже есть
#
#             if leftsum < rightsum and empty == 0:
#                 newpath.append(num_x[leftindx])
#             elif rightsum < leftsum and empty == 0:
#                 newpath.append(num_x[rightindx])
#             elif empty == 1:
#                 newpath.append(num_x[rightindx])
#             elif empty == 2:
#                 newpath.append(num_x[leftindx])
#             i += 1
#     # Выбор второго родителя
#     else:
#         if i == len(num_y) - 1:
#             for j in range(len(num_y)):
#                 if num_y[j] not in newpath:
#                     newpath.append(num_y[j])
#             i += 1
#         else:
#             elementindex = num_y.index(currentversh)
#             for k in range(len(num_y)):
#                 leftindx = (elementindex - (k + 1)) % len(num_y)
#                 rightindx = (elementindex + (k + 1)) % len(num_y)
#                 leftel = num_y[leftindx]
#                 rightel = num_y[rightindx]
#                 if (leftel not in newpath or rightel not in newpath):
#                     break
#             leftsum = Array[currentversh - 1][leftel - 1]
#             rightsum = Array[currentversh - 1][rightel - 1]
#             print('Текущий родитель', num_y)
#             print("Текущая вершина", currentversh)
#             print("Элемент слева", leftel, "Сумма слева", leftsum)
#             print("Элемент справа", rightel, "Сумма справа", rightsum)
#             empty = 0
#             if leftel in newpath:
#                 empty = 1  # 1 если левый элемент уже есть
#             if rightel in newpath:
#                 empty = 2  # 2 если правый элемент уже есть
#
#             if leftsum < rightsum and empty == 0:
#                 newpath.append(num_y[leftindx])
#             elif rightsum < leftsum and empty == 0:
#                 newpath.append(num_y[rightindx])
#             elif empty == 1:
#                 newpath.append(num_y[rightindx])
#             elif empty == 2:
#                 newpath.append(num_y[leftindx])
#             i += 1
#     currentversh = newpath[-1]
#     print('Новая вершина', currentversh)
#     print('Текущий путь', newpath)
#     print('------------------------')
# print('Расстояние для нового пути', cost_fun(convert_list_to_str(newpath)), '\n')

# Все вместе на больших данных
print('Генетический алгоритм')
x = convert_list_to_str(random.sample(range(1, 101), 100))
y = convert_list_to_str(random.sample(range(1, 101), 100))
itr = 0
bestpath = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
bestcost = 999999
xaxis = []
yaxis = []
while itr < 1000000:
    newpath = crossingover(x, y)
    newcost = cost_function(convert_list_to_str(newpath))
    xpath = x
    xcost = cost_function(convert_list_to_str(x))
    ypath = y
    ycost = cost_function(convert_list_to_str(y))
    if newcost < bestcost and newcost < xcost and newcost < ycost:
        bestpath = newpath
        bestcost = newcost
    elif xcost < bestcost and xcost < newcost and xcost < ycost:
        bestpath = xpath
        bestcost = xcost
    elif ycost < bestcost and ycost < xcost and ycost < newcost:
        bestpath = ypath
        bestcost = ycost
    x = convert_list_to_str(mutation(convert_str_to_list(x)))
    y = convert_list_to_str(mutation(convert_str_to_list(y)))
    # x = convert_list_to_str(mutation_d(convert_str_to_list(x), itr))
    # y = convert_list_to_str(mutation_d(convert_str_to_list(y), itr))
    xaxis.append(itr)
    yaxis.append(bestcost)
    itr += 1

print('Лучший путь =', bestpath, 'с результатом', bestcost)
plt.plot(xaxis, yaxis, '-')
plt.xlabel('Итерации')
plt.ylabel('Лучшее расстояние')
plt.title('График сравнения лучшего расстояния по итерациям')
plt.show()
