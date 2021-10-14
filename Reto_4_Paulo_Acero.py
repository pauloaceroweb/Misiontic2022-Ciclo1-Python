def sueldo_bruto(horas, valor_hora):
    if horas <= 40:
        sueldo = horas * valor_hora
        extras = 0
        salario_bruto = sueldo + extras
        return sueldo, salario_bruto, extras
    else:
        if horas > 40:
            sueldo = 40 * valor_hora
            horas_extras = horas - 40
            valor_extras = horas_extras * 1.5
            extras = valor_extras * valor_hora
            salario_bruto = sueldo + extras
            return sueldo, salario_bruto, extras


def descuentos(salario_bruto):
    parafiscales = salario_bruto * 0.09
    salud = salario_bruto * 0.04
    pension = salario_bruto * 0.04
    salario_neto = salario_bruto - (salud + pension + parafiscales)
    total_descuentos = salud + pension + parafiscales
    return parafiscales, salud, pension, total_descuentos, salario_neto

def provisiones(salario_bruto):
    prima = salario_bruto * 8.33/100
    cesantias = salario_bruto * 8.33/100
    int_cesant = salario_bruto * 1.0/100
    vacaciones = salario_bruto * 4.17/100
    return prima, cesantias, int_cesant, vacaciones


h_trab = int(input('Ingrese el total de las horas trabajadas: '))
v_hora = int(input('Ingrese el valor de la hora: '))

s, sb, e = sueldo_bruto(h_trab, v_hora)

print(s)
print(e)
print(sb)

para, sal, pen, td, sn = descuentos(sb)
print(para)
print(sal)
print(pen)
print(td)
print(sn)

prima, cesa, int_cesa, vaca = provisiones(sb)

print(prima)
print(cesa)
print(int_cesa)
print(vaca)
