from io import *

file = open('agenda1.txt', 'w')
file.close()

def agregar_beneficiario():
    f = open('agenda1.txt', 'a')
    nombre = input() + '\n'
    cedula = input() + '\n'
    celular = input() + '\n'
    f.write(nombre)
    f.write(cedula)
    f.write(celular)
    f.close()

def otro_beneficiario():
    nombre = input()
    cedula = input()
    celular = input()
    return nombre, cedula, celular

def leer():
    f = open('agenda1.txt', 'r', encoding='utf-8')
    beneficiarios = f.readlines()
    agenda = list()
    for i in beneficiarios:
        lista_limpia = i.split('\n')
        agenda.append(lista_limpia[0])
    f.close()
    return agenda

agregar_beneficiario()
archivo = leer()
otro = otro_beneficiario()
archivo.extend(otro)
for a in archivo:
    print(a)

print(archivo)

#funcion buscar beneficiario con listas
def buscar_beneficiario(data, nombre_usuario):
    for i, j in enumerate(data):
        if nombre_usuario == j:
            posicion = i + 3
            datos_user = data[i:posicion]
            return datos_user

#elif eleccion == 4:
print('Digite el nombre y apellido del beneficiario a buscar:')
nombre_b = str(input())
data_agenda = leer()
if nombre_b in data_agenda:
    beneficiario_b = buscar_beneficiario(data_agenda, nombre_b)
    for a in beneficiario_b:
        print(a)

def leer():
    f = open('agenda.txt', 'r', encoding='utf-8')
    listado = f.readlines()
    agenda = list()
    for i in listado:
        lista_limpia = i.split('\n')
        agenda.append(lista_limpia[0])
    f.close()
    return agenda

def ver_listado_filtrado(data, letra):
    for i, j in enumerate(data):
        busqueda = data[i]
        if busqueda[0] == letra:
            posicion = i + 3
            datos = data[i:posicion]
            return datos

    for i, j in enumerate(data):
        busqueda = data[i]
        for b in busqueda:
            if b == letra:
                posicion = i + 3
                datos = data[i:posicion]
                return datos