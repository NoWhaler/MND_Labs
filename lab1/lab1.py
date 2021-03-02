import random

a0 = 1
a1 = 3
a2 = 2
a3 = 2

x1 = [random.randrange(1, 21, 1) for i in range(8)]
x2 = [random.randrange(1, 21, 1) for i in range(8)]
x3 = [random.randrange(1, 21, 1) for i in range(8)]
Y = [a0 + a1*x1[i] + a2*x2[i] + a3*x3[i] for i in range(8)]

x01 = (max(x1)+min(x1))/2
x02 = (max(x2)+min(x2))/2
x03 = (max(x3)+min(x3))/2

dx1 = x01 - min(x1)
dx2 = x02 - min(x2)
dx3 = x03 - min(x3)

xn1 = [(x1[i] - x01) / dx1 for i in range(8)]
xn2 = [(x2[i] - x02) / dx2 for i in range(8)]
xn3 = [(x3[i] - x03) / dx3 for i in range(8)]

Yet = a0 + a1*x01 + a2*x02 + a3*x03

k = 100
for i in range(8):
    if Y[i] > Yet and Y[i] < k:
        k = Y[i]

print("a0= %s a1= %s a2= %s a3= %s" % (a0, a1, a2, a3))
print("Список x1, x2, x3:")
print("X1: %s" % x1)
print("X2: %s" % x2)
print("X3: %s" % x3)
print("Y: %s" % Y)
print("Список x0:")
print("x0: %s %s %s" % (x01, x02, x03))
print("Список dx:")
print("dx: %s %s %s" % (dx1, dx2, dx3))
print("Список Xn1, Xn2, Xn3:")
print("Xn1: %s" % xn1)
print("Xn2: %s" % xn2)
print("Xn3: %s" % xn3)
print("Yэт: %s" % Yet)
print("Yэт<-: %s" % k)
