def es_par (var1):
    if var1 % 2 == 0:
        rta = True
    else:
        rta = False
    return rta

numero = int(input('Ingrese el número: '))
if es_par(numero) == True:
    print('Es Par')
else:
    print('Es impar')