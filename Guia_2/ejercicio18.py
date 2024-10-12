def intercalar_listas(lista1, lista2):
    return [elemento for par in zip(lista1, lista2) for elemento in par]


lista1 = [1, 2, 3]
lista2 = ['a', 'b', 'c']
print("Listas intercaladas:", intercalar_listas(lista1, lista2))
