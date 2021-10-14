#Ingrese 10 números
#Suma de Negativos
acum = 0

for i in range (1, 11):
    num = int(input('Ingrese número: '))

    if num < 0:
        acum = acum + num

print('La suma de negativos es: ', acum)