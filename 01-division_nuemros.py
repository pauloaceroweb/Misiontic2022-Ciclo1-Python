#Escriba un programa que pida dos números enteros y que calcule su
#división, escribiendo si la división es exacta o no. Tenga en cuenta
#que no es posible división por CERO.

num1 = int(input("Ingrese el Dividendo: "))
num2 = int(input("Ingrese el Divisor: "))

if num2 == 0:
    print('El divisor es Cero!!')
    print('No se puede hacer la divisón: Error')
else:
    if num1 % num2 == 0:
        resul = num1 / num2
        print('La división es exacta')
        print('La división es:', resul)
    else:
        resul = num1 / num2
        print('La división es inexacta')
        print('La división es:', resul)
