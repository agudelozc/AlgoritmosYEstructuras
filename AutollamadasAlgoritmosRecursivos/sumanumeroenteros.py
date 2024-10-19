"Implementar una función que calcule la suma de todos los números enteros comprendidos entre cero" 
"y un número entero positivo dado"

def sumar_numeros_enteros(n):
    if n == 0:
        return 0
    else:
        return n + sumar_numeros_enteros(n - 1)
    
print(sumar_numeros_enteros(5))