"Desarrollar un algoritmo que permita calcular la siguiente serie:"
"h(n)= 1 + 1/2 + 1/3 + 1/4 + 1/5 + ... + 1/n"

def serie(n):
    if n == 1:
        return 1
    else:
        return 1/n + serie(n-1)

print(serie(2))