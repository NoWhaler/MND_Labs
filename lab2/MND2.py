import random as rand
import math

variant = 9
m = 10
y_max = (30 - variant) * 10
y_min = (20 - variant) * 10
x1_min, x1_max, x2_min, x2_max = -20, 15, -30, 45
xn = [[-1, -1], [1, -1], [-1, 1]]


def average_Y(list):
    avg_Y = []
    for i in range(len(list)):
        sum = 0
        for j in list[i]:
            sum += j
        avg_Y.append(sum / len(list[i]))
    return avg_Y


def dispersion(list):
    dispersion = []
    for i in range(len(list)):
        sum = 0
        for j in list[i]:
            sum += (j - average_Y(list)[i]) * (j - average_Y(list)[i])
        dispersion.append(sum / len(list[i]))
    return dispersion


def fuv(u, v):
    if u >= v:
        return u / v
    else:
        return v / u


def discriminant(x11, x12, x13, x21, x22, x23, x31, x32, x33):
    return x11 * x22 * x33 + x12 * x23 * x31 + x32 * x21 * x13 - x13 * x22 * x31 - x32 * x23 * x11 - x12 * x21 * x33


y = [[rand.randint(y_min, y_max) for j in range(6)] for i in range(3)]
avg_Y = average_Y(y)

sigmaTeta = math.sqrt((2 * (2 * m - 2)) / (m * (m - 4)))

Fuv = []
teta = []
Ruv = []

Fuv.append(fuv(dispersion(y)[0], dispersion(y)[1]))
Fuv.append(fuv(dispersion(y)[2], dispersion(y)[0]))
Fuv.append(fuv(dispersion(y)[2], dispersion(y)[1]))

teta.append(((m - 2) / m) * Fuv[0])
teta.append(((m - 2) / m) * Fuv[1])
teta.append(((m - 2) / m) * Fuv[2])

Ruv.append(abs(teta[0] - 1) / sigmaTeta)
Ruv.append(abs(teta[1] - 1) / sigmaTeta)
Ruv.append(abs(teta[2] - 1) / sigmaTeta)

# коефіцієнт для 0.90
Rkr = 2.29

for i in range(len(Ruv)):
    if Ruv[i] > Rkr:
        print('Помилка, повторіть експеримент')

mx1 = (xn[0][0] + xn[1][0] + xn[2][0]) / 3
mx2 = (xn[0][1] + xn[1][1] + xn[2][1]) / 3
my = (avg_Y[0] + avg_Y[1] + avg_Y[2]) / 3

# коефіцієнти регресії
a1 = (xn[0][0] ** 2 + xn[1][0] ** 2 + xn[2][0] ** 2) / 3
a2 = (xn[0][0] * xn[0][1] + xn[1][0] * xn[1][1] + xn[2][0] * xn[2][1]) / 3
a3 = (xn[0][1] ** 2 + xn[1][1] ** 2 + xn[2][1] ** 2) / 3
a11 = (xn[0][0] * avg_Y[0] + xn[1][0] * avg_Y[1] + xn[2][0] * avg_Y[2]) / 3
a22 = (xn[0][1] * avg_Y[0] + xn[1][1] * avg_Y[1] + xn[2][1] * avg_Y[2]) / 3

# метод Крамера
b0 = discriminant(my, mx1, mx2, a11, a1, a2, a22, a2, a3) / discriminant(1, mx1, mx2, mx1, a1, a2, mx2, a2, a3)
b1 = discriminant(1, my, mx2, mx1, a11, a2, mx2, a22, a3) / discriminant(1, mx1, mx2, mx1, a1, a2, mx2, a2, a3)
b2 = discriminant(1, mx1, my, mx1, a1, a11, mx2, a2, a22) / discriminant(1, mx1, mx2, mx1, a1, a2, mx2, a2, a3)

# практична лінійна регресія
y_pr1 = b0 + b1 * xn[0][0] + b2 * xn[0][1]
y_pr2 = b0 + b1 * xn[1][0] + b2 * xn[1][1]
y_pr3 = b0 + b1 * xn[2][0] + b2 * xn[2][1]

# фактори
dx1 = abs(x1_max - x1_min) / 2
dx2 = abs(x2_max - x2_min) / 2
x10 = (x1_max + x1_min) / 2
x20 = (x2_max + x2_min) / 2

# натуралізовані коефіцієнти
a0 = b0 - (b1 * x10 / dx1) - (b2 * x20 / dx2)
a1 = b1 / dx1
a2 = b2 / dx2

# натуралізоване рівняння регресії
yP1 = a0 + a1 * x1_min + a2 * x2_min
yP2 = a0 + a1 * x1_max + a2 * x2_min
yP3 = a0 + a1 * x1_min + a2 * x2_max

print('Матриця планування для m =', m)
for i in range(3):
    print(y[i])
print('Експериментальні значення критерію Романовського:')
for i in range(3):
    print(Ruv[i])

print('Натуралізовані коефіцієнти: \na0 =', round(a0, 4), 'a1 =', round(a1, 4), 'a2 =', round(a2, 4))
print('У практичний ', round(y_pr1, 4), round(y_pr2, 4), round(y_pr3, 4),
        '\nУ середній', round(avg_Y[0], 4), round(avg_Y[1], 4), round(avg_Y[2], 4))
print('У практичний норм.', round(yP1, 4), round(yP2, 4), round(yP3, 4))
