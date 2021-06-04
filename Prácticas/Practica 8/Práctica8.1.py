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

	def busqueda(self,nodoX, valor):
		if (nodoX == None or valor == nodoX.val):
			return nodoX
		if(valor < nodoX.val):
			return self.busqueda(nodoX.hijoIzq, valor)
		else:
			return self.busqueda(nodoX.hijoDer, valor)


class Principal:
	def main(self):
		ar = Arbol()
		lista = [8,3,10,1,6,14,4,7,13]
		for i in range (0, len(lista)):
			ar.agregar(lista[i])
		ob = (ar.busqueda(ar.obtenerRaiz(),9)).val
		print(ob)

objeto = Principal()
objeto.main()
