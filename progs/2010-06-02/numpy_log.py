#log# Automatic Logger file. *** THIS MUST BE THE FIRST LINE ***
#log# DO NOT CHANGE THIS LINE OR THE TWO BELOW
#log# opts = Struct({'__allownew': True, 'logfile': 'numpy_log.py'})
#log# args = []
#log# It is safe to make manual edits below here.
#log#-----------------------------------------------------------------------
_ip.magic("logstart numpy_log.py")

from numpy import *(
from numpy import *
who 
#?who
_ip.magic("whos ")
who 
_ip.magic("who ")
v = [1, 2, 3]
type(v)
v = array( [1, 2, 3] )
v
v + v
#?v.conjugate
v
v.conjugate ()
2 * v
v * v
dot(v, v)
#?dot
v[2]
cross (v,v)
sin(v)
v + [1,2,3]
M = array( [ [2, 1], [1, 1] )
M = array( [ [2, 1], [1, 1] ] )
M
M = array( [ [2, 1], [5\, 1] ] )
M = array( [ [2, 1], [5, 1] ] )
M
M.transpose 
M.transpose()
M.T
#?M.T
r_ (1,2,3)
r_ [1,2,3]
c_ [1,2,3]
print(_)
a
v
a
v
list(v)
sqrt(dot(v,v))
linalg.norm (v)
linalg.norm (v)
linalg.eig(M)
fromfunction(?\)
#?fromfunction 
M
w
w = r_[1,2]
dot(M, w)
M * M
M
dot(M, M)
a = array([1,2,3])
dot(M, a)
a = array([1,2])
dot(M, a)
a = c_[1,2]
dot(M, a)
a
a
dot(a, r_[1,2])
dot(r_[1,2], a)
outer(r_[1,2], r_[3,4])
#?c_
