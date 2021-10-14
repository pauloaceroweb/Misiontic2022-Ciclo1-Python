lista1 = [[1, 'ANA', 3], [1, 56, -12]]
lista2 = [[1, 'ANA', 3], [1, 56, -12]]
lista3 = [['Carlos', 'Mario', 'Andres', 'Maria', 'Luisa'],
          [3.2, 2.1, 4.5, 2.2, 4.0]]

i = 1
for elem in lista1:
    print(str(i) + ':\t' + str(elem))
    i += 1

largo = len(lista2)
for i in range(largo):
    print(str(i + 1) + ':\t' + str(lista2[i]))

print('***************************************')
#Imprimir lista de estudiantes con su nota final
#Agregar otra lista de fallas
fallas = [2, 1, 1, 0, 4]
lista3.append(fallas)

largo = len(lista3[0])
for i in range(largo):
    print(str(i + 1) + ':\t' + str(lista3[0][i]) + ':\t' + str(lista3[1][i]) + ' Fallas ---> ' + str(lista3[2][i]))

print(lista3)


