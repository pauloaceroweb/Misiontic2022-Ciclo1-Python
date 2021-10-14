from io import *

f = open('archivo1.txt', 'w')
f.write(str(input('Ingrese el nombre y apellido: ')) + '\n')
f.write(str(input('Ingrese la cedula: ')) + '\n')
f.write(str(input('Ingrese el celular: ')) + '\n')
f.close()

print(f.readlines())