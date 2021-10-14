total_horas = 0
tot_fiesta1 = 0
tot_fiesta2 = 0
tot_fiesta3 = 0
valor_max = 0
valor_fiesta = 0
valor_min = 1430000
hay_fiestas = 'S'

while hay_fiestas == 'S' or hay_fiestas == 's':
    invitados = int(input('Ingrese cantidad de invitados: '))
    duracion = int(input('Ingrese la duración de la fiesta: '))
    if invitados <= 25:
        valor_fiesta = 500000
    else:
        if invitados <= 50:
            valor_fiesta = 750000
        else:
            valor_fiesta = 980000

    if duracion <= 3:
        valor_fiesta += 200000
        tot_fiesta1 += 1
    else:
        if duracion <= 6:
            valor_fiesta += 350000
            tot_fiesta2 += 1
        else:
            valor_fiesta += 450000
            tot_fiesta3 += 1
    print('La fiesta costo: ', valor_fiesta)

    if valor_max < valor_fiesta:
        valor_max = valor_fiesta
    else:
        if valor_min > valor_fiesta:
            valor_min = valor_fiesta

    total_horas += duracion
    hay_fiestas = str(input('Se hicieron más fiestas?: '))

print('Cantidad de horas de fiesta en el mes: ', total_horas)
print('Cantidad de fiestas <= 3 horas: ', tot_fiesta1)
print('Cantidad de fiestas de 4 a 6 horas: ', tot_fiesta2)
print('Cantidad de fiesta > 6 horas: ',tot_fiesta3)
print('La fiesta con mayor pago costó: ', valor_max)
print('La fiesta con menor pago costó: ', valor_min)
