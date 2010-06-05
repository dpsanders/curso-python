salida = open("hola.dat", "w")  # write = escribir

salida.write("Hola")

a =3 
salida.write( "a = " + str(a) )

b = -7.6e-1

salida.write("%d  %g " % (a, b) )	

salida.close()

T = 2.5
h = 0.1
L = 200

for T in [0.1, 0.2, 2.5, 2.6]:
	nombre = "ising_T%g_h%g_L%d.dat" % (T, h, L)
	salida = open(nombre, "w")
	salida.write("# Datos de Ising")
	salida.close()

#ising_T2.5_h0.1_L200.dat

