from sympy import *

"""
PDF Page 32, Chapter V, Example 7

If lt and l0 be the lengths of a rod of iron at the temperatures
t Centigrades. and 0 Centigrades. respectively, then lt = l0 (1+0.000012t). 
Find the change of length of the rod per degree Centigrade.
"""

l0 = Symbol('l0')
lt = Symbol('lt')
t = Symbol('t')

expr = l0*(1+Float(0.000012)*t)
result = Derivative(expr, t).doit()  # 1.2e-5*l0

