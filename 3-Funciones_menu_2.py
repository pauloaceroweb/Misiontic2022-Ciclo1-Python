def generar_impares(liminf, limsup):
    for i in range(liminf, limsup):
        if i % 2 != 0:
            print(i, '-', end='')
            mayor = i
            return mayor


def sumar_numeros(num):
    num2 = int(input('Digite el otro número a sumar: '))
    print('La suma de: ', num, ' + ', num2, 'es = ', num+num2)


def generar_suma():
    liminf = int(input('Digite límite inferior: '))
    limsup = int(input('Digite límite superior: '))
    if liminf < limsup:
        suma = 0
        for i in range(liminf+1, limsup):
            suma = suma + 1
        print('La suma de los números es: ', suma)
    else:
        print('Error en límites digitados')


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
        liminf = int(input('Digite el primer número: '))
        limsup = int(input('Digite el primer número: '))
        print(generar_impares(liminf, limsup))
    elif eleccion == 2:
        print('El Volumen es: ', round(calcular_volumen()))
    elif eleccion == 3:
       break
    else:
       print('Error en el ingreso, intente nuevamente')
