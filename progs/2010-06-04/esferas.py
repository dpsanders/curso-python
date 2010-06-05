from visual import *

lista_esferas = []

N = 100

for i in range(N):
	s = sphere()
	lista_esferas.append( s )
	
i = 0
for esfera in lista_esferas:
	#esfera.pos= cos(2.*pi*float(i)/N), sin(2*pi*float(i)/N), 0
	
	esfera.vel = vector(cos(2.*pi*float(i)/N), sin(2*pi*float(i)/N), 0)
	esfera.radius = 0.2
	#esfera.vel = esfera.pos
	i += 1
	
dt = 0.1
for t in range(1000):
	rate(100)
	for esfera in lista_esferas:
		esfera.pos += dt*esfera.vel
	
x

	#s = sphere()
	#lista_esferas.append( sphere() )
	
