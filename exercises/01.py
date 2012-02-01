from sympy import *

# TODO: pprint gives some weird output, but futher testing with numerical
# values is necessary.

x = Symbol('x')
a = Symbol('a')
t = Symbol('t')
u = Symbol('u')
q = Symbol('q')
m = Symbol('m')
n = Symbol('n')

problems = [
	Derivative((x**13), x),                        # Ex. 1
	Derivative(x ** Rational(-3, 2), x),           # Ex. 2
	Derivative(x ** (2 * a), x),                   # Ex. 3       
	Derivative(t ** Float(2.4), t),                # Ex. 4
	Derivative(u ** Rational(1, 3)),               # Ex. 5
	Derivative((x ** -5) ** Rational(1, 3)),       # Ex. 6
	Derivative((1 / x**8) ** Rational(1, 5), x),   # Ex. 7
	Derivative((2*a*x)**(a-1), x),                 # Ex. 8
	Derivative((x**3) ** (1/q), x),                # Ex. 9
	Derivative( (1/(x**m)) ** (1/n), x)            # Ex. 10 
]

for n, p in enumerate(problems):
	print "Problem ", n + 1
	print ""
	pprint(p)
	print ""
	pprint(p.doit())
	print ""
