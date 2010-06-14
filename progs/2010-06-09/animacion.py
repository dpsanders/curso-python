from pylab import *

x = arange(10)
y = x*x

ion()  #interactive "on"

p, = plot(x,y)
#show()
hold(False)

for a in arange(0, 10, 0.1):
	x = arange(10) + a
	#plot(x, y)
	p.set_xdata(x)
	draw()
	