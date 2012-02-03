import sys
from sympy import *

# Exercises in age 24, answers in page 252

x = Symbol('x')
a = Symbol('a')
t = Symbol('t')
u = Symbol('u')
q = Symbol('q')
m = Symbol('m')
n = Symbol('n')

problems = {
	1:  Derivative((x**13), x),
	2:  Derivative(x ** Rational(-3, 2), x),          
	3:  Derivative(x ** (2 * a), x),                 
	4:  Derivative(t ** Float(2.4), t),                
	5:  Derivative(u ** Rational(1, 3)),               
	6:  Derivative((x ** -5) ** Rational(1, 3)),      
	7:  Derivative((1 / x**8) ** Rational(1, 5), x),   
	8:  Derivative((2*a*x)**(a-1), x),                 
	9:  Derivative((x**3) ** (1/q), x),              
	10: Derivative( (1/(x**m)) ** (1/n), x)           
}

if __name__ == '__main__':
	p = int(sys.argv[1])
	if p in problems:
		print "Problem %d\t" % p, problems[1]
		print "Result    \t", problems[1].doit()
		print "Latex     \t", latex(problems[1].doit())
