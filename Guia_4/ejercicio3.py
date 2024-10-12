def buscar_valor(diccionario, clave):
    return diccionario.get(clave, "Clave no encontrada")

diccionario = {'a': 1, 'b': 2}
clave = 'b'
print("Valor encontrado:", buscar_valor(diccionario, clave))
