class Particula:
	def __init__(self, xx=0.0, vv=1.0):
		print "Estoy adentro de __init__"
		self.x = xx
		self.v = vv
	
	def mover(self, dt):
		self.x += dt * self.v
		
	def mover_n_veces(self, n, dt):
		for i in range(n):
			self.mover(dt)
			
	def __str__(self):
		return "Particula(%g, %g)" % (self.x, self.v)
		
	def __add__(self, otra):
		return Particula(self.x + otra.x, self.v + otra.v)
		
		