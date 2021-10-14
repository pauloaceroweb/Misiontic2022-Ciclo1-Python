# Calcular las tablas de multiplicar
print('''    M E N U
1. Tablas de Multiplicar
2. Calcular Areas de Figuras Geométricas
3. Terminar
Digite su opción -------> ''')
opc = int(input())

while True:
    if opc == 1:
        tabla_ini = int(input('Tabla inicial ---> '))
        tabla_fin = int(input('Tabla final ---> '))

        for x in range(tabla_ini, tabla_fin + 1):
            for i in range(1, 11):
                print(x, '\tX', i, '\t=', x * i)
            print('-' * 20)

    elif opc == 2:
        print('''FIGURAS GEOMETRICAS
            1. Círculo
            2. Rectangulo
            Digite su opción ------> ''')
        fig = int(input())
        if fig == 1:
            r = float(input('Digite el radio: '))
            print('Area = ', 3.14*r*r)
        else:
            base = int(input('Digite la base: '))
            altura = int(input('Digite la altura: '))
            print('Area = ', base*altura)
    else:
        break

    print('''    M E N U
    1. Tablas de Multiplicar
    2. Calcular Areas de Figuras Geométricas
    3. Terminar
    Digite su opción -------> ''')
    opc = int(input())
