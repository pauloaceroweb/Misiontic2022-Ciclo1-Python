nombre = str(input('Ingrese su nombre: '))
edad = int(input('Ingrese su edad: '))
id = int(input('Ingrese su identificación: '))
barrio = str(input('Ingrese su Barrio: '))
grado = int(input('Ingrese su grado: '))

valor_mat = 0
valor_esp = 0
valor_derechos = 0
error = False

if grado >= 6 and grado <= 11:
    esp = str(input('Digite la Especialidad: '))
    print('I : Idiomas, E : Electricidad, S : Sistemas, P : Pedagogía')
    if esp == 'I' or esp == 'i':
        valor_esp = 500000
    else:
        if esp == 'E' or esp == 'e':
            valor_esp = 350000
        else:
            if esp == 'S' or esp == 's':
                valor_esp = 520000
            else:
                if esp == 'P' or esp == 'p':
                    valor_esp = 400000
                else:
                    print('Error en la especialidad ingresada')
                    error = True

if error == True:
    print('No se pueden realizar calculos')
else:
    if grado >= 1 and grado <= 5:
        valor_mat = 650000
    else:
        if grado >= 6 and grado <= 8:
            valor_mat = 700000
        else:
            if grado >= 9 and grado <= 10:
                valor_mat = 720000
            else:
                if grado == 11:
                    valor_mat = 800000
                    valor_derechos = 580000
                else:
                    error = True
                    print('Error en el grado digitado')

if error == False:
    print('Datos Basicos del Estudiante:')
    print('Nombre: ', nombre)
    print('Edad: ', edad)
    print('Barrio: ', barrio)
    print('ID: ', id)
    print('Grado: ', grado)
    print('Valor Matricula: ', valor_mat)

    if valor_esp > 0:
        print('Valor Especialidad: ', valor_esp)

    if valor_derechos > 0:
        print('Valor Derechos de Grado: ', valor_derechos)

    print('Total a pagar: ', valor_mat + valor_esp + valor_derechos)


