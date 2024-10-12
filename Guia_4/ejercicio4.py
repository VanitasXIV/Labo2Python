def eliminar_clave(diccionario, clave):
    diccionario.pop(clave, None)
    return diccionario

diccionario = {'a': 1, 'b': 2}
clave = 'a'
print("Diccionario después de eliminar:", eliminar_clave(diccionario, clave))
