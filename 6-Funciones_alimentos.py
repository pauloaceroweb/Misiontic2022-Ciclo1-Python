def calcular_variedad(codigo):
    if codigo >= 1 and codigo <= 10:
        var = 'Salados'
    elif codigo >= 10 and codigo <= 20:
        var = 'Dulces'
    else:
        var = 'Error'
    return var

def calcular_valor_pyv(tipo, variedad, costof):
    if (tipo == 'N' or tipo == 'n') and variedad == 'Salados':
        rta = 2 * costof
        rta2 = rta + costof + (costof * 0.10)
    elif (tipo == 'N' or tipo == 'n') and variedad == 'Dulces':
        rta = 4 * costof
        rta2 = rta + costof + (costof * 0.10)
    elif (tipo == 'A' or tipo == 'a') and variedad == 'Salados':
        rta = 4 * costof
        rta2 = rta + costof + (costof * 0.20)
    else:
        rta = 6 * costof
        rta2 = rta + costof + (costof * 0.20)
    return rta, rta2

valor_prod = 0
cant_tipoA = 0
cant_tipoN = 0
total_valor_prod = 0
siga = True

while siga == True:
    tipo = str(input('Ingrese el tipo: N para Niños y A para adultos: '))
    cod_prod = int(input('Ingrese el rango del código: De 1 a 10 Salados y De 11 a 20 Dulces: '))
    costo_fab = int (input('Ingrese el Costo de Fabricación: '))

    if tipo != 'A' and tipo != 'a' and tipo != 'N' and tipo != 'n':
        print('Error Tipo')
    else:
        variedad = calcular_variedad(cod_prod)
        if variedad != 'Error' and costo_fab > 0:
            valor_prod, precio_venta = calcular_valor_pyv(tipo, variedad,costo_fab)
            print('Variedad = ', variedad)
            print('Valor Producción = ',valor_prod)
            print('Valor venta publico = ', precio_venta)
            if tipo == 'A' or tipo == 'a':
                cant_tipoA += 1
            else:
                cant_tipoN += 1
                total_valor_prod = total_valor_prod + valor_prod
        else:
            if variedad == 'Error':
                print('Error en Variedad')
            else:
                print('Costo de fábrica invalido')

        print('Desea calcular más productos?')
        decision = str(input('Digite S o N'))
        if decision == 'S' or decision == 's':
            siga = True
        else:
            siga = False

print('INFORME FINAL')
print('Cantidad de productos tipo A = ', cant_tipoA)
print('Cantidad de productos tipo N = ', cant_tipoN)
print('Total valores producción Tipo N = ', total_valor_prod)
if cant_tipoN > 0:
    print('Promedio Producción productos tipo N = ', total_valor_prod/cant_tipoN)
else:
    if cant_tipoA > cant_tipoN:
        print('Se fabrican nás productos tipo A = ', cant_tipoA)
    else:
        print('Se fabrican nás productos tipo N = ', cant_tipoN)
