#import os
from os import system
from numpy import arange

for T in arange(0.5, 5, 0.5):
	comando = "python simul.py %g" % T
	system(comando)

