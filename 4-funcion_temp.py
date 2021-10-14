def temperatura(celcius):
    farenheith = (celcius * 9/5) + 32
    return farenheith

temp_celcius = int(input('Ingrese la Temperatura: '))
print('Temperatura en Farenheith es:', temperatura(temp_celcius))