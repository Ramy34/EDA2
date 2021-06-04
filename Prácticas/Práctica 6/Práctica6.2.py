class Vertice:
	def __init__(self,n):
		self.nombre = n
		self.vecinos = list()
		self.distancia = 9999
		self.color = 'white'
		self.pred = -1
	
	def agregarVecino(self,v):
		if v not in self.vecinos:
			self.vecinos.append(v)
			self.vecinos.sort()

class Graph:
    vertices = {}
    
    def agregarVertice (self, vertice):
        if isinstance(vertice, Vertice) and vertice.nombre not in self.vertices:
            self.vertices[vertice.nombre] = vertice
            return True
        else:
            return False
        
    def agregarArista(self, u, v):
        if u in self.vertices and v in self.vertices:
            for key, value in self.vertices.items():
                if key == u :
                    value.agregarVecino(v)
                if key == v:
                    value.agregarVecino(u)
            return True 
        else:
            return False
        
    
    def printPath(self,vert,ini):
        vert.distancia=0
        vert.color='gris'
        vert.pred=-1
        
        if ini.nombre==vert.nombre:
            print("La distancia es Cero")
            
        if ini.nombre>'J' or vert.nombre>'J':
            print("La distancia no existe")
            
        q=list()
        
        q.append(vert.nombre)
        
        while len(q)>0:
            
            u=q.pop()
            node_u=self.vertices[u]
            for v in node_u.vecinos:
                node_v=self.vertices[v]
                if node_v.color=='white':
                    node_v.color='gris'
                    node_v.distancia=node_u.distancia+1
                    node_v.pred=node_u.nombre
                    if node_v.nombre==ini.nombre:
                        print("La distancia es "+str(node_v.distancia))
                        
                        
                   
                    q.append(v)
            self.vertices[u].color='black'
                                        

g=Graph()
a=Vertice('A')
g.agregarVertice(a)
g.agregarVertice(Vertice('B'))
for i in range(ord('A'),ord('K')):
    g.agregarVertice(Vertice(chr(i)))
    
edges=['AB','AE','BF','CG','DE','DH','EH','FG','FI','FJ','GJ']
for edge in edges:
    g.agregarArista(edge[:1],edge[1:])

print("La distancia entre los vertices dados es:")
print("A a D:")
g.printPath(Vertice('A'),Vertice('D'))

print("\nF a F:")
g.printPath(Vertice('F'),Vertice('F'))

print("\nI a Z:")
g.printPath(Vertice('I'),Vertice('Z'))