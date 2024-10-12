def crear_diccionario(claves, valores):
    return dict(zip(claves, valores))

claves = ['a', 'b', 'c']
valores = [1, 2, 3]
print("Diccionario creado:", crear_diccionario(claves, valores))
