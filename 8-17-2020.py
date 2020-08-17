def cons(a, b):
	def pair(f):
		return f(a, b)
	def cdr(a, b):
		return b
	def car(a, b):
		return a
	return pair(car), pair(cdr)

firstVar, lastVar = cons(3,4)
print("First variable: ", firstVar)
print("Last Variable: ", lastVar)

