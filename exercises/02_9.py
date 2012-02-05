from sympy import *

"""
PDF Page 32, Chapter V, Example 9

The frequency n of vibration of a string of diameter D, length L and specific 
gravity o, stretched with a force T, is given by:

[See book for a graphical depiction, this is the TeX representation]
\frac{\sqrt{\frac{T g}{o \pi}}}{D L}

Find the rate of change of the frequency when D, L, o and T are varied singly.
"""

D = Symbol('D')
L = Symbol('L')
o = Symbol('o')
T = Symbol('T')
g = Symbol('g')
pi = Symbol('pi')

# the formula
n = (1 / (D*L)) * ( ( (g*T) / (pi*o) ) ** Rational(1, 2) )

# when D varies
r1 = Derivative(n, D).doit() # -\frac{\sqrt{\frac{T g}{o \pi}}}{D^{2} L}

# when l varies
r2 = Derivative(n, L).doit() # -\frac{\sqrt{\frac{T g}{o \pi}}}{D L^{2}}

# Note: I am not sure of the next two outputs. TODO: Check it further.

# when o varies
r3 = Derivative(n, o).doit() # -\frac{\sqrt{\frac{T g}{o \pi}}}{2 D L o}

# when T varies
r4 = Derivative(n, T).doit() # \frac{\sqrt{\frac{T g}{o \pi}}}{2 D L T}
