def invertir_sublistas(lista_de_listas):
    return [sublista[::-1] for sublista in lista_de_listas]


lista_de_listas = [[1, 2], [3, 4], [5, 6]]
print("Sublistas invertidas:", invertir_sublistas(lista_de_listas))
