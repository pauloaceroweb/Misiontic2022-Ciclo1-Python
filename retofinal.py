from io import *

file = open('agenda.txt', 'w', encoding='utf-8')
file.close()


def agregar_beneficiario():
    f = open('agenda.txt', 'a', encoding='utf-8')
    nombre = input() + '\n'
    cedula = input() + '\n'
    celular = input() + '\n'
    f.write(nombre)
    f.write(cedula)
    f.write(celular)
    f.close()


def ver_listado():
    f = open('agenda.txt', 'r', encoding='utf-8')
    listado = f.read()
    print(listado, end='')
    f.close()


def ver_listado_filtrado():
    f = open('agenda.txt', 'r', encoding='utf-8')
    listado = f.readlines()
    iterador = 0
    letra = input()
    for i in listado:
        if i.startswith(letra):
            print(listado[iterador], end='')
            print(listado[iterador + 1], end='')
            print(listado[iterador + 2], end='')
        iterador = iterador + 1
    f.close()


def buscar_beneficiario():
    f = open('agenda.txt', 'r', encoding='utf-8')
    listado = f.readlines()
    nombre = str(input())
    for i in listado:
        if i.strip() == nombre:
            print(listado[listado.index(i)], end='')
            print(listado[listado.index(i) + 1], end='')
            print(listado[listado.index(i) + 2], end='')
            if not nombre != listado:
                print('No se encuentra el beneficiario en la agenda')
    f.close()


def borrar_beneficiario():
    f = open('agenda.txt', 'r', encoding='utf-8')
    listado = f.readlines()
    f.close()
    ced = input()
    f = open('agenda.txt', 'w', encoding='utf-8')
    nombre = ''
    cedula = ''
    celular = ''
    for i in listado:
        if i.strip() == ced:
            indice = listado.index(i)
            nombre = listado[indice - 1]
            cedula = listado[indice]
            celular = listado[indice + 1]
    for i in listado:
        if i.strip('\n') != nombre.strip('\n') and i != celular and i != cedula:
            f.write(i)
    f.close()


def menu():
    print('Menu Principal')
    print('1. Ver listado')
    print('2. Ver listado filtrado')
    print('3. Agregar beneficiario')
    print('4. Buscar beneficiario')
    print('5. Borrar beneficiario')
    print('6. Salir')

    opc = int(input())
    return opc


while True:
    eleccion = menu()
    if eleccion == 1:
        print('Listado de beneficiarios:')
        ver_listado()

    elif eleccion == 2:
        print('Digite la letra por la que empiezan los beneficiarios:')
        print('Listado filtrado de beneficiarios:')
        ver_listado_filtrado()

    elif eleccion == 3:
        print('Digite la información del beneficiario a agregar:')
        agregar_beneficiario()
        print('El beneficiario ha sido agregado')

    elif eleccion == 4:
        print('Digite el nombre y apellido del beneficiario a buscar:')
        buscar_beneficiario()

    elif eleccion == 5:
        print('Digite la cedula del beneficiario a borrar:')
        borrar_beneficiario()
        print('El usuario ha sido eliminado del listado')

    elif eleccion == 6:
        print('Hasta pronto')
        break