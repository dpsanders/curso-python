# Python Scripting for Computational Science", 3a edicion 2008, Springer,
# H.P. Langtangen

from os import popen
from numpy import arange
# mejor: modulo 'subprocess'

gp = popen("gnuplot", "w")

gp.write("set term gif anim\n")
gp.write("set out 'sin.gif' \n ")
for a in arange(0.1, 10, 0.1):
	gp.write("plot sin(x+%g)\n" % a)
	
gp.write("set out")

gp.close()