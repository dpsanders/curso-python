#log# Automatic Logger file. *** THIS MUST BE THE FIRST LINE ***
#log# DO NOT CHANGE THIS LINE OR THE TWO BELOW
#log# opts = Struct({'__allownew': True, 'logfile': 'estructuras_control.py'})
#log# args = []
#log# It is safe to make manual edits below here.
#log#-----------------------------------------------------------------------
_ip.magic("logstart estructuras_control.py")

a = 3
if a < 5:
    print "a es pequeno"
    a = 2 * a
a = 6
if a < 5:
print("a es pequeno")
    a = 2 * a
if a < 5:
print("a es pequeno")
      a = 2 * a
if a < 5:
    print "a es pequeno"
    a *= 2
    
a
	
_ip.magic("run if.py ")
a = 5
_ip.magic("run if.py ")
_ip.magic("run -I if.py ")
_ip.magic("run -i if.py ")
a = 5
_ip.magic("run if.py")
_ip.magic("run -i if.py ")
a = 10
_ip.magic("run -i if.py ")
a = 010
a = -10
_ip.magic("run -i if.py ")
_ip.magic("pwd ")
_ip.magic("cd ..")
_ip.magic("cd 2010-06-02/ ")
_ip.system("ls")
_ip.system("less if.py")
a = 1
b = 10
if a>0 and b>0:
    print "2 pos"
    
if not a>0:
    print "nopositivo"{
if not a>0:
print("nopositivo"\)
if not a>0:
print("nopositivo"\)
if not a>0:
print("nopositivo")
if not a>0:
    print "nonpos"
    
_ip.magic("run -i if.py ")
_ip.magic("run -i if.py ")
datos = raw_input("Dame ")
datos
i = 0
while i < 10:
    print i
    
while i < 10:
print(i)
while i < 10:
print(i)
while i < 10:
    print i
    i += 1
    
i
_ip.magic("run -i while.py ")
_ip.magic("run -i while.py ")
_ip.magic("run -i while.py ")
l = [1, 3, 17, -100]
for i in l:
    print i
    
for i in l:
    print 2*i
    
l = [1, 2, 7.5, "hola", [3, 4], 1+3j]
l.
l
l[4]
for i in l:
    print i
    
l[4]
l[4][2]
l[4][1]
l[4][0]
l[4, 0]
from numpy import *
a = array([1,2,17])\
for i in a:
    print i
    
M = array([1,2,3,5]).reshape(2,2)
M]
M
for i in M:
    print i
    
M
M[0]
for i in M:\
for i in M:
    for j in i:
        print i, j
        
M
M + M
range(10000)
range(10)
for i in range(10):
    print i
    
for i in range(10000):
    print i
    
resultado = 1
for i in range(100):
    resultado *= i
    
resultado 
resultado = 1
for i in range(1, 101):
    resultado *= i\
    
resultado \
from math import *
factorial (100)
#?factorial ?
#?time 
_ip.magic("time factorial (100)")
factorial (100)
_ip.magic("time factorial (10000)")
factorial (10000)
_ip.magic("time run factorial.py")
_ip.magic("run factorial.py")
float( factorial(100) )
float( factorial(1000) )
#?range 
range(3, 10, 2)
#?xrange
for i in xrange(10000000):
    pass
_ip.magic("time for in xrange(1e7): pass")
for in xrange(1e7): pass
_ip.magic("time for in xrange(10000000): pass")
for in xrange(10000000): pass
_ip.magic(r"time for in xrange(10000000): \_"[:-1])
for in xrange(10000000): \
_ip.magic("time for in xrange(10000000):")
for in xrange(10000000):
_ip.magic("time for i in xrange(10000000):")
for i in xrange(10000000):
_ip.magic("time for i in xrange(10000000): pass")
for i in xrange(10000000): pass
_ip.magic("time for i in range(10000000): pass")
for i in range(10000000): pass
l = range(10000000)
def f(x):
    return x*x
f(10)
f(10.)
f("hola")
def g(x): return 2*x
g("hola")
def h(x, y):
    return 2*x, 3*y
h(10, "hola")
def f(x):
    return [x, x*x, x**3]
f(10)
def f(x):
    """Esta es la descrip[cion de fn f que regresa potencias
    Puedo segiur por varias lienas
    """
    return [x,x**2, x**10]
f(100
)
#?f
s = """Una cadena
Que se extiende
por 
bla
"""
s
