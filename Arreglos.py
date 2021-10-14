from numpy import *

a = array([6,2,13,-1,34,2])
c = array([1,1,1,1,1,1])
nombres = array(['Luis','Carlos', 'Maria', 'Teresa'])
print(a)
#Definicion arrego de cadenas tamaño 10, maximo 50 caracteres
b = zeros(10, 'U50')
for i in range(10):
    b[i]=input()

print(b)
#Los arreglos de numeros se pueden sumar, restar , Multipl y dividir y deben tener la misma cantidad de elementos
print(a+c)
#Sus elementos se puede comparar con >, >=, etc cada elemento
print(a<c)
#Sumarle un dato a todos los elementos
print(a+10)

#Obtener elementos del arreglo
c = a[1:4]
d = a[2:-2]
e = a[:5]
f = a[2:]
print(c)
print(d)
print(e)
print(f)
# Sus elementos se pueden operar entre si con los metodos
print(a.sum())
print(a.sum())
print(a.sum())
print(a.sum())
X= 10 * [9]
print(X)
Y = []*6
for i in range(0,6):
    Y.append(int(input()))
print("Arreglo leido = ", Y)
Y.insert(3, 8)
print("Arreglo leido = ", Y)
unos = ones((3,2))        # a 2D array with 3 rows, 2 columns, filled with ones
print("UNOS= ", unos)
puntos = linspace(2,3,100)  # an array with 100 points beteen (and including) 2 and 3
print("puntos= ", puntos)