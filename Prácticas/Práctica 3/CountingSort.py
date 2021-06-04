#Conuting Sort
def CreaLista(k):
    L = []
    for i in range (k+1):
        L.append(0)
    return L
def CountingSort (A,k):
	C = CreaLista(k)
	B = CreaLista(len(A)-1)
	for j in range (1,len(A)):
		C[A[j]] = C[A[j]]+1
	for i in range (1,k+1):
		C[i] = C[i] + C[i-1]
	for j in range (0,len(A)):
		B[C[A[j]]] = A[j]
		C[A[j]] = C[A[j]]-1
	return B
def inicio(A):
	tamanoLista = int(input("Dame el tamano de tu lista: "))
	while (len(A) < (tamanoLista+1)):
		elemento = int(input("Dame un numero: "))
		A.append(elemento)
	mayor = mayorNumero(A,len(A)) 
	return mayor
def mayorNumero (A,tamanoLista):
    mayor = 0
    for q in range (0,tamanoLista):
        if (A[q] > mayor):
            mayor = A[q]
    return mayor
print("Counting Sort.\n")
A = [0]
k = inicio(A)
print (A)
Hola = CountingSort(A,k)
print(Hola)