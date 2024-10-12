def filtrar_diccionario(diccionario, valor):
    return {k: v for k, v in diccionario.items() if v > valor}

diccionario = {'a': 5, 'b': 10, 'c': 3}
valor = 4
print("Diccionario filtrado:", filtrar_diccionario(diccionario, valor))
