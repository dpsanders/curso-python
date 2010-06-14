from pylab import *

def calcular_campo(x, y, q, malla_X, malla_Y):
	"""Calcular campo de una carga q ubicada en (x,y),
	en la malla (malla_X, malla_Y)
	"""
	
	#desp = array([X-x, Y-y])
	desp_x = malla_X - x  # cpte x del desplazamiento de cada punto de la malla
	desp_y = malla_Y - y  # cpte x del desplazamiento de cada punto de la malla
	
	R = sqrt(desp_x*desp_x + desp_y*desp_y)
	
	Ex = q * desp_x / (R**3)
	Ey = q * desp_y / (R**3)
	
	V = q / R
	
	#distancia = sqrt(dot(desp, desp))
	#E = q * desp / (distancia**3)
	
	return (Ex, Ey, V)
	
	
def teclado(evento):
	if evento.key == "q":
		cargacarga = raw_input("Dame la carga: ")

a = linspace(-5, 5, 21)
b = linspace(-5, 5, 21)

X,Y = meshgrid(a, b)

x, y = 1.5, 0.5

cargas = [ [1.5, 1.5, 1], [-1.5, -1.5, -1] ]

Ex_total = zeros( X.shape, dtype='float')
Ey_total = zeros( X.shape, dtype='float')
V_total  = zeros( X.shape, dtype='float')

for carga in cargas:
	x, y, q = carga
	
	Ex, Ey, V = calcular_campo(x, y, q, X, Y)
	
	Ex_total += Ex
	Ey_total += Ey
	V_total += V


norm = sqrt(Ex_total*Ex_total + Ey_total*Ey_total)
Ex_total /= norm
Ey_total /= norm

#Ex = where(Ex < 1, Ex, 1)
#Ey = where(Ey < 1, Ey, 1)	

quiver(X, Y, Ex_total, Ey_total, norm, pivot='middle')

connect('key_press_event', teclado)

show()
