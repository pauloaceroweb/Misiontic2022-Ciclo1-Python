edad = int(input())

num_salarios_min = 0
punt_examen = 0
porcentaje_edad = 0
porcentaje_salarios_min = 0
porcentaje_punt_examen = 0

if edad >= 15 and edad <= 25:
    if edad >= 15 and edad <= 18:
        porcentaje_edad = 25
    else:
        if edad >= 19 and edad <= 21:
            porcentaje_edad = 15
        else:
            if edad >= 22 and edad <= 25:
                porcentaje_edad = 10

if punt_examen >= 0 and punt_examen <= 100:
    punt_examen = int (input())
    if punt_examen >= 80 and punt_examen < 86:
        porcentaje_punt_examen = 30
    else:
        if punt_examen >= 86 and punt_examen < 91:
            porcentaje_punt_examen = 35
        else:
            if punt_examen >= 91 and punt_examen < 96:
                porcentaje_punt_examen = 40
            else:
                if punt_examen >= 96 and punt_examen <= 100:
                    porcentaje_punt_examen = 45

if num_salarios_min >= 0 and num_salarios_min <= 4:
    num_salarios_min = int(input())
    if num_salarios_min >= 0 and num_salarios_min <= 1:
        porcentaje_salarios_min = 30
    else:
        if num_salarios_min > 1 and num_salarios_min <= 2:
            porcentaje_salarios_min = 20
        else:
            if num_salarios_min > 2 and num_salarios_min <= 3:
                porcentaje_salarios_min = 10
            else:
                if num_salarios_min > 3 and num_salarios_min <= 4:
                    porcentaje_salarios_min = 5

print(porcentaje_edad)
print(porcentaje_punt_examen)
print(porcentaje_salarios_min)
print(porcentaje_edad + porcentaje_punt_examen + porcentaje_salarios_min)