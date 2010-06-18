
from pylab import plot, xlabel, ylabel, savefig, clf, sin
from numpy import arange
from os import system

t = arange(-6.3, 6.3, 0.1)

for i in range(1, 7):
	print "i = ", i
	clf()
	plot(t, sin(i*t))
	xlabel('$x$')
	ylabel('$\sin(%dx)$' % i)

	savefig("sin%d.pdf" % i)

latex = r"""
\documentclass{article}
\usepackage{graphicx}
\usepackage{subfigure}
\begin{document}
\begin{figure}
"""

for i in range(1, 7):
	latex += r"""\subfigure[$i=%d$]{
	\includegraphics[scale=0.3]{sin%d}"""% (i, i) + "}\n"
	
latex += r"""
\end{figure}
\end{document}"""

salida = open("sins.tex",  "w")
salida.write(latex)
salida.close()

comando = "pdflatex sins"
system(comando)

comando = "acroread sins.pdf"
system(comando)