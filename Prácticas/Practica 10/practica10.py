import locale
print(locale.getpreferredencoding()) #Revisar la codificacion

########################## Utilizando el open y close
archivo = open('/users/edaII09/edaII09alu06/Escritorio/prueba.txt','r')
archivo.close()

try:
    archivo = open('/users/edaII09/edaII09alu06/Escritorio/prueba.txt',mode = 'r', encoding = 'utf-8')
    #Realiza operaciones con el archivo
except:
    print("Error al abrir")
finally:
    if archivo:
        archivo.close
########################## Utilizando read
a = open('/users/edaII09/edaII09alu06/Escritorio/prueba.txt','r')
c1 = a.read(3)
c2 = a.read()
print(c1)
#print(c2)
a.close()

########################## Utilizando readline
a3 = open('/users/edaII09/edaII09alu06/Escritorio/prueba.txt','r')
while True:
    linea = a3.readline()
    if not linea:
        break
    print(linea)
a3.close()

########################## Utilizando readlines
archivo = open('/users/edaII09/edaII09alu06/Escritorio/prueba.txt','r')
lista = archivo.readlines() #Lee todas las lineas a una lista
numlin = 0
for linea in lista:
    numlin += 1
    print(numlin, linea)
archivo.close()

########################## Utilizando with-as
with open('/users/edaII09/edaII09alu06/Escritorio/prueba.txt','r') as archivo:
    for linea in archivo: #Recorre linea a linea el archivo
        print(linea)

########################## Utilizando writelines
cadena1 = 'Datos' #Declara cadena1
cadena2 = 'Secretos'
archivo2 = open('/users/edaII09/edaII09alu06/Escritorio/datos2.txt','w')
print(cadena1 + '\n')
archivo2.write(cadena1 + '\n')
archivo2.write("Hola")
archivo2.write(cadena2)
archivo2.close

lista = ['lunes','martes','miercoles','jueves','viernes']
archivo2 = open('datos2.txt','w')
archivo2.writelines(lista)
archivo2.close

########################## Utilizando seek
archivo = open('/users/edaII09/edaII09alu06/Escritorio/prueba.txt','r')
archivo.seek(5)
cadena1 = archivo.read(5)
print(cadena1)
print(archivo.tell())#Muestra la posicion del puntero
archivo.close()

########################## Utilizando pickle
import pickle
lista = ['algoritmos 1','algoritmos 2','estructuras']
archivo = open('materias.dat','wb')
pickle.dump(lista,archivo)
archivo.close()
del lista
archivo = open('materias.dat','rb')
lista = pickle.load(archivo)
print(lista)
archivo.close()

########################## Creando directorios
import os
def crear_directorio(ruta):
    try:
        os.makedirs(ruta)
    except OSError:
        pass
    os.chdir(ruta)
crear_directorio('/users/edaII09/edaII09alu06/Escritorio/nuevo')

########################## Recorriendo directorios
import os
rootDir = '/users/edaII09/edaII09alu06/Escritorio/'
for dirName, subdirList, fileList in os.walk(rootDir):
    print('Directorio encontrado: %s' %dirName)
    for fname in fileList:
        print('\t%s' %fname)

########################## Atributos
archivo = open('/users/edaII09/edaII09alu06/Escritorio/prueba.txt','r')
contenido = archivo.read()
nombre = archivo.name
modo = archivo.mode
encoding = archivo.encoding
archivo.close()

if archivo.closed:
    print("El archivos se ha cerrado correctamente")
else:
    print("El archivo permanece abierto")
print(contenido)
print(nombre)
print(modo)
print(encoding)





