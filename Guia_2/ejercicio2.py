def contar_palabras_unicas(texto):
    palabras = texto.lower().split()
    return len(set(palabras))


texto = input("Ingresa un texto pibe: ")
print("Cantidad de palabras únicas:", contar_palabras_unicas(texto))
