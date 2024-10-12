def agrupar_por_primera_letra(lista_palabras):
    agrupado = {}
    for palabra in lista_palabras:
        letra = palabra[0]
        if letra not in agrupado:
            agrupado[letra] = []
        agrupado[letra].append(palabra)
    return {k: tuple(v) for k, v in agrupado.items()}

palabras = ['manzana', 'mango', 'banana', 'pera']
print("Agrupado por primera letra:", agrupar_por_primera_letra(palabras))
