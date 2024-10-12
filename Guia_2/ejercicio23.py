def suma_digitos(numero):
    suma = 0
    while numero > 0:
        suma += numero % 10
        numero //= 10
    return suma


numero = 12345
print("Suma de los dígitos del número:", suma_digitos(numero))
