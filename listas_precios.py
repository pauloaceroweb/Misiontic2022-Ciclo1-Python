
lista_con_precios = ['Huevos', 1.5, 'Leche', 2, 'Queso', 3.5, 'Jabon', 5]

for i, j in enumerate(lista_con_precios):
    if 'Queso' in str(j):
        posicion = i + 3
        print(lista_con_precios[i])
        print(lista_con_precios[posicion])
