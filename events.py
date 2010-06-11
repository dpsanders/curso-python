# -*- coding: utf-8 -*-
from pylab import *

def teclado(event):
	#print event.key
	#print event.xdata
	#print event.ydata
	print "Se tecleó %s en la posicion (%g, %g)" % (event.key, event.xdata, event.ydata)

def mouse(event):	
  if event.button != 1: 
    return
  x,y = event.xdata, event.ydata
  print "Se oprimió el botón izquierdo en (%g, %g)" % (x, y)

x = arange(10)
y = x*x
p, = plot(x, y)

show()

connect('button_press_event', mouse)
connect('key_press_event', teclado)