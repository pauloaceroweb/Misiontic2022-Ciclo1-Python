from io import *

file = open('prueba.txt', 'w')
print('file: ', file)
file.close()

file = open('prueba.txt', 'r+')
cadena1 = '1- Esta es la primera línea del archivo\n'
cadena2 = '2- Esta será la segunda línea del archivito\n'
cadena3 = '3- Esta será la tercera línea del archivo\n'
file.write(cadena1)
file.write(cadena2)
file.write(cadena3)
file.seek(0)
lista_filas = file.readlines()
print(lista_filas)
file.write('4- Esta es la línea 4')
file.seek(0)
lista_filas = file.readlines()
print(lista_filas)

file.close()
