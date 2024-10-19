"Desarrollar un algoritmo que permita convertir un número entero en sistema decimal a sistema binario."

def entero_a_binario(numero):
    if numero == 0:
        return 0
    else:
        return (numero % 2 + 10 * entero_a_binario(int(numero / 2)))

print(entero_a_binario(10))