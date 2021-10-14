pac_tipo1 = pac_tipo2 = pac_tipo3 = 0
dias_tipo1 = dias_tipo2 = dias_tipo3 = 0

pacientes = 0
hay_paciente = 's'

while hay_paciente == 's' and pacientes < 5:
    tipo = int(input('Ingrese el tipo de enfermedad (1,2,3): '))
    dias_hosp = int(input('Ingrese los días de Hospitalización: '))
    if tipo == 1:
        pac_tipo1 = pac_tipo1 + 1
        dias_tipo1 = dias_tipo1 + dias_hosp
    else:
        if tipo == 2:
            pac_tipo2 = pac_tipo2 + 1
            dias_tipo2 = dias_tipo2 + dias_hosp
        else:
            if tipo == 3:
                pac_tipo3 = pac_tipo3 + 1
                dias_tipo3 = dias_tipo3 + dias_hosp
    hay_paciente = str(input('Hay otro paciente para hospitalizar?: '))
    pacientes = pacientes + 1

print('{:^15}{:^15}{:^15}{:^15}' .format('Tipo Enfer', 'Cant Pacientes', 'Cant días', 'Total a pagar'))
print('{:^15}{:^15}{:^15}{:^15}' .format('1', pac_tipo1, dias_tipo1, dias_tipo1*150000))
print('{:^15}{:^15}{:^15}{:^15}' .format('2', pac_tipo2, dias_tipo2, dias_tipo2*170000))
print('{:^15}{:^15}{:^15}{:^15}' .format('3', pac_tipo3, dias_tipo3, dias_tipo3*190000))