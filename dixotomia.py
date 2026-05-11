import math

n = 100
n = int(input('n = '))
E = float(1)
e = 0
# e = float(input('e = '))
a = float(input('a = '))
b = float(input('b = '))

def summa(s):
    return s**3-2*s**2+3*s-5

f1 = summa(a)
f2 = summa(b)
print('f1 = ',f1, ' f2 = ', f2)

if (f1 == f2):
    print('Корней нет')
else:
    for i in range(n):
        c = round(((a+b)/2), 4)
        F = round((summa(c)), 4)
        if (F < 0):
            a = c
        else:
            b = c
        E = round((b - a), 4)
        print('x', i,' = ', c, ' F(x', i, ') = ', F, '[', a, ',', b, '] ', 'E', i,' = ', E)
        i += 1
        if (E < e):
            break