from sympy import *

# defining variables and  expressions
x = Symbol('x')
expr = x**3 + 4

# calculating dx
d = Derivative(expr, x)
r = d.doit() # builds the derivative result (3*x**2)

# calculating the value on some point
n1 = d.doit_numerically(5) # 75.0000000000000
n2 = r.subs(x, 5)          # 75
