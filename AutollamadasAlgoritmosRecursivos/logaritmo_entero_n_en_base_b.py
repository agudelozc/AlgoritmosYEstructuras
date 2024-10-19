"Implementar una función para calcular el logaritmo entero de número n en una base b. Recuerde que:"
"Logb(n/b) = Logb(n) + Logb(b)"

def logaritmo_entero(n, b):
    if n < b:
        return 0
    else:
        return 1 + logaritmo_entero(n/b, b)