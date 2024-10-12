def contar_palabras(cadena):
    palabras = cadena.split()
    return len(palabras)


cadena = input("Ingresa un texto pibe: ")
print("Número de palabras:", contar_palabras(cadena))
