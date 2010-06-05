entrada = open("distancia.dat", "r")  # read = leer

#lineas = entrada.readlines()

#for linea in lineas:
	#datos = []
	#for palabra in linea.split():
		#datos.append( float(palabra) )
	#print datos

for linea in entrada:
	datos = map(float, linea.split() )
	print datos
	
