"Desarrollar una función que permita convertir un número romano en un número decimal."

def numero_romano_a_decimal(numero_romano, index=0):
    numeros_romanos = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    
    if index >= len(numero_romano):
        return 0
    
    if (index + 1 < len(numero_romano) and 
        numeros_romanos[numero_romano[index]] < numeros_romanos[numero_romano[index + 1]]):
        return (numeros_romanos[numero_romano[index + 1]] - numeros_romanos[numero_romano[index]] 
                + numero_romano_a_decimal(numero_romano, index + 2))
    else:
        return numeros_romanos[numero_romano[index]] + numero_romano_a_decimal(numero_romano, index + 1)

print(numero_romano_a_decimal("I"))  # 1
print(numero_romano_a_decimal("IV"))  # 4
print(numero_romano_a_decimal("XII"))  # 12
print(numero_romano_a_decimal("XXIX"))  # 29
        
        
        