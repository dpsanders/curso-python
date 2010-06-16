from os import system
from sys import exit, argv

#try:
	#nombre, titulo = argv[1:3]
	
#except:
	#print "Sintaxis: python generar-carta.py nombre"
	#exit(1)
	

nombre_archivo = open("nombres.txt")
for linea in nombre_archivo:
	nombre, titulo = linea.split(",")

	entrada = open("temp.tex", "r")
	latex = entrada.read() 
	latex = latex % (nombre, titulo)

#latex = r"""
#\documentclass{article}

#\begin{document}

#Estimado %s:

#Su cartel titulado "%s" ha sido aceptado para tal.

#\end{document}
#""" % (nombre, titulo)


	salida = open("carta.tex", "w")
	salida.write(latex)
	salida.close()

	comando = "pdflatex carta"
	system(comando)
	
	comando = """cp carta.pdf "%s".pdf""" % nombre
	system(comando)
	#comando = "okular carta.pdf"
	#system(comando)
	
