class AST:
	def __init__(self):
		pass
	def mostrar(self):
		pass
	def numero_operaciones(self):
		pass
	def interpreta(self):
		pass

class Numero(AST):
	def __init__(self, valor):
		self.valor = valor
	def mostrar(self):
		return str(self.valor)
	def interpreta(self):
		return self.valor

class Operacion(AST):
	def __init__(self,op,izda,dcha):
		self.op = op
		self.izda = izda
		self.dcha = dcha
	def mostrar(self):
		return '(' + self.izda.mostrar() + self.op + self.dcha.mostrar() + ')'
	def numero_operaciones(self):
		return 1 + self.izda.numero_operaciones() + self.dcha.numero_operaciones()
	def interpreta(self):
		if self.op == "+":
			return self.izda.interpreta() + self.dcha.interpreta()
		else:
			return self.izda.interpreta() * self.dcha.interpreta()

"""n1 = Numero(5)
n2 = Numero(4)
n3 = Numero(7)
n4 = Numero(9)

a1 = Operacion("+",n1,n2)
a2 = Operacion("*",n2,n3)
a3 = Operacion("+",a1,a2)
print(a3.mostrar())"""

postfija = ["5","3","/","3","+"]
pila = []
i = 0
while i != len(postfija):
	E = postfija[i]
	if E.isdigit():
		n1 = Numero(E)
		pila.append(n1)
	elif E == "+" or E == "*" or E == "/" or E == "-":
		if len(pila) < 2:
			print("Error")
		else:
			A2 = pila.pop()
			A1 = pila.pop()
			arbol = Operacion(E,A1,A2)
			pila.append(arbol)
	i = i + 1
if pila == None or len(pila) > 1:
	print("Error")
else:
	E = pila.pop()
print(E.mostrar())