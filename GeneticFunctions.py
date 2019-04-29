import matplotlib.pyplot as plt
import numpy as np
import random
from sklearn.datasets.samples_generator import make_blobs


def f3(x, Y, c=0, a=0, b=0, d=0, e=0, f=0, a1=0, b1=0, d1=0, e1=0, f1=0):
    temp = []
    for y in np.nditer(Y):
        temp.append(
            0.001 * f1 * y ** 5 + 0.001 * e1 * y ** 4 + 0.001 * d1 * y ** 3 + 0.001 * a1 * y ** 2 + 0.001 * b1 * y + 0.001 * f * x ** 5 + 0.001 * e * x ** 4 + 0.001 * d * x ** 3 + 0.001 * a * x ** 2 + 0.001 * b * x + 0.01 * c)
    return temp


def f2(x, c=0, a=0, b=0, d=0, e=0, f=0):
    # return 0.001 * a * (x - 0.01 * q) ** 2 + 0.001 * b * (x - 0.01 * q) + 0.01 * c
    return 0.001 * f * x ** 5 + 0.001 * e * x ** 4 + 0.001 * d * x ** 3 + 0.001 * a * x ** 2 + 0.001 * b * x + 0.01 * c


def fitness(Z1, Z2, coef):
    fit = 0
    for z1, z2 in zip(Z1, Z2):
        if z1[1] > f2(z1[0], *coef):
            fit = fit + 1
        if z2[1] < f2(z2[0], *coef):
            fit = fit + 1
    return fit


def fitness3d(Z1, Z2, coef):
    fit = 0
    for z1, z2 in zip(Z1, Z2):
        if z1[2] > f3(z1[0], z1[1], coef[0], *coef[1], *coef[2]):
            fit = fit + 1
        if z2[2] < f3(z2[0], z2[1], coef[0], *coef[1], *coef[2]):
            fit = fit + 1
    return fit


def SelectionRoulette(list, x1, x2, dimension):
    fitList = []
    average = []
    probability = []
    sum = 0
    output = []
    n = 0
    max = 0
    for i in range(len(list)):
        if dimension == 2:
            fitList.append([fitness(x1, x2, list[i]), i])
            average.append(fitList[i][0])
        elif dimension == 3:
            fitList.append([fitness3d(x1, x2, list[i]), i])
            average.append(fitList[i][0])
    for i in fitList:
        sum = sum + i[0]
    for i in fitList:
        probability.append(i[0] / sum)
    while n * (n - 1) / 2 < len(list):
        n = n + 1
    indexes = np.random.choice(len(list), n, replace=False, p=probability)
    for i in indexes:
        output.append(list[i])
        if dimension == 2:
            if fitness(x1, x2, list[i]) > fitness(x1, x2, list[max]):
                max = i
        elif dimension == 3:
            if fitness3d(x1, x2, list[i]) > fitness3d(x1, x2, list[max]):
                max = i
    temp = 0
    if dimension == 2:
        temp = fitness(x1, x2, list[max])
    elif dimension == 3:
        temp = fitness3d(x1, x2, list[max])
    return output, (list[max], temp), np.average(average)

    #
    # return (list[fitList[0][1]], list[fitList[1][1]], list[fitList[2][1]], list[fitList[3][1]]), len(list), (
    # list[fitList[0][1]], fitList[0][0])


def SelectionTournament(list, x1, x2, dimension):
    fitList = []
    output = []
    average = []
    n = 0
    for i in range(len(list)):
        if dimension == 2:
            fitList.append([fitness(x1, x2, list[i]), i])
            average.append(fitList[i][0])
        elif dimension == 3:
            fitList.append([fitness3d(x1, x2, list[i]), i])
            average.append(fitList[i][0])
    while n * (n - 1) / 2 < len(list):
        n = n + 1
    indexes = np.random.choice(len(list), 2 * n, replace=False)
    indexes = np.sort(indexes)[::-1]
    for i in range(n):
        output.append(list[indexes[i]])
    temp = 0
    if dimension == 2:
        temp = fitness(x1, x2, output[0])
    elif dimension == 3:
        temp = fitness3d(x1, x2, output[0])
    return output, (list[0], temp), np.average(average)

    #
    # return (list[fitList[0][1]], list[fitList[1][1]], list[fitList[2][1]], list[fitList[3][1]]), len(list), (
    # list[fitList[0][1]], fitList[0][0])


def CrossOver(list, n, d):
    t = len(list) - 1
    temp = []
    while t > 0:
        for x in range(t):
            if len(temp) == n:
                break
            row = []
            if d == 2:
                for i in range(len(list[0])):  # number of coefficients
                    crossproduct = Cross(list[len(list) - t - 1][i], list[len(list) - t][i])
                    row.append(crossproduct)
            elif d == 3:
                temp1 = []
                crossproduct = Cross(list[len(list) - t - 1][0], list[len(list) - t][0])
                row.append(crossproduct)
                for i in range(len(list[0][1])):  # number of coefficients
                    crossproduct = Cross(list[len(list) - t - 1][1][i], list[len(list) - t][1][i])
                    temp1.append(crossproduct)
                row.append(temp1)
                temp1 = []
                for i in range(len(list[0][2])):  # number of coefficients
                    crossproduct = Cross(list[len(list) - t - 1][2][i], list[len(list) - t][2][i])
                    temp1.append(crossproduct)
                row.append(temp1)
            temp.append(row)
        t = t - 1
    return temp


def Cross(p1, p2):
    a = ''
    x = bin(abs(p1))
    y = bin(abs(p2))
    for i in range(min(len(x), len(y)) - 2):
        if x[min(len(x), len(y)) - i - 1] == y[min(len(x), len(y)) - i - 1]:
            a = a + x[min(len(x), len(y)) - i - 1]
        else:
            a = a + str(random.getrandbits(1))
    if len(x) > len(y):
        for i in range(len(x) - len(y)):
            if x[len(x) - len(y) + 1 - i] == '1':
                a = a + str(random.getrandbits(1))
            else:
                a = a + '0'
    elif len(x) < len(y):
        for i in range(len(y) - len(x)):
            if y[len(y) - len(x) + 1 - i] == '1':
                a = a + str(random.getrandbits(1))
            else:
                a = a + '0'
    a = a + 'b0'
    if p1 < 0 and p2 < 0:
        a = a + '-'
    elif p1 < 0 or p2 < 0:
        a = a + random.choice(['-', ''])
    output = int(a[::-1], 2)
    # if output > 2047:
    #     output = 2047
    # elif output < -2047:
    #     output = -2047
    return output


def Mutate(x):
    p = list(bin(x))
    if x < 0:
        temp = random.randint(3, len(p) - 1)
        if p[temp] == '1':
            p[temp] = '0'
        else:
            p[temp] = '1'
    else:
        temp = random.randint(2, len(p) - 1)
        if p[temp] == '1':
            p[temp] = '0'
        else:
            p[temp] = '1'
    return (int(''.join(p), 2))


def Mutation(list, percent, dim):
    for i in range(round(len(list) * percent / 100)):
        index = random.randint(0, len(list) - 1)
        temp = []
        if dim == 2:
            for c in range(len(list[0])):
                temp.append(Mutate(list[index][c]))
        elif dim == 3:
            temp1 = []
            temp.append(Mutate(list[index][0]))
            for c in range(len(list[0][2])):
                temp1.append(Mutate(list[index][2][c]))
            temp.append(temp1)
            temp1 = []
            for c in range(len(list[0][1])):
                temp1.append(Mutate(list[index][1][c]))
            temp.append(temp1)
        list[index] = temp
    return list


def BruteForce(x1, x2, x_degree):
    coef = []
    t = 0
    coef.append(random.randint(-400, 1500))
    for i in range(x_degree):
        coef.append(random.randint(-2047, 2047))
    while fitness(x1, x2, coef) != 200 and t < 10000:
        print(fitness(x1, x2, coef))
        coef[0] = random.randint(-400, 1500)
        for i in range(x_degree):
            coef[i] = random.randint(-2047, 2047)
        t = t + 1
    return coef, t
