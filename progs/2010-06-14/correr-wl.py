from sys import argv, exit
from os import system

try:
	Emin, Emax, L, traslape = map(int, argv[1:5])
except:
	print "Sintaxis: python correr-wl.py Emin Emax L traslape"
	exit(1)
	
abajo = Emin

while abajo < Emax:
	arriba = abajo + L
	comando = "python wl.py %d %d" % (abajo, arriba)
	system(comando)
	
	abajo = arriba - traslape