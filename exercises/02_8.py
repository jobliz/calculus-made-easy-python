from sympy import *

"""
PDF Page 32, Chapter V, Example 8

It has been found that if c be the candle power of an incandescent 
electric lamp, and V be the voltage, c = aV**b, where a and b are constants.

Find the rate of change of the candle power with the voltage, and
calculate the change of candle power per volt at 80, 100 and 120 volts
in the case of a lamp for which a = 0.5 x 10**-10 and b = 6.
"""

c = Symbol('c')
a = Symbol('a')
V = Symbol('V')
b = Symbol('b')

# rate of change of the candle power with the voltage
expr = a*V**b
deriv = Derivative(expr, V).doit()

# lamp variable with given constants
lamp = deriv.subs(a, Float(0.5) * (10**-10)).subs(b, 6)

# candle power per volt at 80
r1 = lamp.subs(V, 80)  # 0.983040000000000

# candle power per volt at 100
r2 = lamp.subs(V, 100) # 3.00000000000000

# candle power per volt at 120
r2 = lamp.subs(V, 120) # 7.46496000000000

