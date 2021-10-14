from io import *

arc_buscar = open('prueba1.txt', 'w')
print('buscar por parametro', arc_buscar)
arc_buscar.close()

arc_buscar = open('prueba1.txt', 'r+')
cadena1 = 'Carlos Perez\n'
cadena2 = '74362123\n'
cadena3 = '3108512508\n'
cadena4 = 'Luis Diaz\n'
cadena5 = '5732136\n'
cadena6 = '3226893462\n'

arc_buscar.write(cadena1)
arc_buscar.write(cadena2)
arc_buscar.write(cadena3)
arc_buscar.write(cadena4)
arc_buscar.write(cadena5)
arc_buscar.write(cadena6)
arc_buscar.seek(0)
lista = arc_buscar.readlines()
cedula = '5732136'
existe = False

for i in range(len(lista)-1):
    pos = lista[i+1].find(cedula)
    if pos >= 0:
        print('Beneficiario: ', lista[i])
        existe = True
if existe == False:
    print('No existe cédula')
print(lista)

arc_buscar.close()