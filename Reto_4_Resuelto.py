def sueldo_bruto(valor_hora,cantidad_horas):
	if cantidad_horas>40:
		total_horas_normal = 40 * valor_hora
		total_extras = (cantidad_horas - 40)*(valor_hora * 1.5)
		sueldo_bruto = total_horas_normal+total_extras
		return total_horas_normal,total_extras,sueldo_bruto
	else:
		total_horas_normal = 40 * valor_hora
		total_extras = 0
		sueldo_bruto=cantidad_horas*valor_hora
		return total_horas_normal,total_extras,sueldo_bruto

def descuentos(sueldo_bruto):
	parafiscales=sueldo_bruto*0.09
	salud = sueldo_bruto*0.04
	pension =sueldo_bruto*0.04
	return parafiscales,salud,pension

def sueldo_neto(sueldo_bruto,descuentos):
	return sueldo_bruto-descuentos

def provisiones(sueldo_bruto):
	prima = sueldo_bruto*0.0833
	cesantias = sueldo_bruto*0.0833
	intereses_cesantias = sueldo_bruto*0.01
	vacaciones = sueldo_bruto*0.0417
	return prima,cesantias,intereses_cesantias,vacaciones

def main():
	while True:
		print("1. calcular nomina")
		print("0. salir")
		opcion= int(input("selecione una opcion: "))
		if opcion ==0:
			break
		
		name=input("\nNombre Docente: ")
		cantidad_horas=int(input("\nHoras Trabajadas: "))
		valor_hora=int(input("Valor Hora: "))

		sueldo_bruto_docente=sueldo_bruto(valor_hora,cantidad_horas)

		total_horas_normal,total_extras,sueldo_bruto_docente=sueldo_bruto(valor_hora,cantidad_horas)
		
		print("\nValor horas normales: {} \nValor horas extras: {} \nSueldo bruto: {}".format(total_horas_normal,total_extras,sueldo_bruto_docente))

		
		parafiscales,salud,pension=descuentos(sueldo_bruto_docente)
		print("\nDescuento parafiscales: {} \nDescuento salud: {} \nDescuento pension: {}".format(parafiscales,salud,pension))

		total_descuentos=parafiscales+salud+pension
		print ("Suma de todos los descuentos:",total_descuentos)

		print("\nSueldo neto: {}".format(sueldo_neto(sueldo_bruto_docente,total_descuentos)))

		prima,cesantias,intereses_cesantias,vacaciones=provisiones(sueldo_bruto_docente)
		print("\nProvisiones para prima: {} \nProvisiones para cesantias: {} \nProvisiones para intereses de cesantia: {} \nProvisiones para vacaciones: {}".format(prima,cesantias,intereses_cesantias,vacaciones))
		print("\n\n")
main()