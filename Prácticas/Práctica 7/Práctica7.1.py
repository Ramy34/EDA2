import operator
class Vertice:
    def __init__(self,n):
        self.nombre = n
        self.vecinos = list()

        self.d = 0 #tiempo de descubrimiento
        self.f = 0 #tiempo de termino
        self.color = 'white'
        self.pred = -1

    def agregarVecino(self,v):
        if v not in self.vecinos:
            self.vecinos.append(v)
            self.vecinos.sort()

class Graph:
    vertices = {}
    tiempo = 0

    def agregarVertice(self,vertice):
        if isinstance(vertice, Vertice) and vertice.nombre not in self.vertices:
            self.vertices[vertice.nombre] = vertice
            return True		
        else:
            return False

    def agregarArista(self, u, v):
        if u in self.vertices and v in self.vertices:
            for key, value in self.vertices.items():
                if key == u:
                    value.agregarVecino(v)
            return True
        else:
            return False

    def imprimeGrafo(self):        
        print(resultado)

    def dfs(self,vert):
        global lista
        global tiempo
        global resultado
        lista = {}
        tiempo = 0
        for u in sorted(list(self.vertices.keys())):
            if self.vertices[u].color == 'white':
                self.dfsVisitar(self.vertices[u])
            lista[self.vertices[u].nombre] = self.vertices[u].f
        resultado = sorted(lista.items(), key=operator.itemgetter(1))

    def dfsVisitar(self,vert):
        global tiempo
        tiempo = tiempo + 1
        vert.d = tiempo
        vert.color = 'gris'	
        for v in vert.vecinos:
            if self.vertices[v].color == 'white':
                self.vertices[v].pred = vert
            self.dfsVisitar(self.vertices[v])
            vert.color = "black"
            tiempo = tiempo + 1
            vert.f = tiempo

class Principal:
    def main(self):
        g = Graph()
        a = Vertice('A')
        g.agregarVertice(a)
        g.agregarVertice(Vertice('B'))
        for i in range(ord('A'),ord('K')):
            g.agregarVertice(Vertice(chr(i)))
        edges = ['AB', 'AE', 'BF', 'CG', 'DE', 'DH', 'EH', 'FG', 'FI', 'FJ', 'GJ']
        for edge in edges:
            g.agregarArista(edge[:1], edge[1:])
        g.dfs(a)
        g.imprimeGrafo()

o = Principal()
o.main()