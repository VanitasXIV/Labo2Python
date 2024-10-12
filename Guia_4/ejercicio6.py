def contar_pares(lista_pares):
    frecuencia = {}
    for par in lista_pares:
        frecuencia[par] = frecuencia.get(par, 0) + 1
    return frecuencia

pares = [(1, 2), (2, 3), (1, 2), (2, 3), (3, 4)]
print("Frecuencia de pares:", contar_pares(pares))
