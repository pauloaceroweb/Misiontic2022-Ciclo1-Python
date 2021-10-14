temp_max = int(input())
temp_min = int(input())

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

    temp_max = int(input())
    temp_min = int(input())

total_dias = dias_temp_error + dias_temp_error_max + dias_temp_error_min + dias
total_dias_temp_error = dias_temp_error + dias_temp_error_max + dias_temp_error_min

print(total_dias)
print(total_dias_temp_error)
print(dias_temp_error_min)
print(dias_temp_error_max)
print(dias_temp_error)
print(prom_temp_max)
print(prom_temp_min)
print((total_dias_temp_error*100)/total_dias)
