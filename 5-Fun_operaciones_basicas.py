def operaciones_basicas(x, y):
    suma = x + y
    resta = x - y
    producto = x * y
    return suma, resta, producto


num1 = int(input('Digite primer número: '))
num2 = int(input('Digite segundo número: '))

s, r, p = operaciones_basicas(num1, num2)

print('La suma de ', num1, ' + ', num2, 'es: ', s)
print('La resta de ', num1, ' - ', num2, 'es: ', r)
print('El producto de ', num1, ' * ', num2, 'es: ', p)
