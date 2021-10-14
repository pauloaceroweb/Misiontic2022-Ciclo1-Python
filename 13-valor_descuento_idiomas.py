print('Los programas disponibles en el instituto son:')
print('Digite I o i para informacón de Inglés:')
print('Digite F o f para informacón de Frances:')
print('Digite P o p para informacón de Portugues:')
print('Digite A o a para informacón de Aleman:')

programa = input('Ingrese la inicial del progrma: ')

if programa == 'I' or programa == 'i':
    descuento = 350000 * 0.3
    valor = 350000 - descuento
    print('El valor de inscripción a Ingles es: ', valor)
    print('El valor del descuento para la inscripción a Ingles es: ', descuento)
elif programa == 'F' or programa == 'f':
    valor = 385000
    print('El valor de inscripción a Francés es: ', valor)
    print('Este programa no tiene descuento')
elif programa == 'P' or programa == 'p':
    valor = 420000
    print('El valor de inscripción a Portugues es: ', valor)
    print('Este programa no tiene descuento')
elif programa == 'A' or programa == 'a':
    descuento = 395000 * 0.15
    valor = 395000 - descuento
    print('El valor de inscripción a Alemán es: ', valor)
    print('El valor del descuento para la inscripción a Aleman es: ', descuento)
else:
    print('Digite un valor correcto')