temp_max = float(input('Temperatura máxima: '))
temp_min = float(input('Temperatura mínima: '))

dias = 0
dias_temp_error = 0
dias_temp_error_max = 0
dias_temp_error_min = 0
sum_temp_max = 0
sum_temp_min = 0
prom_temp_max = 0
prom_temp_min = 0

while temp_max != 0 or temp_min != 0:
    if (temp_max > 35 and temp_min < 5) or (temp_max < 5 and temp_min > 35):
        dias_temp_error += 1
    else:
        if temp_max < 5 or temp_min < 5:
            dias_temp_error_min += 1
        else:
            if temp_max > 35 or temp_min > 35:
                dias_temp_error_max += 1
            else:
                if temp_max <= 35 and temp_min >= 5:
                    dias += 1
                    sum_temp_max += temp_max
                    prom_temp_max = sum_temp_max / dias
                    sum_temp_min += temp_min
                    prom_temp_min = sum_temp_min / dias
                else:
                    if temp_max == 0 and temp_min == 0:
                        break

    temp_max = float(input('Temperatura máxima: '))
    temp_min = float(input('Temperatura mínima: '))

total_dias = dias_temp_error + dias_temp_error_max + dias_temp_error_min + dias
print('Total dias de la salida de campo: ', total_dias)
total_dias_temp_error = dias_temp_error + dias_temp_error_max + dias_temp_error_min
print('Total días con error: ', total_dias_temp_error)
print('Días con error en Temperatura menor a 5: ', dias_temp_error_min)
print('Días con error en Temperatura mayor a 35: ', dias_temp_error_max)
print('Dias con temperaturas mayores a 35 y menores a 5: ', dias_temp_error)
print('Temperatura media mínima: ', int(prom_temp_min))
print('Temperatura media máxima: ', int(prom_temp_max))
print('Porcentaje de días con Error: ', int((total_dias_temp_error*100)/total_dias), '%')
