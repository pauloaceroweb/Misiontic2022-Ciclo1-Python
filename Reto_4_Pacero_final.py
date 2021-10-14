def valor_horas(horas, valor_hora):
    if horas <= 40:
        sueldo = horas * valor_hora
        extras = 0
        return sueldo, extras
    elif horas > 40:
        sueldo = 40 * valor_hora
        horas_extras = horas - 40
        valor_extras = horas_extras * 1.5
        extras = valor_extras * valor_hora
        return sueldo, extras

def sueldo_bruto(sueldo, extras):
    salario_bruto = sueldo + extras
    return salario_bruto

def des_parafiscales(salario_bruto):
    parafiscales = salario_bruto * 0.09
    return parafiscales

def des_salud(salario_bruto):
    salud = salario_bruto * 0.04
    return salud

def des_pension(salario_bruto):
    pension = salario_bruto * 0.04
    return pension

def descuentos(salud, pension, parafiscales):
    total_descuentos = salud + pension + parafiscales
    return total_descuentos

def sal_neto(salario_bruto, total_descuentos):
    salario_neto = salario_bruto - total_descuentos
    return salario_neto

def prov_prima(salario_bruto):
    prima = salario_bruto * 8.33/100
    return prima

def prov_cesantias(salario_bruto):
    cesantias = salario_bruto * 8.33/100
    return cesantias

def prov_int_cesantias(salario_bruto):
    int_cesant = salario_bruto * 1.0/100
    return int_cesant

def prov_vacaciones(salario_bruto):
    vacaciones = salario_bruto * 4.17/100
    return vacaciones


h_trab = int(input('Ingrese el total de las horas trabajadas: '))
v_hora = int(input('Ingrese el valor de la hora: '))

sn, ext = valor_horas(h_trab, v_hora)
print('Valor horas normales: ', sn)
print('Valor horas extras: ', ext)
sb = sueldo_bruto(sn, ext)
print(sb)
p = des_parafiscales(sb)
print(p)
s = des_salud(sb)
print(s)
pe = des_pension(sb)
print(pe)
td = descuentos(s, pe, p)
print(td)
sn = sal_neto(sb, td)
print(sn)
prim = prov_prima(sb)
print(prim)
ces = prov_cesantias(sb)
print(ces)
int_ces = prov_int_cesantias(sb)
print(int_ces)
vac = prov_vacaciones(sb)
print(vac)
