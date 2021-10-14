'''
Programa lee secuencia de números, cuantos son pares y cuantos son impares.
Se termina cuando ingrese Cero (0)
'''

numero = int(input('Ingrese un número y cero (0) para terminar: '))

pares = 0
impares = 0

while numero != 0:
    if numero % 2 == 0:
        pares = pares + 1
    else:
        impares = impares + 1
    numero = int(input('Ingrese el siguiente número: '))

print('Los pares son: ',pares)
print('Los impares son: ',impares)
