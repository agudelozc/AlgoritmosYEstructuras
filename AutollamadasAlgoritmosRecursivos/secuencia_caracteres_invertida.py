"Dada una secuencia de caracteres, obtener dicha secuencia invertida."

def secuencia_invertida(secuencia):
    if secuencia == "":
        return ""
    else:
        return secuencia_invertida(secuencia[1:]) + secuencia[0]
    
print(secuencia_invertida("hola"))