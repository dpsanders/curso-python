#log# Automatic Logger file. *** THIS MUST BE THE FIRST LINE ***
#log# DO NOT CHANGE THIS LINE OR THE TWO BELOW
#log# opts = Struct({'__allownew': True, 'logfile': 'mayavi_log.py', 'wthread': 1})
#log# args = []
#log# It is safe to make manual edits below here.
#log#-----------------------------------------------------------------------
_ip.magic("logstart mayavi_log.py")

_ip.magic("logstart mayavi_log.py")
z.series (x, 0, 10)
x,y, z = random.rand(3, 10)
from numpy import *
from numpy import *A
from numpy import *AA
x,y, z = random.rand(3, 10)
c = random.rand()
from enthought.mayavi import mlab
mlab.points3d(x, y, z, c)
x
y
z
c
c = random.rand(10)
mlab.points3d(x, y, z, c)
clf()
c
def V(x,y,z):
    return cos(
def V(x,y,z):
    return cos(10*x) + cos(10*y) + cos(10*z) + 2*(x**2+y**2+z**2)
X, Y, Z = mgrid[-2:2:100j, -2:2:100j, -2:2:100j]
X
V(X,Y,Z)
mlab.clf()
mlab.contour3d(X, Y, Z, V)
