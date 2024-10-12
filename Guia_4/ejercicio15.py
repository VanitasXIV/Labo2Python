def invertir_diccionario(diccionario):
    invertido = {}
    for clave, valor in diccionario.items():
        if valor in invertido:
            if isinstance(invertido[valor], list):
                invertido[valor].append(clave)
            else:
                invertido[valor] = [invertido[valor], clave]
        else:
            invertido[valor] = clave
    return invertido

diccionario = {'a': 1, 'b': 2, 'c': 1}
print("Diccionario invertido:", invertir_diccionario(diccionario))
