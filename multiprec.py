# -*- coding: utf-8 -*-
from mpmath import *
from sys import argv

precision = int(argv[1])

mp.dps = precision   # num de digitos decimales

y = mpf('25.0')
x = mpf('0.1')

for i in range(20):
  x = 0.5*(x + (y/x))
  #print x,
  diff = log10(x - 5.0, 10)
  #nprint (log10(x - 5.0), 10)
  