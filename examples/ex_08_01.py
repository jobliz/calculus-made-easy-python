from sympy import *

print("""
PDF Page 58, Chapter VIII, Example 1

A body moves so that the distance x (in feet), which it travels from a certain 
point O, is given by the relation x = 0.2*t**2 + 10.4, where t is the time in 
seconds elapsed since a certain instant. 

Find the velocity and acceleration 5 seconds after the body began to move, 
and also find the corresponding values when the distance covered is 100 feet.

Find also the average velocity during the first 10 seconds of its motion.
(Suppose distances and motion to the right to be positive.)
""")

print("\n\tThe first relation, as given in the problem\n")
t = Symbol('t')
f = Function('f')
x = Float(0.2)*t**2 + 10.4
pprint(x)

print("\n\tVelocity\n")
v = diff(x, t)
pprint(v)

print("\n\tAcceleration\n")
a = diff(v, t)
pprint(a)

print("\n\tWhen t = 0, x = 10.4 and v = 0\n")
print "x =", x.subs(t, 0)
print "v =", diff(v.subs(t, 0), t)

print("\n\tWhen t = 5, v = 0.4 x 5 = 2 ft./sec.; a = 0.4 ft./sec2.\n")
print "v = ", v.subs(t, 5)
print "a = ", a.subs(t, 5)

print("""\n\tWhen x = 100, 100 = 0.2t2 + 10.4, or t2 = 448,
\tand t = 21.17 sec.; v = 0.4 x 21.17 = 8.468 ft./sec.\n""")

# TODO: Rest of example


