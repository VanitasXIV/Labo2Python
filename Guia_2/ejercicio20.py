from itertools import combinations

def combinaciones_dos_caracteres(lista):
    return list(combinations(lista, 2))

lista_caracteres = ['a', 'b', 'c', 'd']
print("Combinaciones de dos caracteres:", combinaciones_dos_caracteres(lista_caracteres))
