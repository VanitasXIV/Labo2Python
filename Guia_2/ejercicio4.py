def interseccion_listas(lista1, lista2):
    return list(set(lista1) & set(lista2))


lista1 = [1, 2, 3, 4, 5]
lista2 = [4, 5, 6, 7, 8]
print("Intersección de las listas:", interseccion_listas(lista1, lista2))
