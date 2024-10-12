def actualizar_diccionario(diccionario, nuevas_claves, nuevos_valores):
    diccionario.update(dict(zip(nuevas_claves, nuevos_valores)))
    return diccionario

diccionario = {'a': 1, 'b': 2}
nuevas_claves = ['b', 'c']
nuevos_valores = [3, 4]
print("Diccionario actualizado:", actualizar_diccionario(diccionario, nuevas_claves, nuevos_valores))
