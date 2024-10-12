def contar_palabras(lista_palabras):
    frecuencia = {}
    for palabra in lista_palabras:
        frecuencia[palabra] = frecuencia.get(palabra, 0) + 1
    return frecuencia

palabras = ['manzana', 'banana', 'manzana', 'pera', 'banana']
print("Frecuencia de palabras:", contar_palabras(palabras))
