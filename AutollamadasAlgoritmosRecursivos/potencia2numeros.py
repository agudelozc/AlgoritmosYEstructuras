"Implementar una función para calcular la potencia dado dos números enteros, el primero representa la base y segundo el exponente."

def potencia_dos_numeros(base, exponente):
    if exponente == 0:
        return 1
    else:
        return base * potencia_dos_numeros(base, exponente - 1)
    
print(potencia_dos_numeros(2, 3))