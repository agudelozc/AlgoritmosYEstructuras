"Implementar una función para calcular el producto de dos números enteros dados."

def producto_dos_numeros(a, b):
    if  b == 0:
        return 0
    else:
        return a + producto_dos_numeros(a, b - 1)
     
print(producto_dos_numeros(2, 3))