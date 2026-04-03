x = 0.68
r = round((x**3 + x - 1), 4)
print(r)

x = 0.69
r = round((x**3 + x - 1), 4)
print(r)

x = round(((1/3)*(1-0.68)**(-(2/3))), 1)
print(x)

print('----------------------------')

n = 3
x = 0.5
for i in range(n):
    x = round(((1 - x) ** (1/3)), 4)
    print(x)

print('----------------------------')

x = 0
r = -1
while r < 0:
    r = round((x**3 + x - 1), 4)
    print(r)
    x += 0.1