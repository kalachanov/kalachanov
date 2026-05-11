import math

n = 100
n = int(input('n = '))
# e = float(input('e = '))
a = float(input('a = '))
b = float(input('b = '))
E = a - b
i = 1

def summa(s):
    return s**3-2*s**2+3*s-5

f1 = summa(a)
f2 = summa(b)
print('f1 = ',f1, ' f2 = ', f2)

if (f1 == f2):
    print('Корней нет')
else:
    for fi in range(n):
        c = round((a - summa(a) * ((b-a)/(summa(b) - summa(a)))), 4)
        F = round((summa(c)), 4)
        if (F < 0):
            a = c
        else:
            b = c
        E = round((b - a), 4)
        print('C', i,' = ', c, '[', a, ',', b, '] ', 'E', i,' = ', E)
        i += 1