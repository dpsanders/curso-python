
#from numpy import *	
from pylab import *

def f(x):
	return -x

#x0 = 10

def harmonico(xvec):
	x, y = xvec
	return array([y, -x])

def pendulo(xvec):
	x, y = xvec
	return array([y, -sin(x)])
	

def euler(t, x, dt, f):
	return x + f(x) * dt
	
def rk2(t, x, dt, f):
	k1 = f(x)
	k2 = f(x + dt * k1/2.)
	return x + dt * k2

def mouse(evento):
	x0, y0 = evento.xdata, evento.ydata
	
	t, x = integrar([x0, y0], 0., 10., 0.1, pendulo, rk2)
	#t2, x2 = integrar(10, 0., 10., 0.1, f, rk2)
	x = array(x)
	#plot(x, 'o')
	plot(x[:,0], x[:,1], 'o')
	

def integrar(x0, t0, tf, dt, f, metodo):

	x = x0
	t = t0

	dt = 0.1

	datos_t = [t0]
	datos_x = [x0]


	#f = harmonico
	
	while t < tf:
		
		x_nuevo = metodo(t, x, dt, f)
		t += dt
		x = x_nuevo
		
		datos_t.append(t)
		datos_x.append(x)
		
	return datos_t, datos_x
		
	
#metodos = [euler, rk2]
metodos = [rk2]

for metodo in metodos:
	t, x = integrar([1,0], 0., 10., 0.1, pendulo, metodo)
	#t2, x2 = integrar(10, 0., 10., 0.1, f, rk2)
	x = array(x)
	#plot(x, 'o')
	plot(x[:,0], x[:,1], 'o')

connect('button_press_event', mouse)
