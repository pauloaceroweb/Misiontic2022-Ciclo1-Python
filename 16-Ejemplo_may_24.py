suma_par = 0
suma_impar = 0
cant_par = 0
cant_impar = 0

for i in range (1, 101):
   if i%2 == 0:
       suma_par = suma_par + i
       cant_par = cant_par + 1
   else:
      suma_impar = suma_impar + i
      cant_impar = cant_par + 1

print('La suma de los pares es: ', suma_par)
print('El promedio de los pares es: ', suma_par/cant_par)
print('La suma de los pares es: ', suma_impar)
print('El promedio de los pares es: ', suma_impar/cant_impar)