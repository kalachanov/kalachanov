import sympy

x = sympy.symbols('x')
F = x * sympy.log(x) - 1
xx = float(input('x0 = '))
i = 1
n = 1000

FF = sympy.diff(F, x)

print(F)
print(FF)

def function(fff):
    return xx - (float(F.subs({x: xx})) / float(FF.subs({x: xx})))    

for ifor in range(n):
    if (xx == round((function(xx)), 4)):
        break
    xx = round((function(xx)), 4)
    print('x', i, ' = ', xx)
    i += 1