x = float(2.5)
a = [0, 1, 2, 3, 4]

def f0(s):
    return ((x-a[0])/(s-a[0]))
def f1(s):
    return ((x-a[1])/(s-a[1]))
def f2(s):
    return ((x-a[2])/(s-a[2]))
def f3(s):
    return ((x-a[3])/(s-a[3]))
def f4(s):
    return ((x-a[4])/(s-a[4]))

for i in range(5):
    if i == 0:
        L = f1(a[i]) * f2(a[i]) * f3(a[i]) * f4(a[i])
    if i == 1:
        L = f0(a[i]) * f2(a[i]) * f3(a[i]) * f4(a[i])
    if i == 2:
        L = f0(a[i]) * f1(a[i]) * f3(a[i]) * f4(a[i])
    if i == 3:
        L = f0(a[i]) * f1(a[i]) * f2(a[i]) * f4(a[i])
    if i == 4:
        L = f0(a[i]) * f1(a[i]) * f2(a[i]) * f3(a[i])
    print('L', i, '=', L)