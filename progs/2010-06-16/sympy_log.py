#log# Automatic Logger file. *** THIS MUST BE THE FIRST LINE ***
#log# DO NOT CHANGE THIS LINE OR THE TWO BELOW
#log# opts = Struct({'__allownew': True, 'logfile': 'sympy_log.py', 'pylab': 1})
#log# args = []
#log# It is safe to make manual edits below here.
#log#-----------------------------------------------------------------------
_ip.magic("logstart sympy_log.py")

from sympy import *
x
x, y, z = symbols('xyz')
x 
x = symbols('y')
x 
x, y, z = symbols('xyz')
x 
x + x
#?symbols
jamon = symbols('jamon')
jamon
jamon = symbols('jamon ')
jamon 
jamon + jamon
x 
y 
z 
z = x + y
z = z*z
z 
z.expand ()
z = x*x + 2*x + 1
z 
z = (1+x)**2
z = x*x + 2*x + 1
z == (1+x)**2
(1+x)**2
z == ( (1+x)**2 ).expand()
z 
z.coeff (x**2)
z.subs(x, 1)
limit(sin(x) / x, x, 0)
limit(2 - 1/ x, x, 0)
oo 
limit(2 - 1/x, x, oo)
diff(sin(2*x), x)
diff(sin(2*x), x, 3)
cos(x).series(x, 0, 10)
z = cos(x) + sin(x)
z.series (x, 0, 10)
(cos(x) + sin(x)).series()
(cos(x) + sin(x)).series(x, 10)
#?z.series 
#?normal
integrate(log(x), x)
x 
x.__repr__ 
#?x.__repr__
x.__repr__()
x.__str__()
type(x)
#?x.__add__?
