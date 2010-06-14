from pylab import *

def mouse(evento):
	print "Boton ", evento.button
	print "en el lugar ", evento.xdata, evento.ydata
	
	x, y = evento.xdata, evento.ydata
	#plot(x, y, 'o')
	#axis([-5, 5, -5, 5])
	
	datos_x.append(x)
	datos_y.append(y)
	
	p.set_xdata(datos_x)
	p.set_ydata(datos_y)
	
	draw()

def teclado(evento):
	print "Tecla ", evento.key
	print "en el lugar ", evento.xdata, evento.ydata
	
	if evento.key == "r":
		datos_x.pop()
		datos_y.pop()
	
	p.set_xdata(datos_x)
	p.set_ydata(datos_y)
	
	draw()
		
	
datos_x = [0]
datos_y = [0]

p, = plot(datos_x, datos_y, 'o')
axis([-5, 5, -5, 5])

show()

connect('button_press_event', mouse)
connect('key_press_event', teclado)
