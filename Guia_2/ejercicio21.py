from itertools import combinations

def encontrar_sublistas(lista):
    sublistas = []
    for i in range(len(lista) + 1):
        for comb in combinations(lista, i):
            sublistas.append(list(comb))
    return sublistas


lista = [1, 2, 3]
print("Todas las sublistas posibles:", encontrar_sublistas(lista))
