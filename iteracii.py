import math

E = 0.001
x = 0.5
a = 1
i = 1

for ifor in range(100):
    x = round((math.cos(x)), 4)
    if ((math.fabs(x - a)) < E):
        break
    else:
        print(x, ' ', i)
        a = x
    i += 1