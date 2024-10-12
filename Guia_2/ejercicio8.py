def eliminar_duplicados(lista):
    return list(dict.fromkeys(lista))

lista = [1, 2, 2, 3, 4, 4, 5]
print("Lista sin duplicados:", eliminar_duplicados(lista))
