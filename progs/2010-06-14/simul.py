#T = raw_input("Dame la temp: ")
#h = raw_input("Dame el campo: ")

##print "T = ", T, "; h = ", h

from sys import argv, exit

#print "Argumentos: ", argv

try:
	T = float(argv[1])
	#h = float(argv[2])
	#print T, h
	#modelo = argv[3]

except:
	#print "OYE! Faltan args"
	#exit(1)
	T = 1
	h = 1
	modelo = 'ising'
	
print  "simul", 2*T
#, h, modelo