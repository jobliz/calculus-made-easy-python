from sympy import *

"""
PDF Page 33, Chapter V, Example 11

Find, from first principles, the rate at which the following vary
with respect to a change in radius:

	(a) the circumference of a circle of radius r;
	(b) the area of a circle of radius r;
	(c) the lateral area of a cone of slant dimension l;
	(d) the volume of a cone of radius r and height h;
	(e) the area of a sphere of radius r;
	(f) the volume of a sphere of radius r.
"""

# Where does the area of a circle come from?
# http://www.worsleyschool.net/science/files/circle/area.html

# Yay, math for morons like us! =)
# http://library.thinkquest.org/20991/geo/solids.html

# The formula for (c)
# http://mathcentral.uregina.ca/QQ/database/QQ.09.06/h/michael2.html

pi          = Symbol('pi')
radius      = Symbol('r')
diameter    = Symbol('D')
slantheight = Symbol('l')
height      = Symbol('h')

CircleArea      = pi*radius**2
Circumference   = pi*diameter
Circumference2  = pi*radius*2
ConeArea        = pi*radius*slantheight + pi*radius**2
ConeVolume      = Rational(1, 3)*pi*radius**2*height
SphereArea      = 4*pi*radius**2
SphereVolume    = Rational(4, 3)*pi*radius**3
ConeLateralArea = pi * radius * slantheight

# (a) the circumference of a circle of radius r
pa = Derivative(Circumference2, radius).doit()         # tex:  2 \pi

# (b) the area of a circle of radius r;
pb = Derivative(CircleArea, radius).doit()             # tex:  2 \pi r

# (c) the lateral area of a cone of slant dimension l
pc = Derivative(ConeLateralArea, radius).doit()        # tex:  l \pi

# (d) the volume of a cone of radius r and height h
pd = Derivative(ConeVolume, radius).doit()             # tex:  2*h*pi*r/3

# (e) the area of a sphere of radius r
pe = Derivative(SphereArea, radius).doit()             # tex:  8 \pi r

# (f) the volume of a sphere of radius r
pf = Derivative(SphereVolume, radius).doit()           # tex:  4 \pi r^{2}
