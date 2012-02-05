import sys
from sympy import *

# exercises in page 31, answers in page 252

a = Symbol('a')
x = Symbol('x')
c = Symbol('c')
z = Symbol('z')
n = Symbol('n')
t = Symbol('t')

problems = {
	1: Derivative(a*x**3 + 6, x),
	2: Derivative(13*x**Rational(3, 2) - c, x),           
	3: Derivative(12*x**Rational(1, 2) + c ** Rational(1, 2), x),
	4: Derivative(c**Rational(1, 2) * x**Rational(1, 2), x),
	5: Derivative((a*z**n - 1) / c, z), # sympy solves n-1 putting one var below
	6: Derivative(Float(1.18)*t**2 + Float(22.4))
}

if __name__ == '__main__':
	p = int(sys.argv[1])
	if p in problems:
		print "Problem %d\t" % p, problems[p]
		print "Result    \t", problems[p].doit()
		print "Latex     \t", latex(problems[p].doit())


