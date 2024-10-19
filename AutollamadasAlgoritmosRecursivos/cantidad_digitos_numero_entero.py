"Desarrollar un algoritmo que cuente la cantidad de dígitos de un número entero"

def cuenta_digitos_entero(n):
    if n < 10:
        return 1
    else:
        return 1 + cuenta_digitos_entero(n // 10)
    
print(cuenta_digitos_entero(20))  # Output: 5