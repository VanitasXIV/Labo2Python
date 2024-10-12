def encontrar_faltante(lista):
    n = len(lista) + 1
    suma_esperada = n * (n + 1) // 2
    return suma_esperada - sum(lista)


lista = [1, 2, 4, 5]
print("Número faltante:", encontrar_faltante(lista))
