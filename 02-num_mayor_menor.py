#Escriba un programa que pida dos números y que conteste cuál es el
#menor y cuál el mayor o que escriba que son iguales.

num1 = int(input('Ingrese el número 1: '))
num2 = int(input('Ingrese el número 2: '))

if num1 == num2:
    print('Los números son iguales: ', num1, '=', num2)
else:
    if num1 > num2:
        print('El número mayor es: ', num1)
        print('El número menor es: ', num2)
    else:
        print('El número mayor es: ', num2)
        print('El número menor es: ', num1)