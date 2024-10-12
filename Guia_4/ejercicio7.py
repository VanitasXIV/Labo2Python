def agrupar_por_longitud(lista_palabras):
    agrupado = {}
    for palabra in lista_palabras:
        longitud = len(palabra)
        if longitud not in agrupado:
            agrupado[longitud] = []
        agrupado[longitud].append(palabra)
    return agrupado

palabras = ['uno', 'dos', 'tres', 'cuatro', 'cinco']
print("Agrupado por longitud:", agrupar_por_longitud(palabras))
