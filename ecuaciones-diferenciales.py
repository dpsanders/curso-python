
# Codigo para implementar los distintos metodos para la tarea 2
# Las funciones euler etc. funcionan de manera **igual** para ecuaciones
# de orden superior si utilizamos *vectores*

from pylab import *		# para graficas


	
def euler_completo(x0, t_final, dt, f):
	lista_t  = []
	lista_x = []
	
	x = x0
	t = 0.
	
	while t < t_final+dt:		# para incluir t_final
		lista_t.append(t)
		lista_x.append(x)
		
		x += dt * f(x,t)
		t += dt
		
	return lista_t, lista_x
	
	
def rk2_completo(x0, t_final, h, f):			# aqui se decidio utilizar h en lugar de dt para el incremento
	lista_t  = []
	lista_x = []
	
	x = x0
	t = 0.
	
	while t < t_final+h:		# para incluir t_final
		lista_t.append(t)
		lista_x.append(x)
		
		k1 = f(x,t)
		k2 = f(x + 0.5*h*k1, t+0.5*h)
	
		x += h * k2
		t += h
		
	return lista_t, lista_x
	
	
def rk4_completo(x0, t_final, h, f):
	lista_t  = []
	lista_x = []
	
	x = x0
	t = 0.
	
	while t < t_final+h:		# para incluir t_final
		lista_t.append(t)
		lista_x.append(x)
		
		k1 = f(x,t)
		k2 = f(x + 0.5*h*k1, t+0.5*h)
		k3 = f(x + 0.5*h*k2, t+0.5*h)
		k4 = f(x + h*k3, t+h)
		
		x += h/6. * (k1 + 2.*k2 + 2.*k3 + k4)
		t += h
		
	return lista_t, lista_x
	
	
# Dado que las funciones euler, rk2 y rk4 son tan similares, podemos extraer la parte comun, tal que
# hay una sola funcion ' integrar' , y los metodos nada mas hacen un paso, regresando el estimado
# de la derivada segun el metodo, como sigue:


def euler(x, t, h, f):
	
	return f(x,t)
	
def rk2(x, t, h, f):
	k1 = f(x,t)
	k2 = f(x + 0.5*dt*k1, t+0.5*dt)
	
	return k2
	
def rk4(x, t, h, f):
	k1 = f(x,t)
	k2 = f(x + 0.5*h*k1, t+0.5*h)
	k3 = f(x + 0.5*h*k2, t+0.5*h)
	k4 = f(x + h*k3, t+h)
		
	return (k1 + 2.*k2 + 2.*k3 + k4) / 6.
	

def integrar_1er_orden(x0, t_final, h, f, metodo):		
	# metodo es el metodo que utilizar, que estima la derivada
	lista_t  = []
	lista_x = []
	
	x = x0
	t = 0.
	
	while t < t_final+h:		# para incluir t_final
		lista_t.append(t)
		lista_x.append(x)
	
		derivada = metodo(x, t, h, f)
		
		x += h * derivada
		t += h
	
	return lista_t, lista_x

	
	
	
# Hasta ahora, nada mas hemos *definido* las funciones,
# es decir, le hemos dicho a la maquina como se *implementa* 
# el metodo de Euler etc.

# Pero no le hemos dicho que *ejecute* (corra) ninguna funcion
# Para hacerlo, tenemos que *llamar* a la funcion como sigue

# Tampoco hemos definido ninguna funcion que se integrara:

def logistica(x,t):
	return x*(5. - x)
	


# Las variables que definimos aqui son *independientes* de las que 
# hay adentro de las funciones euler etc.

dt = 0.2
t_final = 5
x0 = 0.1

t, x = euler_completo(x0, t_final, dt, logistica)		
# utiliza ' logistica'  como la f dentro de euler, y guarda el resultado en t y x
# esta es la primera linea en el programa que realmente *hace* algo (aparte de las definiciones de las variables)
plot(t, x, 'bo-', label='euler')
show()

t, x = rk2_completo(x0, t_final, dt, logistica)		
plot(t, x, 'go-', label='RK2')
show()

t, x = rk4_completo(x0, t_final, dt, logistica)		
plot(t, x, 'ro-', label='RK4')
show()


# Para no repitir tanto, podemos hacer algo mas listo:
metodos = [euler, rk2, rk4]		# una lista de los metodos que queremos utilizar

f = figure()		# crear nueva figura

for metodo in metodos:		# iterar por la lista
	t, x = integrar_1er_orden(x0, t_final, dt, logistica, metodo)			# integrar con este metodo
	plot(t, x, 'o-', label=metodo.__name__)		# cualquier funcion f tiene f.__name__, que es el nombre de la funcion
	show()
	
legend()			# mostrar la leyenda del plot


# Pregunta 3:
# Las funciones definidas *no tienen que cambiar*!!
# Utilizamos vectores

# Ecuaciones
# x' = y
# y' = -omega^2 * x

# En vectores:
# x' = f(x)
# f(x) = (y, -omega^2*x)

omega = 1.
omega_cuadrado = omega*omega   # para no tener que hacer la multiplicacion cada vez

def harmonico(x_vec, t):
	# tratar x_vec como vector!
	xx, yy = x_vec   # separar sus componentes
	#  Alternativa:  x, y = x_vec[0], x_vec[1]
	
	return array([yy, -omega_cuadrado*xx])		# regresamos un arreglo (vector) para poder utilizarlo en calculos
	
	

def integrar(x0, t_final, h, f, metodo):		# funciona nada mas para arreglos
	# metodo es el metodo que utilizar, que estima la derivada
	lista_t  = []
	lista_x = []
	
	x = x0
	t = 0.
	
	while t < t_final+h:		# para incluir t_final
		lista_t.append(t)
		lista_x.append(x.copy())			
		# x.copy() hace una copia de x como una lista
		# si no hacemos esto, entonces los elementos "cambian" cuando x cambia!
		
		# una alternativa es  lista_x.append(list(x)) -- agrega una version de x como lista
		
		derivada = metodo(x, t, h, f)
		
		x += h * derivada
		t += h
	
	return lista_t, lista_x

# Crear una nueva figura:
f = figure(figsize=(8,8)) 		# figsize cambia el tamano / forma de la figura -- aqui es cuadrada 

x0 = array([1., 0.])
t_final = 10.
dt = 0.1


metodos = [euler, rk2, rk4]		# una lista de los metodos que queremos utilizar

for metodo in metodos:		
	t, x = integrar(x0, t_final, dt, harmonico, metodo)		
	x = array(x)		# convertir la lista de listas en un arreglo para poder extraer componentes:
	
	plot(x[:,0], x[:,1], 'o-', label=metodo.__name__)		
	show()
		
legend()			# mostrar la leyenda del plot
	
