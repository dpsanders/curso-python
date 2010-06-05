from mpmath import *  # PRECISION ARBITRARIA

# from math import *   PARA PRECISION NORMAL

#y = 25.
#x0 = 0.1

#x = x0

mp.dps = 1000

y = mpf('25.0')
x = mpf('10000')


for i in range(20):
	x_prima = 0.5 * ( x + (y / x) )
	#print x_prima
	print i,
	nprint(log10(x - 5.), 10)
	x = x_prima