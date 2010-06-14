

def f(t):
	c = cos(2 * pi * t)
	e = exp(-t)
	return c*e
	
t = arange(0, 5, 0.1)

subplot(221)   # renglones, columnas, cual de los reng*col
l = plot(t, f(t))
grid(True)
ylabel('Amortiguada')

subplot(222)
plot(t, cos(2*pi*t))
grid(True)
ylabel('No amortiguada')

subplot(223)   # renglones, columnas, cual de los reng*col
l = plot(t, f(t))
grid(True)
ylabel('Amortiguada')

subplot(224)
plot(t, cos(2*pi*t))
grid(True)
ylabel('No amortiguada')
