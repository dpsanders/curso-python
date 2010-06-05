# 	a = 3

a = float(raw_input("Dame valor de a: "))

if a < 0:
	print "a neg"
	a = -a
	print "otra linea mas"
	
elif a == 0:
	print "a = 0"
	
else:
	print "a pos"
