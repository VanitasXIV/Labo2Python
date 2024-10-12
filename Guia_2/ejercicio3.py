def frecuencia_caracteres(cadena):
    frecuencia = {}
    for char in cadena:
        frecuencia[char] = frecuencia.get(char, 0) + 1
    return frecuencia

cadena = input("Ingresa un texto pibe: ")
print("Frecuencia de caracteres:", frecuencia_caracteres(cadena))
