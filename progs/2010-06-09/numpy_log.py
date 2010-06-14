#log# Automatic Logger file. *** THIS MUST BE THE FIRST LINE ***
#log# DO NOT CHANGE THIS LINE OR THE TWO BELOW
#log# opts = Struct({'__allownew': True, 'logfile': 'numpy_log.py', 'pylab': 1})
#log# args = []
#log# It is safe to make manual edits below here.
#log#-----------------------------------------------------------------------
plot(x, x*x)

_ip.magic("logstart numpy_log.py")

x = arange(10)
plot(x, x*x)
_ip.system("acroread cuad.pdf ")
savefig("cuad.pdf")
_ip.system("acroread cuad.pdf ")
xlabel("x")
ylabel("f(x)")
title("Una grafica de sumo interes")
plot(x, 2*x)
f = figure()
#?figure
plot(x, 3*x)
plot(x, 3*x, 'o')
figure(2)
plot(x, 3*x, 'o')
figure(1)
plot(x, 5*x, 'o')
figure(2)
plot(x, 6*x, 'o')
#?plot
plot(x, 7*x, 'ko', linewidth=3, markersize=5)
plot(x, 7*x, 'ko-, linewidth=3, markersize=5)
plot(x, 7*x, 'ko-', linewidth=3, markersize=5)
plot(x, 7*x, 'ko-', linewidth=3, markersize=10)
#?plot
plot(x, 7*x, 'ko-', linewidth=3, markersize=10, markercolor=blue)
plot(x, 7*x, 'ko-', linewidth=3, markersize=10, markercolor="blue")
#?PLOT
#?plot
plot(x, 7*x, 'ko-', linewidth=3, markersize=10, markerfacecolor="blue")
clf()
p = plot(x, 7*x, 'ko-', linewidth=3, markersize=10, markerfacecolor="blue")
p
p[0]
p[0].remove()
draw()
p, = plot(x, 7*x, 'ko-', linewidth=3, markersize=10, markerfacecolor="blue")
p
p.remove()
plot(x)
plot(x, 2*x, x, 3*x)\
p, q = plot(x, 4*x, x, 5*x)\
p
q
p.remove()
draw()
ax = gca()
#?gca
_ip.system("cat > datos.dat")
clf()
X = loadtxt ("datos.dat")
X
X.reshape(8)
plot(X)
clf()
plot(X[:,0], X[:,1])
clf()
plot(X[:,0], X[:,1], 'x')
plot(X[:,0], X[:,1], 'x', markersize=10)
plot(X[:,0], X[:,1], 'x', markersize=10, clip=False)
#?plot
plot(X[:,0], X[:,1], 'x', markersize=10, clip_on = False
)
plot(X[:,0], X[:,1], 'kx', markersize=20, clip_on = False
)
#?loadtxt
_ip.system("vim datos.dat ")
X = loadtxt ("datos.dat", comments="#")
X
X = loadtxt ("datos.dat")
Z
X
#?loadtxt
x, y  = loadtxt ("datos.dat", unpack=True)
x
y
loadtxt ("datos.dat", unpack=True)
plot(x, y, 'o')
f = figure(figsize=(8,8))
plot(x, y, 'o')
a = arange(1000)
a
clf()
plot(a, a**(-0.5))
clf()
loglog(a, a**(-0.5))
a = arange(1, ]1000)
a = arange(1, \1000)
a = arange(1, 000)
a = arange(1, 1000)
loglog(a, a**(-0.5))
a**(-0.5)
y = a**(-0.5)
clf()
loglog(a, y)
clf()
semilogx(a,y)
semilogy(a,y)
clf()
semilogy(a,y)
hold(False)
plot(x, x*2)
plot(x, x*3)
plot(x, x*10)
hold(True)
plot(x, x*10)
plot(x, x*3)
xlabel("$\exp(x)+x^2 + \sqrt(67)")
xlabel("$\exp(x)+x^2 + \sqrt(67)$")
xlabel("$\exp(x)+x^2$")
clf()
xlabel("$\exp(x)+x^2$")
hold(True
hold(False)
hold(True)
plot(x)
figure()
plot(x)
xlabel("$\exp(x)+x^2$")
xlabel("$\exp(x)+x^2$", fontsize=16)
xlabel("$\exp(x)+x^2$", fontsize=24)
text(1.5, 2, "y=x+z / \sqrt{7}")
text(1.5, 2, "$y=x+z / \sqrt{7}$")
t = text(.5, 2, "$y=x+z / \sqrt{7}$")
t.remove()
draw()
_ip.magic("run migraf.py ")
clf()
_ip.magic("run migraf.py ")
show()
clf()
_ip.magic("run oscilacion.py ")
_ip.magic("run oscilacion.py ")
show()
_ip.magic("run oscilacion.py ")
_ip.magic("run -i  oscilacion.py ")
show()
#?subplot
_ip.magic("run animacion.py ")
_ip.magic("run animacion.py ")
_ip.magic("run animacion.py ")
p, = plot(x)
p
p.set_xdata (x+5)
draw()
_ip.magic("run animacion.py ")
clf()
x = randn(1000000)
x
#?randn
#?normal
#?randn
X
x
hist(x, 100)
#?hist
M = rand(1000)
M = M+M.T
valores_propios = eigvalsh(M)
M = rand(1000, 10000)
M = rand(1000, 10000)
M = rand(1000, 1000)
M = M+M.T
valores_propios = eigvalsh(M)
valores_propios.sort()
clf()
plot(valores_propios)
plot(valores_propios, 'o')
valores_propios = valores_propios [:-1]
clf()
plot(valores_propios, 'o')
dif = valores_propios[1:] - valores_propios[:-1]
clf()
plot(dif)
clf()
hist(dif, 100)
clf)(
clf()
hist(dif, 100, normed=False)
clf()
hist(dif, 100, normed=True)
#?quiver
a = r_[-5:5:11j]
a
b = r_[-5:5:11j]
a
b
X, Y = meshgrid(a, b)
clf()
quiver(X, Y, X, Y)
X
clf()
quiver(X, Y, Y, X)
#?quiver
quiver(X, Y, Y, X, pivot='middle')
a
b
X
Y
zip(X, Y)
X
x = 0.5
y = 0.56
y = 0.5
X - x
Y - y
_ip.magic("run campos.py ")
clf()
_ip.magic("run campos.py ")
show()
