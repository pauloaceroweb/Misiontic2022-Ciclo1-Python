import math


def calcular_area():
    print('''MENU AREAS
        1. Calcular Area Círculo
        2. Calcular Area Rectangulo
        Digite la opción ------>''')
    opcion1 = int(input())
    if opcion1 == 1:
        radio = float(input('Digite el Radio: '))
        area = math.pi * pow(radio, 2)
    else:
        largo = float(input('Digite el largo del rectángulo: '))
        ancho = float(input('Digite el ancho del rectángulo: '))
        area = largo * ancho
    return area


def calcular_volumen():
    print('''MENU VOLUMENES
        1. Calcular Volumen Esfera
        2. Calcular volumen prisma rectangular
        Digite la opción -------> ''')
    opcion1 = int(input())
    if opcion1 == 1:
        radio = float(input('Digite el Radio: '))
        vol = math.pi * pow(radio, 3) * 4 / 3
    else:
        largo = float(input('Digite el largo de la base: '))
        ancho = float(input('Digite el ancho de la base: '))
        altura = float(input('Digite la altura del prisma: '))
        vol = largo * ancho * altura
    return vol


def menu():
    print('''MENU PRINCIPAL
        1. Calcular Areas
        2. Calcular Volumenes
        3. Salir
        Digite la opción -------> ''')
    opc = int(input())
    return opc


while True:
    eleccion = menu()
    if eleccion == 1:
        print('El Area es: ', round(calcular_area()))
    elif eleccion == 2:
        print('El Volumen es: ', round(calcular_volumen()))
    elif eleccion == 3:
        break
    else:
        print('Error en el ingreso, intente nuevamente')
