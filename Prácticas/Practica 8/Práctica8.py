class Nodo:
	def __init__(self, valor):
		self.hijoIzq = None
		self.hijoDer = None
		self.val = valor

class Arbol:
	def __init__(self):
		self.raiz = None

	def obtenerRaiz(self):
		return self.raiz

	def agregar(self, val):
		if(self.raiz == None):
			self.raiz = Nodo(val)
		else:
			self.agregarNodo(val, self.raiz)

	def agregarNodo(self, val, nodo):
		if(val < nodo.val):
			if(nodo.hijoIzq != None):
				self.agregarNodo(val, nodo.hijoIzq)
			else:
				nodo.hijoIzq = Nodo(val)
		else:
			if(nodo.hijoDer != None):
				self.agregarNodo(val, nodo.hijoDer)
			else:
				nodo.hijoDer = Nodo(val)

	def imprimePreorden(self):
		if(self.raiz != None):
			self.preorden(self.raiz)

	def preorden(self, nodo):
		if (nodo != None):
			print(str(nodo.val))
			if(nodo.hijoIzq != None):
				self.preorden(nodo.hijoIzq)
			if(nodo.hijoDer != None):
				self.preorden(nodo.hijoDer)

	def imprimeInorden(self):
		if(self.raiz != None):
			self.inorden(self.raiz)

	def inorden(self, nodo):
		if (nodo != None):
			if(nodo.hijoIzq != None):
				self.preorden(nodo.hijoIzq)
			print(str(nodo.val))
			if(nodo.hijoDer != None):
				self.preorden(nodo.hijoDer)

	def imprimePostorden(self):
		if(self.raiz != None):
			self.postorden(self.raiz)

	def postorden(self, nodo):
		if (nodo != None):
			if(nodo.hijoIzq != None):
				self.preorden(nodo.hijoIzq)
			if(nodo.hijoDer != None):
				self.preorden(nodo.hijoDer)
			print(str(nodo.val))

class Principal:
	def main(self):
		ar = Arbol()
		lista = [8,3,10,1,6,14,4,7,13]
		for i in range (1, len(lista)):
			ar.agregar(lista[i])
		print("Pre-orden")
		ar.imprimePreorden()
		print("In-orden")
		ar.imprimeInorden()
		print("Post-orden")
		ar.imprimePostorden()

objeto = Principal()
objeto.main()
